This guide explains how to send/post messages in Slack groups and private chats using Shuffle.

## Actions
- **Get Channel List**: Retrieves `channel_id`, which is required to post a message.
- **Send/Post Message**: Sends a message to a Slack channel.

## Requirements
- A Slack account
- A Slack bot app with permission to post messages in chat
- API key for authentication

---

## Setup

### How to Create a Slack App
1. Create a Slack account.
2. Go to the [Create Slack App](https://api.slack.com/apps?new_app=1) page.
3. Follow the [Slack App Creation Guide](https://api.slack.com/start/overview#creating).
4. Once the app is created, assign the required roles and permissions using this guide: [Sending Messages with Slack API](https://api.slack.com/messaging/sending).
5. Obtain the API key:
   - Navigate to "OAuth & Permissions" from your Slack App homepage.
   - Copy the **Bot User OAuth Token** (`xoxb-your-token`).

### Configure Slack App with a Slack Channel
1. Open Slack and go to the channel where you want to receive messages.
2. Open "Channel Details."
3. Click on the three dots icon for more options.
4. Select **"Add Apps"** and search for the app you created.
5. Click **"Install"** to install the app in your channel scope.
6. Your application can now post messages via API requests.

---

## Posting Messages via Shuffle

### Getting Slack Channel ID
To post a message, you need the `channel_id`. There are two ways to obtain it:

1. **From Slack Web Interface**:
   - Open Slack in a web browser.
   - Navigate to the desired channel.
   - The URL will be in the format: `https://app.slack.com/client/XXXXXXXXXX/channel_id`.
   - The last part of the URL is your `channel_id`.

2. **Using Slack API (`conversations.list`)**:
   - Use the [Get Channel List](https://api.slack.com/methods/conversations.list) API method.
   - This method retrieves all channel IDs programmatically.

### Posting a Message
1. Select the **"Post Message"** action in the Shuffle app.
2. Create an **Authentication entry** using the API Key obtained earlier.
3. Provide the following parameters:
   - **`channel_id`** (ID of the channel where the message should be posted)
   - **`message`** (Text content of the message)
4. Execute the action, and the message will be sent to Slack.

### Example API Request
```bash
curl -X POST "https://slack.com/api/chat.postMessage" \
-H "Authorization: Bearer xoxb-your-token" \
-H "Content-Type: application/json" \
-d '{
    "channel": "C01234567",
    "text": "Hello, this is a test message from Shuffle!"
}'
```

---

## Important Notes
- **Permissions**: Ensure your Slack app has the correct permissions (`chat:write` for posting messages, `channels:read` for retrieving channel info).
- **Use Slack's API for Best Accuracy**: The URL method for retrieving `channel_id` may not always be reliable. The API method is preferred.

