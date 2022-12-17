# Sevco
### API Key
### Suggest Edits
The Sevco API key can be retrieved from the user profile page.

![image](https://user-images.githubusercontent.com/58112539/190456785-2da1542f-7839-4508-a745-bf8c227f273a.png)

From the Profile page, click Issue a new API Key

![image](https://user-images.githubusercontent.com/58112539/190456817-2ec006a6-b369-4a87-9068-cff81d13b1d5.png)

Copy the API Token to start working with the Sevco Developer APIs

# Using the API
Some basics about how the Sevco Developer APIs work

### REST APIs
All APIs are REST APIs over HTTPS. You can interact with the APIs using any HTTP interface such as wget or curl:

```
curl https://api.sev.co/v1/admin/org
```

Of course, that command will receive an error response - 403 Unauthorized.

### API Authentication
API requests are authenticated with a per-user API token. You can find your token by logging into the console, pulling up your user profile.

User API tokens are per-user, carry the same rights and privileges as the associated user. See Users, Privileges and Rights for more information on the different roles, rights and privileges in the system. To use it, your API requests must have an HTTP Request Header of the format:

``` 
Authorization: Token [token from your user profile]
```

To add a customer header with curl, use the -H flag:

```
curl -H 'Authorization: Token [token]' https://api.sev.co/v1/admin/org
```

...and now you're making authenticated API requests!
