# AI Agent
The Shuffle AI Agent is a controllable and transparent, multipurpose AI Agent. [Full documentation on AI in Shuffle can be found here](https://shuffler.io/docs/AI).

## Authentication
By default, we use Shuffle's LLM of choice, which can be controllable by you. 

## Workflow
Using it in a workflow can be done without any configuration, unless you want to use your own model. It is currently limited based on actions, but will be expanded in the future to work like the other parts described in the next sections.

When used in a workflow, it will run in the relevant environment of choice, and is constrained by the selected actions.

<img width="364" height="541" alt="image" src="https://github.com/user-attachments/assets/119d676b-4b9e-45ce-a837-ec3b5579336b" />

## Agent UI
By going to /agents, you can try agents by themselves. By default, it has access to all actions of [Singul](https://singul.io).

<img width="794" height="281" alt="image" src="https://github.com/user-attachments/assets/61e50572-9c83-4cd6-9152-e7a4b26dab5a" />

## MCP
Every App is now an MCP server. What this means in practice is that ANYTHING uploaded to Shuffle can be used by ANY agent you have, anywhere, without having to host your own server for it. 

API:
```
POST /api/v1/apps/{appid}/mcp
```

Example of us using it on the Agent page:

<img width="770" height="268" alt="image" src="https://github.com/user-attachments/assets/e3f9728e-7121-42f7-957e-b5e78437cd1b" />
