# OpenAPI v1.2 handling
Example for how to handle Graylog:
```
api-spec-converter --from=swagger_1 --to=swagger_2 http://127.0.0.1:9000/api/api-docs > graylog2.json
```

This creates a version to API. To make it work for Shuffle:
1. Download the entire spec as seen above
2. Copy the thing into Shuffle - If it doesn't work, validate the JSON.
3. Add image in Shuffle
4. Upload the spec 

## Example 2 with Ironscales
1. Get all the urls from their site to be merged, and set a name
```
	"https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/get-token",
	"https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/mitigation",
	"https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/incident",
	"https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/campaigns",
	"https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/company",
	"https://appapi.ironscales.com/appapi/docs/partner-full/api-docs/appapi/license",
```
2. Add them to the list in ../merge_multi.py
3. Run the converter
```
api-spec-converter --from=swagger_1 --to=swagger_2 ironscales_tmp.json > ironscales.json
```
4. Upload the spec
