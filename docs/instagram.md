# Instagram Graph API – Posts and Media Setup Guide

This guide explains how to obtain your **API keys** and **access tokens** for the **Instagram Graph API**, which allows you to publish, read, and manage posts (media) on **Instagram Business** or **Creator** accounts linked to a Facebook Page.

---

## 1. Prerequisites

Before using the Instagram Graph API, you need:

- A **Facebook Developer Account**  
- A **Facebook App** with the **Instagram Graph API** product added  
- An **Instagram Business** or **Creator** account  
- The Instagram account **connected to a Facebook Page**

The Instagram Graph API is built on the same **Facebook Graph API platform**, so the authentication process and tokens are the same.

---

## 2. Getting API Credentials

### Step 1 – Create a Facebook App

1. Go to [Facebook for Developers](https://developers.facebook.com/).
2. Click **My Apps** → **Create App**.
3. Choose **Other** or **Business** as your app type.
4. Set your **App Display Name** and **Contact Email**.
5. Once created, you’ll get:
   - **App ID** – identifies your app.
   - **App Secret** – keep this private.

---

### Step 2 – Add the Instagram Graph API Product

1. In the left sidebar, click **Add Product**.
2. Select **Instagram Graph API**.
3. Click **Set Up**.

This adds Instagram-specific permissions to your app.

---

### Step 3 – Add Facebook Login (for OAuth)

The Instagram API uses **Facebook Login** to authorize access.

1. Under your app, click **Add Product → Facebook Login → Set Up**.
2. Configure **Valid OAuth Redirect URIs**, such as:

   ```
   https://yourdomain.com/set_authentication
   ```

3. Save your changes.

---

## 3. Getting Access Tokens

Instagram Graph API uses **OAuth 2.0**, just like Facebook.  
There are two main tokens involved:

| Token Type | Description |
|-------------|--------------|
| **User Access Token** | Grants access to a user’s connected Instagram accounts. |
| **Page Access Token** | Grants access to a specific Facebook Page (and its linked Instagram account). |

---


### Example: Read Posts from an Instagram Account

```
GET https://graph.facebook.com/v22.0/{ig-user-id}/media
Authorization: Bearer {page-access-token}
```

Example response:

```json
{
  "data": [
    {
      "id": "17900123456789012",
      "caption": "Posted via API",
      "media_type": "IMAGE",
      "media_url": "https://example.com/photo.jpg"
    }
  ]
}
```

---

## 4. Permissions (Scopes)

When authenticating with OAuth, request the following scopes depending on your needs:

| Scope | Description |
|--------|--------------|
| `instagram_basic` | Read basic profile info and media. |
| `instagram_content_publish` | Publish media to Instagram. |
| `pages_show_list` | Retrieve a list of Pages the user manages. |
| `pages_read_engagement` | Read content and engagement metrics for Pages. |
| `public_profile` | Read basic public info. |

Your app must go through **App Review** if it will be used beyond development.

---

## 5. Summary

- **App ID + App Secret** → Identify your app  
- **User Token** → Represents an authorized user  
- **Page Token** → Grants access to linked Instagram account  
- **OAuth 2.0** handles authorization and token exchange  
- **Scopes** define permissions for media read/write access

All of these correspond to the `facebookOAuth` security scheme in your OpenAPI spec.

---

## 6. References

- [Instagram Graph API Docs](https://developers.facebook.com/docs/instagram-api/)
- [Getting Started Guide](https://developers.facebook.com/docs/instagram-basic-display-api/getting-started)
- [Facebook Login for Apps](https://developers.facebook.com/docs/facebook-login)
- [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens)
