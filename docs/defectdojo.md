# Defectdojo

### Authentication via OAuth2/SAML2

OAuth2/SAML2 let users authenticate against enterprise directories.

### Auth0

In the same way as with other identity providers, it’s now possible to leverage Auth0 to authenticate users on DefectDojo.

1. Inside your Auth0 dashboard create a new application (Applications / Create Application / Single Page Web Application).

2. On the new application set the following fields:

* Name: “Defectdojo”
* Allowed Callback URLs:
[https://the_hostname_you_have_dojo_deployed:your_server_port/complete/auth0/](https://the_hostname_you_have_dojo_deployed:your_server_port/complete/auth0/)

3. Copy the following info from the application:

* Domain
* Client ID
* Client Secret

4. Now, edit the settings (see Configuration) with the following information:

```
  DD_SOCIAL_AUTH_AUTH0_OAUTH2_ENABLED=True
    DD_SOCIAL_AUTH_AUTH0_KEY=(str, '**YOUR_CLIENT_ID_FROM_STEP_ABOVE**'),
    DD_SOCIAL_AUTH_AUTH0_SECRET=(str,'**YOUR_CLIENT_SECRET_FROM_STEP_ABOVE**'),
    DD_SOCIAL_AUTH_AUTH0_DOMAIN=(str, '**YOUR_AUTH0_DOMAIN_FROM_STEP_ABOVE**'),
```
5. Restart DefectDojo, and you should now see a Login with Auth0 button on the login page.
