import requests
import os
import sys

if len(sys.argv) <= 1:
    print("Please pass your Shuffle apikey")
    exit()

apikey = sys.argv[1]
print(apikey)

baseurl = "https://shuffler.io"
if len(sys.argv) > 2:
    baseurl = "http://localhost:5002"
    baseurl = sys.argv[2]

print("Uploading apps to %s" % baseurl)

def upload(filename, category, apikey):
    headers = {
        "Authorization": "Bearer %s" % apikey,
        "Content-Type": "application/json",
    }
    
    firsturl = "%s/api/v1/validate_openapi" % baseurl
    with open(filename, "r") as tmp:
        print("Uploading %s with category %s" % (filename, category))
        filedata = tmp.read()
        #print("FIRST: %s" % firsturl)
        ret1 = requests.post(firsturl, headers=headers, data=filedata)
        if ret1.status_code != 200:
            print("Failed step 1 for validate of %s with %d" % (filename, ret1.status_code))
            return

        #return

        # http://localhost:5001/api/v1/get_openapi/5dc6d934e70b09599783e9b38492ae82
        handle_id = ret1.json()["id"]
        get_url = "%s/api/v1/get_openapi/%s" % (baseurl, handle_id)
        #get_url = "http://localhost:5001/api/v1/get_openapi/8b33b5e6a2637fb47a95f19812ad48c1"
        #print("GET  : %s" % get_url)
        #print("GET  : %s" % get_url)
        ret2 = requests.get(get_url, headers=headers)
        if ret2.status_code != 200:
            print(ret2.text)
            print("Failed step 2 for validate of %s with %d" % (filename, ret2.status_code))
            return

        test_json = ret2.json()
        #try: 
        #    test_json["body"]["info"]["x-categories"] = [category]
        #except: 
        #    continue

        #break
        last_url = "%s/api/v1/verify_openapi?sharing=true" % baseurl
        print("Building %s" % filename)
        #print("Last : %s" % last_url)

        try:
            ret3 = requests.post(last_url, headers=headers, data=test_json["body"])
            if ret3.status_code != 200:
                print("Failed step 3 for validate of %s with %d" % (filename, ret3.status_code))
                print("RET (%s): %s" % (filename, ret3.text))
                #print("Headers: %s" % ret3.headers)
                return
        except:
            print("Error uploading %s in step 3" % filename)

        #exit()
    
            #print("RET3 SUCCESS!")



# 1 mig    POST http://localhost:5001/api/v1/validate_openapi 
# 2 setup. GET the ID 
#           http://localhost:5001/api/v1/get_openapi/5dc6d934e70b09599783e9b38492ae82
# 3 build: POST http://localhost:5001/api/v1/verify_openapi 

#filenames = {}
#files = os.listdir(".")
#for newfile in files:
#    if not os.path.isdir(newfile):
#        continue
#category = newfile

newfile = "."
files = os.listdir(newfile)
for subfile in files:
    if subfile.endswith(".yaml") or subfile.endswith(".yml"):
        try:
            upload("%s/%s" % (newfile, subfile), "", apikey)
        except:
            print("error with file.")
            pass
