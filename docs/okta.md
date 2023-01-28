# OKTA

### Authentication

Okta APIs support two authentication options:

* [OAuth 2.0 and OpenID Connect](https://developer.okta.com/docs/reference/core-okta-api/#oauth-20-and-openid-connect-authentication)
* [API token](https://developer.okta.com/docs/reference/core-okta-api/#api-token-authentication)

### OAuth 2.0 and OpenID Connect authentication

You can interact with Okta APIs that use scoped OAuth 2.0 access tokens for a number of Okta endpoints. Each access token enables the bearer to perform specific actions on specific Okta endpoints, with that ability controlled by the scopes that the access token contains. See [OpenID Connect and OAuth 2.0 API > Client authentication methods](https://developer.okta.com/docs/reference/api/oidc/#client-authentication-methods).

Refer to the following guides for OAuth 2.0 and OpenID Connect authentication implementations:

* For user access token requests, see [Implement OAuth for Okta](https://developer.okta.com/docs/guides/implement-oauth-for-okta/).
* For service access token requests, see [Implement OAuth for Okta with service app](https://developer.okta.com/docs/guides/implement-oauth-for-okta-serviceapp/).
* For partner service apps in the Okta Integration Network (OIN), see [Build an API service integration](https://developer.okta.com/docs/guides/build-api-integration/main/).

### API token authentication 

The Okta API requires the custom HTTP authentication scheme **SSWS** for API token (API key) authentication. Requests must have a valid API token specified in the HTTP **Authorization** header with the **SSWS** scheme.

For example:

```
Authorization: SSWS 00QCjAl4MlV-WPXM...0HmjFx-vbGua
```

**Note**: See [Create an API token](https://developer.okta.com/docs/guides/create-an-api-token/) for instructions on how to get an API token for your organization.

The API token isn't interchangeable with an Okta [session token](https://developer.okta.com/docs/reference/api/authn/#session-token), access tokens, or ID tokens used with [OAuth 2.0 and OpenID Connect](https://developer.okta.com/docs/reference/api/oidc/).
