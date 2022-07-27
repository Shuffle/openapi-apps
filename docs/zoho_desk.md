# Zoho Desk
The app is to be used with Zoho desk, and uses Oauth2. To use it, we need to make an app in the Zoho portal.

## Set up auth
Go to https://api-console.zoho.com/ and Login. 

### 1. Set up client
After logged in, make a new app by clicking "Add Client". Make sure to select a new "Server based app". 

![image](https://user-images.githubusercontent.com/5719530/181389800-25c6f891-c1c0-4f68-8dde-41034f9afb7e.png)

Choose any name, and set the homepage to e.g. shuffler.io. Once done, set the redirect URL to your local instance (Onprem) or shuffler.io (cloud), and make sure to add /set_authentication on the end.

Example: https://IP:3443/set_authentication

![image](https://user-images.githubusercontent.com/5719530/181390004-4223bf60-cac0-4728-a80e-e382a934b707.png)

### 2. Find and use the auth
With the initial setup, we now have a client ID and secret. Make a new Workflow in Shuffle where we'll make use of them!

![image](https://user-images.githubusercontent.com/5719530/181390114-d589a8c4-4855-4ef8-9ffd-ac205693c774.png)

### 3. Authentication
After dragging in the node for Zoho Flow in a workflow in Shuffle, click it, then click the orange button "Authenticate" on the right side. This will show the following window. In this window, make sure to fill in these fields:

- Client ID
- Client Secret
- Scopes (e.g. Desk.Tickets.Read if you want to READ tickets). You can select multiple.

![image](https://user-images.githubusercontent.com/5719530/181390325-5f58b6fe-a3e9-44df-a223-60f0bf9b36c1.png)

When done, click the "OAuth2 request" button. This will make a new popup window show up. If all well, you'll see a little something like the below image. Once you accept this, it will redirect to Shuffle and add all the auth for you.

![image](https://user-images.githubusercontent.com/5719530/181390503-8229dd39-11c8-4c8b-9f8f-b1008ed00b83.png)

## Using the app
Once Authentication is done, you can actually use the app. The app will need an Organization ID in a header, which you can find in your organization on desk.zoho.com.









#### DEVELOPER NOTES FOR LEARNING MANUAL OAUTH2  
- Using 0auth with Zoho Desk.

This following content is based off of the Zoho Desk API documentation that can be found here: https://desk.zoho.com/DeskAPIDocument#OauthTokens#MakingTheAuthorizationRequest

Postman (https://www.postman.com/) was found to be very useful for building and organizing necessary Curl requests.

ngrok was also found to be useful for generating a redirect_uri that can be used.

Example to generate the redirect uri:

- Open terminal and run the command ngrok http 8080
- Copy the https:// one to use in a later step

1. Once you have your Zoho Desk instance available. Navigate to the Setup icon and select API under the Developer Space column.

2. Take note of the OrgId and it will be necessary later on.

3. Navigate to Zoho’s Developer Console which can be found here: https://api-console.zoho.com/ and follow the required steps in the Zoho Documentation to register a Web-based application. Once successful registration has taken place, take note of your client_id and client_secret.

The following is an example of the Query Params that successfully worked when placed in the browser to perform the authorization grant:

https://accounts.zoho.com/oauth/v2/auth?response_type=code&client_id=1000.TD0GSFCSZQU7S1T0G9RNYB1JE7T7RA&scope=Desk.tickets.READ,Desk.basic.READ&redirect_uri=https://3f6e-2600-1700-17c0-8740-66bc-debf-b1e0-1510.ngrok.io&access_type=offline

When successful, you will see an accept or reject button. Take note that after clicking accept you will then be provided the grant token in the URL bar of your browser.

4. At this point you should have the following information that will be necessary to build our request for an access token:

(Examples)
code: 1000.9532bca3ee9d6c8c0dc495322a059b22.bc86bd119b24d11c123a4567d589d1
client_id: 1000.TD0GSFCSZQU7S1T0G9RNYB1JE7T7RA
client_secret: 8b36ddb237ba1ff9be0297fbf04d61bf2a585b2143
redirect_uri: https://3f6e-2600-1700-17c0-8740-66bc-debf-b1e0-1510.ngrok.io

5. Using Postman the following example Curl command using POST method returned successful results, providing the access_token and refresh_token.

Example:

curl -X POST https://accounts.zoho.com/oauth/v2/token?code=1000.9532bca3ee9d6c8c0dc495322a059b22.bc86bd119b24d11c123a4567d589d1&grant_type=authorization_code&client_id=1000.TD0GSFCSZQU7S1T0G9RNYB1JE7T7RA&client_secret=8b36ddb237ba1ff9be0297fbf04d61bf2a585b2143&redirect_uri=https://3f6e-2600-1700-17c0-8740-66bc-debf-b1e0-1510.ngrok.io

6. At this point we can use the refresh token we generated in the last step to create a Curl request to refresh our Oauth token rather than having to generate a grant token like we did at the beginning of the process for every time we want to use the API.

Example:

curl -X POST https://accounts.zoho.com/oauth/v2/token?refresh_token=1000.ac204c137f5c5a52cb5557f427b46e40.ee7c2647062d7228a30e92346516c498&client_id=1000.TD0GSFCSZQU7S1T0G9RNYB1JE7T7RA&client_secret=8b36ddb237ba1ff9be0297fbf04d61bf2a585b2143&scope=Desk.tickets.READ,Desk.basic.READ&redirect_uri=https://3f6e-2600-1700-17c0-8740-66bc-debf-b1e0-1510.ngrok.io&grant_type=refresh_token 

7. Now that we have our access_token and refresh_token in place, we can start using the API. The following is a request that performed a successful GET request returning the existing tickets in the Zoho Desk instance.

curl -X GET "https://desk.zoho.com/api/v1/tickets" -H "orgId:767307793" -H "Authorization:Zoho-oauthtoken 1000.706709335250bb3d02de98da2ac065fa.e8a94fb3cd6ddb60d897dad4d06da66f"





