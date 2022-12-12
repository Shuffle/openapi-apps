# Alienvault

### Authentication

The USM Anywhere APIs use OAuth 2.0 for endpoint protection, which provides token-based authentication and authorization on the Internet. The diagram below illustrates the authorization flow between the user and the USM Anywhere APIs.

<img>

Before you can retrieve a token, you must create a client ID and secret code in USM Anywhere for your user account.

**Important:** Only USM Anywhere users of the Manager role can create new API clients.


**To get your client ID and secret code**

Click the  icon and select **Profile Settings**.
On the Profile page, select the **API Clients** tab.
Click **New Client**.
Enter an alphanumeric name for the client and click **Create Client**.

The system generates the secret code.

**Note:** This code is only available when it is first generated, so be sure to keep it secure and copy it when it is displayed. If you want to generate a new code, use the Reset Secret link.


Then, you need to use the oauth/token endpoint to request a token used for authentication by the other API endpoints. For example:

```
curl -X POST "https://<your-subdomain>.alienvault.cloud/api/{version}/oauth/token?grant_type=client_credentials" \
     -d @request_body \
     --user <username>:<password>
```

The POST command has a single www-form-urlencoded parameter, grant_type, and currently the only supported value is client_credentials. Use the client ID for username and the secret code for password.

The response to this POST command contains the OAuth token that must be used to make subsequent requests to the other API endpoints.

```
{
	"access_token": "xxx.yyy.zzz",
	"token_type": "bearer",
	"expires_in": 899,
	"scope": "trust read write",
	"jti": "3b4cc123-2164-44cb-ae34-9c76d7c429ab"
}
```

The OAuth access token expires after 30 minutes. When or before it expires, you must use the oauth/token endpoint to re-authenticate and get a new token.

Next, you must use the token in the header on subsequent requests to the other endpoints. For example:

Authorization: Bearer <access_token>

### Requests and Responses

All connections should use the HTTPS protocol using the public Domain Name System (DNS) name for your subdomain. For example:

```
GET https://<your-subdomain>.alienvault.cloud/api/2.0/alarms
GET https://<your-subdomain>.alienvault.cloud/api/2.0/alarms/{alarmId}
```

A given client is limited to 100 GET and 50 POST requests per second for a USM Anywhere subdomain. When exceeding the threshold, a 429 response is returned until you are back under the rate limit.

Most endpoints in the USM Anywhere APIs support standard REST paradigms. You can either retrieve a collection or a member of a collection.

### Get a Collection

Enter this request to get a colleciton:

GET https://<your-subdomain>.alienvault.cloud/api/2.0/alarms

**Important:** The USM Anywhere APIs can only access alarm and event data stored in the local system; raw logs in cold storage are not accessible by the API calls.

You will receive this response for the request:

```
{
  "_links": {
    "first": {
      "href": "https://<your-subdomain>.alienvault.cloud/api/2.0/alarms?page=0&size=20&sort=timestamp_occured,desc",
      "templated": false
    },
    "self": {
      "href": "https://<your-subdomain>.alienvault.cloud/api/2.0/alarms",
      "templated": false
    },
    "next": {
      "href": "https://<your-subdomain>.alienvault.cloud/api/2.0/alarms?page=1&size=20&sort=timestamp_occured,desc",
      "templated": false
    },
    "last": {
      "href": "https://<your-subdomain>.alienvault.cloud/api/2.0/alarms?page=175&size=20&sort=timestamp_occured,desc",
      "templated": false
    }
  },
  "_embedded": {
    "alarms": [
        ... content omitted for clarity ...
    ]
  },
  "page": {
    "size": 20,
    "totalElements": 3506,
    "totalPages": 176,
    "number": 0
  }
}
```

Collection responses are JSON objects with a structure that allows pagination using Hypermedia as the Engine of Application State (HATEOAS)-style links. See USM Anywhere API References for the complete example.

### Get a Member of a Collection

Enter this request to get a member of a collection:

```
GET https://<your-subdomain>.alienvault.cloud/api/2.0/alarms/{alarmId}
```
**Important:** The USM Anywhere APIs can only access alarm and event data stored in the local system; raw logs in cold storage are not accessible by the API calls.

You will receive this response for the request:

```
{
	"uuid": "971918fd-a569-548a-5a80-1ffcda2a8365",
 	"has_alarm": false,
 	"needs_enrichment": true,
 	"priority": 20,
 	"suppressed": false,
 	"destinations": [],
 	"sources": [],
	"timestamp_occured": "1517932134000",
 	"events": [
		... content omitted for clarity ...
				],
 	"_links": {
		"self": {
			"href": "https://<your-subdomain>.alienvault.cloud/api/2.0/alarms/971918fd-a569-548a-5a80-1ffcda2a8365",
			"templated": false
			}
 		   }
}
```
Single-item responses are JSON objects that represent the resource state. See USM Anywhere API References for the complete example.

**Note:** Timestamp fields such as timestamp_occured and timestamp_received are epoch time in milliseconds.
