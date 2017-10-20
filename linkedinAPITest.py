from linkedin import linkedin

token = linkedin.LinkedInDeveloperAuthentication('86574c81g5oec7','gE7EGSbjRB0pXfA1','https://YOUR_AUTH0_DOMAIN/login/callback',linkedin.PERMISSIONS.enums.values())

application=linkedin.LinkedInApplication(authentication)

application.get_profile()