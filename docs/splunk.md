# Splunk

### Authentication and authorization

There are two methods of authentication that you can use to access REST endpoints:

- Username and password
- Splunk authentication tokens

If you do not hold a valid authentication token, then authentication with credentials is the only available method for access to endpoints and REST operations. [Set up authentication with tokens](http://docs.splunk.com/Documentation/Splunk/9.0.1/Security/Setupauthenticationwithtokens) in Securing Splunk Enterprise.

Splunk users must have role or capability-based authorization to use REST endpoints. Users with an administrative role, such as admin, can access authorization information in Splunk Web.

Splunk users must have role or capability-based authorization to use REST endpoints. Users with an administrative role, such as admin, can access authorization information in Splunk Web.

- To view the roles assigned to a user, select **Settings** > **Access controls** and click **Users**.
- To determine the capabilities assigned to a role, select **Settings** > **Access controls** and click **Roles**.

The default authenticated session timeout is one hour, which Splunk Enterprise users can adjust using the ```sessionTimeout``` setting in the ```[general]``` stanza of the ```server.conf``` file.

### Authentication with HTTP Authorization tokens

The API supports token-based authentication using the standard HTTP Authorization header. For example:

1. Get a session key using the /services/auth/login endpoint:

``` curl -k https://localhost:8089/services/auth/login --data-urlencode username=admin --data-urlencode password=pass```

The response is your session key:

``` 
<response> 
  <sessionKey>192fd3e46a31246da7ea7f109e7f95fd</sessionKey>
</response>
```
2. In subsequent requests, set the header Authorization value to the session key (<sessionKey>). For example:
  
``` curl -k -H "Authorization: Splunk 192fd3e46a31246da7ea7f109e7f95fd" . . . ```
  
### Direct endpoint access with valid Splunk authentication tokens
In version 7.3 and higher of the Splunk platform, you can also use Splunk authentication tokens to access REST endpoints, without the need to authenticate with credentials and obtain a session key.

Tokens must be valid and must not have expired, and the instance you want to access must have token authentication enabled. There is no need to perform a separate login task to obtain a token, but like standard HTTP authorization, you must provide the token with each web request you generate.

To use authentication tokens to access endpoints, set the header Authorization value to the full token that you have been given to access the instance. For example:

``` curl -k -H "Authorization: Bearer eyJfd3e46a31246da7ea7f109e7f95fd" . . . ```
  
### Basic HTTP authentication
  
Splunk Enterprise also supports basic authentication, as defined by RFC 1945. This is the mechanism used when you access resources using a Web browser.
