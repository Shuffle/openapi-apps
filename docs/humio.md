# Humio

### API Authentication

All but a few of Humio's API endpoints require authentication. Clients have to provide an API Token along with each request in the form of a Bearer Token.
To provide your API token in a HTTP header:

**INI Files**
```
Authorization: Bearer $API_TOKEN
```
