# Gmail docs
The gmail app is used to read and send email messages using Gmail. It uses Oauth2 to connect, and has all their API abilities. You can connect this to either one mailbox or multiple.

[Click for a sample workflow](https://shuffler.io/workflows/e506060f-0c58-4f95-a0b8-f671103d78e5)

## Authentication
To connect to Gmail, use Oauth2. This requires two external things:
- A client ID
- A client secret

To get these, follow this guide from Google https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid

**PS: Remember to set the App in Google Cloud to Production, otherwise refresh tokens may time out after some time**

When you have them, fill them in as such:
![image](https://user-images.githubusercontent.com/5719530/160306577-9fc973ab-328f-4005-a036-43589a2e2690.png)

Then find the right scope. These three allow for most of what you want to do with Gmail.
![image](https://user-images.githubusercontent.com/5719530/160306410-99df4d2a-1d35-462b-ab34-289eaa53f393.png)

And remember to unselect this button, as it's not needed for Gmail.
![image](https://user-images.githubusercontent.com/5719530/160306424-f662f8c3-87e0-40ec-a321-9589596575db.png)

Now click the authenticate button! This will take you through a sign-in page of your gmail account. With the right delegation, one user can read all mailboxes.

