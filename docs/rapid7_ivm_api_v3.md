## InsightVM
- An app to interact with InsightVM and Nexpose

## Authentication
- Basic auth is used, therefore use your username & password for authentication.

## Notes
1. If you're running nexpose/InsightVM on localhost,
- Use your device's local IP. Since docker container can not connect directly on your host, You should not use localhost or 127.0.0.1.
- Set SSL verify to false while running app in workflow.
