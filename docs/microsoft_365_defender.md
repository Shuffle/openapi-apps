# Microsoft 365 Defender

To connect with and receive data and actions from Microsoft 365 Defender, you'll need to connect to it using Oauth2. 

In general, you’ll need to take the following steps to use the APIs:

- Create an Azure Active Directory (Azure AD) application.
- Get an access token using this application.
- Use the token to access Defender for Cloud Apps API.

### Authentication
To authenticate this app, you'll need an app registered in the Azure Portal. This app should use what's called **"application permissions"**, NOT "delegated permissions". More about this farther down. 

**Required**:
- tenant_id
- client_id
- client_secret

### Permissions 
Permissions are meant to be granular according to your needs. Make sure to not give too many permissions. To make the whole app work, add the following permissions to your app. How to register an app farther down.

**Application Permissions:** 

## How to register app in Active Directory on Azure portal

### Step 1: Go to the Azure portal

 - You'll need to go to the [Azure Portal](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) and login.

### Step 2: Go to the Azure Active Directory Service

 Navigate to Azure Active Directory > App registrations > New registration.


### Step 3: Register a New App

- Set the name of your choice.
- Set the redirect URI to https://shuffler.io/set_authentication (SaaS) or http://HOSTNAME:3443/set_authentcation for your local version.
- Click register on the bottom

![image](https://github.com/Shuffle/openapi-apps/assets/31187099/d48dd53b-93cb-47ae-bbb6-6811c40b8db4)


### Step 4: Set up certificates and permissions     

To enable your app to access Defender for Cloud Apps and assign it 'Read all alerts' permission, on your application page, select API Permissions > Add permission > APIs my organization uses >, type Microsoft Cloud App Security, and then select Microsoft Cloud App Security.

![image](https://github.com/Shuffle/openapi-apps/assets/31187099/28a83595-0cee-44fd-80cf-ce72ab51bdb7)


Select Application permissions > Investigation.Read, and then select Add permissions.

![image](https://github.com/Shuffle/openapi-apps/assets/31187099/cf379100-30bd-44c3-b658-6bf773bbb885)


You need to select the relevant permissions. To determine which permission you need, look at the Permissions section in the API you're interested to call. See [Supported Permissions Scopes](https://learn.microsoft.com/en-us/defender-cloud-apps/api-authentication-application#supported-permission-scopes)

Select Grant admin consent. Every time you add a permission, you must select Grant admin consent for it to take effect.

![image](https://github.com/Shuffle/openapi-apps/assets/31187099/37630f62-72e9-4da4-b680-88499c69d756)


Here are the parts that we'll need to configure. The Tenant ID and Client ID are available right away. 

![image](https://user-images.githubusercontent.com/5719530/181117491-cd5d242f-b2db-4b5c-bcf5-57c6a08a3e27.png)

Under "Certificates & Secrets" click "New client secret" and set a name you'll remember with a long expiration time (1 year+). Make sure to copy the VALUE of the key you've just got. It's relevant in the next step in Shuffle.

![image](https://user-images.githubusercontent.com/5719530/181117696-59125d90-b28d-481f-aed4-ad51b4def809.png)

With this done, go to the "API permissions" tab and click "Add a permission". From here select "Microsoft Graph" and "Application Permissions"

### Step 5: Activate and modify the app
Due to Microsoft API's using a tenant, we will need to modify the App slightly. This first requires us to [import (open source) or activate it (cloud)](https://shuffler.io/apps/d71641a57deeee8149df99080adebeb7). After this is done, go to /apps (Apps button), and find the app and click the "Edit" button.

Now that you're inside the app editor, scroll down the "Authentication" part. This is where you should add your tenant in both fields as outlined below.

![image](https://user-images.githubusercontent.com/5719530/181118637-90e65bb7-7aea-434c-a79c-30d599baa038.png)

When done, scroll all the way to the bottom of the page and click Save.

### Step 6: Using the prepared authentication
With all prepararration done, open up a Workflow (either new or one of our [public workflows](https://shuffler.io/workflows/828c3d2d-475b-454c-a6af-a241e708f0c7)). 

1. From the left side, drag in the Microsoft 365 Defender app
2. Click the app
3. Click the large orange "Authenticate Microsoft 365 Defender" button
4. Fill in the required fields that we prepared
5. Click the "Oauth2 Request" button!
