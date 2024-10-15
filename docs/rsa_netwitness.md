# RSA NetWitness
### Obtaining the API Key and URL for Authentication

To authenticate with the NetWitness platform, you will need two key pieces of information:

- **API Key**: This is required for authorizing your requests.
- **Base URL**: The URL of your NetWitness API instance.

### Steps to Get the API Key

1. **Login to the NetWitness Platform**:
   - Navigate to the login page of your NetWitness instance and enter your credentials.

2. **Access API Key Management**:
   - Once logged in, go to the **Admin** or **User Settings** section (this might vary depending on the version).
   - Look for an option like **API Keys** or **Tokens**.
   
3. **Generate a New API Key**:
   - Select the option to create a new API key.
   - You might be prompted to specify permissions or a usage scope for the API key (choose based on your needs).
   - After confirming, your new API key will be displayed. **Make sure to copy it immediately**, as you may not be able to retrieve it later.

4. **Store the API Key Securely**:
   - Store this API key securely, as it will be used for authentication in the NetWitness app.

### Steps to Get the Base URL

1. **Identify the NetWitness API Base URL**:
   - The Base URL is typically the URL of your NetWitness instance followed by `/api`.
   - For example: `https://<your-netwitness-instance-url>/api/`.

2. **Verify API Access**:
   - You can verify if the URL is correct by using a tool like [httpapp](https://shuffler.io/apps/ebfe7d5c80000676588f86731db0a555) with `curl` Action. It should return an API response or prompt you for credentials.
### Example of API Key and URL:

- **API Key**: `your-api-key-here`
- **URL**: `https://your-netwitness-instance-url/api/`
