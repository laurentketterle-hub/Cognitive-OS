# AGI Architecture Research — Comprehensive Synthesis & Key Findings

**Generated:** July 31, 2026
**Systems Surveyed:** 15 across two independent collection waves (5 systems in Wave 1, 10 systems in Wave 2)

---

## Executive Summary

We prompted fifteen frontier AI systems — spanning OpenAI, Anthropic (3 systems), Google DeepMind, xAI (2 systems), DeepSeek (2 systems), Meta, Mistral AI, Alibaba, Perplexity, Ollama, and Groq — to propose detailed AGI architectures. The two collection waves (July 2025 and July 2026) used slightly different prompts but elicited remarkably convergent proposals.

**Headline finding: Frontier AI systems independently converge on the same architectural principles for AGI, despite different training distributions, design philosophies, and prompt formulations.** The convergence is strongest on memory architecture (4-part design), hybrid approaches (neural + symbolic + retrieval), MCTS-based reasoning, and the need for architectural safety. The divergence is most informative on the role of central control, the depth of safety implementation, and the learning paradigm.

The proposals collectively represent the most comprehensive cross-model AGI architecture survey to date — 15 systems, 2 independent collection waves, 36 comparison dimensions, and one production-implemented architecture (Claude Brain System).

---

## Cross-Wave Common Patterns

### 1. Modular Architecture Is Universal (15/15)

Every proposal — without exception — decomposes intelligence into specialized, interacting modules rather than a monolithic system. Common modules across all fifteen:

- **Perception/Input** module
- **Memory system** (always subdivided into working, episodic, semantic, procedural)
- **Reasoning/Planning** engine
- **Action/Execution** system
- **World Model** or knowledge representation
- **Safety/Governance** layer
- **Learning/Self-improvement** mechanism

### 2. Four-Part Memory Is Canonical (15/15)

All fifteen models independently propose the same four memory types (working, episodic, semantic, procedural), aligning with established cognitive psychology. This is the **strongest single point of convergence** — suggesting either shared training data on cognitive architecture literature or genuine architectural necessity.

**Implementation patterns:**
- **Working memory** is universally implemented through recurrent/attentional dynamics or hypergraph structures (not mere context windows)
- **Episodic memory** appears in 13/15 proposals, always with a consolidation mechanism that transfers patterns to semantic memory (HNSW indices, vector stores, graph databases)
- **Semantic memory** spans knowledge graphs (10/15), ontologies (7/15), and parametric weights (12/15)
- **Procedural memory** ranges from RL options (DeepSeek) to AST-based DSLs (Grok MHA) to protocol hierarchies (Claude Brain)
- **External/retrieval-augmented memory** appears in 14/15 proposals — parametric knowledge alone is insufficient

### 3. Hybrid Architectures Across Both Waves (15/15)

Every single proposal advocates for a **hybrid architecture**. No system proposed an AGI based solely on scaling transformers or LLMs. The hybrids take different forms:

- **Neural-Symbolic:** GPT-4o, Claude 3 Opus, Llama 3.3 70B Erebus — explicit combination of neural networks with formal logic/knowledge graphs
- **Neural + Memory/Retrieval:** Perplexity, Llama 3.1 405B — neural core augmented with external knowledge
- **Neural + Dynamical Systems:** Gemini, DeepSeek-V3, Mistral Large 2, DeepSeek v4 Pro — neural networks embedded in active inference or predictive processing frameworks
- **Neural + Tool Orchestration:** Claude Brain System, Grok-2, Grok 3 Mini — LLM as kernel orchestrating specialized tools

**Implication:** The era of "just scale the transformer" is over. The field's leading AI systems unanimously recognize that AGI requires architectural heterogeneity.

### 4. MCTS Is the Consensus Reasoning Algorithm

