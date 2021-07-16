import os
import yaml

def fixfile(filename):
    #print(filename)
    data = ""
    with open(filename, "r") as tmp:
        data = yaml.load(tmp.read())

        try:
            # Rewrites swagger if it's wrong
            version = data["swagger"]
            if version == "3.0":
                data["openapi"] = "3.0.0"
                del data["swagger"]
                print("Fixed swagger for %s" % filename)
        except KeyError as e:
            try:
                version = data["openapi"]
                if version == "3.0" or version == "2.0":
                    data["openapi"] = "3.0.0"
                    print("Fixed openapi for %s" % filename)
            except KeyError as e:
                print("Error: %s" % e)

    if isinstance(data, object):
        with open(filename, "w+") as tmp:
            tmp.write(yaml.dump(data))
    else:
        print("Failed to write data. Type: %s" % type(data))


newfile = "."
files = os.listdir(newfile)
for subfile in files:
    if subfile.endswith(".yaml") or subfile.endswith(".yml"):
        fixfile("%s/%s" % (newfile, subfile))
