# Pagerduty

## Authentication

```
All REST API requests must be made over HTTPS. Connections made using HTTP will be refused.
```

All REST API calls require authentication. In order to make successful requests to the REST API, you must provide a valid form of authorization.

## API Token Authentication

The PagerDuty REST API supports authenticating via an account or user API token. Account API tokens have access to all of the data on an account, and can either be granted read-only access or full access to read, write, update, and delete. For PagerDuty accounts with [Advanced Permissions](https://support.pagerduty.com/docs/advanced-permissions), user API tokens have access to all of the data that the associated user account has access to.

Only account administrators have the ability to [generate account API tokens](https://support.pagerduty.com/docs/using-the-api#section-generating-a-general-access-rest-api-key).

Tokens should be sent in the request as part of an **Authorization** header, using this format:

```
Authorization: Token token=y_NbAkKc66ryYTWUXYEu
```

Below is how to set the header in a few popular HTTP libraries. Note that this only sets the header; other code may be needed to create and process the request.
