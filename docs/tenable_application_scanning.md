# Tenable Application Scanning

### Authorization

Tenable.io generates a unique set of API keys for each user account. These keys allow your application to authenticate to the Tenable.io API without creating a session.

To authorize your application to use the Tenable.io API, you must include the X-ApiKeys header element in your HTTP request messages.

### X-ApiKeys Header Element

The X-ApiKeys header element has the following format:

```
HTTP

X-ApiKeys: accessKey=ACCESS_KEY; secretKey=SECRET_KEY;
```

The ACCESS_KEY and SECRET_KEY parameters correspond to the API keys that Tenable.io generates for each system user.

### Example

```
HTTP

curl -H "X-ApiKeys:
accessKey=2c935f507d0686382bb383e4daf92eef8b4a349b9b9de2bf85343c0f7e7265db;
secretKey=0553ac5757e8e741d6ef034dc06618106e7855887428e662adcde8862d017cf9"
https://cloud.tenable.com/scans
```
