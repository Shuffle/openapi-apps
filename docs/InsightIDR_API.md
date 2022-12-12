# InsightDR API
### Managing Platform API Keys

An application programming interface key, or API key, allows you to set up access to the Insight platform. The API key is a unique identifier that serves as a form of authentication when you make calls to our API. In order to share data between your security applications and the Insight platform, you’ll need to generate an API key.

There are two types of platform API keys:

**User key** - Represents a specific user in an organization. This type of key can only be created by a user and inherits the permissions of the user. You cannot generate a user key for other users.

**Organization key** - Represents an entire organization and is a super key. This type of key can do everything across all products. You can only generate an organization key if you are a platform or organization administrator.

### API keys based on your Insight account role

API key generation capabilities depend on your account role on the Insight platform. Find your account role in the following table to determine the type of key you can generate.

| Role                   | Permissions |
| ---------------------- | ----------- |
| Platform administrator | You can generate, view, and manage API keys across all organizations. |
| Organization administrator | You can only generate, view, and manage API keys within your assigned organization. |
| User | You can only generate, view, and manage your own keys. |

### Generate an organization key

A platform or organization administrator can generate an organization key. You will need to copy the key immediately after you generate it. You will not be able to retrieve the key again after you navigate away from it.

**To generate an organization key:**

1. Log in to your Insight account.
2. After you’ve logged in, go to the “API Keys” page.
3. From the “API Keys” page, go to the “Organization Keys” tab and click the New Organization Key button.
4. When the “Generate New Organization Key” panel appears, select an organization and provide a name for the key.
5. Generate the key. A new window opens and displays the generated key.
6. Copy the key. You will not be able to view it again after you close the window.

![Screen Shot 2018-10-22 at 2 38 02 PM](https://user-images.githubusercontent.com/58112539/203650834-08c32e23-8c34-4979-a81d-cfa3ddfd7def.png)

### Generating a user key

Any user can generate a user key. A user key will inherit your account’s permissions, so anything you can do, your API key can do. Just remember that you need to copy the key immediately after you generate it. You will not be able to retrieve the key if you don't.

**To generate a user key:**

1. Log in to your Insight account.
2. After you’ve logged in, go to the “API Keys” page.
3. From the “API Keys” page, click the New User Key button.
4. When the Generate New User Key panel appears, select an organization and provide a name for the key.
5. Generate the key. A new window opens and displays the generated key.
6. Copy the key. You will not be able to view it again after you close the window.

![Screen Shot 2018-10-22 at 2 43 03 PM](https://user-images.githubusercontent.com/58112539/203651109-f08ac3dd-5733-46c3-ad40-cee27815fce9.png)

### View API keys

To see a list of API keys that are viewable to you, log into your Insight account and go to the “API Keys” page. The keys you can view depend on your role on the Insight platform.

The following table shows what each role should be able to view:

| Role                   | Access |
| ---------------------- | ----------- |
| User | You’ll only be able to see your own API keys. |
| Organization admin | You’ll be able to see all of the API keys for your assigned organization. |
| Platform admin | You’ll be able to see all of the API keys across all organizations. |

### Revoke an API key

Revoking an API key removes it from the Insight platform and makes it inaccessible to its owner. This action is permanent. You cannot revert this action, so please make sure that you are not removing any keys that other users may need.

To revoke a key, log in to your Insight account. Go to the “API Keys” page, find the key you want to revoke, and click the Delete button. Confirm that you want to revoke the key.

Please note that deleting a user’s account does not delete organization keys that they’ve generated; it only removes their user keys. If you are deleting a user, and you also want to delete their organization keys, you will need to go to the “API Keys” page and manually remove their keys.

### Changes to account permissions

Changes to your account’s permissions may affect your ability to view and manage API keys.

For example, if you created an organization API key, and your role changes to read/write only, you will no longer be able to manage the key. You’ll need to contact a platform administrator if you need to make changes to that key.
