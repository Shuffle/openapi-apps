# APIFreaks

[APIFreaks](https://apifreaks.com) is an API hub for developers. This app exposes the
security-enrichment and geospatial endpoints most useful inside Shuffle workflows:
IP intelligence, WHOIS, DNS, SSL, domain, geocoding, GeoDB, timezone, user-agent
parsing, and astronomy — 43 actions in total.

## Authentication

All endpoints authenticate with an API key sent in the `X-apiKey` request header.
Get a free key at https://apifreaks.com/signup.

- **Base URL:** `https://api.apifreaks.com`
- **Auth type:** API key (header `X-apiKey`)

## Categories & actions

| Category | Actions | Example use in a playbook |
| --- | --- | --- |
| IP Geolocation | 6 | Geolocate + risk-score an IP from a SIEM alert |
| WHOIS | 8 | Enrich a domain/IP/ASN observable; pull registrant + history |
| DNS | 4 | Resolve records, historical + reverse DNS on an indicator |
| SSL | 2 | Inspect a domain's certificate + full chain |
| Domain | 4 | Check availability; enumerate subdomains (attack surface) |
| GeoDB | 10 | Country/city/region reference data & flags |
| Geocoding | 2 | Forward/reverse geocoding for locations |
| Timezone | 3 | Resolve/convert timezone for a location or IP |
| User Agent | 2 | Parse a User-Agent string into device/OS/browser |
| Astronomy | 2 | Sunrise/sunset & astronomical data for a location |

## Typical enrichment flow

Suspicious IP → **IP Geolocation** (risk score, VPN/proxy/Tor/bot signals) →
**IP WHOIS + ASN** (network owner) → **reverse DNS / WHOIS** on the domain →
**SSL certificate** check → enrich the case in TheHive/MISP and alert the analyst.

## Links

- Website: https://apifreaks.com
- API docs / Swagger: https://apifreaks.com/api/swagger
- Sign up (free key): https://apifreaks.com/signup