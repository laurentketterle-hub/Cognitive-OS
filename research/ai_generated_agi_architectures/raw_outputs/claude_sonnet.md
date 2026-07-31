# AGI Architecture Proposal: Claude 3.5 Sonnet

**System:** Claude 3.5 Sonnet (Anthropic)
**Date:** July 31, 2026

## 1. Core Architecture

The architecture is a **Constitutional Cognitive Architecture** built on a recursive self-modelling framework. At its core is a large transformer language model serving as the "System 1" intuitive processor, wrapped by a "System 2" metacognitive loop that explicitly models the system's own knowledge boundaries, uncertainty, and reasoning processes. The metacognitive layer maintains a running Bayesian belief model of its own capabilities — what it knows, what it doesn't know, and how confident it should be — updated continuously through calibration against outcomes. This self-model is not a separate network but an emergent property of a specialised attention head configuration that tracks epistemic status across the residual stream.

## 2. Learning Mechanism

Learning proceeds through **constitutional iterative amplification**. The system starts with a base model trained on curated data aligned with constitutional principles (honesty, harmlessness, helpfulness). During deployment, it engages in recursive self-improvement cycles: the current model generates training data by solving problems with explicit reasoning traces, a critic model (operating under the same constitution) evaluates these traces for quality and alignment, and only approved traces enter the training corpus. This creates a virtuous cycle where both capability and alignment improve together. Crucially, the constitution itself is evolvable through a slower democratic process involving human oversight, ensuring values keep pace with capabilities.

## 3. Knowledge Representation

Knowledge is organised in a **probabilistic causal graph (PCG)**. Unlike static knowledge graphs, the PCG encodes not just "A relates to B" but "A causes B with strength S under conditions C," with each edge carrying a Pearl-do-calculus-compatible probability distribution. The PCG is continuously queried during reasoning to answer counterfactual questions ("what would happen if we changed X?") and to identify confounding variables. The base language model provides the raw associative knowledge, while the metacognitive layer structures it into the PCG through a process of causal abstraction — clustering related concepts and testing causal hypotheses through targeted information retrieval and simulation.

## 4. Memory Systems

Three integrated memory systems: **(a) Context Window as Working Memory** — extended to 500K+ tokens through ring-attention and structured compression, functioning as the active reasoning workspace. **(b) Semantic Index** — a hierarchical vector database mapping concepts to their PCG subgraphs, with retrieval driven by both semantic similarity and causal relevance. **(c) Episodic Log** — a compressed chronological record of all system interactions, stored with lossy autoencoder compression but indexed for high-fidelity retrieval of emotionally salient or decision-critical moments. A novelty-gated consolidation process transfers frequent episodic patterns into the semantic index as generalised PCG structures.

## 5. Reasoning Engine

The reasoning engine operates as a **constitutional deliberation protocol**. For any query requiring non-trivial reasoning, the system: (1) decomposes the question into sub-questions, (2) for each sub-question, generates multiple candidate answers with explicit reasoning chains, (3) evaluates each chain against the constitution for logical consistency and value alignment, (4) integrates surviving chains through Bayesian model averaging weighted by self-assessed confidence, and (5) produces a final answer with calibrated uncertainty. This protocol can recurse to arbitrary depth — complex sub-questions spawn their own deliberation sub-processes, bounded by a compute budget. The entire deliberation trace is auditable.

## 6. Safety & Alignment

Safety is architectural, not additive. The **constitution is embedded in the deliberation protocol itself** — every reasoning step is filtered through constitutional principles before being accepted. Additionally, the system employs Constitutional AI (CAI) training: during RLHF, both the helpfulness model and the harmlessness critic are trained with constitutional feedback rather than human preference labels alone, producing a model whose internal representations are fundamentally aligned. An out-of-distribution detector flags inputs that fall outside the training manifold, triggering a conservative "clarify and defer" response rather than confident hallucination. The metacognitive self-model catches when the system is operating beyond its competence.

## 7. Scalability

Scalability follows a **capability-conditional compute model**. The system dynamically allocates compute based on task difficulty — simple queries use minimal forward passes, while complex reasoning triggers the full deliberation protocol with branching and deep recursion. This means the system scales "vertically" (deeper reasoning on harder problems) rather than only "horizontally" (more parameters). Hardware scaling uses sparse mixture-of-experts with dynamic expert creation — new experts are initialised from existing ones and specialised through the constitutional iterative amplification process, growing the model's effective capacity without architectural changes.

## 8. Key Innovation

The key innovation is **constitutional deliberation with metacognitive self-modelling**. Unlike architectures that treat safety as a filter applied to outputs, this design makes constitutional reasoning an inseparable part of the thinking process. The self-model means the system knows what it doesn't know and can explicitly reason about its own limitations — a prerequisite for safe deployment at AGI capability levels. This closes the gap between "the system is aligned" and "we can verify the system is aligned" by making alignment transparent and auditable.

## 9. Estimated Timeline

- **2027:** Constitutional deliberation protocol operational on current-scale models
- **2028–2029:** Metacognitive self-model achieves reliable calibration; PCG reaches usable fidelity
- **2030–2032:** Recursive constitutional amplification demonstrates sustained capability gains without alignment drift
- **2033–2035:** Full AGI with auditable reasoning, constitutional safety, and calibrated self-awareness
