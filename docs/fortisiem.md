## FortiSIEM
FortiSIEM app to interact with FortiSIEM from Shuffle.

## Actions

| No. | Action | Description | Parameters |
|-----|--------|-------------|------------|
| 1   | **Fetch Incidents**  | Retrieves incidents from FortiSIEM based on provided filters and returns a list of incidents. | **access_key**, **secret_key**, **fqdn**, start_time, end_time, filter, limit, **DryRun** |
| 2   | **Create Incident**  | Allows the creation of an incident in FortiSIEM based on the provided information. | **access_key**, **secret_key**, **fqdn**, **incident_name**, description, severity, **DryRun** |
| 3   | **Update Incident**  | Updates the details of a specific incident in FortiSIEM. | **access_key**, **secret_key**, **fqdn**, **incident_id**, description, status, severity, **DryRun** |
| 4   | **Close Incident**   | Closes a specific incident in FortiSIEM based on the provided incident ID. | **access_key**, **secret_key**, **fqdn**, **incident_id**, closure_reason, **DryRun** |
| 5   | **Get Incident Status** | Retrieves the status of a specific incident from FortiSIEM. | **access_key**, **secret_key**, **fqdn**, **incident_id**, **DryRun** |
| 6   | **List Users**       | Lists all users in the FortiSIEM system with optional filters. | **access_key**, **secret_key**, **fqdn**, filter, limit, **DryRun** |
| 7   | **Create User**      | Creates a new user in FortiSIEM with the provided details. | **access_key**, **secret_key**, **fqdn**, **username**, email, role, **DryRun** |
| 8   | **Update User**      | Updates the details of an existing user in FortiSIEM. | **access_key**, **secret_key**, **fqdn**, **username**, email, role, **DryRun** |
| 9   | **Delete User**      | Deletes a specific user from FortiSIEM. | **access_key**, **secret_key**, **fqdn**, **username**, **DryRun** |
| 10  | **Get User Info**    | Retrieves information of a specific user based on the username. | **access_key**, **secret_key**, **fqdn**, **username**, **DryRun** |

__Note__:
- **access_key**, **secret_key**, and **fqdn** (Fully Qualified Domain Name) are used for authentication.
- **Bold** parameters are compulsory required.
- *Italic* parameters can take a single value as well as multiple values in a comma-separated manner (E.g., value1,value2,value3).

## Requirements

1. **FortiSIEM** account.
2. **Access key**, **Secret key**, and **FQDN** (Fully Qualified Domain Name) of the FortiSIEM system.

### How to obtain the Access Key and Secret Key:
1. Log in to your FortiSIEM instance.
2. Go to **Admin** > **API Settings**.
3. Generate and copy the **API Key** (access key and secret key).
4. Ensure that your API key has appropriate permissions for accessing or modifying incidents, users, and other system settings.
