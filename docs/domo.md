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
- Select curl action and add following into curl statment
 ```
curl -v -u your_client_id:your_client_secret "https://api.domo.com/oauth/token?grant_type=client_credentials&scope=data%20dashboard"
```
- Run the workflow and you'll get an access token in response.

### Step 3: Use access token
- Now use access token you got from the http app as an authentication for the Domo app.

