# SMSEagle

SMSEagle gateway is a dedicated device that enables businesses to send and receive SMS/MMS messages directly through cellular carriers.</br>
API allows you to remotely control and automate gateway's features.

# Requierments

The SMSEagle APIv2 is available for every SMSEagle device, running software version 5.0 and higher.<br/>
Requires a physical SMSEagle gateway, but can be tested beforehand on our [demonstration device](https://www.smseagle.eu/demo/).
Detailed APIv2 documentation can be found on [SMSEagle API page](https://www.smseagle.eu/docs/apiv2/).</br>

# Actions
- Send messages and queue calls
- List and manage messages/calls
- Create, list and manage contacts, groups and shifts on SMSEagle device
- Get SMSEagle device modem information
    
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
  
+ API key (access token) in a HTTP request header *(recommended option)*<br/>
    <pre>access-token: 123abc456def789</pre>
+ API key (access token) in a query parameter
    <pre>http://.../api/v2/...?access_token=123abc456def789...</pre>
+ API key (access token) as a parameter in a request body
    <pre>
  {
      ...
      access_token: 123abc456def789
      ...
  }</pre>
  
Select your preferred method to suit your current tech stack and security requirement level.

# Response codes
| **HTTP Code** | **Description**                                            |
|---------------|------------------------------------------------------------|
| 200           | Request successful (e.g. returns requested data or status) |
| 400           | Invalid request (e.g. missing required parameters)         |
| 401           | Invalid API key                                            |
| 403           | User has no access to this method                          |
| 404           | Resource not found                                         |
| 405           | Unknown method                                             |
| 500           | Internal server error                                      |