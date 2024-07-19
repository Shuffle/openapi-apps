# Microsoft Sentinel
Previously called Azure Sentinel. 


## Usage Overview 
Make sure that an api-version query is always present. The below is the default used for this app.
```
api-version=2021-10-01
```

Our suggestion: Start with the 

## Authentication
This app supports auto-authentication (cloud), but may require admin consent to work.

To authenticate, we need these fields:
- Tenant ID
- Client ID
- Client Secret
- Subscription ID
- Resource Group Name
- Workspace Name

We'll dig into where to find each of these.

![image](https://user-images.githubusercontent.com/5719530/200817491-a12b8b4d-f1a1-42a1-9f2e-709cb6398aa1.png)


### Subscription ID
1. Sign in to the Azure portal.
2. Under the Azure services heading, select Subscriptions. If you don't see Subscriptions here, use the search box to find it.
3. Find the Subscription ID for the subscription shown in the second column. If no subscriptions appear, or you don't see the right one, you may need to switch directories to show the subscriptions from a different Azure AD tenant.
4. Copy the Subscription ID. You can paste this value into a text document or other location.

Sample: e30ef9e0-d830-40fb-92c7-b5952a40b046

### Resource Group Name
Go to https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/microsoft.securityinsightsarg%2Fsentinel
The name should be under the resource group name column for your Microsoft Sentinel.

Sample: cloud-shell-storage-westeurope

### Workspace Name
Find the workspace name in the same location as the Resource Group Name:
https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/microsoft.securityinsightsarg%2Fsentinel
It should be the "name" for the setup of your Microsoft Sentinel

Sample: shuffle


# Authorization
The application needs access. Here's how: 

1. You need to log into your Azure Active Directory and click on "App registrations" to register the app. Name it, if asked for type of application choose web and 
   click on "Register".
2. Api permissions > Add a permission > Select an API > Log Analytics API > Application permissions
  ![image](https://github.com/Shuffle/openapi-apps/assets/31187099/31460b84-06fd-478a-9602-479e938a99a5)
3. Ensure Data.Read is selected > Add permissions
4. You will also need some Microsoft graph API permissions, still in Api permissions > Add a permission > Microsoft graph > Application permission. You will need the following permissions:
   - SecurityActions.ReadWrite.All
   - SecurityAlert.ReadWrite.All
   - SecurityEvents.ReadWrite.All
   - SecurityIncident.ReadWrite.All
       
   ![image](https://github.com/Shuffle/openapi-apps/assets/31187099/b66fdbbd-d5d8-4315-971b-467123cfae28)
6. Your applications current configuration page should look similar to this once admin premissions have been granted. Click "Grant admin consent" for the app to work > Click "Yes"
   ![image](https://github.com/Shuffle/openapi-apps/assets/31187099/88b7fea2-28a2-4645-a7b1-389df5c5280e)
   ![image](https://github.com/user-attachments/assets/facff167-52bc-4df9-9b94-3970b0164dac)
8. Our next step is to move on to the "Certificates & secrets" so the application can be authenticated on the Shuffle-side.> Click "+ New client secret". > Click 
   "+ New client secret".
   ![image](https://github.com/Shuffle/openapi-apps/assets/31187099/944cc5ac-dad3-4b0a-b947-0af7e1c63c03)
9. You will want to copy the value of this secret. You will need it later when you test your API connection to your Sentinel's Workspace.
   ![image](https://github.com/Shuffle/openapi-apps/assets/31187099/069e19d4-7b67-43a6-99b1-7cefbcdf672e)
10. For your other required credentials > Overview while still in your app.
   ![image](https://github.com/Shuffle/openapi-apps/assets/31187099/0ccff3d0-779f-4d83-b6b7-46d991b34f7f)
11. Now all that remains is giving the AAD Application permissions to your Sentinel Workspace
-  Let's start by finding your Sentinel Workspace resource within your Azure Portal.
  ![image](https://github.com/Shuffle/openapi-apps/assets/31187099/ca489ee4-7685-4ad3-98da-ce01a8c332d6)
- Scroll down to Settings > Workspace settings > Access Control (IAM) > click "+ Add" > Add role assignment
- Under role, select search for ```Log Analytics Reader``` > click "Next"
  ![image](https://github.com/Shuffle/openapi-apps/assets/31187099/c8584b39-bbfd-4f1f-b5f8-712140ff75b7)
- Under members, click "+ Select members" > In the search bar look for the app you made in step one above by name > Click on it and then click "Review + assign"
  ![image](https://github.com/Shuffle/openapi-apps/assets/31187099/3051d822-fc05-4f97-94da-916fa310a184)
 

   
   
