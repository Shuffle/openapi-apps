# Checkpoint Smart Console API

### API Key Authentication

An API key is a token that a client provides when making API calls.

API key authentication provides an administrator the ability to use a token for authenticating to the API interface instead of using a the usual username / password.

### Configuring API key authentication for administrators

You can use [SmartConsole](https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_SecurityManagement_AdminGuide/Topics-SECMG/API-key-auth.htm#) to configure an API key for authenticating to the management API.

```
Note - The administrator can only use the API key for executing API commands and cannot use it for SmartConsole authentication.
```

To configure API authentication for an administrator in SmartConsole Example:

1. In SmartConsole click **Manage & Settings** > **Permissions & Administrators** > **Administrators**

2. Click the **New** icon at the top menu.

The **New Administrator** window opens.

2. Give the administrator a name

3. In the **Authentication Method** field select **API Key**.

4. Click [Generate API key](https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_SecurityManagement_AdminGuide/Resources/Images/Images-for-SECMG/api-auth.png).

![api-auth_thumb_0_113](https://user-images.githubusercontent.com/58112539/210101669-e894bae6-b306-4972-b4e1-35381511797d.png)

5. A new API key window opens.

  a. Click **Copy key to Clipboard**

  b. Save the key for a later use (provide it to the relevant administrator).

6. Click **OK**.

7. Publish the SmartConsole session.

### Example

This example demonstrates how to use the API-key for login and creating a simple-gateway using the API.

Log in to the Expert mode.

Use the previously generated key for the login, and save the standard output to a file (redirect it to a file using the ">" sign):

Syntax:
```
mgmt_cli login api-key <api-key> > /<Path_To>/<Filename>
```
Example:
```
mgmt_cli login api-key mvYSiHVmlJM+J0tu2FqGag12 > /var/tmp/token.txt
```
Run a mgmt_cli command, use the -s /<path_to>/<filename>flag

Syntax:
```
mgmt_cli -s /<Path_To>/<Filename> add simple-gateway name "<Name of Security Gateway Object>" ip-address <IP address> one-time-password <Password> <Name of Software Blade> true <Name of Software Blade> true ... <Name of Software Blade> true
```
Example:
```
mgmt_cli -s /var/tmp/token.txt add simple-gateway name "gw1" ip-address 192.168.3.181 one-time-password "aaaa" firewall true vpn true
```
For more details, see the [Check Point Management API Reference](https://sc1.checkpoint.com/documents/latest/APIs/index.html).

