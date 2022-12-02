from keycloak.JWTValidator import JWTValidator
from django.conf import settings
from django.contrib.auth import get_user_model

from keycloak.utils import get_all_keys


class BaseHandler:
    default_claims_map: dict
    required_claims: list
    user_get_claim: str
    required_settings_map = {
        "KEYCLOAK_DEFAULT_CLAIMS_MAP": "default_claims_map",
        "KEYCLOAK_REQUIRED_CLAIMS": "required_claims",
        "KEYCLOAK_USER_GET_CLAIM": "user_get_claim",
    }

    def __init__(self) -> None:
        self.get_settings()
        self.validate()
        self.user_model = get_user_model()

    def handle(self, decoded_token):
        raise NotImplementedError()

    def validate(self):
        if (
            not self.user_get_claim in self.required_claims
            and not self.user_get_claim in self.default_claims_map
        ):
            raise ValueError(
                "The KEYCLOAK_USER_GET_CLAIM value must exist in both KEYCLOAK_REQUIRED_CLAIMS and KEYCLOAK_DEFAULT_CLAIMS_MAP"
            )

    def get_settings(self):
        settings_keys = self._get_setting_keys()
        [self._get_setting(setting) for setting in settings_keys]

    def _get_token_claims(self):
        claims_keys = get_all_keys(obj=self.default_claims_map)
        return claims_keys

    def _get_setting(self, setting):
        value = getattr(settings, setting, None)
        if not value:
            raise ValueError(
                "%s setting is empty or is not specified in your settings.", setting
            )
        setattr(self, self.required_settings_map[setting], value)

    def _get_setting_keys(self):
        keys = get_all_keys(obj=self.required_settings_map)
        return keys


class NewUserHandler(BaseHandler):
    def handle(self, decoded_token):
        claims = self._get_token_claims()
        user_info = JWTValidator.get_user_claims(
            decoded_token, claims, self.required_claims
        )
        self._check_user(user_info)
        return self._get_user(user_info)

    def _check_user(self, user_info: dict):
        filter = self._get_filter(user_info)
        if self.user_model.objects.filter(**filter).exists():
            return True
        else:
            self.__handle_new_user(user_info)

    def __handle_new_user(self, user_info):
        mapped_info = self.__map_user_info(user_info)
        self.user_model.objects.create_user(**mapped_info)

    def __map_user_info(self, user_info: dict):
        items = user_info.items()
        mapped_items = list(map(self.__replace_claim_for_property, items))
        return dict(mapped_items)

    def __replace_claim_for_property(self, item):
        claim = item[0]
        return (self.default_claims_map[claim], item[1])

    def _get_user(self, user_info):
        filter = self._get_filter(user_info)
        user = self.user_model.objects.get(**filter)
        return user

    def _get_filter(self, user_info):
        return {
            self.default_claims_map[self.user_get_claim]: user_info[self.user_get_claim]
        }
