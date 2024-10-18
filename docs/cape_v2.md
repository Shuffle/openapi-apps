# CAPEv2
This documentation will cover the authentication process.

## Authentication

The **CAPE v2 app** requires an API key to authenticate and interact with the CAPE API. To use this app, ensure a CAPE instance is running with API access enabled.

### Required Fields:
- **API Key**: This is the authentication token your CAPEv2 instance generates.
- **Base URL**: Your CAPEv2 instance's URL typically ends with `/apiv2/`.

### Steps to Obtain the API Key

1. **Login to CAPEv2**:
   - Navigate to your CAPEv2 instance and log in with an administrative account.

2. **Generate API Key**:
   - Go to **User Settings** or **API Access** under your account settings.
   - Select **Generate API Key**. 
   - Copy the API key and store it securely in the app.

3. **Base URL**:
   - The base URL is the address of your CAPE instance followed by `/apiv2/`.
   - Example: `http://<your-cape-instance-ip>/apiv2/`.

## Error Codes

The following error codes are common when interacting with the CAPE v2 API:

- **400 Bad Request**: The request was malformed or missing required fields.
- **401 Unauthorized**: Invalid or missing API key.
- **404 Not Found**: The requested task or resource does not exist.
- **500 Internal Server Error**: A server error occurred on the CAPE instance.

This documentation provides a basic overview of using the CAPEv2 tool for automating malware analysis using CAPE's API. Please look at the official [CAPE API documentation](https://github.com/kevoreilly/CAPEv2/blob/master/docs/book/src/usage/api.rst) for more detailed API documentation.

