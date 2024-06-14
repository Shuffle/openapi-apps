# Introduction
Hashicorp vault is a Key Management System (KMS) used to sensitive user- and application-keys. 

## KMS
Shuffle supports Hashicorp Vault as a KMS. This means you can follow the [KMS guide](https://shuffler.io/docs/extensions#KMS) to set it up to be one.

## Authentication
To use the vault in Shuffle, make sure:
1. It is unsealed
2. You have your Client Token available
3. The API port is available to Shuffle (8200)

When these are done, fill it in on the Shuffle side, and you should be able to start using the app.

<img width="315" alt="image" src="https://github.com/Shuffle/openapi-apps/assets/5719530/67807532-70d6-4e2e-8a05-330795348884">
