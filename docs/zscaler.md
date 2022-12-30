# Zscaler

### API Key Authentication

Zscaler provides secured access to cloud service API and Sandbox Submission API using different authentication schemes:

| API                     | Supported Authentication Methods                  |
| ----------------------- | ------------------------------------------------- |
| Cloud Service API       | OAuth 2.0 (recommended)                           |       
|                         | Combination of  Basic Authentication and API Key  |
|                         |                                                   |
| Sandbox Submission API  | Combination of Basic Authentication and API Token |

### OAuth 2.0 Authentication

OAuth 2.0 allows third-party applications to obtain controlled access to protected resources using access tokens. Zscaler uses the Client Credentials grant type, in which the clients exchange their credentials for an access token. For more information, see [About API Authentication Using OAuth 2.0](https://help.zscaler.com/zia/about-api-authentication-using-oauth-2.0).

```
Zscaler recommends the OAuth 2.0 authentication method for accessing the cloud service API.
```
Your organization must meet the following prerequisites before you can access the API:

**Prerequisites for OAuth 2.0 Authentication**
Your organization must meet the following requirements to be able to use OAuth 2.0 authentication.

* You must have an API subscription. If you do not have a subscription, submit a Zscaler Support ticket.
* You must have the [API Roles](https://help.zscaler.com/zia/adding-api-roles) configured in the ZIA Admin Portal.
* You must have your client applications registered on your authorization server (i.e., PingFederate, Okta, or Azure AD) with the required scope and configured appropriately. To learn how to set up client applications on your OAuth 2.0 service provider, see the respective help documentation.
* You must have your [OAuth 2.0 authorization server added](https://help.zscaler.com/zia/managing-oauth-2.0-authorization-servers#add-auth-server) to the ZIA Admin Portal.

When the prerequisites are met, you can securely access the API in the following way:

### Retrieve your Base URL
The host and basePath for the cloud services API is $zsapi.<Zscaler Cloud Name>/api/v1. Check which Zscaler cloud name was provisioned for your organization and use it to replace <Zscaler Cloud Name>. For example:

* zsapi.zscalerbeta.net
* zsapi.zscalerone.net
* zsapi.zscalertwo.net
* zsapi.zscalerthree.net
* zsapi.zscaler.net
* zsapi.zscloud.net

To locate your base URL:

1. Log in to the ZIA Admin Portal using your admin credentials. You must be assigned an admin role that includes the Authentication Configuration functional scope.
2. Go to Administration > Cloud Service API Security.
3. On the OAuth 2.0 Authorization Servers tab, the base URL is displayed within the table.

### Authenticate the client and retrieve an access token

You need to configure the client application registered with the authorization server to send a POST request to the token endpoint with the following parameters and retrieve an access token:

* client_id: A unique, public identifier issued to the client application during registration with the authorization server. This identifier is used with client_secret for authentication. This information is obtained from the OAuth 2.0 service console.

* client_secret: A secret string used by the client application for authenticating with the authorization server. This information is obtained from the OAuth 2.0 service console.

* grant_type: The OAuth flow that defines the various methods in which a client application can obtain an authorization grant from the authorization server and the sequence in which the OAuth 2.0 authorization process takes place. The Zscaler service uses the client_credentials grant type, which allows clients to access protected resources outside of the context of users.

* scope: Scope defines the permissions required by the client application to access the API. You must configure the scope value in the <Zscaler Cloud Name>::<Org ID>::<API Role> format, where:

- <Zscaler Cloud Name> represents the cloud on which your organization is provisioned.
- <Org ID> represents your organization ID obtained from the ZIA Admin Portal (under Administration > Settings > Company Profile).
- <API Role> represents an API role configured in the ZIA Admin Portal (under Administration > Authentication > Role Management).

For example, ```zscalerbeta.net::8956412::sampleRole```

The client makes a POST request to the token endpoint with the client credentials (client ID and client secret) presented using HTTP Basic authentication. Alternatively, the client credentials can also be provided using the client_id and client_secret parameters in the body of the POST request. For more information, see OAuth 2.0 RFC 6749, section 2.3.

Example POST request to the token endpoint:

```
POST /as/token.oauth2 HTTP/1.1
Host: localhost:9031
Authorization: Basic xxxxxxx
Content-Type: application/x-www-form-urlencoded
{
    "grant_type": "client_credentials",
    "scope": "zscalerbeta.net::8956412::sampleRole"
}
```

If the request is successful, a 200 OK response is returned to the client with the access token and other information in a JSON structure, as follows:

```
HTTP/1.1 200 OK
Date: Thu, 25 Aug 2022 11:35:21 GMT
X-FRAME-OPTIONS: SAMEORIGIN
Referrer-Policy: origin
Cache-Control: no-cache, no-store
Pragma: no-cache
Expires: Thu, 01 Jan 1970 00:00:00 GMT 
Content-Type: application/json;charset=utf-8
Set-Cookie: PF=QL6IbHFouxkNFPXZ6uQT06;Path=/;Secure;HttpOnly;SameSite=None 
Transfer-Encoding: chunked 

{
    "access_token": "xxxxxxx",
    "token_type": "Bearer",
    "expires_in": 7199
}

PF QL6IbHFouxkNFPXZ6uQT06
```
If an unsuccessful POST request is made to the token endpoint, the response code returns a 400 error.

* [Make an API call](https://help.zscaler.com/zia/getting-started-zia-api)
* [Activate configuration changes](https://help.zscaler.com/zia/getting-started-zia-api)

To learn more about rate limiting and HTTP status codes, see [About Rate Limiting](https://help.zscaler.com/zia/about-rate-limiting) and [About Error Codes](https://help.zscaler.com/zia/about-error-handling). If you encounter any issues with the API, contact Zscaler Support.
