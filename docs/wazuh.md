# Wazuh 

### Authentication

Wazuh API endpoints requires authentication in order to be used. Therefore, all calls must include a JSON Web Token. JWT is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. Follow the steps below to log in using GET /security/user/authenticate and obtain a token in order to run any endpoint:

Use the cURL command to log in. The Wazuh API will provide a JWT token upon success. Replace <user> and <password> with yours. By default, the user is wazuh, and the password is wazuh. If SSL (HTTPS) is enabled in the API and it is using the default self-signed certificates, it will be necessary to add the parameter -k. Use the raw option to get the token in a plain text format. Querying the login endpoint with raw=true is recommended when using cURL commands as tokens could be long and difficult to handle. Exporting the token to an environment variable will ease the use of API requests after login.

Export the token to an environment variable to use it in authorization header of future API requests:


```
TOKEN=$(curl -u <user>:<password> -k -X GET "https://localhost:55000/security/user/authenticate?raw=true")
```
  

By default (raw=false), the token is obtained in an application/json format. If using this option, copy the token found in <YOUR_JWT_TOKEN> without the quotes.

```
Output
{
    "data": {
        "token": "<YOUR_JWT_TOKEN>"
    },
    "error": 0
}
```
  
Send an API request to confirm that everything is working as expected:

```
curl -k -X GET "https://localhost:55000/" -H "Authorization: Bearer $TOKEN"
Output
{
    "data": {
        "title": "Wazuh API",
        "api_version": "4.0.0",
        "revision": 4000,
        "license_name": "GPL 2.0",
        "license_url": "https://github.com/wazuh/wazuh/blob/master/LICENSE",
        "hostname": "wazuh-master",
        "timestamp": "2020-05-25T07:05:00+0000"
    },
    "error": 0
}
```
  
Once logged in, it is possible to run any API endpoint following the structure below. Please, do not forget to replace <endpoint> with the string corresponding to the chosen endpoint. If the environment variable is not going to be used, replace $TOKEN with the JWT token obtained.

```
curl -k -X <METHOD> "https://localhost:55000/<ENDPOINT>" -H  "Authorization: Bearer $TOKEN"
```
