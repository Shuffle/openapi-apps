# Automation API

Automation functionality is designed to automatically generate signatures for intrusion detection systems. To enable signature generation for a given attribute, Signature field of this attribute must be set to Yes. Note that not all attribute types are applicable for signature generation, currently we only support NIDS signature generation for IP, domains, host names, user agents etc., and hash list generation for MD5/SHA1 values of file artefacts. Support for more attribute types is planned. To make this functionality available for automated tools an authentication key is used. This makes it easier for your tools to access the data without further form-based-authentication.

## General

### Automation URL
The documentation will include a default MISP URL in the examples. Don't forget to replace it with your MISP URL.

Default MISP URL in the documentation:

``` https://<misp url>/ ```

### Automation key
The authentication of the automation is performed via a secure key available in the MISP UI interface. Make sure you keep that key secret as it gives access to the entire database! The [API](https://misp.gitbooks.io/misp-book/content/GLOSSARY.html#api) key is available in the event actions menu under automation.

Since version 2.2 the usage of the authentication key in the URL is deprecated. Instead, pass the auth key in an Authorization header in the request. The legacy option of having the auth key in the URL is temporarily still supported but not recommended.

The authorization is performed by using the following header:

``` Authorization: YOUR API KEY ```

When submitting data in a POST, PUT or DELETE operation you also need to specify in what content-type you encoded the payload. This is done by setting one of the below Content-Type headers:

```
Content-Type: application/json 
Content-Type: application/xml
```

**Example**

```curl --header "Authorization: YOUR API KEY" --header "Accept: application/json" --header "Content-Type: application/json" https://<misp url>/```

By appending .json or .xml the content type can also be set without the need for a header.
