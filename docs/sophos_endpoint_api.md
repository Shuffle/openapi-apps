# Sophos Endpoint 

### API Authentication

### Authentication

A service principal must authenticate with [Sophos ID](https://id.sophos.com/), our Identity Provider (IDP), to acquire a time-limited and scope-limited authentication token. These tokens follow the JSON Web Token (JWT) standard.

To obtain a JWT token, make a POST request to Sophos ID passing in the Client ID and the Client Secret for the service principal. As a [cURL](https://curl.haxx.se/) command:

```
curl -XPOST -H 'Content-Type:application/x-www-form-urlencoded' \
            -d 'grant_type=client_credentials&client_id=<id>&client_secret=<secret>&scope=token' \
                   https://id.sophos.com/api/v2/oauth2/token
```
The command has been split across multiple lines for legibility. Replace ```<id>``` with your Client ID and ```<secret>``` with your Client Secret.

The JWT token returned by Sophos ID must be passed in the ```Authorization``` header for subsequent API calls. The header should look as follows:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0
                      NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5M
                      DIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

The header above has been split across multiple lines and indented for legibility.

### Authorization

The service principal must have the right set of permissions to make an API call. While our APIs are in Preview, a service principal will have access to limited functionality, but all access is at the [SuperAdmin](https://community.sophos.com/kb/en-us/125168#Predefined%20admin%20roles) level.
