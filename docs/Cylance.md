# Cylance 
Usability based on the API documentation outlined in their PDF: https://docs.blackberry.com/content/dam/docs-blackberry-com/release-pdfs/en/cylance-products/api-and-developer-guides/Cylance_User_API_Guide.pdf

## Authentication
Authentication in Cylance is a bit tricky, requiring the following from you:

1. An App ID
2. An App Secret
3. A Tenant ID

When you have all these, fill in the three items mention at the top of the following code within the quotes `"`. Once filled in, copy the WHOLE script into the "**Header**" field for the Cylance action you want to run.
One good action to test: List Threats

```python
Authorization: Bearer {% python %}
app_id = "APPID"
app_secret = "APPSECRET"
tenant_id = "TENANTID"

from datetime import datetime, timedelta
import uuid
import jwt
import sys

timeout = 1800
now = datetime.utcnow()
timeout_datetime = now + timedelta(seconds=timeout)
epoch_time = int((now - datetime(1970, 1, 1)).total_seconds())
epoch_timeout = int((timeout_datetime - datetime(1970, 1, 1)).total_seconds())
jti_val = str(uuid.uuid4())
AUTH_URL = "https://protectapi.cylance.com/auth/v2/token"
claims = {
    "exp": epoch_timeout,
    "iat": epoch_time,
    "iss": "http://cylance.com",
    "sub": app_id,
    "tid": tenant_id,
    "jti": jti_val,
    #"scp": ["policy:create","policy:list","policy:read","policy:update"]
}

encoded = jwt.encode(claims, app_secret, algorithm='RS256')
print(encoded)
{% endpython %}
Content-Type: application/json
Accept: application/json
```

If this works, and you get a 200 or 201 response, you can now move on to saving this authentication. What this requires is:

1. Fill in the "Apikey" field in Shuffle with everything between the `{% python %}` and `{% endpython %}` sections
2. Instead of newlines between each item, change it to use semi-colons. This is because newlines are not accepted in this kind of execution.
3. Try it again, while the WHOLE script is in the "Apikey" field. If you still get a 200, huzzah!

As this is not trivial, please contact support@shuffler.io if you need help.
