# Palo Alto XDR Incident Mgmt

## Authentication
The API requires three variables: 

- **API Key**: The API Key is your unique identifier used as the "Authorization:{key}" header required for authenticating API calls. Depending on your desired security level, you can generate two types of API keys, Advanced or Standard, from your Cortex XDR app.
- **API Key ID**: The API Key ID is your unique token used to authenticate the API Key. The header used when running an API call is "x-xdr-auth-id:{key_id}".
- **URL**:  The FQDN is a unique host and domain name associated with each tenant. When you generate the API Key and Key ID, you are assigned an individual FQDN.

More about how to authenticate here: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-API-Reference/Get-Started-with-APIs

