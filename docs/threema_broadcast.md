# Threema Broadcast API Shuffler.io App

The **Threema Broadcast API** is designed to let third-party applications seamlessly communicate with Threema Broadcast identities. This app provides integrations with the Threema Broadcast API to enable automated workflows through [Shuffler.io](https://shuffler.io).

## Authentication

All requests to the Threema Broadcast API must be authenticated using an **X-API-Key**.

- **Creating an API Key**:
  - Navigate to: `Threema Broadcast > Settings > Your profile > API Keys`.
  - Generate an API key to use with your requests.

- **Authentication Header**:
  - Include the API key in your requests using the header:
    ```http
    X-API-Key: <your-api-key>
    ```

- **IP Restriction**:
  - Ensure the remote IP matches the IP specified for the generated API key (if applicable).

## API Usage Limits

- **Request Limits**:
  - A maximum of **10,000 requests per day** is allowed.
  - Exceeding this limit will result in an HTTP status code `429`.

- **Recipient Ratios**:
  - The ratio of the number of recipients to the number of groups, feeds, or distribution lists created via the API must not exceed **1:10**.

- **File Management**:
  - Only outgoing files can be viewed in Broadcast.
  - Incoming files are **not saved** and cannot be accessed.

- **Page Size**:
  - Setting a `pageSize` less than `0` or greater than `5000` will result in a **400 Bad Request** error.

## API Methods and Documentation

Detailed documentation for each API method is available in the OpenAPI specification:
[Threema Broadcast API Documentation](https://broadcast.threema.ch/en/api-doc).

## Error Handling

### Common Error Codes:
| **HTTP Code** | **Reason**                              |
|---------------|------------------------------------------|
| `400`         | Invalid request (e.g., invalid `pageSize`). |
| `429`         | Request limit exceeded.                 |
| `401`         | Invalid or missing API key.             |

---

For more details or troubleshooting, refer to the official [Threema Broadcast API Documentation](https://broadcast.threema.ch/en/api-doc).
