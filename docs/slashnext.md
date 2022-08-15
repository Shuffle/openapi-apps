# Slashnext
Slashnext is an API used for IOC enrichment. This API has been built out based on their [CLI](https://github.com/slashnext/SlashNext-URL-Analysis-and-Enrichment/blob/master/Python%20SDK/docs/SlashNext%20Phishing%20IR%20SDK%20Guide.pdf)

## Authenticate
Authentication with Slashnext uses an API-key in the "authkey" query parameter. You can find the API-key within their cloud instance. The URL should in most cases point to "https://oti.slashnext.cloud"

Once authenticated, try the "Get API Quota" or "Get host reputation" action with a domain as seen below. 

![image](https://user-images.githubusercontent.com/5719530/184736016-77d43ece-f5f3-45ca-a17a-1a622b9527f3.png)
