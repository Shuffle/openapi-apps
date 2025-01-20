The SMSEagle APIv2 is available in SMSEagle software version 5.0 and higher.
    
# Getting Started
Before you can start using API, first you need to enable API access on your SMSEagle device.
  1. Go to **Web-GUI** > menu **Users**

  2. Create a new User with access level "User"

  3. Click **Access to API** beside newly created user

  4. Select **APIv2** and generate API Access token using a button **Generate new token**

  5. Add access permissions in section **APIv2 Permission**

  6. Optionally you may choose to give access to data of all users with a checkbox **Access to resources of all users** (by default you can access only to data created by this particular API key)
  
Main URL for API requests: <b>YOUR-SMSEAGLE-DEVICE-URL/api/v2/{method}</b><br>
for example: http://192.168.0.100/api/v2/messages/sms
  
# Authentication
SMSEagle APIv2 supports the following authentication methods:
  
+ API key (access token) in a HTTP request header *(recommended option)*
+ API key (access token) in a query parameter
+ API key (access token) as a parameter in a request body
  
Select your preferred method to suit your current tech stack and security requirement level.
