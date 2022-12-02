import re
import sys
import jwt
from jwt import PyJWKClient, InvalidIssuerError
from django.conf import settings
import logging

from keycloak.utils import get_all_keys

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)


class JWTValidator:
    __token: str

    def __init__(self, token: str) -> None:
        self._set_token(token)

    def _set_token(self, token):
        """
        Reserved method to set the private token property.
        """
        if " " in token:
            raise ValueError("Invalid token")

        self.__token = token

    def validate(self):
        # Check first if the token issuer is trusted
        self._validate_iss()

        # Obtain the publics keys from the issuer certs
        RSA_public_keys = self._get_public_keys()

        # Use the public keys to verify the token
        decoded_jwt = jwt.decode(
            self.__token,
            key=RSA_public_keys.key,
            algorithms="RS256",
            audience="account",
        )

        return decoded_jwt

    @classmethod
    def get_user_claims(cls, decoded_token: dict, claims: list, required: list):
        items: list = decoded_token.items()
        cls._check_required_claims(items, required)
        user_info = dict(filter(lambda claim: claim[0] in claims, items))
        logger.debug("user extracted info : %s", user_info)
        return user_info

    @classmethod
    def _check_required_claims(cls, items: list, required: list):
        if required:
            claims = get_all_keys(items=items)

            checks = list(map(lambda required: required in claims, required))
            if not all(checks):
                raise KeyError(
                    "A required claim from %s is not in the token claims." % (required)
                )
        else:
            raise ValueError(
                "There's not required claims. \n At least one required claim is needed to check if user exists"
            )

    def _validate_iss(self):
        """
        Takes the token iss and check against the OAUTH_TRUSTED_ISSUERS settings.

        Raises:
            - ValueError
            - jwt.InvalidIssuerError
        """
        trusted_issuers = getattr(settings, "KEYCLOAK_OAUTH_TRUSTED_ISSUERS", [])
        if not trusted_issuers:
            raise ValueError(
                "OAUTH_TRUSTED_ISSUERS is empty or is not specified in your settings."
            )

        iss = self._get_issuer()
        if iss not in trusted_issuers:
            raise InvalidIssuerError(f"The token issuer {iss} is not trusted")
        return iss

    def _get_issuer(self):
        """
        Gets the decoded token and returns the `iss` property.
        """

        decoded_token = self.__get_unverified_decoded_token()
        iss = self.__check_issuer(decoded_token["iss"])
        return iss

    def _get_public_keys(self):
        url = self.__get_certs_url()
        print(f"URL : {url}")
        jwk_client = PyJWKClient(url)
        try:
            public_keys = jwk_client.get_signing_key_from_jwt(self.__token)
        except jwt.exceptions.PyJWKClientError as err:
            logger.error(err, exc_info=True)
            raise InvalidIssuerError("PyJWKClient connection refused")
        return public_keys

    def __get_unverified_decoded_token(
        self,
    ):
        """
        Returns an unverified decoded jwt.
        """
        decode_token = jwt.decode(
            self.__token, algorithms="RS256", options={"verify_signature": False}
        )
        return decode_token

    def __get_certs_url(self):
        iss = self._get_issuer()
        return f"{iss}/protocol/openid-connect/certs"

    def __check_issuer(self, iss: str):
        """
        Check and fix the issuer format.
        """
        if iss.endswith("/"):
            return re.sub(r".$", "", iss)
        return iss
