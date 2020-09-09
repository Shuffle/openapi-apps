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
