# Open security apis
A directory to be used for OpenAPI specifications used by the security industry. Some are made by me, while other's are contributed or gathered by others. 

[OpenAPI website](https://www.openapis.org/)

## Why?
The security industry is in need standardization on the API front, and I thought this might be a good place to start. OpenAPI definitions are usually well hidden on vendors' websites where I've dug some of them up, before adding them here.

## About
Shuffle is an [automation platform](https://shuffler.io) that leverages OpenAPI rather than a proprietary, code specific ecosystem to prevent the lockin issues with current SOAR products. It's based on NSA's [WALKOFF](https://github.com/nsacyber/walkoff), and works well with their platform as well. If something is off, please make a pull request or reach out.

## Contribute
You can contribute an OpenAPI3, OpenAPI2 or Json-Schema specification in either JSON/Yaml format. There is no specific documentation format yet. If you have extra documentation for the app, please add it to /docs with the same name. E.g.
```
discord.yaml
docs/discord.md ## OR without md (below)
docs/discord
```

## Goal
1. Help standardize the API's for each TYPE of product (alerts, tickets)
2. Not having to write custom python code for everything I automate anymore
3. Teach security people about OpenAPI

## Want a quickstart? Check this repo and import one in Shuffle
* [Shuffle unverified apps](https://github.com/frikky/security-openapi-unverified)

## Other resources (non-infosec)
* [openapi-directory](https://opencollective.com/openapi-directory)
* [security-apis](https://github.com/deralexxx/security-apis)
