# Alive5 SMS

Alive5 provides two-way business texting for customer communication.

## Authentication

1. In the Alive5 dashboard, open [Integrations](https://app-prod.alive5.com/integrations) and select **API Key**. Copy your existing key, or choose **Generate** if your account does not have one.
2. In Shuffle, find [Alive5 SMS](https://shuffler.io/apps/8eb1156b6dd59788bdb99efd65dcc31a) under **Apps** or **Discover public apps** and add it to your workspace.
3. Enter your Alive5 API key in the app authentication and save it. The app sends the key in the `X-A5-APIKEY` header with no prefix.
4. Add Alive5 SMS to a workflow, select an action, and choose the saved authentication.

## Actions

- **List channels and users** (`get_list_channels_and_users`): Find accessible channels and assigned agents. No action-specific inputs are required. Results in `data.Items` include `channel_id`, `channel_label`, and `agents` with `user_id` and `screen_name`.
- **Send SMS** (`post_send_sms`): Submit one outbound text. Set the JSON `body` fields `phone_number_from` (Alive5 business number), `phone_number_to` (recipient), `channel_id`, `user_id` (an agent assigned to that channel), and `message`. Both numbers use E.164 format. The submitted message ID is at `data.data.message_id`.
- **List SMS conversations** (`get_list_sms_conversations`): Read recent conversations in `data.Items`. No action-specific inputs are required. This is a snapshot of recent activity, not a complete message archive or an automatic inbound-message trigger.
- **Custom action** (`custom_action`): Shuffle's generic HTTP action. Set `method` and `url`; use `path`, `headers`, `queries`, or `body` as needed for the request.

## Example: send an SMS

Run **List channels and users**. Choose an SMS channel whose `channel_label` is your business phone number, then copy its `channel_id` and an assigned agent's `user_id`.

Add **Send SMS** and set its `body` to the following, replacing the example IDs and numbers with your channel details and a recipient number you control:

```json
{
  "phone_number_from": "+14155550100",
  "phone_number_to": "+14155550123",
  "channel_id": "example-channel-id",
  "user_id": "example-user-id",
  "message": "Hello from Alive5."
}
```

Run the workflow and check the response. A message ID confirms submission, not delivery. Use recipients who have agreed to receive texts from your business.

## Response handling

Alive5 may return HTTP 200 with an API error. Check `code`, `error`, `data.code`, `data.error`, and `data.errors` before continuing. An empty `error` object is used in successful responses. If a send result is unclear, inspect conversation history before retrying to avoid duplicate messages.

See the [Alive5 authentication guide](https://imraghavojha.github.io/alive5-docs/api/authentication.html) and [Shuffle connector guide](https://imraghavojha.github.io/alive5-docs/connectors/shuffle.html) for details.
