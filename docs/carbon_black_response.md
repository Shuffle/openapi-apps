# Carbon Black Response

### REST API Authentication

Carbon Black EDR (Endpoint Detection and Response) is the new name for the product formerly called CB Response.

Each EDR user has a personal API key. That API key confers all rights and capabilities assigned to that user to anyone possessing the API key. Therefore, treat your API key as you would your password. If the API Token is missing or compromised, you can reset the API key to generate a new token and revoke any previous API keys issued to a user.

To find a API key corresponding with a particular Carbon Black user account, log into the console as that user, then click the username in the upper right -> Profile info.

![image](https://user-images.githubusercontent.com/58112539/192383514-32b5765a-39bb-4226-98c5-06c1372fd874.png)

Then, click the “API Token” button on the left hand side to reveal the API token for the logged-in user. If there is no API token displayed, click the “Reset” button to create a new one.

![image](https://user-images.githubusercontent.com/58112539/192383560-0c5ea842-8d95-4b1b-9a4d-0788bc3abdfe.png)