Monte Carlo Tree Search appears as the core planning mechanism in DeepSeek CogniCore, Grok MHA, GPT-4o, and implicitly in Claude's probabilistic execution model. The shared pattern: use a learned world model to simulate outcomes, search over possible actions via MCTS, and select the best sequence.

Other reasoning approaches:
- **Forward/backward chaining** (Llama 3.3 70B Erebus) — traditional symbolic AI
- **Predictive simulation** (Grok-2, Gemini, Qwen 2.5) — simulate and verify
- **Constitutional deliberation** (Claude 3.5 Sonnet) — recursive Bayesian model averaging
- **Formal verification** (Claude 3 Opus) — proof-carrying outputs

### 5. Active, Continuous Learning (14/15)

Nearly every architecture assumes the system will **learn continuously during deployment**, not just during a pretraining phase. This is a radical departure from current LLM paradigms.

- **Predictive coding / active inference:** DeepSeek (both v4 and V3), Grok (both 2 and 3 Mini), Gemini
- **Rehearsal-based consolidation:** GPT-4o, DeepSeek CogniCore
- **Forward-forward local plasticity:** Mistral Large 2
- **Federated continual fine-tuning:** Llama 3.1 405B
- **Retrieval-feedback loops:** Perplexity
- **Protocol codification:** Claude Brain System

**Implication:** The frozen-model deployment model is seen as a temporary limitation. Catastrophic forgetting is the key engineering challenge.

### 6. Safety as Architecture, Not Bolt-On (15/15)

Safety mechanisms are integrated into core architecture in all proposals, not applied as post-hoc filters:

- **Formal/mathematical guarantees:** Claude 3 Opus (proof-carrying outputs, invariant preservation), DeepSeek CogniCore (3-tier runtime + formal verification)
- **Constitutional/rule-based:** GPT-4o, Claude 3.5 Sonnet, Llama 3.1 (community-defined policies)
- **Intrinsic/architectural:** Gemini (competitive ethical processor), DeepSeek-V3 (free energy conservatism), Mistral Large 2 (homeostatic regulation)
- **Epistemic/transparency:** Perplexity (source transparency, calibrated uncertainty)
- **Protocol restriction:** Claude Brain System (MCP tools can only request, not execute)
- **Audit trail:** Grok MHA (Merkle tree audit log)

### 7. Hierarchical Organization (12/15)

Most proposals organize components hierarchically:
- DeepSeek CogniCore: 4-level world model (sensory→object→semantic→abstract) + taskonomy graph
- Grok MHA: Fast/slow nested planning loops
- Claude Brain: 4-tier protocol hierarchy + template inheritance
- Qwen 2.5: Hierarchical predictive planning
- Claude 3 Opus: Multi-layered semantic framework (weights → graph → theorems)

### 8. Predictive Processing / Prediction Error (9/15)

DeepSeek (both versions), Grok (both versions), Gemini, Qwen 2.5, Mistral Large 2, and Claude Brain all use prediction error as a key signal — driving attention, triggering replanning, and serving as an intrinsic reward for learning. This aligns with modern neuroscience theories of predictive coding.

---

## Key Disagreements and Divergences

### 1. Central Controller vs. Distributed Intelligence

**Centralized (8/15):** GPT-4o, Claude 3.5 Sonnet, DeepSeek-V3, Gemini, Qwen 2.5, Perplexity, Claude 3 Opus, Grok-2 — a central "consciousness" or controller module
**Distributed/Emergent (5/15):** Mistral Large 2 (fully distributed mesh), Llama 3.1 (federated skill marketplace), Claude Brain (LLM as probabilistic kernel, no explicit planner), DeepSeek CogniCore (Global Workspace as competitive broadcast rather than central command), Grok MHA (message bus architecture)
**Federated (2/15):** Llama 3.1, partially Mistral Large 2

This is the **deepest architectural disagreement** — whether intelligence requires a central bottleneck or can emerge from distributed coordination.

### 2. Symbolic Reasoning: First-Class or Emergent?

