"""RRF feature utilities used by the local reranker helpers."""
from __future__ import division
from typing import Optional


def compute_rrf_features(ranks_by_system, k=60):
    """Compute reciprocal-rank-fusion metrics for a candidate.

    The caller provides a mapping of system identifiers ("bm25", "dense",
    etc.) to 1-based ranks. The function converts those to reciprocal-rank
    contributions and aggregates several interpretable statistics:

    * ``rrf_score`` – the canonical RRF sum ``sum(1 / (k + rank))``
    * ``supporting_systems`` – how many rankers contributed
    * ``mean_reciprocal_rank`` – average reciprocal contribution
    * ``best_rank`` – the smallest rank provided (i.e., best position)

    Invalid or non-positive ranks raise ``ValueError`` to surface issues
    early, matching the expectation that the caller replaces any placeholder
    data with real ranking signals.
    """
    if ranks_by_system is None:
        ranks_by_system = {}

    if not isinstance(ranks_by_system, dict):
        raise TypeError("ranks_by_system must be a dictionary of system->rank")

    if not ranks_by_system:
        return {
            'rrf_score': 0.0,
            'supporting_systems': 0,
            'mean_reciprocal_rank': 0.0,
            'best_rank': None
        }

    reciprocal_ranks = []
    best_rank: Optional[int] = None

    for system, rank in ranks_by_system.items():
        if rank is None:
            raise ValueError("Rank for system '%s' must not be None" % system)
        if not isinstance(rank, int):
            raise TypeError("Rank for system '%s' must be an integer" % system)
        if rank <= 0:
            raise ValueError("Rank for system '%s' must be positive" % system)

        reciprocal = 1.0 / (k + rank)
        reciprocal_ranks.append(reciprocal)
        if best_rank is None or rank < best_rank:
            best_rank = rank

    rrf_score = sum(reciprocal_ranks)
    supporting_systems = len(reciprocal_ranks)
    mean_reciprocal_rank = rrf_score / supporting_systems if supporting_systems else 0.0

    return {
        'rrf_score': rrf_score,
        'supporting_systems': supporting_systems,
        'mean_reciprocal_rank': mean_reciprocal_rank,
        'best_rank': best_rank
    }
