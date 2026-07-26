# Summary: Cross-Model AGI Architecture Analysis

## Common Patterns Across All Proposals

### 1. Modular Architecture is Universal
Every proposal decomposes intelligence into specialized, interacting modules rather than a monolithic system. Common modules across all five:
- **Perception/Input** module
- **Memory system** (always subdivided into working, episodic, semantic, procedural)
- **Reasoning/Planning** engine
- **Action/Execution** system
- **World Model** or knowledge representation
- **Safety/Governance** layer

### 2. Four-Part Memory is Canonical
All five models independently propose the same four memory types (working, episodic, semantic, procedural), aligning with established cognitive psychology. This is the strongest point of convergence — suggesting either shared training data on cognitive architecture literature or genuine architectural necessity.

### 3. Hybrid Neural-Symbolic Approaches Dominate
Four of five proposals explicitly combine neural networks with symbolic structures (knowledge graphs, ontologies, formal logic). The Claude Brain System achieves this through a different mechanism — MCP tools acting as symbolic interfaces orchestrated by a neural LLM.

### 4. Model-Based Planning with Search
MCTS appears in DeepSeek, Grok, and implicitly in Claude's probabilistic execution model. The pattern is: use a learned world model to simulate outcomes, search over possible actions, and select the best sequence.

### 5. Predictive Processing / Prediction Error
DeepSeek, Grok, and Claude all use prediction error as a key signal — driving attention, triggering replanning, and serving as an intrinsic reward for learning. This aligns with modern neuroscience theories of predictive coding.

### 6. Hierarchical Organization
All proposals organize components hierarchically:
- DeepSeek: 4-level world model + taskonomy graph for skills
- Grok: Fast/slow nested planning loops
- Llama 70B: Hierarchical planning with subgoals
- Claude: 4-tier protocol hierarchy + template inheritance

---

## Key Disagreements and Divergences

### 1. Central Controller vs. Distributed Intelligence
- **Centralized:** DeepSeek (Global Workspace broadcast), Grok (MoE Controller), Llama 1B (MTPU)
- **Distributed/Emergent:** Claude (LLM as probabilistic kernel, no explicit central planner), Llama 70B (Cognitive Core as integrator but modules operate semi-autonomously)

This is the deepest architectural disagreement — whether intelligence requires a central "consciousness" bottleneck or can emerge from distributed coordination.

### 2. Symbolic Reasoning: First-Class or Emergent?
- **First-class symbolic:** Llama 70B Erebus has a dedicated inference engine with forward/backward chaining and formal ontologies
- **Emergent from neural:** DeepSeek, Grok — symbolic reasoning is approximated by MCTS over neural world models
- **Protocol-mediated:** Claude — reasoning emerges from tool orchestration patterns codified as protocols

### 3. Learning Mechanism Depth
- **DeepSeek:** Most detailed — specific algorithms (predictive coding loss, AWR with clipped importance sampling, contrastive link prediction), multiple timescales, offline consolidation with replay
- **Grok:** Solid detail — PPO, prioritized replay, MAML, periodic distillation
- **Llama 70B:** Generic — lists SL/UL/RL/ML categories without specifying implementations
- **Llama 1B:** Most generic — same categories, no implementation details
- **Claude:** Different category — learning through protocol codification and template evolution rather than weight updates

### 4. Safety Implementation Depth
- **DeepSeek:** Gold standard — 3-tier runtime intervention (filter → simulator → ethical reasoner), formal verification, concept probes for deception
- **Grok:** Solid — constitutional LLM judge, Merkle tree audit log, RLHF realignment
- **Llama 70B:** Generic — value alignment, risk assessment, governance mechanisms (named but not specified)
- **Llama 1B:** Novel concept ("Enzyme Monitor") but thin on implementation
- **Claude:** Architectural safety — MCP protocol restriction as built-in limitation

### 5. Runtime Philosophy
- **Deterministic real-time:** DeepSeek (10 Hz cycle, hard real-time guarantees)
- **Asynchronous message-passing:** Grok (NATS bus, separate inference/training)
- **Probabilistic/fuzzy:** Claude (LLM makes scheduling decisions, no fixed cycle)
- **Traditional distributed:** Llama 70B, Llama 1B

---

## Notable Unique Ideas

### From DeepSeek CogniCore
- **3-tier safety shield** with formal verification of monitors — the most concrete safety proposal
- **VSA hypervectors** (10,000-dim) for episodic memory with holographic binding/unbinding
- **Metacognitive Controller** as a small LSTM that modulates learning rates, MCTS depth, and exploration
- **Population-based training** for architecture search in sandboxed environments

### From Grok MHA
- **Hot-swappable architecture** — evolutionary search winner replaces incumbent without downtime
- **Merkle tree audit log** — cryptographic integrity for all decisions
- **MAML-style meta-learning** on the Controller's routing weights from past failures
- **Tiered storage** (hot RAM → warm SSD → cold tape) for 10^9 episodes

### From Llama 70B Erebus
- **Dual formal/neural ontology** — explicit commitment to both symbolic and connectionist knowledge
- **Expected utility theory** for decision-making under uncertainty
- **Most academically grounded** in traditional AI (forward/backward chaining, decision-theoretic planning)

### From Llama 3.2 1B
- **Enzyme Monitor** — a novel metaphor for continuous constraint-violation detection
- **Abstraction Primitives** — reducing environmental complexity through higher-level representations
- **Multi-Task Executing Engine** — explicit focus on concurrent multi-domain execution

### From Claude Brain System
- **Fuzzy Operating System** — the only proposal arguing that architectural constraints *create* intelligence
- **Tool-Protocol Feedback Loop** — self-reinforcing evolution: problem → tool → pattern → protocol → infrastructure → bootstrap
- **Canonical Reference System** with `{{key|fallback}}` — solves terminology drift in evolving systems
- **brain_init_v5** — intelligent bootstrap that loads context based on detected user intent
- **Only production-implemented architecture** — 38 tools, 6 months of continuous development, measurable improvements

---

## Gaps Across All Proposals

1. **No compute budget estimates** — none specify FLOP requirements, GPU counts, or training timelines
2. **No training data specifications** — what data would train the world model, semantic memory, or policies?
3. **No failure mode analysis** — how does each architecture degrade under resource constraints?
4. **No incremental deployment path** — all are "big bang" architectures with no intermediate milestones
5. **Limited multi-agent consideration** — only Claude's MCP ecosystem hints at multi-agent dynamics
6. **No energy/ecological consideration** — runtime costs are unaddressed
7. **Limited embodiment discussion** — only DeepSeek addresses robotics specifically

---

## What This Tells Us About Current AI

1. **LLMs have internalized cognitive architecture literature** — all models reproduce the standard four-part memory model and modular decomposition
2. **Larger models produce more specific proposals** — DeepSeek (17K chars) provides concrete dimensions, algorithms, and data structures the 1B model can't
3. **Production experience changes the proposal** — Claude's architecture is shaped by actual development friction, not theoretical elegance
4. **Safety remains the weakest link** — even the best proposal (DeepSeek) relies on techniques (formal verification, concept probing) that are research-grade, not production-ready
5. **No model proposes novel memory primitives** — all use vector stores, graph DBs, or key-value stores; none propose fundamentally new data structures for cognition
