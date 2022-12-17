# Greynoise

### Authentication & Authorization

GreyNoise is a cybersecurity platform that collects and analyzes Internet-wide scan and attack traffic. This data is made available through the web-based Visualizer and GreyNoise APIs so users can contextualize existing alerts, filter false-positives, identify compromised devices, and track emerging threats.

The GreyNoise API uses a user API key for authenticating and authorizing users over SSL.

### User API keys

To use the GreyNoise API, requests must send a user API key in the header named Key. The token can be obtained from the account page when logged in to GreyNoise Visualizer.

<img width="754" alt="99d0a17-Screen_Shot_2020-08-25_at_8 44 29_PM" src="https://user-images.githubusercontent.com/58112539/200335982-5784e9ce-1141-4307-b6c8-e774acbdb569.png">

Example cuRL

```
curl --include -X GET -H 'key: UserAPIKey' \
     'https://api.greynoise.io/v2/noise/context/12.34.5.5'
```
