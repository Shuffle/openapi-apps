Burp Suite Enterprise Edition provides an API key for authentication. Follow the steps below to generate and retrieve your API key.

## Log in to Burp Suite Enterprise**
1. Open your web browser and navigate to your Burp Suite Enterprise instance.
2. Log in using your administrator credentials.

---

## Navigate to API Key Management**
1. Go to **"Settings"** or **"Administration"** from the sidebar.
2. Locate the **API Key Management** section.
3. Click on **"Generate New API Key"**.

---

## Copy and Store the API Key**
1. Copy the newly generated API key.
2. Store it securely (e.g., in an environment variable or a secure vault like AWS Secrets Manager).

**Warning:** Do not share your API key publicly or store it in plain text.

## Troubleshooting
- **API Key Not Found?** Ensure you have the correct permissions to generate API keys.
- **Unauthorized (401)?** Check if your API key is valid and properly included in the request headers.
- **Base URL Incorrect?** Use the correct API base URL (`http://localhost:8080/api` for local setups or `https://your-burp-server.com/api`).
