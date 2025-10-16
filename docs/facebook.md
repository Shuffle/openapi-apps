# Facebook Graph API – Pages and Posts Setup Guide

This guide explains how to obtain your **API keys** and **access tokens** from the Facebook Developer Portal, and how to use them to access **Page** and **Post** endpoints in the Graph API.

---

## 1. Getting Your API Credentials

### Step 1 – Create a Facebook Developer Account
1. Go to the [Facebook for Developers Portal](https://developers.facebook.com/).
2. Log in with your Facebook account.
3. Click **"Get Started"** and follow the prompts to verify your account.

---

### Step 2 – Create a New App
1. Go to [My Apps](https://developers.facebook.com/apps/).
2. Click **"Create App"**.
3. Choose the **"Other"** app type unless you’re integrating with a specific product like Messenger.
4. Select a display name, contact email, and app purpose (e.g., “For Everything Else”).
5. Click **Create App**.

Once the app is created, you’ll be redirected to its **Dashboard**, where you can find:

- **App ID** → identifies your application.  
- **App Secret** → keep this private; it’s used to sign requests.  

You’ll need both for OAuth authentication.

---

### Step 3 – Add the "Facebook Login" Product
1. On the left sidebar, click **“Add Product”** → **Facebook Login**.
2. Choose **Web** or **Other** as your platform.
3. Set your **Valid OAuth Redirect URIs**, for example: https://yourdomain.com/set_authentication
4. Save changes.

---

## 2. Generating an Access Token

There are several kinds of tokens in the Graph API, depending on context:

| Token Type | Description | Example Usage |
|-------------|--------------|----------------|
| **User Access Token** | Represents a logged-in user. | Reading user posts, managing their pages. |
| **Page Access Token** | Represents a Facebook Page, obtained via a User token. | Creating, reading, deleting posts on a Page. |
| **App Access Token** | Represents the app itself. | App-level actions like debugging tokens. |




---
