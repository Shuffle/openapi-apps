## Trellix App
Trellix app to interact with Trellix systems using API access tokens for authentication.

## Actions

| No. | Action | Description | Parameters |
|-----|--------|-------------|------------|
| 1   | Fetch Incidents | Retrieves incidents from the Trellix system using the API. | `access_token`, **incidentId**, **startTime**, **endTime**, **pageSize** |
| 2   | Create Incident | Creates a new incident within the Trellix system. | `access_token`, **incidentType**, **description**, **severity** |
| 3   | Update Incident | Updates an existing incident with new information. | `access_token`, **incidentId**, **status**, **resolution** |
| 4   | Delete Incident | Deletes an incident from the system. | `access_token`, **incidentId** |
| 5   | Fetch Events for Incident | Retrieves events associated with a specific incident. | `access_token`, **incidentId** |

## Requirements

1. Trellix account with API access enabled.
2. Access token for authentication.

### How to Obtain the Access Token

You can request your API access token using one of the following methods:

#### 1. **Using cURL Command Line Tool**

To request an access token via the command line, use the following cURL request:

```bash
curl -k -X GET "https://<your_trellix_api_url>/hx/api/v3/token" -H "Accept: application/json" -u <username>:<password>
```

This will return an access token like the example below:

```json
{
  "access_token": "[YOU API KEY]",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

#### 2. **Using the API Documentation Module**

To generate an access token through the API Documentation Module:

1. **Login** to the Trellix Endpoint Security Web UI as an administrator.
2. From the **Modules menu**, select **API Documentation**.
3. In the **APIs** field, choose a category, such as **lighthouse**.
4. In the **AUTHENTICATION** section, enter your HTTP Basic **username** and **password** credentials, and click **Set**.
5. Expand the **Authentication** section from the API list and select the **Get** method. Click **Try** to test the request. 
6. If successful, the system will return your access token.

For more detailed instructions, refer to the official [Trellix API Documentation](https://docs.trellix.com/bundle/api_1-0-0_ug/page/configuring-the-api-documentation-module/api-authorization-and-authentication/access-token.html).
