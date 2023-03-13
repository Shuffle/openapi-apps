# Authenticating Fortigate

In order to obtain the FortiGate API key, you will need to log in to the FortiGate web interface and select the System > Advanced > API > Generate Key option.

Enter the API key name and click OK to generate the API key. The API key will then be displayed on the screen.

Copy the API key as you will use it to authenticate your calls in Shuffle.

In Shuffle, drag in the fortigate app into your workflow. Click on it and click on the Authenticate button.

![WhatsApp Image 2023-03-10 at 13 08 12](https://user-images.githubusercontent.com/31187099/224637343-c5a83314-3464-4902-950d-23688558ad77.jpeg)

In the pop out window type in your fortigate url then click submit  i.e 
``` https://10.0.0.4:433 ```

![WhatsApp Image 2023-03-10 at 13 09 48](https://user-images.githubusercontent.com/31187099/224637539-d8092f16-2fec-4b6f-877e-a2bb93713da9.jpeg)

In your headers ensure parse the api key you were given in the first step i.e 
```
Authorization: Bearer casu3wi4br98tbr4494b4i944b4bkbd9 
Content-Type: application/json
Accept: application/json
```

![WhatsApp Image 2023-03-10 at 13 22 46](https://user-images.githubusercontent.com/31187099/224638066-2b433861-c735-48f2-b50d-77de36f99d26.jpeg)

![WhatsApp Image 2023-03-10 at 13 22 09](https://user-images.githubusercontent.com/31187099/224638025-206a6aee-a6e2-429e-a2d0-252ae56d0f30.jpeg)

## To block an IP in FortiGate

1. Ensure a FireWall policy is created in the Fortigate console, you will be provided with a Policy ID

2. See publicy shared workflow [here](https://shuffler.io/workflows/b52fa3f2-9cdb-4a39-bc7c-0c85f17386c5?queryID=36760ac26e40a19152dc04b800ad81f5) on how to block ip's in Fortigate Firewall. 
