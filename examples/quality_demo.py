"""Minimal runnable demo for Savant RRF quality evaluation and embeddings.

This example expects a bearer token in the environment variable SAVANT_API_TOKEN.
It demonstrates synchronous calls and basic error handling for the generated
Swagger client.
"""
from __future__ import print_function
import os
import swagger_client
from swagger_client.rest import ApiException


def get_api_client():
    """Configure the API client with the bearer token from the environment."""
    token = os.getenv("SAVANT_API_TOKEN")
    if not token:
        raise RuntimeError("Please export SAVANT_API_TOKEN with your bearer token")

    configuration = swagger_client.Configuration()
    configuration.access_token = token
    # Optional: tune timeouts or disable SSL verification for local testing
    configuration.timeout = 20
    # configuration.verify_ssl = False  # Not recommended for production

    return swagger_client.ApiClient(configuration)


def run_quality_request(api_client):
    api = swagger_client.DefaultApi(api_client)
    body = swagger_client.QualityRequest(
        prompt="Explain quantum entanglement to a first-year physics student",
        answers=[
            swagger_client.QualityAnswerInput(
                answer="Entanglement is when particles share a state,"
                " so measuring one instantly tells you about the other",
                metadata={"candidate": "concise"},
            ),
            swagger_client.QualityAnswerInput(
                answer=(
                    "Entanglement means two particles remain correlated even"
                    " when separated, like a paired deck where drawing one"
                    " card defines the partner elsewhere."
                ),
                metadata={"candidate": "analogy"},
            ),
        ],
        include_roles_profile=True,
        normalize_scores=True,
    )

    try:
        response = api.evaluate_quality(body)
    except ApiException as exc:
        print("Request failed with status {}: {}".format(exc.status, exc.reason))
        raise
    else:
        for idx, result in enumerate(response.results):
            print("Candidate {}: Φ score = {}".format(idx + 1, result.metrics.phi))
            if result.roles_profile:
                print("  Top roles: {}".format(result.roles_profile.top_roles))


def run_embedding_request(api_client):
    api = swagger_client.DefaultApi(api_client)
    body = swagger_client.EmbedRequest(
        texts=[
            "Electrons occupy discrete energy levels in an atom.",
            "Transformer models use self-attention layers to mix context.",
        ],
        normalize_embeddings=True,
        include_dimension=True,
    )

    try:
        response = api.get_embeddings(body)
    except ApiException as exc:
        print("Embedding request failed with status {}: {}".format(exc.status, exc.reason))
        raise
    else:
        print("Embedding dimension: {}".format(response.dimension))
        print("First vector length: {}".format(len(response.embeddings[0].values)))


if __name__ == "__main__":
    client = get_api_client()
    run_quality_request(client)
    run_embedding_request(client)