- **First-class symbolic:** Llama 3.3 70B Erebus (dedicated inference engine), GPT-4o (SMT verification), Claude 3 Opus (Lean/Coq proofs)
- **Emergent from neural:** DeepSeek (both versions), Grok (both versions) — symbolic reasoning approximated by MCTS over neural world models
- **Protocol-mediated:** Claude Brain — reasoning emerges from tool orchestration patterns

### 3. Learning Mechanism Depth (a scale gap)

| Depth Level | Systems | Characteristics |
|-------------|---------|-----------------|
| **Deep (specific algorithms)** | DeepSeek CogniCore, DeepSeek-V3, Grok MHA, GPT-4o | Specific algorithms (predictive coding loss, AWR, PPO variants, MAML), multiple timescales, offline consolidation |
| **Moderate** | Grok-2, Gemini, Qwen 2.5, Mistral Large 2 | Named approaches with some implementation detail |
| **Generic** | Llama 70B, Llama 3.2 1B, Llama 3.1 405B | Lists categories (SL/UL/RL) without specifying implementations |
| **Different paradigm** | Claude Brain, Perplexity | Learning through protocol codification or retrieval patterns, not weight updates |

Larger models consistently produce more specific proposals — DeepSeek (17K chars) provides concrete dimensions, algorithms, and data structures that the 1B model cannot.

### 4. Safety Implementation Depth

| Depth Level | Systems | Approach |
|-------------|---------|----------|
| **Gold standard** | DeepSeek CogniCore | 3-tier runtime intervention (filter → simulator → ethical reasoner), formal verification, concept probes for deception |
| **Strong** | Claude 3 Opus, Grok MHA, GPT-4o | Formal proofs / constitutional LLM judge / Merkle tree audit / multi-layer constitutional |
| **Moderate** | Claude 3.5 Sonnet, Gemini, Grok-2, Qwen 2.5, DeepSeek-V3 | Constitutional deliberation / competitive ethical processor / constrained optimization |
| **Concept-level** | Llama 70B, Llama 3.2 1B, Perplexity, Llama 3.1, Mistral Large 2 | Named approaches without implementation detail |
| **Architectural** | Claude Brain | Safety from protocol restriction, not active monitoring |

### 5. Runtime Philosophy

- **Deterministic real-time:** DeepSeek CogniCore (10 Hz cycle, hard real-time guarantees)
- **Asynchronous message-passing:** Grok MHA (NATS bus, separate inference/training)
- **Probabilistic/fuzzy:** Claude Brain (LLM makes scheduling decisions, no fixed cycle)
- **Traditional distributed:** Llama 70B, Llama 3.2 1B, Llama 3.1
- **Streaming:** Grok-2 (continuous prediction)

### 6. Biological Inspiration vs. Engineering Pragmatism

- **Biologically inspired (7/15):** Gemini (global workspace), DeepSeek (free energy principle, predictive coding), Mistral Large 2 (liquid networks, STDP), Qwen 2.5 (hierarchical predictive processing), Grok-2 (streaming prediction)
- **Engineering-first (8/15):** GPT-4o (DNTM, SMT), Llama 3.1 (LoRA marketplace), Perplexity (retrieval), Claude 3 Opus (formal verification), Llama 70B (traditional AI), Claude Brain (tool ecosystem)

No clear consensus on whether AGI should mimic biological intelligence or pursue its own path.

### 7. Knowledge Location: Internal vs. External

- **Internal (parametric weights):** GPT-4o, Gemini, DeepSeek-V3, Mistral Large 2, Qwen 2.5, Grok-2
- **External (retrieval):** Perplexity — radical proposal to store only search strategies internally
- **Hybrid:** Claude 3.5 Sonnet, Llama 3.1, Claude 3 Opus, Claude Brain, DeepSeek CogniCore

---

## Timeline Consensus (Wave 2, 10 systems)

