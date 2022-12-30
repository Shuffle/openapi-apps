# CrowdSec

### How to use the API?

Let’s assume that CrowdSec is in place and that you can use the command line client (CLI).

### Authenticate on the API

To authenticate to the API you need to generate a key for the bouncer. Most of the bouncers offered on the CrowdSec hub have an installation script that does this for you. However, if you develop your own bouncer, here is how to get a key:

cscli bouncers add BouncerdeTest

This will then give you an API key that you will need to specify in your Bouncer configuration.

![627d209ca23dd7b8c200393c_1](https://user-images.githubusercontent.com/58112539/210032008-36d8adf7-48be-4fd0-bd54-41f9ef322f47.png)

If it's a machine you want to register, you can do it in 2 different ways. The simplest is to use the following command:

```
cscli machines add MachinedeTest –auto
```

![627d209cca7b12032112bd57_2](https://user-images.githubusercontent.com/58112539/210032053-5f844c99-2597-4001-a570-00a2e6cda767.png)

This will generate a login and password for you in a yaml config file which you can then use.

![627d209c6400cbcc777eeca3_3](https://user-images.githubusercontent.com/58112539/210032083-fa204c4f-c244-4540-889d-55943e206cdf.png)

This is in the case where you are only running locally on the same machine. Now if you are on a remote machine, you need to register your API server like this:

```
cscli lapi register -u 
```

Then validate the addition of the machine, this time on the server where the Local API is located.

```
cscli machines validate MachinedeTest
```

Then to list the registered machines, simply do:

![627d209c24a45bf7a0c63ba6_4](https://user-images.githubusercontent.com/58112539/210032166-68e7bec5-72d2-48a6-9819-8270c54bd759.png)
