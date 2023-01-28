# IBM X-Force

## Authentication

You must have an IBM ID to use the XFE API. Register for an IBM ID at [IBM id registration](https://www.ibm.com/account/profile/us?page=reg). Once registered you will need to verify your account using the token in the e-mail message that you receive.

When verified, login to [X-Force Exchange](https://exchange.xforce.ibmcloud.com/) then follow these steps to generate a new API Key and Password:

1. View your Profile summary by clicking the User icon in the top right hand corner of the X-Force Exchange Home Page.

<img width="150" alt="user-profile" src="https://user-images.githubusercontent.com/58112539/215296308-8decce4b-9bc3-4f42-84fc-e311a0882ec1.png">

2. Click the Settings link in the lower left corner to view the Settings Page, then click the API Access link in the settings page to view the [API details page](https://exchange.xforce.ibmcloud.com/settings/api).

<img width="500" alt="user-settings" src="https://user-images.githubusercontent.com/58112539/215296314-4fc10f04-116e-4b12-a3cb-3c84848d2117.png">

3. Click the Generate button to create a new API Key and Password.

<img width="500" alt="user-settings-api-gen" src="https://user-images.githubusercontent.com/58112539/215296317-339376c2-eb33-45d5-8e52-857c0cfd083e.png">

Once you generate your password, makes sure to save it, as it is only shown when the key/password is generated. When you revisit your profile again, only the key is shown. Also, Your API key should not be shared, as it is specific to your ID. Finally, API keys and passwords do not expire. If you forget your password, you can generate a new API key/password pair.

Our API only allow HTTPS connections that support TLS protocol version 1.2 or newer. All other connections will be rejected.
