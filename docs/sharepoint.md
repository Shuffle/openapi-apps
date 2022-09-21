# Microsoft Graph
To connect with and receive emails from Office365, you'll need to connect to it using Oauth2. This app can get and update emails as you wish, and will be expanded over time to handle all relevant Microsoft Graph API's.

### Authentication
To authenticate this app, you'll need an app registered in the Azure Portal. This app should use what's called **"delegated permissions"**, NOT "application permissions". More about this farther down. 

**Required**:
- tenant_id
- client_id
- client_secret

### Permissions 
Permissions are meant to be granular according to your needs. Make sure to not give too many permissions. To make the whole app work, add the following permissions to your app. How to register an app farther down.

**Application Permissions:** 

## How to register app in Active Directory on Azure portal ?

### Step 1: Go to the Azure portal

 - You'll need to go to the [Azure Portal](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) and login.

### Step 2: Go to the Azure Active Directory Service

- Once you are logged into Azure, Register a new application so you can access
the Microsoft Graph API. To register a new application go to your **Azure Active Directory**
and once there go down to **App Registrations** a new window will pop up.

### Step 3: Register a New App
- Set the name of your choice.
- Set the redirect URI to https://shuffler.io/set_authentication (SaaS) or http://HOSTNAME:3443/set_authentcation for your local version.
- Click register on the bottom

![image](https://user-images.githubusercontent.com/5719530/181117189-51f33764-3486-456f-a821-66b89db7c4c2.png)

### Step 4: Set up certificates and permissions
Here are the parts that we'll need to configure. The Tenant ID and Client ID are available right away. 

![image](https://user-images.githubusercontent.com/5719530/181117491-cd5d242f-b2db-4b5c-bcf5-57c6a08a3e27.png)

Under "Certificates & Secrets" click "New client secret" and set a name you'll remember with a long expiration time (1 year+). Make sure to copy the VALUE of the key you've just got. It's relevant in the next step in Shuffle.

![image](https://user-images.githubusercontent.com/5719530/181117696-59125d90-b28d-481f-aed4-ad51b4def809.png)

With this done, go to the "API permissions" tab and click "Add a permission". From here select "Microsoft Graph" and "Delegated Permissions"

![image](https://user-images.githubusercontent.com/5719530/181117885-eb0db1b8-fe2f-47a1-b778-8bcf09bb4a39.png)

Now search for "Mail" and select "Mail.ReadWrite" (come back for any permission you may need later.

### Step 4: Activate and mdify the app
Due to Microsoft API's using a tenant, we will need to modify the App slightly. This first requires us to [import (open source) or activate it (cloud)](https://shuffler.io/apps/d71641a57deeee8149df99080adebeb7). After this is done, go to /apps (Apps button), and find the app and click the "Edit" button.

![image](https://user-images.githubusercontent.com/5719530/181118510-654f42a8-5636-4443-9aac-5eac5d7b6e0a.png)

Now that you're inside the app editor, scroll down the "Authentication" part. This is where you should add your tenant in both fields as outlined below.

![image](https://user-images.githubusercontent.com/5719530/181118637-90e65bb7-7aea-434c-a79c-30d599baa038.png)

When done, scroll all the way to the bottom of the page and click Save.

### Step 5: Using the prepared authentication
With all prepararration done, open up a Workflow (either new or one of our [public workflows](https://shuffler.io/workflows/828c3d2d-475b-454c-a6af-a241e708f0c7)). 

1. From the left side, drag in the Outlook Graph app
2. Click the app
3. Click the large orange "Authenticate Outlook Graph" button
4. Fill in the required fields that we prepared
5. Click the "Oauth2 Request" button!

![image](https://user-images.githubusercontent.com/5719530/181119221-ddbc3c2d-b64b-4b76-b65f-d74cae00a96d.png)

Once this is clicked, you'll see a login window. Make sure to login the account you want to read or send emails from. You will eventually be redirected back to Shuffle, and the window will close as the authentication is added to Shuffle automatically.

PS: If you had any trouble with any of these steps, please [contact us](https://shuffler.io/contact) or ask on [Discord](ttps://discord.gg/B2CBzUm) for help.

### Step 6: Using the app
You can now use it to your liking. Don't be afraid of [adding more API](https://developer.microsoft.com/en-us/graph/graph-explorer)'s to it and playing around with the Graph API and its permissions!
