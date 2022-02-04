# Domo App
App for intreacting to Domo through shuffle. Currently supports dataset and page actions. 

## Authentication
To use this app, You'll need  access token. To get access token you'll need to get client id and client secret first.

### step 1: Create client ID and secret
- In order to generate a client ID and client secret you will need your Domo instance name (i.e. the name preceding your domo.com URL.
- Log in to [developer portal](https://developer.domo.com/)
- Once logged in, click on “My Account” to create a new client.
- create your client by adding a client name, description, and client’s scope. this app requires dashboard and data scopes.

### Step 2: Generate access token
- To generate access token, go to your shuffle workflow and add http app into it.
- Add the following to the URL field: https://api.domo.com/oauth/token?grant_type=client_credentials&scope=data%20dashboard
- Add the Client ID and Client Secret to the Username and Password field respectively (Basic Auth) as seen below:

![image](https://user-images.githubusercontent.com/5719530/149952528-e060812b-59bc-4fd2-b44d-3285f0efbbc7.png)

- Run the workflow and you'll get an access token in response.

![image](https://user-images.githubusercontent.com/5719530/149952858-db4ae8f9-0e28-4086-b708-e11f8af36218.png)

In this case, it can be used as such in the next step:
```
$http_1.access_token
```

### Step 3: Use access token
- Now use access token you got from the http app as an authentication for the Domo app.

