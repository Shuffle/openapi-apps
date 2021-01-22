import os
import yaml
import json

algolia_client_key = os.getenv("ALGOLIA_CLIENT", "")
algolia_secret_key = os.getenv("ALGOLIA_SECRET", "")
algolia_index = os.getenv("ALGOLIA_INDEX", "")
if not algolia_client_key:
    print("env ALGOLIA_CLIENT not defined")
    exit(3)

if not algolia_secret_key:
    print("env ALGOLIA_SECRET not defined")
    exit(3)

if not algolia_client_key:
    print("env ALGOLIA_INDEX not defined")
    exit(3)

basedir = ".."
arr = os.listdir(basedir)
print("Files: %d" % len(arr))

def cleanup_openapi(filename, openapi):
    try:
        del openapi["info"]["version"]
        del openapi["info"]["contact"]
    except KeyError:
        pass

    actions = 0
    for pathkey, pathvalue in openapi["paths"].items():
        for key, value in pathvalue.items():
            actions += 1
            try:
                del value["responses"]
            except KeyError:
                pass

            try:
                del value["description"]
            except KeyError:
                pass

            try:
                del value["parameters"]
            except KeyError:
                pass

            try:
                del value["requestBody"]
            except KeyError:
                pass

            #print(value)

    openapi["objectID"] = openapi["info"]["title"]
    new_openapi = {
        "objectID": openapi["objectID"],
        "info": {
            "x-logo": openapi["info"]["x-logo"],
            "title": openapi["info"]["title"],
        },
        "actions": actions,
    }

    try:
        new_openapi["info"]["description"] = openapi["info"]["description"]
    except KeyError:
        pass

    try:
        new_openapi["category"] = openapi["info"]["x-categories"][0]
    except KeyError:
        pass

    return new_openapi

max_size = 10000000
#max_size = 15000
all_objects = []
largest = 0
for filename in arr:
    if not filename:
        continue

    if not filename.endswith(".yml") and not filename.endswith(".yaml"):
        continue

    #print(filename)
    with open("%s/%s" % (basedir, filename), "r") as tmp:
        test = tmp.read()
        print("File %s is %d" % (filename, len(test)))
        if len(test) > largest:
            largest = len(test)

        if len(test) > max_size:
            print("File %s is too big. %d vs %d (max)" % (filename, len(test), max_size))
            continue

        tmp.seek(0)
        try:
            loaded = yaml.load(tmp, Loader=yaml.FullLoader)
            openapi = cleanup_openapi(filename, loaded)

            #print("NEW LEN: %d" % len(str(openapi)))
            if len(str(openapi)) > 10000:
                continue

            all_objects.append(openapi)

            #with open('%s.json' % filename, 'w') as fp:
            #    json.dump(loaded, fp)
        except yaml.scanner.ScannerError as e:
            print("Yaml error in file %s: %s" % (filename, e))
    #break

print("Largest filesize: %d" % largest)

from algoliasearch.search_client import SearchClient
client = SearchClient.create(algolia_client_key, algolia_secret_key)
index = client.init_index(algolia_index)

res = index.save_objects(all_objects, {'autoGenerateObjectIDIfNotExist': False})
print(res)
#    {'firstname': 'Jimmie', 'lastname': 'Barninger'},
#    {'firstname': 'Warren', 'lastname': 'Speach'}
#], 
#print(res)
