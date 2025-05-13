# Harmony Endpoint Management API

## Prerequisites
 
-  clientId
-  accessKey
  
## Authentication

- The nature of authentication for this app requires you to get 2 token keys to be used for authentication of future requests.
- For the app in shuffle there will be 2 fields that you need to setup inorder for you to be able to authenticate and utilize the app in Shuffle

![image](https://github.com/user-attachments/assets/4e2ff047-f5d8-4a7e-853f-ed722b4b06dc)
1. API Key parameter
  - In the API key parameter you will paste in the following python script. Providing your clientID and accessKey as well.

```
{% python %}
import requests
import json

url = "https://cloudinfra-gw.portal.checkpoint.com/auth/external"


payload = {
  "clientId": "",
  "accessKey": ""
}


headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.json()["data"]["token"])

{% endpython %}
```
2. x-mgmt-api-token parameter
   - In the x-mgmt-api-token parameter paste in the following python script.
  
```
{% python %}
import requests
import json

url = "https://cloudinfra-gw.portal.checkpoint.com/auth/external"
payload = {
  "clientId": "",
  "accessKey": ""
}


headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
#print(response.text)

data = response.json()
token = data["data"]["token"]

#print(token)

second_url = "https://cloudinfra-gw.portal.checkpoint.com/app/endpoint-web-mgmt/harmony/endpoint/api/v1/session/login/cloud"
headers = {
  "Authorization": "Bearer %s" % token,
  "Content-type": "application/json",
  "Accept": "application/json"

}
response = requests.post(second_url, headers=headers)
print(response.json()["apiToken"])
{% endpython %}
```
- Once this is done you should be able to make subsequent requests seamlessly with your saved and encrypted authentication.

  ## NOTE:
  - You will need to provide appropriate headers where necessary i.e
    Content-Type=application/json
    Accept=application/json
    x-mgmt-run-as-job: on
  - Remember to provide the appropriate CLIENTID and ACCESSKEY where required in the provided python scripts.
