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




# Jira Open-api App Documentation
Documentation for the Jira Open-api App on shuffle.

## Setup
* Most functions in Jira require your authentication so you'll first have to set this up, under authentication by clicking on the + symbol adjacent to the authentication field.
* In the pop up window you'll have to fill in your Jira credentials, your Jira sign up email as the username and your API Token as the password and then your domain https://your-domain.atlassian.net/

https://user-images.githubusercontent.com/31187099/146574392-6da43ad7-2670-4563-a094-f839831c3ea4.mp4

## Available Actions

1. Get all application roles - Returns all application roles in Jira.

https://user-images.githubusercontent.com/31187099/146574803-be9bd1d9-e3b6-419c-86bd-e872bf45eb19.mp4

2. Get Audit Records -Returns a list of audit records. [Not available on Jira cloud ]

https://user-images.githubusercontent.com/31187099/146574905-a8f91b6b-3cb9-432f-8a90-a72da923de8c.mp4

3. Get all dashboards - Returns a list of dashboards owned by or shared with the user. The list may be filtered to include only favorite or owned dashboards.  This operation can be accessed anonymously.

https://user-images.githubusercontent.com/31187099/146575021-3e34baa1-8955-4b75-93cc-5c2080ea6b81.mp4

4. Create dashboard - Creates a dashboard. This is an EXPERIMENTAL feature on Jira's side.

https://user-images.githubusercontent.com/31187099/146575179-1308b1b0-2273-4bbf-963b-954c4ce65d4f.mp4

5. Create issue - Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask. A transition may be applied, to move the issue or subtask to a workflow step other than the default start step, and issue properties set.

https://user-images.githubusercontent.com/31187099/146575278-3bf105c7-6482-4037-936d-c5e68bb2b4b4.mp4

6. Add Attachment - Adds one or more attachments to an issue. Attachments are posted as multipart/form-data

https://user-images.githubusercontent.com/31187099/146575376-856b02c6-ee19-4e0f-90c2-2a8da0d8477c.mp4

7. Get issue events - Returns all issue events

https://user-images.githubusercontent.com/31187099/146586474-098a454d-c2ca-41cf-a2b4-441e71d4c161.mp4

8. List all issues - List all issues

https://user-images.githubusercontent.com/31187099/146586507-60d5eabd-5acd-4779-b1ad-9e93ec32b614.mp4


