"""Example showing how to run the local RRF reranker."""
from swagger_client.api.default_api import DefaultApi
from swagger_client.models.rerank_candidate import RerankCandidate
from swagger_client.models.rerank_request import RerankRequest


def main():
    api = DefaultApi()
    request = RerankRequest(
        query="graphene superconductivity",
        candidates=[
            RerankCandidate(candidate_id="a", text="doc a", ranks={"bm25": 3, "dense": 1}),
            RerankCandidate(candidate_id="b", text="doc b", ranks={"bm25": 1, "dense": 4}),
            RerankCandidate(candidate_id="c", text="doc c", ranks={}),
        ],
        k=60,
        top_n=2,
    )

    response = api.rerank(request)
    print(f"Query: {response.query}\n")
    for result in response.results:
        print(
            f"candidate={result.candidate_id}, rank={result.rank}, score={result.score:.4f}, "
            f"best_rank={result.features['best_rank']}, systems={result.features['supporting_systems']}"
        )


if __name__ == "__main__":
    main()
