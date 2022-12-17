# Hashdd

### Authentication

Calls to the API require an API key to be set in the ```X-API-KEY HTTP``` header. Your API key is available in the WebUI on the (Dashboard page)[https://hashdd.com/dashboard] after you authenticate.

### Endpoints

```/v1/knownlevel/```

The ```knownlevel``` endpoints are meant to provide a simple Good/Unknown determinationfor a hash. They're optimized for minimal lookup time by using probabilistic data structures called [Bloom filters](https://en.wikipedia.org/wiki/Bloom_filter). It's important to note that Bloom filters do have the potential for [False Positive](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors) matches so depending on your use-case, this may not be an ideal endpoint

Example

```curl https://api.hashdd.com/v1/knownlevel/838DE99E82C5B9753BAC96D82C1A8DCB

{"result": "SUCCESS", "message": null, "hash": "838DE99E82C5B9753BAC96D82C1A8DCB", "knownlevel": "Good"}
```


```/v1/downloads/```

Our ```downloads``` endpoints are provided for offline searches for known hashes. When you have many (greater than 100) hashes that need to be evaluated, it's much more performant to do an offline search rather than to use our APIs. For these use-cases, we provide downloadable lists and pre-built lookup structures. Our ```downloads``` endpoints return short-lived URLs that grant temporary access to our offline files which are stored within Google's Cloud Storage.
