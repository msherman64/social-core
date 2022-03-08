import jwt
from social_core.backends.keycloak import KeycloakOAuth2


class ChameleonOAuth2(KeycloakOAuth2):  # pylint: disable=abstract-method
    def get_user_details(self, response):
        """Map fields in user_data into Django User fields"""

        return {
            'username': response.get('preferred_username'),
            'email': response.get('email'),
            'fullname': response.get('name'),
            'first_name': response.get('given_name'),
            'last_name': response.get('family_name'),
            'groups': response.get('project_names')
        }

