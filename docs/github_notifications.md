## Github notifications tracker

Github notification app for managing notifications & issues from shuffle.

## Actions

| No. | Action | Description 
|-----|--------|------------|
|1 | Get all notifications | Fetches all notification | 
|2 | Get repository notifications | Repository specific notifications | 
|3 | Mark notifications as read | Marks all notifications as "read" removes it from the default view on GitHub | 
|4 | Get user profile | Fetches user profile |
|5 | Get pull requests | Fetches all pull requests from public repositories | 
|6 | List issues assigned to the authenticated user |List issues assigned to the authenticated user across all visible repositories  | 
|7 |List repository issues | List issues in a repository |
|8 | Get an issue | Returns an issue |
|9 | Create an issue | Any user with pull access to a repository can create an issue | 
|10| Update an issue | Issue owners and users with push access can edit an issue |
|11| Add assignee to an issue | Adds assignee to an issue

## Authentication

- Github supports bearer authentication, therefore you'll need to generate token from your github account.  

#### How to get Github API token ?

1. Start off by going to your [GitHub Settings page](https://github.com/settings/profile).
2. Use the sidebar to access Personal access tokens.
3. Click on the Generate new token button in the top right of the view.
4. Give the token a name, such as: Shuffle GitHub Token. Then check all required scopes.
5. Click Generate token and GitHub will take you back to the list of tokens from before. Copy the code.

