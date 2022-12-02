from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework import exceptions as rf_exceptions
from rest_framework.request import Request
from rest_framework.authentication import BaseAuthentication, exceptions
from jwt.exceptions import InvalidTokenError
from keycloak.JWTValidator import JWTValidator
from keycloak.token_user_handler import NewUserHandler

import logging

logger = logging.getLogger(__name__)


class KeycloakJWTAuthentication(BaseAuthentication):
    token_user_handler = NewUserHandler

    def authenticate(self, request: Request):
        try:
            token = request.headers["Authorization"].split(" ")[1]
        except KeyError as err:
            raise exceptions.AuthenticationFailed("Access credentials not provided.")

        print(f"token: {token}")

        validator = JWTValidator(token)
        try:
            decoded_token = validator.validate()
            user = self.handle_token_user(decoded_token)
            print(user)
        except InvalidTokenError as err:
            logger.error(err)
            raise rf_exceptions.AuthenticationFailed(
                err.args[0], status.HTTP_401_UNAUTHORIZED
            )
        except KeyError as err:
            logger.error(err)
            raise rf_exceptions.AuthenticationFailed(
                err.args[0], status.HTTP_401_UNAUTHORIZED
            )
        except Exception as err:
            logger.error("Unhandled error :\n%s", err)
            raise err

        return (user, decoded_token)

    def authenticate_header(self, request):
        return 'Bearer realm="Access to REST api for decidir-t project"'

    def handle_token_user(self, decoded_token):
        handler = self.get_token_user_handler()
        return handler.handle(decoded_token)

    def get_token_user_handler(self):
        return self.token_user_handler()
