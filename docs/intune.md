# Intune

### Using the Microsoft Graph API

Intune provides data into the Microsoft Graph API in the same way as other cloud services do, with rich entity information and relationship navigation. Use the Microsoft Graph API to combine information from other services and Intune to build rich cross-service applications for IT professionals or end users.  

The following example shows how you can determine whether an application is installed on a user's device: 

* 1. Get from Azure Active Directory a list of devices registered to a user: 
(https://graph.microsoft.com/users/{user}/ownedDevices)[https://graph.microsoft.com/users/{user}/ownedDevices]

* 2. Then view the list of applications for your tenant: 

(https://graph.microsoft.com/deviceAppManagement/mobileApps)[https://graph.microsoft.com/deviceAppManagement/mobileApps]

* 3. Take the ID from the application and determine the installation state for the application (and therefore user): 

(https://graph.microsoft.com/deviceAppManagement/mobileApps/{id}/deviceStatuses/)[https://graph.microsoft.com/deviceAppManagement/mobileApps/{id}/deviceStatuses/]


# Accessing the Microsoft Graph API for Intune

Intune supports both (https://learn.microsoft.com/en-us/graph/auth-v2-user)[delegated permissions] and (https://learn.microsoft.com/en-us/graph/auth-v2-service)[application permissions]. Delegated and application permissions support both read and write operations. Delegated and application permissions support both single tenant applications, as well as multi-tenant applications. For more information about the permissions available through Microsoft Graph, see (https://learn.microsoft.com/en-us/graph/permissions-reference)[Microsoft Graph permissions reference].

# Using permissions

The Microsoft Graph API controls access to resources via permissions. As a developer, you must specify the permissions you need to access Intune resources. Typically, you specify the permissions in the Azure Active Directory portal. For more information, see (https://learn.microsoft.com/en-us/graph/permissions-reference)[Microsoft Graph permissions reference].

# Interaction between Microsoft Graph APIs for Windows updates

Microsoft Graph includes two sets of APIs that you can use to manage Windows updates:

* Intune APIs

* Windows updates APIs

You can use either API to manage Windows updates; however, these two APIs are not compatible with each other. Each can overwrite the configurations made by the other without providing visibility into that action. Use of both APIs to manage updates can result in unexpected behaviors, including what appears to be temporary configurations for update deployments that are canceled or modified without an identified cause.
