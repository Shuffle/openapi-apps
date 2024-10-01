# Microsoft Dynamics 365

The **Microsoft Dynamics 365** app allows interaction with Microsoft Dynamics APIs like financial, CRM, and ERP services, enabling automation via Shuffle SOAR. 
The app uses **OAuth 2.0** authentication for secure access.

### Notes:
- **access_token** is mandatory for all actions and must be obtained through **OAuth 2.0** authentication.

## Prerequisites

1. **Azure Active Directory (Azure AD)**: Register an application in Azure AD.
2. **Microsoft Dynamics 365 Access**: Ensure API permissions are granted.

## Authentication

The **Microsoft Dynamics 365** app uses **OAuth 2.0** authentication. Follow the steps below to configure your app and obtain the access token required for API calls.

### Step 1: Register the App in Azure AD

1. Go to the [Azure Portal](https://portal.azure.com).
2. Navigate to **Azure Active Directory** > **App registrations** > **New registration**.
3. Provide a **name** for your app and specify the **Redirect URI** (https://shuffler.io/set_authentication (SaaS) or http://HOSTNAME:3443/set_authentcation for your local version).
4. Copy the **Application (client) ID** and **Directory (tenant) ID** after registration.

### Step 2: Configure API Permissions

1. Go to your app's **API permissions**.
2. Click **Add a permission** > **APIs my organization uses**.
3. Choose **Dynamics 365 Business Central**, then add relevant permissions (e.g., `Financials.ReadWrite.All`).
4. Grant **admin consent** for these permissions.

### Step 3: Generate Client Secret

1. In your Azure app, go to **Certificates & Secrets**.
2. Create a new **client secret** and copy the secret value. This will be used during authentication.

### Step 4: Obtain Access Token

To interact with the Microsoft Dynamics 365 API, you need to obtain an **access token** by making a `POST` request to the OAuth 2.0 token endpoint:
```
POST https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token
```
Request body example:
```
client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials&scope=https://api.businesscentral.dynamics.com/.default
The response will contain an access_token, which is required for all subsequent API calls.
```
### Step 5: Use Access Token in API Requests
Include the access token in the Authorization header of all API requests. Example:
```
curl -X GET https://api.businesscentral.dynamics.com/v2.0/{tenant_id}/api/v2.0/companies \
-H "Authorization: Bearer {access_token}"
```
