# Create API key API

Creates an API key for access without requiring basic authentication.

## Request

```
POST /_security/api_key

PUT /_security/api_key
```
## Prerequisites

To use this API, you must have at least the manage_own_api_key cluster privilege.

If the credential that is used to authenticate this request is an API key, the derived API key cannot have any privileges. If you specify privileges, the API returns an error. See the note under role_descriptors.

### Description

The API keys are created by the Elasticsearch API key service, which is automatically enabled. For instructions on disabling the API key service, see API key service settings.

A successful request returns a JSON structure that contains the API key, its unique id, and its name. If applicable, it also returns expiration information for the API key in milliseconds.

By default, API keys never expire. You can specify expiration information when you create the API keys.

See API key service settings for configuration settings related to API key service.

### Request body
The following parameters can be specified in the body of a POST or PUT request:

name
(Required, string) Specifies the name for this API key.

role_descriptors
(Optional, object) The role descriptors for this API key. This parameter is optional. When it is not specified or is an empty array, then the API key will have a point in time snapshot of permissions of the authenticated user. If you supply role descriptors then the resultant permissions would be an intersection of API keys permissions and authenticated user’s permissions thereby limiting the access scope for API keys. The structure of role descriptor is the same as the request for create role API. For more details, see create or update roles API.

Due to the way in which this permission intersection is calculated, it is not possible to create an API key that is a child of another API key, unless the derived key is created without any privileges. In this case, you must explicitly specify a role descriptor with no privileges. The derived API key can be used for authentication; it will not have authority to call Elasticsearch APIs.

expiration
(Optional, string) Expiration time for the API key. By default, API keys never expire.

metadata
(Optional, object) Arbitrary metadata that you want to associate with the API key. It supports nested data structure. Within the metadata object, keys beginning with _ are reserved for system usage.

### Examples

The following example creates an API key:

```
POST /_security/api_key
{
  "name": "my-api-key",
  "expiration": "1d",   
  "role_descriptors": { 
    "role-a": {
      "cluster": ["all"],
      "index": [
        {
          "names": ["index-a*"],
          "privileges": ["read"]
        }
      ]
    },
    "role-b": {
      "cluster": ["all"],
      "index": [
        {
          "names": ["index-b*"],
          "privileges": ["all"]
        }
      ]
    }
  },
  "metadata": {
    "application": "my-application",
    "environment": {
       "level": 1,
       "trusted": true,
       "tags": ["dev", "staging"]
    }
  }
}
```
A successful call returns a JSON structure that provides API key information.

```
{
  "id": "VuaCfGcBCdbkQm-e5aOx",        
  "name": "my-api-key",
  "expiration": 1544068612110,         
  "api_key": "ui2lp2axTNmsyakw9tvNnw", 
  "encoded": "VnVhQ2ZHY0JDZGJrUW0tZTVhT3g6dWkybHAyYXhUTm1zeWFrdzl0dk5udw=="  
}
```

Unique id for this API key

Optional expiration in milliseconds for this API key

### Generated API key


API key credentials which is the Base64-encoding of the UTF-8 representation of the id and api_key joined by a colon (:).

To use the generated API key, send a request with an Authorization header that contains an ApiKey prefix followed by the API key credentials (the encoded value from the response).

``` 
curl -H "Authorization: ApiKey VnVhQ2ZHY0JDZGJrUW0tZTVhT3g6dWkybHAyYXhUTm1zeWFrdzl0dk5udw==" \
http://localhost:9200/_cluster/health\?pretty 
```

If your node has xpack.security.http.ssl.enabled set to true, then you must specify https when creating your API key

On a Unix-like system, the encoded value can be created with the following command:

```
echo -n "VuaCfGcBCdbkQm-e5aOx:ui2lp2axTNmsyakw9tvNnw" | base64 
```

Use -n so that the echo command doesn’t print the trailing newline character


# Authenticate API

Enables you to submit a request with a basic auth header to authenticate a user and retrieve information about the authenticated user.

### Request
GET /_security/_authenticate


### Description
A successful call returns a JSON structure that shows user information such as their username, the roles that are assigned to the user, any assigned metadata, and information about the realms that authenticated and authorized the user.

### Response codes
If the user cannot be authenticated, this API returns a 401 status code.

### Examples
To authenticate a user, submit a GET request to the /_security/_authenticate endpoint:

```
GET /_security/_authenticate
```
The following example output provides information about the "rdeniro" user:

```
{
  "username": "rdeniro",
  "roles": [
    "admin"
  ],
  "full_name": null,
  "email":  null,
  "metadata": { },
  "enabled": true,
  "authentication_realm": {
    "name" : "file",
    "type" : "file"
  },
  "lookup_realm": {
    "name" : "file",
    "type" : "file"
  },
  "authentication_type": "realm"
}
```
