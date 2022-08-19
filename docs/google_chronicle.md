# Google Chronicle
Google Chronicle is one of Google's acquistions to get into the security market, focused on Search and Detection of malicious behavior.

## Authentication
As with all apps, you need to get started with Authentication. For Chronicle, like with a lot of Google services, it requires constant re-authentication to avoid using expired tokens.

1. Get a credential file from Google
2. Upload it to Shuffle's [File Storage](https://shuffler.io/admin?tab=files)
3. In a workflow, find the "Get JWT from file" action in the Shuffle Tools app

![image](https://user-images.githubusercontent.com/5719530/185631449-c5923b8d-716e-4bdb-8c46-e7cadaa185d3.png)

![image](https://user-images.githubusercontent.com/5719530/185632059-3ea39d9e-69cb-4121-9a6c-8a8f2fd9faa0.png)

5. The JWT generated in step 3 can now be used in Google Chronicle's "Api-key" 
