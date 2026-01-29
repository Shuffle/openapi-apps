# Gmail docs
The gmail app is used to read and send email messages using Gmail. It uses Oauth2 to connect, and has all their API abilities. You can connect this to either one mailbox or multiple.

[Click for a sample workflow](https://shuffler.io/workflows/e506060f-0c58-4f95-a0b8-f671103d78e5)

## Authentication
To connect to Gmail, use Oauth2. This requires two external things:
- A client ID
- A client secret

To get these, follow this guide from Google [https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid)

**PS: The App in Google Cloud needs to be in EXTERNAL mode, and be set to Production. Refresh Tokens WILL time out after some time otherwise.**

![image](https://github.com/Shuffle/openapi-apps/assets/5719530/e5830e85-b3bf-4f8c-9047-99ea66b110cd)

When you have them, fill them in as such:
![image](https://user-images.githubusercontent.com/5719530/160306577-9fc973ab-328f-4005-a036-43589a2e2690.png)

Then find the right scope. These three allow for most of what you want to do with Gmail.
![image](https://user-images.githubusercontent.com/5719530/160306410-99df4d2a-1d35-462b-ab34-289eaa53f393.png)

Now click the authenticate button! This will take you through a sign-in page of your gmail account. With the right delegation, one user can read all mailboxes.

--

## Client ID & Client Secret
To get Client ID and Client Secret, get your credentials [here](https://console.cloud.google.com/apis/credentials?referrer=search&project=shuffler). 

Need more help? See [Google's guide](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid).

## Scopes
Scopes allows your to set what you’re allowed to do with gmail.

**Default Scope** is set automatically when specified scopes have not been selected.

The Default Scope includes:
![image](https://user-images.githubusercontent.com/5719530/160306410-99df4d2a-1d35-462b-ab34-289eaa53f393.png)

## Ready to Authenticate!
Now click the authenticate button!

This will take you through a sign-in page of your gmail account. With the right delegation, one user can read all mailboxes.


