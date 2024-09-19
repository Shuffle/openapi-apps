# FortiEDR
FortiEDR app to interact with the Fortinet Endpoint Protection and Response Platform using API authentication.

## Authentication

1. FortiEDR account with API access enabled.
2. `X-Auth-Token` or basic authentication credentials (username and password).

## How to Authenticate with FortiEDR API

You can authenticate with FortiEDR's API using either **basic authentication** or **API token authorization**.

1. **Basic Authentication**

The user must have the REST API role assigned to perform API calls using basic authentication. This role is necessary to make any API request.
- Example of a basic authentication request:

```bash
curl -k -H "Authorization: Basic <base64(username:password)>" https://<YOURDOMAINNAME>/management-rest/events/list-events
```

If successful, the response will include an **X-Auth-Token**, which can be used for future API calls without needing to supply your credentials again.

2. **API Token Authorization (X-Auth-Token)**

After receiving the `X-Auth-Token` from the initial basic authentication request, you can use it to authorize further API requests.

- Each API request must include the `X-Auth-Token` in the request headers as shown below:

```bash
curl -k -H "X-Auth-Token: <your_token>" https://<YOURDOMAINNAME>/management-rest/events/list-events
```

#### Token Regeneration

If you need to regenerate the `X-Auth-Token`, you must perform another API request using basic authentication. This will revoke the previous token and generate a new one.

For more information, refer to the [FortiEDR API Documentation](https://fortinetweb.s3.amazonaws.com/docs.fortinet.com/v2/attachments/df7ab511-7435-11ea-9384-00505692583a/API_Guide_V4.1.pdf).
```
