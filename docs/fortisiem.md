# FortiSIEM
FortiSIEM app to interact with FortiSIEM from Shuffle.

__Note__:
- **access_key**, **secret_key**, and **fqdn** (Fully Qualified Domain Name) are used for authentication.
- **Bold** parameters are compulsory required.
- *Italic* parameters can take a single value as well as multiple values in a comma-separated manner (E.g., value1,value2,value3).

## Authentication

1. **FortiSIEM** account.
2. **Access key**, **Secret key**, and **FQDN** (Fully Qualified Domain Name) of the FortiSIEM system.

### How to obtain the Access Key and Secret Key:
1. Log in to your FortiSIEM instance.
2. Go to **Admin** > **API Settings**.
3. Generate and copy the **API Key** (access key and secret key).
4. Ensure that your API key has appropriate permissions for accessing or modifying incidents, users, and other system settings.
