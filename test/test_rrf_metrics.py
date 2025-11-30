import math
import pytest

from swagger_client.rrf_metrics import compute_rrf_features


def test_compute_rrf_features_returns_rrf_values():
    ranks = {"bm25": 1, "dense": 5, "hybrid": 10}
    features = compute_rrf_features(ranks, k=50)

    expected_score = (1 / 51.0) + (1 / 55.0) + (1 / 60.0)
    assert math.isclose(features["rrf_score"], expected_score)
    assert features["supporting_systems"] == 3
    assert math.isclose(features["mean_reciprocal_rank"], expected_score / 3)
    assert features["best_rank"] == 1


def test_compute_rrf_features_handles_empty_map():
    features = compute_rrf_features({})
    assert features == {
        "rrf_score": 0.0,
        "supporting_systems": 0,
        "mean_reciprocal_rank": 0.0,
        "best_rank": None,
    }


def test_compute_rrf_features_rejects_invalid_rank():
    with pytest.raises(ValueError):
        compute_rrf_features({"bm25": 0})
