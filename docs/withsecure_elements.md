# WithSecure Elements
WithSecure Elements is an EDR / XDR API you can connect to. [Documentation from the vendor](https://connect.withsecure.com/getting-started/elements/).

## Authentication
Authentication in WithSecure Elements is done using Oauth2 with Application Permissions. This means you need:

- A Token URL: https://api.connect.withsecure.com/as/token.oauth2
- Client ID
- Client Secret

You can find these in the WithSecure Elements portal by going under Management > Org Details > API Clients.  

<img width="533" alt="image" src="https://github.com/Shuffle/openapi-apps/assets/5719530/b48515af-307b-463b-abca-c63088cc4f7a">

From here, you can use the Client ID and Secret to authenticate the app in the Shuffle UI. 

<img width="339" alt="image" src="https://github.com/Shuffle/openapi-apps/assets/5719530/98479d28-d325-4dc3-b85b-7c21fc42435e">

After it's authenticated, try an action to see if you get a 200 OK. 

**PS: It may be necessary to change the Token URL in the App itself based on the tenant: https://shuffler.io/apps/withsecure_elements**










