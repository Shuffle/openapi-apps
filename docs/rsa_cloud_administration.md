# RSA App Authentication

1. Obtain your API key from RSA console in *Platform* -> *API Access Management*
Then you can *Add API Client* in *OAuth Client* tab.
Fill the basic informations then in Authentication, **keep in notes** displayed **Client ID** in addition of the generated **private key**.
When the private key is generated, it needs to be pasted in the *Client Secret* form.

![edit 1](https://github.com/user-attachments/assets/c129cd25-a454-4d64-a04a-c8f22558f272)

2. Select the permission you need and then, save and finish. Don't forget to **Push Changes** for each modification you apply!

![edit 1](https://github.com/user-attachments/assets/e11f6834-e0a4-4d2e-96b3-def82d8408a1)

4. Fill in the key parameter in the script below with the contents of the .key file generated in the above step.
```
{% python %} import json;import time;import jwt;from jwt.algorithms import RSAAlgorithm;import requests; response = requests.post("https://<TENANT>.auth-eu.securid.com/oauth/token", data={"grant_type": "client_credentials","scope": "","client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer","client_assertion": jwt.encode({"iss": "<CLIENT_ID>","sub": "<CLIENT_ID>","aud": "https://<TENANT>.auth-eu.securid.com/oauth/token","iat": int(time.time()),"exp": int(time.time()) + 300,"jti": str(int(time.time()))}, RSAAlgorithm.from_jwk(json.dumps(<PRIVATE_KEY>)), algorithm="RS256", headers={"kid": <PRIVATE_KEY>.get("kid", None)})}); data = response.json();access_token = data.get("access_token"); print(access_token) {% endpython %}
```

To fill the correct information and secrets, you'll need to replace following strings:
- <TENANT> by the name of you tenant (You can find it in the URL you are using - ex : https://**mytenant**.access-eu.securid.com/AdminInterface/ -> Replace the strings by **mytenant** )
- <CLIENT_ID> by the client ID you recovered previously
- <PRIVATE_KEY> by the private key you recovered previously (This one need to be **Onelined**!)

4. Then provide the above python script as your api key when authenticating the app in Shuffle.

5. Remember to provide your URL as well (Which is different than the URL used to get Bearer Token)
While used URL for getting the token is *https://mytenant.auth-eu.securid.com*, the one to use the API will be *https://mytenant.access-eu.securid.com*.

![image](https://github.com/user-attachments/assets/00bc0e61-a3d7-41ff-8806-66b432f2cd7a)


