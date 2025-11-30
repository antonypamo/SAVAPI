import pytest

from swagger_client.api.default_api import DefaultApi
from swagger_client.models.rerank_candidate import RerankCandidate
from swagger_client.models.rerank_request import RerankRequest


def test_rerank_orders_by_rrf_score():
    api = DefaultApi()
    body = RerankRequest(
        query="quantum sensing",
        candidates=[
            RerankCandidate(candidate_id="a", text="doc a", ranks={"bm25": 2}),
            RerankCandidate(candidate_id="b", text="doc b", ranks={"bm25": 1}),
        ],
        k=50,
        top_n=1,
    )

    response = api.rerank(body)
    assert response.k == 50
    assert len(response.results) == 1
    assert response.results[0].candidate_id == "b"
    assert response.results[0].rank == 1
    assert response.results[0].features["best_rank"] == 1


def test_rerank_requires_candidates():
    api = DefaultApi()
    with pytest.raises(ValueError):
        api.rerank(None)
    with pytest.raises(ValueError):
        api.rerank(RerankRequest(query="q", candidates=[]))


def test_rerank_supports_candidates_without_ranks():
    api = DefaultApi()
    request = RerankRequest(
        query="astrochemistry",
        candidates=[
            RerankCandidate(candidate_id="x", text="doc x", ranks={}),
            RerankCandidate(candidate_id="y", text="doc y", ranks={"dense": 3}),
        ],
    )

    response = api.rerank(request)
    assert len(response.results) == 2
    zero_candidate = next(r for r in response.results if r.candidate_id == "x")
    assert zero_candidate.features["rrf_score"] == 0.0

    ranked_candidate = next(r for r in response.results if r.candidate_id == "y")
    assert ranked_candidate.features["supporting_systems"] == 1
