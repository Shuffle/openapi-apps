# Fortigate Firewall

First and foremost you will need to authenticate your app.

1. From your Fortigate Firewall console get the bearer token as we will use this for authentication.
### General steps would be:

- Log in to FortiGate console - Access the FortiGate web interface using a web browser
- Navigate to the API Settings - In the FortiGate web interface, go to System > API > Settings
- Generate API Key- Click on the "Generate" button or a similar option to create a new API key.
- Define API Key Settings - You may be asked to define specific settings for the API key, such as the access level or privileges it should have. Follow the on-screen instructions to configure the API key settings.
- Save API Key - After configuring the API key settings, the FortiGate device will generate a unique API key for you. Make sure to save this key securely, as it will be required for API authentication.
- Use the API Key - When making API requests to the FortiGate device, include the API key in the request headers for authentication. Typically, you'll add an Authorization header with the key in the following format:

```
Authorization: Bearer <your_api_key>
```

2. Once step one above is done, jump into your Shuffle workflow. Drag in the Fortigate App into your workflow then click on it.

![Alt text](image.png)

3. Click authenticate fortigate firewall. Add the fortigate console url. Click on submit once done.

![Alt text](image-1.png)

4. Proceed to select the action you are intersted in, Once done paste the below in you header parameter inputting your bearer token. 
```
Authorization: Bearer <replace_this_with_token>.
Content-Type: application/json
Accept: application/json
```
6. Fill in other required parameters and you are good to go.