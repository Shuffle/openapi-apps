# GitGuardian

### Authentication

The GitGuardian API uses API keys to authenticate requests.

You need to [create an account](https://dashboard.gitguardian.com/auth/signup) before getting started in order to get an API key.

Your API key can be created and revoked from the [API section of your dashboard](https://dashboard.gitguardian.com/api).

Your API key must kept private and should neither be embedded directly in the code nor versioned in Git. (Please do not push GitGuardian's API keys to public GitHub repositories ^^).

Beware your API keys can expire and can be revoked.

Use [/v1/health](https://api.gitguardian.com/docs#operation/health_check) to check the validity of your token if needed.

```
curl -H "Authorization: Token ${TOKEN}" \
  https://api.gitguardian.com/v1/health
 ```

### BearerAuth

```
Usage: Token <API Key> in authorization header.
```

* Security Scheme Type	HTTP
* HTTP Authorization Scheme	bearer
* Bearer format	"Token <API Key>"
