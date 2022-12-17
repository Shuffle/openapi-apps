# Sophos Central 

### API

This guide takes you through a few simple steps to get authenticated and start calling Sophos Central APIs.

At the end of this guide, you will have:

1. Created a "service principal"
2. Authenticated using your new credentials
3. Discovered the UUID assigned to you by Sophos
4. Enumerated the "tenants" you manage
5. Retrieved the list of endpoints for each tenant
A "service principal" is a set of credentials that can be used to authenticate and call APIs.

A "tenant" is a collection of resources such as devices, events, policies and people. You can read more about this in the [documentation](https://developer.sophos.com/intro) under the "Partners, organizations and tenants" section.

### Step 1 - Create a service principal
We will show you how you can sign in to Sophos Central Partner and create a service principal.

Step 1a - Sophos Central Partner
Sign in to Sophos Central Partner. Go to [https://central.sophos.com/manage/partner](https://central.sophos.com/manage/partner).

Click 'Settings & Policies' and then click the "API Credentials" link.

![image](https://user-images.githubusercontent.com/58112539/197648263-a1e34508-9b2d-442c-ae80-4ccebb9b9e0d.png)

![image](https://user-images.githubusercontent.com/58112539/197648296-a45bd5c8-4468-4bad-946a-4cf5fd1bd4b0.png)

Step 1b - Add a new set of credentials

Supply a name for your credential set and a description, then click 'Add'.

![image](https://user-images.githubusercontent.com/58112539/197648306-91d4b8df-7478-4958-9af0-5f14f061267e.png)

Note: To delete these credentials later, after you no longer need them, click on the entry in the credentials list to open the details view, then click 'Delete'. Next, click 'Delete' in the popup dialog to confirm deletion.

![image](https://user-images.githubusercontent.com/58112539/197648317-893d72ca-239e-41c0-ac10-689a8b314eff.png)

Step 1c - Grab your client ID and secret

Click 'Copy' to note down the client ID. Also show the client secret.

![image](https://user-images.githubusercontent.com/58112539/197648331-3bf0a3fa-ad6b-4c82-aba3-f896ac6e4c40.png)

Click 'Copy' to note down the client secret.

![image](https://user-images.githubusercontent.com/58112539/197648346-13797fd1-c2e9-459d-a7ca-e4a53362ae34.png)

⚠️ WARNING: It is your responsibility to store your client ID and secret securely. If these are lost or stolen, an attacker will be able to call APIs on your behalf and steal your data or cause damage.

Now you are ready to start calling APIs.
