# Research lab workflows with the Savant RRF client

This guide outlines a few practical flows for research groups using the generated
Python client to explore retrieval-augmented and quality-evaluation workflows.

## 1. Rerank literature snippets locally

1. Assemble candidate abstracts from multiple sources (e.g., arXiv search,
   institutional repositories) and record their ranks per source.
2. Construct `RerankRequest` objects that include the upstream ranks so the
   reciprocal-rank-fusion scores can be computed locally via `DefaultApi.rerank`.
3. Use the returned `features` per candidate to audit how much each system
   contributed and filter by `supporting_systems` when you need consensus-only
   results.

## 2. Evaluate generated answers with Savant quality metrics

1. Generate candidate answers to a prompt with your preferred LLM.
2. Submit them through `evaluate_quality` with `normalize_scores=True` to obtain
   Φ, Ω, SRRF, and CRRF scores alongside optional roles profiles.
3. Sort by `metrics.phi` and track `meta_score` to flag outliers for manual
   inspection during paper writing or experiment reviews.

## 3. Build embeddings for lab notebooks and datasets

1. Batch notebook entries or dataset descriptions with `EmbedRequest` and enable
   `include_dimension` to capture the embedding size.
2. Store the normalized vectors in your vector database; the consistent
   dimension helps keep the schema stable across experiments.
3. Use the embeddings to drive similarity search for experiment retrieval and to
   seed future reranking requests with contextual candidates.

## 4. Tutor junior researchers on new topics

1. Let new collaborators submit questions through `tutor_with_savant_rrf` with
   `student_level` tuned to their background.
2. Set `include_candidates=True` during pilot studies to review alternate
   answers and their Savant metrics for pedagogy tuning.
3. Combine the tutoring response with a follow-up `roles_profile` call to surface
   the conceptual angles emphasized in the explanation.
