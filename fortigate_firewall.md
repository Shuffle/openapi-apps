# Authorization and Permissions

In most cases, once a user is authenticated by a method such as OAuth or Basic Authentication, the api will check if the user is authorized to use that endpoint based on the permissions they have been assigned by higher level administrators.

Permissions are contained within built-in admin profiles which are configured in **System > Administration > Admin Profiles**. Generally, for example, if an admin has the 'Can view local users' permission, they will be able to successfully perform a GET request to the '/localusers' endpoint. Similarly, if they do NOT have 'Can change local users' permission, any of their POST requests to the '/localusers' endpoint should fail. These profiles can be assigned to an admin by selecting an admin under **Authentication > User Management > Local / Remote Users**, and adding an admin profile, which contains the correct permission, to their list of applicable admin profiles.

If you want to give an admin only the permissions required to use an endpoint, without giving them the many permissions that go along with a built-in permission set, you can make a custom permission set with only the permissions required. This can be done by navigating to **System > Administration > Admin Profiles**, creating a custom permission set with permissions of your choice, and then applying that admin profile to your admin user.

For a summary of the authentication methods, permission sets, and permissions that each endpoint requires, see the [Authorization and Permissions Table](https://docs.fortinet.com/document/fortiauthenticator/6.4.0/rest-api-solution-guide/870944/authorization-and-permissions).
