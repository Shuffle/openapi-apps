# CrowdStrike API Access 

The CrowdStrike API is managed from the CrowdStrike Falcon UI by the Falcon Administrator. From there, multiple API clients can be defined along with their required scope. The scopes below define the access options.

* Detections – Provides access to Falcon detections, including behavior, severity, host, timestamps, and more.

* Hosts – Provides host details including OS, version, sensor specific data, and more.

* Host groups – Provides access to host groups used to enumerate and assign policies.

* Prevention policies – Provides access to sensor policies for external management.

* Sensor update policies – Provides access to update settings for the sensor.

* User management – Allows for the management of users who access the CrowdStrike Falcon UI.

Once an API client is defined and a scope is set, any number of customer tools can query the CrowdStrike API using the given credentials. OAuth2 is used for authentication of the incoming API requests. OAuth2 access tokens have a validity period of 30 minutes. The diagram below illustrates the typical application calls made to the API. First, the Access Token must be requested first, and then subsequent requests include the Access Token in the Authorization header.

### Defining your first API Client

To define a CrowdStrike API client, you must be designated as Falcon Administrator role to view, create, or modify API clients or keys. Secrets are only shown when a new API Client is created or when it is reset.

When logged into the Falcon UI, navigate to Support > API Clients and Keys. From there you can view existing clients, add new API clients, or view the audit log. When you click “Add new API Client” you will be prompted to give a descriptive name and select the appropriate API scopes. After you click save, you will be presented with the Client ID and Client Secret. The secret will only be shown once and should be stored in a secure place. If the Client Secret is lost, a reset must be performed and any applications relying on the Client Secret will need to be updated with the new credentials.

![api-clients-1](https://user-images.githubusercontent.com/58112539/191856590-d60ed0fd-3d4e-47d5-b309-985f6cb97890.png)

![new-api-client-2](https://user-images.githubusercontent.com/58112539/191856604-e4274c8c-4ef8-4465-ab2d-4e01272c9a6b.png)

### Testing the API

CrowdStrike provides access to Swagger for API documentation purposes and to simplify the development process.

Each CrowdStrike cloud environment has a unique Swagger page. Please refer to the [CrowdStrike OAuth2-Based APIs](https://falcon.crowdstrike.com/documentation/46/crowdstrike-oauth2-based-apis) documentation for your cloud environment
