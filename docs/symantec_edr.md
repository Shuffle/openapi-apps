# Symantec EDR
Shuffle integration for Symantec EDR.
### Authentication
This Symantec EDR APIs uses oauth2 authentication mechanism. Follow the below steps to authenticate Symantec EDR with Shuffle.
**Step 1:** Go to shuffle workflow and create a new workflow. Drag in the Symantec EDR app and select "Get Token" action. Use client ID and Client Secret as a username and password in action parameter. Now you'll receive following payload in response.
```json
{ 
 "access_token":"eyJraWQiOiI...MThXmQ",
   "token_type":"Bearer",
   "expires_in":3600
}
```
**Step 2:** Now select the action you want to use from action list and send in the "access_token" in this action's header as "Authorization: Bearer {access_token}"

