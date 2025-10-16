# X.com API v2 – Setup and Usage Guide

This guide explains how to obtain your **API keys** from X.com’s (formerly Twitter’s) Developer Portal and how to use them to authenticate with the **X API v2** for creating, reading, and managing posts (tweets).

---

## 1. Getting Your API Keys

### Step 1 – Sign Up for a Developer Account
1. Visit the [X Developer Portal](https://developer.x.com/en/portal/dashboard).
2. Sign in with your X (Twitter) account.
3. Apply for **Developer Access** if you haven’t already.
   - You’ll need to describe how you plan to use the API.
   - Approval is usually automated for standard use.

---

### Step 2 – Create a Project and App
1. Once approved, click **"Projects & Apps" → "Overview" → "Create App"**.
2. Enter a project name and description.
3. After creation, your new app will show a **set of credentials**:
   - **API Key** (formerly "Consumer Key")
   - **API Key Secret**
   - **Bearer Token**
4. Under **"Keys and Tokens"**, you can also generate:
   - **Access Token**
   - **Access Token Secret**
   - These are tied to your user account (used for posting, deleting, etc.).

Keep these credentials private. Anyone with these tokens can access your account through the API.

---

### Step 3 – Enable OAuth 2.0
Under the **"User authentication settings"** tab:
1. Toggle **OAuth 2.0** ON.
2. Add a **Callback URL** (for example, `http://localhost:3000/callback` during local testing).
3. Choose permissions based on your intended use:
   - `tweet.read` → read public posts
   - `tweet.write` → create or delete posts
   - `users.read` → read user profiles
4. Save your settings, then note the **Client ID** and **Client Secret**.

These are used for the OAuth 2.0 flow (authorization code with PKCE).

---

## 2. Authenticating with the API

### Using Bearer Token (App-only)
For read-only operations (like getting posts), you can use the **Bearer Token** directly:

```bash
curl -H "Authorization: Bearer YOUR_BEARER_TOKEN" \
     https://api.x.com/2/users/{user_id}/tweets
