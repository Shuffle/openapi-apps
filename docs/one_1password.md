You can use the 1Password Events API to retrieve information about activity in your 1Password account – like audit events, item usage, and sign-in attempts – and send it to your security information and event management (SIEM) system.

> **Tip**  
> This API reference documents the latest version of the 1Password Events API specifications (1.4.0).

---

## Requirements

Before you can use the 1Password Events API, you'll need to:

- Sign up for 1Password Business.
- Set up an Events Reporting integration in your account.
- Create a bearer token and select the event features it can access.

---

## About the API

The 1Password Events API is a REST-style API that follows the OpenAPI 3.0 Specifications. All communication between clients and servers occurs over HTTPS.

You can use your preferred language and tools for testing and implementing the Events API. This reference uses `curl` on the command line to demonstrate example requests.

> The API can access data from the last **120 days**. For older data, use the **Activity Log** in your 1Password account.

---

## Request Methods

| Method | Usage                                                                 |
|--------|-----------------------------------------------------------------------|
| `GET`  | Use with the `introspect` endpoint to return token access info.       |
| `POST` | Use with `auditevents`, `itemusages`, and `signinattempts` endpoints. |

---

## Servers and Base URLs

The API service ID is `events`, and the base URL depends on your 1Password hosting location.

| If your account is hosted on:     | Your base URL is:                          |
|----------------------------------|--------------------------------------------|
| `1password.com`                  | `https://events.1password.com`             |
| `ent.1password.com`              | `https://events.ent.1password.com`         |
| `1password.ca`                   | `https://events.1password.ca`              |
| `1password.eu`                   | `https://events.1password.eu`              |

---

## Endpoints

Each endpoint begins with the base URL and follows this format:

```

base_url/path

```

Replace `base_url` with your account's API base, and `path` with:

- `introspect`
- `auditevents`
- `itemusages`
- `signinattempts`

**Example:**  
For an account on `ent.1password.com` retrieving audit events:  
```

[https://events.ent.1password.com/api/v2/auditevents](https://events.ent.1password.com/api/v2/auditevents)

```

---

## Endpoint Versions

The API supports **V1** and **V2** versions for each main endpoint.

| Version | When to Use                                                                 |
|---------|------------------------------------------------------------------------------|
| V2      | For MSP-related data or new integrations.                                   |
| V1      | For existing integrations without MSP support.                              |

See the [API changelog](https://developer.1password.com/docs/events-api/changelog/) for details.

---

## Authorization

Each request must be authorized using a **Bearer Token**.

### Required Headers

| Header            | Value                                |
|-------------------|--------------------------------------|
| `Authorization`   | `Bearer YOUR_BEARER_TOKEN`           |
| `Content-Type`    | `application/json` (for POST only)   |

**Example:**

```

Authorization: Bearer YOUR_BEARER_TOKEN
Content-Type: application/json

````

> Verify token scopes via the **Events Reporting integration** or a `GET` call to `introspect`.

---

## Pagination

The Events API uses **cursor-based pagination**.

### Types of Cursors

#### Reset Cursor (First request)

Use a `ResetCursor` object to start querying data:

```json
{
  "limit": 100,
  "start_time": "2023-03-15T16:32:50-03:00",
  "end_time": "2023-03-15T17:32:50-03:00"
}
````

* `limit`: Max records to return.
* `start_time`/`end_time`: ISO 8601 format.

#### Continuing Cursor

Use this in follow-up requests:

```json
{
  "cursor": "aGVsbG8hIGlzIGl0IG1lIHlvdSBhcmUgbG9va2luZyBmb3IK"
}
```

> Splunk and Elastic integrations store this cursor automatically.

---

## Rate Limits

| Limit           | Value  |
| --------------- | ------ |
| Requests/minute | 600    |
| Requests/hour   | 30,000 |

Exceeding the limits will return:

```
429 | Too many requests
```

---

## Resources

* [1Password Developer Portal](https://developer.1password.com)
* [Events API Reference](https://developer.1password.com/docs/events-api/reference/)
* [Changelog](https://developer.1password.com/docs/events-api/changelog/)

```
