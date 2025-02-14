# TheHive
The TheHive app for Shuffle allows users to interact with TheHive's API, enabling functionalities such as case management, alerts, observables, and more. Authentication is required via API Key and Instance URL to use TheHive.

## Authentication
This app requires authentication using an API Key and an Instance URL.

1. **Go to TheHive API Key Management:**
   - Navigate to TheHive instance you are using.
   - Log in with your administrator credentials.

2. **Create an API Key:**
   - Go to your user profile settings.
   - Under **API Keys**, click **Create a new API Key**.
   - Copy the API Key immediately, as it won't be displayed again.

3. **Find Your TheHive Instance URL:**
   - The Instance URL is the base URL of your TheHive server (e.g., `http://your-instance`).

4. **Add the API Key and URL to Shuffle:**
   - Open the TheHive app in Shuffle: [TheHive App](https://shuffler.io/apps/5fefa1911e01a005b54f94dcb6830d82)
   - Click on **Authentication**.
   - Enter the API Key under the **apikey** field.
   - Enter your TheHive Instance URL under the **url** field.

5. **Save and Test:**
   - Click **Save** to store the credentials.
   - Run a test action to verify authentication.

## Example Configuration
- **API Key:** `eyJhbGciOiJIUzI1...`
- **Instance URL:** `http://your-instance`

## Notes
- TheHive API Keys should be stored securely and not shared.
- TheHive API may have rate limits depending on the instance configuration.
- Ensure your API Key has the necessary permissions for your intended use case.

For more details, refer to TheHive API documentation: [TheHive API Docs](https://docs.strangebee.com/thehive/api-docs/).

