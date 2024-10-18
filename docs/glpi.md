# GLPI
This documentation covers the authentication process with the GLPI tool.

## Authentication

To use the GLPI API through this app, you need an API token from your GLPI instance. Just so you know – authentication is done via this token, which you must include in request.

### Required Fields for Authentication:
- **API Token**: This is the API key you generate from your GLPI instance.
- **Base URL**: The URL of your GLPI instance, ending with `/apirest.php`.

### Steps to Obtain the API Token

1. **Login to GLPI**:
   - Access your GLPI instance and log in with an administrator account.

2. **Generate API Token**:
   - Navigate to the **API Setup** section under **Administration > Users**.
   - Select the user for whom you wish to generate the API token or create a new one.
   - Enable user API access and generate an API token.
   - **Copy** the token and keep it secure, as it will be used for authentication in the app.

3. **Base URL**:
   - The base URL should be your GLPI instance followed by `/apirest.php`.
   - Example: `https://<your-glpi-instance>/apirest.php`.
  
## Error Codes

The following error codes are common when interacting with the CAPE v2 API:

- **400 Bad Request**: The request was malformed or missing required fields.
- **401 Unauthorized**: Invalid or missing API key.
- **404 Not Found**: The requested task or resource does not exist.
- **500 Internal Server Error**: A server error occurred on the CAPE instance.

For more detailed API documentation, please refer to the [GLPI API Documentation](https://github.com/ramylson/glpi/blob/master/glpi/apirest.md).

