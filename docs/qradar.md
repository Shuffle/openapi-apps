# QRadar 

### RESTful API 

### What is the purpose of APIs in ServiceDesk Plus?

You access the RESTful API by sending HTTPS requests to specific URLs (endpoints) on the QRadar® SIEM Console. To send these requests, use the HTTP implementation that is built in to the programming language of your choice. Each request contains authentication information, and parameters that modify the request.

### QRadar and API versions

Every QRadar version has a REST API version, as described in the following table:

![image](https://user-images.githubusercontent.com/58112539/191135221-982e367a-e080-4efe-8592-0d27d9691134.png)

### API endpoints

An API endpoint contains the URL of the resource that you want to access and the action that you want to complete on that resource. The action is indicated by the HTTP method of the request: GET, POST, PUT, or DELETE.

### Required permissions to access the API

Authentication information must be included in every API request as an HTTP header. Provide the required access credentials in one of the following ways:

* A user name and password for a QRadar user that is specified in the authorization header.

* You specify the user name and password by using HTTP basic authentication. Although you can make API requests by providing a user name and password for every request, use authorized service tokens for all API integrations with QRadar. Only the user name and password option is supported for viewing the Documentation Page.

For more information about creating user roles, security profiles, and users, see the IBM® QRadar Administration Guide.

An authorized services token that is specified in the SEC header.
To authenticate as an authorized service, you create an authentication token that uses authorized services. QRadar authorized services have roles and security profiles assigned that control access to the various API resources.

The token is valid until the expiry date that you specified when you created the authorized service.

For more information about creating user roles, security profiles and authorized services, see the IBM QRadar Administration Guide.

The following table highlights the required role and the security profile impacts for each API endpoint:

![image](https://user-images.githubusercontent.com/58112539/191135346-b36396c8-3225-4924-a623-04b7245a8f07.png)

### API requests and responses

When you send an API request, the server returns an HTTP response. The HTTP response contains a status code to indicate whether the request succeeded and the details of the response in the response body. Most resources format this response as JavaScript Object Notation (JSON). You can use the JSON packages or libraries that are built in to the programming language that you use to extract the data.

For a complete example of this process, see the sample code in [GitHub](https://github.com/ibm-security-intelligence/api-samples).

### Version headers

You use version headers to request a specific version of the API. If you don't provide a version header, the latest version of the API is used, which might break integrations when QRadar is upgraded. If you provide a version header every time you use an API, it makes it easier to upgrade to newer versions of QRadar without breaking your API clients.

The APIs use the major and minor components of semantic versioning. Natural numbers are used to designate major versions of the API, for example, '3'. Minor versions of the API are designated with a major and minor component, for example, '3.1'. You can set the version header to a major or a minor version of the API. Changes that are compatible with existing versions are introduced with an incremented minor version number. Any incompatible changes are introduced with a major version number increment.

When a major version of the API is specified in the version header without a minor component, the server responds with the latest minor version within the major API version. For example, if the client requests version '3', the server responds with version '3.1'. If you want to use version 3.0, you must request '3.0' in the version header. If you request a version greater than the latest version of an endpoint, the latest available version of that endpoint is returned. Each endpoint is listed under every version it is valid for, even if it's unchanged in the newer versions.

### Endpoint deprecation

An API endpoint is marked as deprecated to indicate that it is not recommended for use and will be removed in a future release. To give integrations time to use an alternative, a deprecated endpoint continues to function for at least 1 release before it is removed. The interactive API documentation page indicates that an endpoint is marked as deprecated. Also, the API response message for a deprecated endpoint includes the header Deprecated. An individual API endpoint, or an entire version of API endpoints can be marked as deprecated. The deprecated endpoints still continue to function until they are removed.

When an API endpoint completes the deprecation process, it is removed. Endpoints that are removed no longer respond successfully. An attempt to call a removed endpoint returns an error. An HTTP 410 Gone response is returned for individual removed endpoints. An HTTP 422 Unprocessable Entity response is returned for requests for a version that is no longer supported.

Include the version header in API requests to call a specific version of an API endpoint. API integrations that do not explicitly request a particular version are not supported. If you do not specify a version, your request is directed to the latest available version. If a release includes a new, incompatible version of an endpoint, your integration might break. Have your request version in one location in your code to ease upgrading as newer versions become available
