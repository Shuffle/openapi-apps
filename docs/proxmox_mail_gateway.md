# Proxmox Mail Gateway
This app interacts with PMG via its REST API, enabling you to automate tasks such as user management, rule creation, and monitoring of email statistics.

## Authentication

The PMG requires authentication via user credentials or API tokens.

### Required Fields for Authentication:
- **Username**: The PMG username (e.g., `root@pam`).
- **Password**: The password for the specified username.
- **Base URL**: Your PMG instance's URL typically ends with `/api2/json`.

If you would like more detailed information, you can refer to the [Proxmox Mail Gateway Administration Guide](https://pmg.proxmox.com/pmg-docs/pmg-admin-guide.pdf).
