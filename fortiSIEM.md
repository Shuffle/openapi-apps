# API Integration

This REST API based caller makes an HTTP(S) request with an input XML that defines the query. Since a query can take some time and the number of returned results can be large, the query works as follows:

* Caller submits the query and gets a Query Id back from FortiSIEM. This is done via Request API.
* Caller polls for query progress and waits until the query is completed. This is done via Polling API.
* When the query is completed, Caller gets the results via Results API.
- Caller gets the total number of query results and the query result fields.
- Caller gets the results - one chunk at a time.

This API provides a way to programmatically run any query on the event data. Following are the specifications for:

* [Request API](https://docs.fortinet.com/document/fortisiem/6.3.0/integration-api-guide/451674/events-and-report-integration#Request)
* [Polling API](https://docs.fortinet.com/document/fortisiem/6.3.0/integration-api-guide/451674/events-and-report-integration#Polling)
* [Results API](https://docs.fortinet.com/document/fortisiem/6.3.0/integration-api-guide/451674/events-and-report-integration#Results)

### Request API Specifications
**Input URL**	[https://<Accelops_IP>/phoenix/rest/query/eventQuery](https://<Accelops_IP>/phoenix/rest/query/eventQuery)
**Input Parameters**	 XML file containing the query parameters.
**Input Credentials**	
**Enterprise deployments:** User name and password of any FortiSIEM account
**Service Provider deployments:** User name and password of Super account for getting incidents for all organizations. If incidents for a specific organization are needed, then an organization-specific account and an organization name is needed.
**Output**	 queryId or an error code if there is a problem in handling the query or the query format.

### Polling API Specifications
The request will poll until the server completes the query.

**Input URL**	[https://<Accelops_IP>/phoenix/rest/query/progress/<queryId](https://<Accelops_IP>/phoenix/rest/query/progress/<queryId>)
**Output**	progress (pct)
Until progress reaches 100 (completed), caller needs to continue polling FortiSIEM. This is because the server may need to aggregate the results or insert meta-information before sending the results.

### Results API Specifications
**Input URL**	[https://<Accelops_IP>/phoenix/rest/query/events/<queryId>/<begin>/<end>](https://<Accelops_IP>/phoenix/rest/query/events/<queryId>/<begin>/<end>)
**Output**	totalCount (first time) and an XML containing the incident attributes.
For the first call, begin = 0 and end can be 1000. You must continuously query the server by using the same URL, but increasing the begin and end until the totalCount is reached.

Refer to [Example Usage](https://docs.fortinet.com/document/fortisiem/6.3.0/integration-api-guide/929584/example-usage) for a sample query.
