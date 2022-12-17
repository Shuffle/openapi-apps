# Sumo Logic

### API Authentication

This guide contains information about API authentication and the Sumo Logic endpoints to use for your API client.

Sumo Logic APIs follow Representational State Transfer (REST) patterns and are optimized for ease of use and consistency. All API docs have been developed with the [OpenAPI Specification](https://www.openapis.org/), unless otherwise stated. You can generate client libraries in many languages and explore automated testing.

### Authentication

Sumo Logic supports the following options for API authentication:

* Access ID and access key
* Base64 encoded access id and access key

See [Access Keys](https://help.sumologic.com/docs/manage/security/access-keys/) to learn how to generate an access key. Make sure to copy the key you create, because it is displayed only once.

### Access ID and Access Key

When you have an ```accessId``` and ```accessKey``` you can execute requests such as the following:

```
curl -u "<accessId>:<accessKey>" -X GET <API Endpoint>
```

Where <API Endpoint> is the Sumo Logic API URL you're sending requests to. For more information, see [Sumo Logic Endpoints](https://help.sumologic.com/docs/api/getting-started/#sumo-logic-endpoints-by-deployment-and-firewall-security).

### Basic Access (Base64 encoded)

If you prefer to use [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), you can do a Base64 encoding of your ```<accessId>:<accessKey>``` to authenticate your HTTPS request. The following is an example request, replace the placeholder <encoded> with your encoded access id and access key string:

```
curl -H "Authorization: Basic <encoded>" -X GET <API Endpoint>
```

The spacing in the "Authorization" field is required.

### Base64 example

In most Linux distributions you can use the 'base64' command. If the access id was Aladdin and your access key was OpenSesame then the command would be as follows:

```
echo -n "Aladdin:OpenSesame" | base64 --wrap 0
```

The ```-n``` ensures that an extra newline is not encoded.

This would yield a Base64 encoded string ```QWxhZGRpbjpPcGVuU2VzYW1l``` that is used like this:

```
"Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l"
```
