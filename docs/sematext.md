This docs explains how to authenticate with the Sematext.

## Base URL
The base URL for Sematext API requests depends on your region. Common base URLs include:
- `https://logs.spm-api.eu/api/v3/` (Europe)
- `https://logs.sematext.com/api/v3/` (US)

## Authentication Method
Authentication is done using an API access token, which should be included in the request headers.

## Authentication Request
To authenticate and retrieve a list of applications, use the following `curl` command:

```sh
curl -X GET "https://logs.spm-api.eu/api/v3/apps" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Accept: application/json"
```

### Parameters:
- **Authorization Header**: Pass the API access token using `Bearer YOUR_ACCESS_TOKEN`.
- **Accept Header**: Ensure the response is in JSON format.

## Response Example
A successful request returns a JSON response similar to:

```json
{
  "applications": [
    {
      "id": "12345",
      "name": "MyApp",
      "type": "logs"
    }
  ]
}
```

## Troubleshooting
- If you receive a `401 Unauthorized` error, ensure that your token is valid and correctly included in the request.
- Check that you're using the correct API base URL for your region.

## Additional Resources
For more details, refer to the [Sematext API Documentation](https://github.com/sematext/sematext-api-client-python).

