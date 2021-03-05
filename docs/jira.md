# Jira App

The Jira app for creating and managing issues from shuffle workflow.

![alt text](https://github.com/dhaval055/security-openapis/blob/master/jira-app.png?raw=true)


## Actions

- Create issue
- Get issue
- List all issues
- Search issues
- Add attachment
- Delete attachment
- Add comment on issue
- Get comments
- Update comment
- Delete comment
- List all projects
- Get project

## Requirements

1. You'll need base url and API token for using this app.
2. Your base url should be like this - https://your-domain.atlassian.net.
3. Then, go to [Generate API token](https://id.atlassian.com/manage-profile/security/api-tokens) and login with your atlassian account.
4. Create API token with suitable label (For security reasons it isn't possible to view the token after closing the creation dialog).
5. Copy token and keep it somewhere safe.
6. You should store the token securely, just as for any password.

## Setup

You'll need following for setting up Jira in shuffle workflow

#### Authentication

1. username_basic (Your Jira account email)
2. password_basic (Use the API token as password)
3. url (Use base URL)

## Note

- In some actions you're required to fill out all paramters otherwise it'll throw an error sometimes.
- When using Create issue action,Format for Due date parameter is yyyy-mm-dd. 
- When using add attachment action, make sure you upload file in shuffle it self first goto Admin &#8594; Files &#8594; upload files & copy the file id. Use the same in file_id parameter. For more info refer [this](http://shuffler.io/docs/organizations#files)