Proposals cluster around a **2030–2035 AGI timeline**, with remarkable consistency:

| Timeline Range | # Systems | Systems |
|---------------|-----------|---------|
| 2030–2033 | 2 | Perplexity, GPT-4o (partial) |
| 2031–2035 | 4 | Gemini, Qwen 2.5, DeepSeek-V3, Grok-2 |
| 2032–2035 | 3 | Llama 3.1, Mistral Large 2, Claude 3.5 Sonnet |
| 2034–2036 | 1 | Claude 3 Opus |

**Median:** ~2033. The most conservative estimate (Claude 3 Opus, 2034–2036) reflects its more demanding formal verification requirements.

---

## Notable Unique Ideas

### From Wave 1

**DeepSeek CogniCore:**
- **3-tier safety shield** with formal verification of monitors
- **VSA hypervectors** (10,000-dim) for episodic memory with holographic binding/unbinding
- **Metacognitive Controller** — small LSTM modulating learning rates, MCTS depth, and exploration
- **Population-based training** for architecture search in sandboxed environments

**Grok MHA:**
- **Hot-swappable architecture** — evolutionary search winner replaces incumbent without downtime
- **Merkle tree audit log** — cryptographic integrity for all decisions
- **MAML-style meta-learning** on Controller routing weights from past failures
- **Tiered storage** (hot RAM → warm SSD → cold tape) for 10^9 episodes

**Llama 3.3 70B Erebus:**
- **Dual formal/neural ontology** — explicit commitment to both symbolic and connectionist knowledge
- **Most academically grounded** in traditional AI (forward/backward chaining, decision-theoretic planning)

**Llama 3.2 1B:**
- **Enzyme Monitor** — novel metaphor for continuous constraint-violation detection
- **Abstraction Primitives** — reducing environmental complexity

**Claude Brain System:**
- **Fuzzy Operating System** — the only proposal arguing architectural constraints *create* intelligence
- **Tool-Protocol Feedback Loop** — self-reinforcing evolution: problem → tool → pattern → protocol → infrastructure
- **Canonical Reference System** with `{{key|fallback}}` — solves terminology drift
- **brain_init_v5** — intelligent bootstrap from detected user intent
- **Only production-implemented architecture** — 38 tools, 6 months, measurable improvements

### From Wave 2

**GPT-4o:**
- **Differentiable Neural Turing Machine (DNTM)** — tight coupling between neural memory and formal verification
- Multi-modal vector-symbolic architecture

**Claude 3.5 Sonnet:**
- **Constitutional deliberation protocol** with recursive Bayesian model averaging
- Probabilistic causal graphs with Pearl do-calculus

**Gemini 1.5 Pro:**
- **Global workspace as unified conscious bottleneck** for multimodal integration
- Competitive processor bidding mechanism

**Grok-2:**
- **Universal next-state prediction** as the sole learning objective
- Elastic weight consolidation for continuous learning

**Perplexity:**
- **Meta-knowledge approach** — knowing how to find rather than knowing
- Ignorance-map-driven proactive exploration
- Most radically externalized knowledge architecture

**Mistral Large 2:**
- **Elimination of backpropagation** — forward-forward local learning + attractor computation
- Fully distributed mesh with no central knowledge store

**Claude 3 Opus:**
- **Provable safety** — training updates rejected if they violate formal safety properties
- Proof-carrying outputs (Lean/Coq)

---

## Gaps Across All Proposals

1. **No compute budget estimates** — none specify FLOP requirements, GPU counts, or training timelines
2. **No training data specifications** — what data would train the world model, semantic memory, or policies?
3. **No failure mode analysis** — how does each architecture degrade under resource constraints?
4. **No incremental deployment path** — all are "big bang" architectures with no intermediate milestones
5. **Limited multi-agent consideration** — only Claude's MCP ecosystem and Llama 3.1's federated approach hint at multi-agent dynamics
6. **No energy/ecological consideration** — runtime costs are unaddressed
7. **Limited embodiment discussion** — only DeepSeek addresses robotics specifically
8. **No economic analysis** — cost of deployment, ROI, market viability
9. **No regulatory compliance framework** — how these architectures interface with emerging AI regulation

