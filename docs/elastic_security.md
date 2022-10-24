# Elastic Security

Elastic Security is Elastic's CLOUD API. This does not work with local Elasticsearch or Opensearch databases. For that, use the [Elasticsearch app](https://shuffler.io/apps/971706758e274c2e4083f2621fb5a6f7).

## Prerequisites

To use this API, you must have access to an Elastic Security instance with the following information:
- Username
- Password
- URL 

### Usage
Elastic Security is an EDR + SIEM, and hence we focus on a few different areas:
- Alerts
- Cases
- Host Isolation

A good sample workflow to handle Alerts and Cases can be found here:
- [Elastic Security - Get alerts](https://shuffler.io/workflows/c866ec56-d6b2-44f1-aaa9-64f469bb593f)

This is a **Trigger workflow** and works by getting information that can be forwarded into cases and alerts in other systems, with or without enrichment. 
