## Datadog App
Monitoring and analytics tool for information technology (IT) and DevOps teams that can be used to determine performance metrics as well as event monitoring for infrastructure and cloud services.

## Requirements

1. Datadog account
2. Agent setup
3. API key setup
4. APPLICATION key setup

## Setup

- __How to Create Datadog App?__
1. Create a Datadog account
2. Select your fav platforms i.e. your stack.
3. download and install datadog agent
4. Get your API key
   - Follow link : `Your Agent URL`/organization-settings/api-keys<br>
5. Get your APPLICATION key
   - Follow link : `Your Agent URL`/organization-settings/application-keys<br>

## Note
- You have to manually pass `API key` and `APPLICATION key` in request header.
- example:
   - Content-Type=application/json
     DD-API-KEY=`Your API Key`
     DD-APPLICATION-KEY=`Your APPLICATION Key`