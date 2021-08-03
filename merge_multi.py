import requests
import yaml
import json

fullname = "ironscales"
locations = [
    "https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/get-token",
    "https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/mitigation",
    "https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/incident",
    "https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/campaigns",
    "https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/company",
    "https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/license",
]

full_item = {}
for location in locations:
    ret = requests.get(location)
    jsondata = ret.json()
    for key, value in jsondata.items():
        if isinstance(value, list):
            #print("%s is list" % key)
            for item in value:
                try:
                    full_item[key].append(item)
                except KeyError:
                    full_item[key] = [item]
        elif isinstance(value, dict):
            for subkey, subvalue in value.items():
                try:
                    full_item[key][subkey] = subvalue
                except KeyError:
                    full_item[key] = {}
                    full_item[key][subkey] = subvalue
        else:
            if len(value) > 0:
                full_item[key] = value

        #print(key, value)
    #print(ret.text)
    #print(ret.status_code)
    #break

with open("%s_tmp.yaml" % fullname, "w+") as tmp:
    tmp.write(yaml.dump(full_item))
with open("%s_tmp.json" % fullname, "w+") as tmp:
    tmp.write(json.dumps(full_item))

print(full_item)

