# AbuseIPDB

### Create an AbuseIPDB API key

We also assume that you have an account registered with AbuseIPDB, and have verified your domain and [created an API key](https://www.abuseipdb.com/account). The API is free to use, but you do have to [create an account](https://www.abuseipdb.com/register).

### Verify Fail2Ban AbuseIPDB Reporting Action Is Installed
The ability to report abusive IPs directly to AbuseIPDB was added to the master Fail2Ban repository in v0.10.0 (January 2017). If you have an older version of Fail2Ban installed on your server, you'll either have to update Fail2Ban or install the abuseipdb.conf action file yourself. To check what version of Fail2Ban you have installed, run the following command:

```fail2ban-client -V```

You can verify that your installation of Fail2Ban supports AbuseIPDB by checking that the action config file /etc/fail2ban/action.d/abuseipdb.conf exists. If it does not exist, you can add it manually by copying the latest config file from the [Fail2Ban Github](https://github.com/fail2ban/fail2ban/blob/0.11/config/action.d/abuseipdb.conf) .

Your /etc/fail2ban/jail.local file (the customizable version of jail.conf) should also contain the following definition for "action_abuseipdb":

```config
# Report ban via abuseipdb.com.
#
# See action.d/abuseipdb.conf for usage example and details.
#
action_abuseipdb = abuseipdb
```

If this action definition code doesn't exist, add it to your jail.local before the line ```action = %(action_)s```. That's all you need to support the AbuseIPDB Fail2Ban action!

## What will the AbuseIPDB action do?

The AbuseIPDB action will cause the IP address that triggered a Fail2Ban jail to be automatically reported to the AbuseIPDB API via a cURL command. By default this report will include the the log file snippet that triggered Fail2Ban's ban in the your report's comment field. The comment can be modified or disabled by looking for the snippet 'comment=<matches>' in action.d/abuseipdb.conf as follows:

```
actionban = curl --tlsv1.0 --fail 'https://api.abuseipdb.com/api/v2/report' \
    -H 'Accept: application/json' \
    -H 'Key: <abuseipdb_apikey>' \
    --data-urlencode 'ip=<ip>' \
    --data-urlencode 'comment=<matches>' \
    --data 'categories=<abuseipdb_category>'
```
