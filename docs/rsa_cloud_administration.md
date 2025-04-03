# RSA App Authentication

1. Obtain your API key from RSA console (use legacy API keys)

![edited](https://github.com/user-attachments/assets/370911af-878d-43e2-b39d-04b24c34b984)


2. Select Super Admin role, save and download the key is something like this ea34ebf2-f553-4fe3-8969-357527397de0.key.

![edit 1](https://github.com/user-attachments/assets/c129cd25-a454-4d64-a04a-c8f22558f272)


4. Fill in the key parameter in the script below with the contents of the .key file generated in the above step.
```
{% python %}
import jwt
def generate_token():
    key = {"customerName":"","accessID":"","description":"","accessKey":"","adminRestApiUrl":""}
    exp = time.time() + 60 * 60 
    jwt_claims = {
        "iat": time.time(), # Set issued at time to the current time.
        "exp": exp, # Set expiration time
        "aud": key["adminRestApiUrl"],  # Audience of the claim.
        "sub": key["accessID"], # Access ID from the Admin API Key.
    }

    # Use the accessKey from the Admin API key file and the RS256 algorithm to generate the JWT
    return jwt.encode(jwt_claims, key["accessKey"], algorithm="RS256")
    
print(generate_token())
{% endpython %}
```
4. Then provide the above python script as your api key when authenticating the app in Shuffle.

5. Remember to provide your URL as well

![image](https://github.com/user-attachments/assets/e3a25ca5-e9d2-4f75-8a97-fd74784a0634)

- NOTE:
On your RSA console use Legacy API keys and NOT OAuth clients

![image](https://github.com/user-attachments/assets/cfd5a697-d767-4fe6-8782-4573d6990bb1)

