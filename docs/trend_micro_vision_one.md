# Trend Micro Vision One

### API Authentication
You will need:
- [The API URL](https://automation.trendmicro.com/xdr/Guides/First-Steps-Toward-Using-the-APIs)
- An Authorization token

### URL
Based on your Region, it will be one of the following:
```
api.au.xdr.trendmicro.com
api.eu.xdr.trendmicro.com
api.in.xdr.trendmicro.com
api.xdr.trendmicro.co.jp
api.sg.xdr.trendmicro.com
api.xdr.trendmicro.com
```

### Generate authentication token

Generates an authentication token for an account with API access

Account role permissions required:
* User Accounts
* View
* Configure account settings

AUTHORIZATIONS [bearerAuth](https://automation.trendmicro.com/xdr/api-v2#section/Authentication/bearerAuth)

PATH PARAMETERS

* email - required
* string - The parameter should be url encoded

![image](https://user-images.githubusercontent.com/58112539/192380004-4083fee3-fb2e-4ec4-8a35-ca5e8404a153.png)
