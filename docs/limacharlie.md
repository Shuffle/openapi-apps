# LimaCharlie

### API Keys

LimaCharlie Cloud has a concept of API keys. Those are secret keys that can be created and named, and then in turn be used to retrieve a JWT that can be associated with the LC REST Api at [https://api.limacharlie.io](https://api.limacharlie.io).

This allows construction of headless applications able to securely acquire time-restricted REST authentication tokens it can then use.

The list of available permissions can be programmatically retrieved from this URL: [https://app.limacharlie.io/owner_permissions](https://app.limacharlie.io/owner_permissions)

### Managing

The API Keys are managed through the organization view of the [https://limacharlie.io](https://limacharlie.io) web interface.

### Getting a JWT

Simply issue an HTTP GET or HTTP POST (recommended) such as:

```
curl -X POST "https://jwt.limacharlie.io/" -d "oid=c82e5c17-d520-4ef5-a4ac-c454a95d31ca&secret=1b1ae891-4316-4124-b859-556dd92add00"
where the oid parameter is the organization id as found through the web interface and the secret parameter is the API key.
```

The return value is a simple JSON response with a jwt component which is the JWT token. This token is only valid for one hour to limit the possible damage of a leak, and make the deletion of the API keys easier.

### User API Keys

User API keys are to generate JWT tokens for the REST API. In contrast to Organization API keys, the User API keys are associated with a specific user and provide the exact same access across all organizations. This makes User API Keys very powerful but also riskier to manage. Therefore we recommend using Organization API keys whenever possible.

The User API keys can be used through all the same interfaces as the Organization API keys. The only difference is how you get the JWT. Instead of giving an oid parameter to https://jwt.limacharlie.io/, provide it with a uid parameter available through the LimaCharlie web interface.

In some instances, the JWT resulting from a User API key may be to large for normal API use, in which case you will get an HTTP 413 Payload too large from the API gateway. In those instances, also provide an oid (on top of the uid) to the jwt.limacharlie.io REST endpoint to get a JWT valid only for that organization.

You may also use a User API Key to get the list of organizations available to it by querying the following REST endpoint:

```
https://app.limacharlie.io/user_key_info?secret=<YOUR_USER_API_KEY>&uid=<YOUR_USER_ID>&with_names=true
```

### Ingestion Keys

The artifact collection in LC requires Ingestion Keys, which can be managed through the REST API section of the LC web interface. Access to manage these Ingestion Keys requires the ingestkey.ctrl permission.
