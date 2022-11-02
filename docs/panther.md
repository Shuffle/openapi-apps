# Panther
Panther is a Cloud-first SIEM built on GraphQL available at https://panther.com

## Paramteres
Panther takes two parameters:
- URL: The URL requires your Tenant, which is the sub-domain you interact with normally in the browser. 
- API-key: can be found by going to https://TENANT.runpanther.net/settings/api/tokens/. Change the URL to your tenant. 

## Webhooks
The best way to utilize Shuffle with Panther is to forward alerts using webhooks. 
This can be configured by logging into the Panther UI, clicking "Alert destinations" and setting this to forward to a Webhook in Shuffle. 
