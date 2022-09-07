# Sophos XG Firewall
## Actions:
1. Authentication -  To Check the Authentication

2. Add a Host     -  It adds a IP in Sophos XG Firewall under category “System”--> “Host and Services”-->IPHost-->‘Type’ : IP.

3. List a Host    -  This action provide a list of Host under Sophos XG Firewall under category “System”--> “Host and Services”-->IPHost-->Type : IP/IPRange/Network/IPList

4. Add List of IPs - This action create the list of IPs in Sophos XG Firewall under category “System”--> “Host and Services”-->IPHost-->Type : IPList.

5. Create a Firewall Rule to Block a list of IPs.

   Prerequisite: name of the ‘list_of_ips’ which may be created either by this app action name: ‘Add a List of Ips’ or manually by in
    Sophos XG Firewall under category “System”--> “Host and Services”-->IPHost-->Select ‘Type’ : IPList.

    Use Case: Create a Firewall rule for Blocking a List of Ips.  It it required to provide (i) login username (ii) password (iii) name of the IPList.

    Description: This Rule is created to Block the Ips listed in the IPList. Source Zone is set to ‘Any’ and Source Network and Devices is set to the name of the IPList provided by you. Destination Zone, Desitnation Network and Destination services is set to ‘Any’. Rest all mandatory Controls and Filters are enabled.