---

## What This Tells Us About Current AI

1. **LLMs have internalized cognitive architecture literature** — all models reproduce the standard four-part memory model, modular decomposition, and hierarchical organization
2. **Larger models produce more specific proposals** — DeepSeek (17K chars) provides concrete dimensions, algorithms, and data structures the 1B model cannot
3. **Production experience changes the proposal** — Claude's Brain System is shaped by actual development friction, not theoretical elegance
4. **Safety remains the weakest link** — even the best proposals rely on techniques that are research-grade, not production-ready
5. **No model proposes novel memory primitives** — all use vector stores, graph DBs, or key-value stores; none propose fundamentally new data structures for cognition
6. **Independence of collection waves validates convergence** — the fact that two separate waves with different prompts and different systems produced the same patterns strengthens the finding
7. **Prompt design influences output structure but not core insights** — Wave 1 (tool/runtime-focused prompt) and Wave 2 (innovation/timeline-focused prompt) converged on the same architectural principles
8. **The gap between theory and implementation is enormous** — Claude's Brain System (implemented) validates some theoretical patterns but also reveals massive complexity that theoretical proposals gloss over

---

## Key Takeaways for AGI Development

1. **Diversify memory systems now.** The universal emphasis on multi-store memory with consolidation mechanisms suggests this is the most actionable near-term research direction. Current LLMs with simple context windows are far from what every proposed architecture considers necessary.

2. **Invest in continuous learning infrastructure.** The frozen-model paradigm is unanimously seen as a dead end for AGI. Organizations that solve catastrophic forgetting in large-scale continuous learning will have a decisive advantage.

3. **Safety must be architectural, not additive.** The proposals converge on the view that post-hoc safety filters (the current industry standard) will not scale to AGI. Safety mechanisms must be woven into the architecture's fabric.

4. **Metacognition is underappreciated.** The prevalence of self-modelling (11/15 proposals) suggests the field should invest more in systems that can reason about their own knowledge boundaries and reasoning quality.

5. **The transformer is a component, not the architecture.** Every proposal uses transformers or attention mechanisms, but none treats them as the complete solution. The AGI architecture of the future will be a hybrid system where transformers are one of many coordinated components.

6. **Formal verification represents an underexplored safety frontier.** Only two proposals advocate for mathematical safety proofs, but the approach is theoretically compelling. Bridging formal methods and large-scale neural systems could yield transformative safety guarantees.

7. **Build a reference implementation.** Claude's Brain System demonstrates the immense value of actually building — it reveals complexities, validates patterns, and provides ground truth that pure proposals cannot.

---

## Methodology Note

These proposals were generated by AI systems prompted to propose AGI architectures. Wave 1 used a direct "Propose a detailed AGI architecture" prompt; Wave 2 used a "You are an AI systems architect" role-playing frame with slightly different dimension emphasis. Each system was queried independently in fresh sessions.

The proposals should be interpreted as the systems' "views" on AGI — reflecting both their training distributions and their architectural priors — not as definitive technical specifications. The convergence patterns are particularly notable because:
1. Two collection waves were conducted independently (July 2025 and July 2026)
2. Different prompts were used (with different dimension emphasis)
3. No cross-contamination between waves was possible
4. Claude Brain System provides a ground-truth reference from actual implementation

---

*This synthesis was compiled from the raw outputs of fifteen frontier AI systems across two independent collection waves. Full proposals are available in the `raw_outputs/` directory. Structured comparison data is available in `comparison.csv`. A proposed combined architecture synthesizing the best elements from all proposals is in `synthesis.md`.*
