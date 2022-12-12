# Mimecast

### Authentication and Authorization

### Overview
* All requests to the Mimecast API require authorization.
* Authorization is defined using a signature in the Authorization Header.
* A signature includes a user specific Access Key and a combination of unique values signed with a user specific Secret Key using HMAC-SHA1 encryption. This process is described in the Authorization guide.
* An Access Key and Secret Key together is known as a binding. A binding is linked to a Registered Application.
* To get an Access Key and Secret Key you need to authenticate users using their primary email address and a password.

### Authentication Strategy Considerations
Choosing the correct authentication strategy for your integration is critical for success. Typically there are 2 types of integration, 

1. Scripts or server applications
2. Applications with a user interface

The sections below describe each of these integration types.

### Application with a user interface
Examples of this type of integration include,

* End user archive search to discover and view messages
* Administrator access to view and action messages held by policy.

When developing this type of application you will provide a UI for the user to add their email address and password in order to login and receive the access and secret keys required to authorize requests.

As access key and secret key values expire after the period of time defined in the Authentication Cache TTL setting in the service user's effective Authentication Profile you will need to securely store the user's credentials so you can use the Refresh Binding method when the access and secret key expires.

**IMPORTANT:** It is bad practice for a user to have more than one access key and secret key for a given application on a given device. Mimecast limits the number of access key and secret key bindings a single user can have. To avoid issues make sure you refresh expired access key and secret key bindings properly. This process is discussed in the Login reference guide.

### Scripts or server applications
Examples of this type of integration include,

* scripts to collect log data for SIEM integration,
* server applications that call the API for account level use cases like
 * monitoring gateway queues
 * updating policies
 * updating managed senders
 * updating managed URL's
 * users and groups management
 * administrator archive search
 * customer life-cycle management

 When developing this type of application you will,

1. use a single user that has the Mimecast administrator permissions to perform the actions required by your use case.
2. update the **Authentication Cache TTL** setting in the service user's effective Authentication Profile to "Never Expire."

This will result in you storing a single access key and secret key combination that will be used to authorize requests. You will not need to store user name and password combinations.

**NOTE:** In the event of the access and secret key becoming compromised you can revoke them from the Mimecast Administration Console in the **Administration | Services | Applications** menu item and clicking the **Registered Application** button. 
