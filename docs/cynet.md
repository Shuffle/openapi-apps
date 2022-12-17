# Cynet 
### API Authentication

Cynet APIs use access tokens to authenticate requests.

To call a Cynet API, you must use your Cynet 360 username and password to get an access token. The Cynet 360 user must have the Cynet API User permission. For more information on users and roles, click [here](https://help.cynet.com/en/articles/63). Use this account in the api/account/token API call to generate an access token. The access token is used as a header key/value pair to authenticate every API call to the Cynet 360 server. The access token is valid for 60 minutes. Every user can have one valid API token at a time.

### Get Token

```
https://YOUR_DOMAIN.api.cynet.com
/api/account/token
```

Authenticates to the Cynet API engine using configured credentials. The response returns a token, which is used for all other API requests.

* Request Sample Language

```
curl --request POST \
  --url https://your_domain.api.cynet.com/api/account/token \
  --header 'Content-Type: application/json' \
  --data '{}'
 ```
