# Set up auth
https://api-console.zoho.com/

Make the app **server auth**

# Using 0auth with Zoho Desk.

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





