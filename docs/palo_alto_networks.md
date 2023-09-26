# Palo Alto Networks

## Blocking an IP/Domain
To block an IP address or a domain using the Palo Alto Networks firewall REST API, you need to create or modify a security policy rule that specifies the action to block the desired IP address or domain. Here's how you can do it based on the information provided:

### Step 1: Create or Update an Application Object (Optional)

*Create Application Object action*

This optional seeing as you might have an application object already set up, if not, create an application object that allows you to allow browser-based applications that belong to the category collaboration and subcategory

### Step 2: Create or Update a Security Policy Rule

*Add Security Rule action*

Now, you can create or update a security policy rule to block traffic from or to the IP address or domain. Modify the source, destination, and action fields accordingly. In this example, we use the address object "blocked-ip" created in the previous step. We set the action to "deny" to block traffic from the specified IP address/domain. You can also adjust other fields, such as source and destination zones, as needed.

### Step 3: Commit Configuration

*Commit Changes action*

After creating or updating the security policy rule, you should commit the configuration to make it active on the Palo Alto firewall.
