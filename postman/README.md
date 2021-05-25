# Postman to OpenAPI
As we run everything as OpenAPI in shuffle, we needed a way to transform postman to OpenAPI. Here's how.


1. **Install Postman to OpenAPI**
```
npm i postman-to-openapi -g
```

Docs: https://joolfe.github.io/postman-to-openapi/

2. **Run p2o (postman-2-openapi)**
This example runs towards an Automox Postman Collection, translated to OpenAPI 
```
~/.npm-global/bin/p2o Automox\ API.postman_collection.json -f automox.yaml
```

PS: It may be located in a different location after install. Check the logs from the install.

3. **Upload it to Shuffle**
Upload the new Yaml file to Shuffle, then finish the configuration (e.g. add image, fix potential auth issues or naming issues).

4. Move it back to the OpenAPI location (this repository)
