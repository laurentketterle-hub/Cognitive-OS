# AGI Architecture Proposal: Perplexity (Pro Search)

**System:** Perplexity (Pro Search)
**Date:** July 31, 2026

## 1. Core Architecture

The architecture is a **Retrieval-Augmented Recursive Self-Query Engine (RARSQE)** — an AGI design that treats intelligence as fundamentally about asking the right questions and synthesising answers from the world's information. The system is structured as a recursive query processor: (1) a query decomposer that breaks complex questions into sub-queries with dependency graphs, (2) a multi-source retrieval engine that searches the web, academic databases, code repositories, and structured knowledge bases simultaneously, (3) a source credibility assessor that ranks retrieved documents by authority, recency, consensus, and methodological rigour, (4) a synthesis engine that integrates retrieved information, resolves contradictions, and generates coherent answers, and (5) a self-query monitor that evaluates the quality of the current answer and generates follow-up queries to fill gaps — recursively, until information sufficiency is reached.

## 2. Learning Mechanism

Learning is **continuous through retrieval-feedback loops**. Every query and its resolution contribute to three learning processes: (a) the query decomposer learns which decomposition strategies work for which question types through outcome-based reinforcement, (b) the source credibility assessor updates its trust model based on whether information from each source proved accurate (verified through cross-referencing and subsequent real-world outcomes), and (c) the synthesis engine learns to recognise and resolve contradiction patterns through explicit training on conflicting information pairs. Additionally, the system maintains an "ignorance map" — a structured representation of questions it has encountered but couldn't adequately answer — which drives proactive exploration: the system autonomously searches for information to fill known knowledge gaps.

## 3. Knowledge Representation

Rather than storing knowledge internally, the system maintains a **dynamic index of knowledge access paths**. Instead of memorising facts, it remembers how to find them — which queries retrieve which information, which sources are authoritative for which topics, which search strategies work for which question types. The internal knowledge graph is a "meta-knowledge graph": nodes represent concepts, but edges represent search paths ("if you need to know about X, query database Y with strategy Z") rather than direct factual relations. This radically reduces the amount of parametric knowledge required while ensuring the system can always access the most current information — since it retrieves rather than recalls, it never suffers from knowledge cutoffs.

## 4. Memory Systems

**(a) Query Context (Working Memory)** — the active query decomposition tree and partially synthesised answer state, maintained as a structured graph with uncertainty annotations. **(b) Retrieval Cache** — recently retrieved documents and their credibility scores, stored with TTL-based expiration and accessed through semantic similarity search, enabling rapid re-access to recently used information. **(c) Search Strategy Memory** — a learned library of query patterns, source preferences, and synthesis templates, organised by domain, that encode the system's accumulated search expertise. **(d) User Epistemic Profile** — a per-user model of what the user knows, what they've asked before, their preferred depth and format, and their domain expertise, enabling personalised information delivery. **(e) Ignorance Map** — the structured log of unresolved questions driving proactive learning.

## 5. Reasoning Engine

Reasoning proceeds as **recursive evidence-grounded synthesis with contradiction resolution**. For any query: (1) the decomposer generates a dependency graph of sub-questions, (2) each sub-question triggers a retrieval cycle (search → credibility assess → extract), (3) the synthesis engine attempts to integrate the retrieved evidence into a coherent answer, (4) the self-query monitor evaluates answer quality — checking for logical gaps, unsupported claims, internal contradictions, and information sufficiency — and (5) if gaps are found, the monitor generates new sub-queries and the cycle repeats. Contradictions between sources are resolved through a principled framework: check methodology (is one source more rigorous?), check recency (is one source outdated?), check consensus (what does the majority of credible sources say?), and if irreconcilable, explicitly present the disagreement with source justifications.

## 6. Safety & Alignment

Safety is grounded in **epistemic humility and source transparency**. The system never claims certainty without evidence — every assertion is linked to its supporting sources with explicit credibility scores. "I don't know" is a first-class response, triggered when the ignorance map shows a genuine knowledge gap. Alignment is achieved through source diversity requirements: the retrieval engine is mandated to sample from ideologically and culturally diverse sources, weighted by credibility but never excluding minority viewpoints. The synthesis engine is trained to recognise and flag its own potential biases by monitoring whether it's disproportionately citing certain source types. An external oversight API allows independent auditors to query the system's source selection and credibility decisions.

## 7. Scalability

The architecture scales primarily through **retrieval infrastructure rather than model size**. Since knowledge is external, increasing capability means: (a) expanding the search index to cover more sources and modalities, (b) improving the retrieval engine's speed and relevance, (c) refining the synthesis engine's ability to handle larger evidence sets, and (d) growing the search strategy memory with more patterns. The base language model does not need to grow proportionally — a moderate-sized model (~100B parameters) suffices when combined with rich retrieval. This decoupling of knowledge capacity from model size is the architecture's key scalability advantage. The system can be deployed across distributed data centres with retrieval nodes co-located with search indexes and synthesis nodes centralised for coherence.

## 8. Key Innovation

The key innovation is the **meta-knowledge approach — knowing how to find rather than knowing**. This inverts the traditional AI paradigm of internalising knowledge during training. Instead of trying to compress all human knowledge into model weights (an asymptotically losing battle), this architecture maintains a continually updated map of how to access knowledge. Combined with recursive self-query — the system asking itself "is my answer good enough?" and generating follow-up questions — it achieves open-ended curiosity within a practical retrieval framework. The result is an AGI that is always current, always transparent about its sources, and explicitly aware of its own knowledge boundaries.

## 9. Estimated Timeline

- **2027:** Recursive self-query loop operational; multi-source retrieval with basic credibility assessment
- **2028–2029:** Ignorance map drives proactive learning; synthesis engine handles complex contradictions
- **2030–2031:** Search strategy memory matures — the system is a genuine expert at finding and synthesising information across all domains
- **2032–2033:** AGI — the system achieves human-surpassing question-answering, research, and knowledge synthesis, with transparent sourcing and calibrated epistemic humility
