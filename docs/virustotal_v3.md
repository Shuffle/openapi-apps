# Virustotal V3

### Authentication

For authenticating with the API you must include the x-apikey header with your personal API key in all your requests. Your API key can be found in your VirusTotal account user menu:

![image](https://user-images.githubusercontent.com/58112539/197265155-aa240ad2-b57c-4840-adf0-551959ab506a.png)

Your API key carries all your privileges, so keep it secure and don't share it with anyone. Always use HTTPS instead of HTTP for making your requests.

### API responses

Most endpoints in the VirusTotal API return a response in JSON format. Unless otherwise specified, a successful request's response returns a 200 HTTP status code and has the following format:

```
{
  "data": <response data>
}
```
```<response data>``` is usually an [object](https://developers.virustotal.com/reference/objects) or a list of objects, but that's not always the case. An example of this is the [/files/upload_url](https://developers.virustotal.com/reference/files-upload-url) endpoint, which returns a URL. Refer to each endpoint's documentation to learn more about its return data structure.
