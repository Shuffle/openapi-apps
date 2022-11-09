# Microsoft Sentinel
Previously called Azure Sentinel.

## Authentication
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
Sign in to the Azure portal.
Under the Azure services heading, select Subscriptions. If you don't see Subscriptions here, use the search box to find it.
Find the Subscription ID for the subscription shown in the second column. If no subscriptions appear, or you don't see the right one, you may need to switch directories to show the subscriptions from a different Azure AD tenant.
Copy the Subscription ID. You can paste this value into a text document or other location.

e30ef9e0-d830-40fb-92c7-b5952a40b046

### Resource Group Name
Go to https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/microsoft.securityinsightsarg%2Fsentinel
The name should be under the resource group name column for your Microsoft Sentinel.

cloud-shell-storage-westeurope

### Workspace Name
Find the workspace name in the same location as the Resource Group Name:
https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/microsoft.securityinsightsarg%2Fsentinel
It should be the "name" for the setup of your Microsoft Sentinel

shuffle


# Authorization
The application needs access. Here's how: TBA
