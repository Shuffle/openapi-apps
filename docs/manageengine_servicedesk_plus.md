# Manage Engine ServiceDesk Plus

### API 

### What is the purpose of APIs in ServiceDesk Plus?

Application Programming Interface (API) is used to integrate various applications and facilitate sharing of data between them. The integration can be achieved with any third party (external) applications or web services that are capable of sending the data via HTTP protocol.

### How does the Rest API operate based on the given parameters?

The operations performed with REST API is based on the operation' parameter and is sent to the URL via HTTP POST method. The URL format is as shown below,

```http://<servername>:<port number>/sdpapi/<module>```

### How is the authentication carried out in Rest API?

Authentication to the ServiceDesk Plus application is key based i.e., an API key is sent along with the URL for every operation. This key is technician based and can be generate for technicians with login privilege. The role given to the technician is also taken into consideration, so the key is valid only for the role given to the technician. Once the key is generated, the key is manually transferred to the integrated application so that the application can use the key for further API operations. If the key is invalid (key is expired or the technician login is disabled), then the operation fails and an error is propagated to the integrated application.

### How do I generate the API key?

The authentication between ServiceDesk Plus and integrated application is through an API key. A unique key is generated for a technician with login permission in ServiceDesk Plus application.

To generate the API Key, click Admin -> Technicians under User block.

If you want to generate the API key to the existing technician, then click the edit icon beside the technician.

If you want to generate the API key to a new technician, click Add New Technician link, enter the technician details and provide login permission.

Click Generate link under the API key details block. You can select a time frame for the key to expire using the calendar icon or simply retain the same key perpetually.

If a key is already generated for the technician, a Re-generate link appears.

### What are the operations supported by the Rest API?

The REST API supports only request related operations such as:

* Adding new request, editing, closing, deleting and viewing existing requests.

* Adding new notes to a request, editing, deleting and viewing existing notes.

* Adding work-log to a request, editing, deleting and viewing existing work-logs.

Please refer to the link for attributes model for Rest API
[https://help.servicedeskplus.com/api/rest-api.html](https://help.servicedeskplus.com/api/rest-api.html)

What response would ServiceDesk Plus send back to the third-party tool that is using the REST API for the operation "ADD_REQUEST"?

The application would send back the Request ID as an XML response.

### How do I perform the “Add_Notes” operation in REST API?

To add notes via REST API, you just need to parse the default Notes fields that is already present in ServiceDesk Plus. You can find those fields under Admin -> API -> RESTAPI -> Notes.
