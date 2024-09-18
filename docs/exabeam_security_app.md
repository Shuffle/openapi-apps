## Exabeam API App
Exabeam app to interact with Exabeam Advanced Analytics from Shuffle.

### How to Obtain the API Key:
To create an API key, you must have administrator privileges.

1. Go to **Settings** > **API Keys**.
2. If there are no existing **API keys**, in the center of the page, click **New API Keys**. **(If there are existing API keys, click New Keys.)**

  ![5a0ff23-image](https://github.com/user-attachments/assets/d7f76440-ffd0-49a7-b611-a6520fd0123c)

3. In the New API Key dialog box, do the following:
   - Provide a descriptive Key Name.
   - select one of the permission sets in the Permissions drop-down menu.
   
   ![9ddf284-image](https://github.com/user-attachments/assets/54838f64-b717-422e-86bb-32f5ef7f3432)

   - Click Create.
   (A message displays to indicate that your API key has been successfully created.)
   
   ![6cbd1e6-api-key-created](https://github.com/user-attachments/assets/8a2fc5bb-fde6-472c-9330-52fd3973210f)

   **Copy the **Key** and **Secret** (displayed only once).**

### API Rate Limits

- **Authentication API**: 50 requests/5 minutes per IP.
- **Public APIs**: 100 requests/minute per IP.

### Edit or Delete an API Key

- To edit, modify **Key Name** or **Permissions** in **API Keys**.
- To delete, use the **Delete** option.

## Exabeam API Gateways

When initiating an API call, choose the appropriate base URL based on your deployment region.

| Exabeam Region | GCP Region              | Organization URL                          | API Base URL                              | IP Address        |
|----------------|-------------------------|-------------------------------------------|-------------------------------------------|-------------------|
| US West        | `us-west1`               | `https://org-name.exabeam.cloud/`         | `https://api.us-west.exabeam.cloud/`      | `34.117.5.37`     |
| US East        | `us-east1`               | `https://org-name.use1.exabeam.cloud/`    | `https://api.us-east.exabeam.cloud/`      | `34.110.195.68`   |
| Canada         | `northamerica-northeast1`| `https://org-name.ca.exabeam.cloud/`      | `https://api.ca.exabeam.cloud/`           | `34.117.239.155`  |
| Europe         | `europe-west3`           | `https://org-name.eu.exabeam.cloud/`      | `https://api.eu.exabeam.cloud/`           | `34.120.192.204`  |
| Switzerland    | `europe-west6`           | `https://org-name.euw6.exabeam.cloud/`    | `https://api.ch.exabeam.cloud/`           | `34.160.203.65`   |
| Singapore      | `asia-southeast1`        | `https://org-name.sg.exabeam.cloud/`      | `https://api.sg.exabeam.cloud/`           | `34.149.143.252`  |
| Japan          | `asia-northeast`         | `https://org-name.jp.exabeam.cloud/`      | `https://api.jp.exabeam.cloud/`           | `34.98.109.122`   |
| Australia      | `australia-southeast1`   | `https://org-name.au.exabeam.cloud/`      | `https://api.au.exabeam.cloud/`           | `34.117.215.18`   |

Use these URLs to ensure you connect to the correct region.


For detailed instructions, visit the [Exabeam API Documentation](https://developers.exabeam.com/exabeam/docs/api-keys).
