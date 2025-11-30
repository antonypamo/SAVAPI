# swagger_client.DefaultApi

All URIs are relative to *https://api.savant-rrf.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate_quality**](DefaultApi.md#evaluate_quality) | **POST** /v1/quality | Conceptual quality evaluation for LLM answers
[**get_embeddings**](DefaultApi.md#get_embeddings) | **POST** /v1/embed | Text embeddings with RRFSAVANTMADE
[**get_roles_profile**](DefaultApi.md#get_roles_profile) | **POST** /v1/roles_profile | Icosahedral roles profile for a text
[**tutor_with_savant_rrf**](DefaultApi.md#tutor_with_savant_rrf) | **POST** /v1/tutor | Tutoring with Savant RRF (Phi9_4)

# **evaluate_quality**
> QualityResponse evaluate_quality(body)

Conceptual quality evaluation for LLM answers

Evaluates one or more candidate answers to a prompt using Savant RRF metrics (Φ, Ω, SRRF, CRRF, E_H) and a meta-classifier, optionally returning their icosahedral role profiles and ranking. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.QualityRequest() # QualityRequest | 

try:
    # Conceptual quality evaluation for LLM answers
    api_response = api_instance.evaluate_quality(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->evaluate_quality: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualityRequest**](QualityRequest.md)|  | 

### Return type

[**QualityResponse**](QualityResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embeddings**
> EmbedResponse get_embeddings(body)

Text embeddings with RRFSAVANTMADE

Produces high-level conceptual embeddings using the RRFSAVANTMADE encoder for scientific and RRF-related text. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmbedRequest() # EmbedRequest | 

try:
    # Text embeddings with RRFSAVANTMADE
    api_response = api_instance.get_embeddings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_embeddings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmbedRequest**](EmbedRequest.md)|  | 

### Return type

[**EmbedResponse**](EmbedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles_profile**
> RolesProfileResponse get_roles_profile(body)

Icosahedral roles profile for a text

Computes the 12-dimensional icosahedral role distribution (physics, geometry, information, ethics, etc.) for a given piece of text. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.RolesProfileRequest() # RolesProfileRequest | 

try:
    # Icosahedral roles profile for a text
    api_response = api_instance.get_roles_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_roles_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolesProfileRequest**](RolesProfileRequest.md)|  | 

### Return type

[**RolesProfileResponse**](RolesProfileResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tutor_with_savant_rrf**
> TutorResponse tutor_with_savant_rrf(body)

Tutoring with Savant RRF (Phi9_4)

Generates a pedagogical answer to a scientific question and internally evaluates its conceptual quality and icosahedral role profile using Savant RRF v1.0 (Phi9_4). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TutorRequest() # TutorRequest | 

try:
    # Tutoring with Savant RRF (Phi9_4)
    api_response = api_instance.tutor_with_savant_rrf(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tutor_with_savant_rrf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TutorRequest**](TutorRequest.md)|  | 

### Return type

[**TutorResponse**](TutorResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

