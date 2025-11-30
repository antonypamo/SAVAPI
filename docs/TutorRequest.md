# TutorRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | Scientific or RRF-related question to be answered. | 
**student_level** | **str** | Target level of the explanation. | [optional] [default to 'undergrad']
**language** | **str** | Language code guiding the answer style. | [optional] [default to 'en']
**max_new_tokens** | **int** | Maximum number of tokens to generate for the answer. | [optional] [default to 256]
**include_roles_profile** | **bool** | Whether to include the icosahedral roles profile in the response. | [optional] [default to True]
**include_candidates** | **bool** | Whether to include internal candidate answers and their metrics. | [optional] [default to False]
**metadata** | **dict(str, object)** | Optional metadata for client-side tracking (session_id, user_id, etc). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

