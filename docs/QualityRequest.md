# QualityRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | Prompt or question that produced the candidate answers. | 
**answers** | [**list[QualityAnswerInput]**](QualityAnswerInput.md) | Candidate answers to evaluate. | 
**include_roles_profile** | **bool** | Whether to include roles profile for each answer. | [optional] [default to True]
**return_top_k** | **int** | Number of top-ranked answers to return. If omitted, returns all answers sorted by score.  | [optional] 
**normalize_scores** | **bool** | Whether to include a normalized score in [0, 1]. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

