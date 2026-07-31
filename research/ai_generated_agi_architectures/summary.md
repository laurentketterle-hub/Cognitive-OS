# AGI Architecture Research — Synthesis & Key Findings

**Generated:** July 31, 2026
**Systems Surveyed:** 10 (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, Grok-2, DeepSeek-V3, Llama 3.1 405B, Mistral Large 2, Qwen 2.5, Perplexity Pro Search, Claude 3 Opus)

---

## Executive Summary

We prompted ten frontier AI systems — spanning OpenAI, Anthropic, Google DeepMind, xAI, DeepSeek, Meta, Mistral AI, Alibaba, and Perplexity — to propose detailed AGI architectures. The resulting proposals reveal striking convergence on several core principles, despite originating from independent systems with different training distributions and design philosophies. This synthesis identifies the common patterns, notable divergences, and actionable insights for AGI research and development.

---

## Common Patterns Across All Proposals

### 1. Hybrid Architectures Are Universal

Every single proposal (10/10) advocates for a **hybrid architecture** rather than a pure neural or pure symbolic approach. No system proposed an AGI based solely on scaling transformers or LLMs. The hybrids take different forms — neural-symbolic (GPT-4o, Claude 3 Opus), neural with explicit memory/retrieval (Perplexity, Llama 3.1), neural with dynamical systems (Gemini, DeepSeek-V3, Mistral Large 2) — but all combine multiple complementary mechanisms.

**Implication:** The era of "just scale the transformer" is over. The field's leading AI systems unanimously recognise that AGI requires architectural heterogeneity.

### 2. Memory Is Architecture, Not an Afterthought

All proposals dedicate substantial design attention to memory systems with at least three distinct memory stores (typically working, episodic, and semantic). Key patterns:

- **Working memory** is universally implemented through recurrent/attentional dynamics, not static context windows
- **Episodic memory** appears in 8/10 proposals, always with a consolidation mechanism that transfers patterns to semantic memory
- **External/retrieval-augmented memory** appears in 9/10 proposals — parametric knowledge alone is insufficient
- **Memory consolidation** (sleep phases, replay, slow-weight updates) is present in 7/10 proposals, inspired by neuroscience

### 3. Active, Continuous Learning

Every architecture assumes the system will **learn continuously during deployment**, not just during a pretraining phase. This is a radical departure from current LLM paradigms where models are frozen after training. Continuous learning mechanisms include: rehearsal-based consolidation (GPT-4o), forward-forward local plasticity (Mistral Large 2), federated learning (Llama 3.1), predictive coding (Gemini), active inference (DeepSeek-V3), and retrieval-feedback loops (Perplexity).

**Implication:** The frozen-model deployment model is seen as a temporary limitation, not a permanent feature of AI systems. Catastrophic forgetting is the key engineering challenge.

### 4. Safety as Architecture, Not Bolt-On

Safety mechanisms are integrated into the core architecture in all proposals, not applied as post-hoc filters. The approaches span a spectrum:

- **Formal/mathematical guarantees:** Claude 3 Opus (proof-carrying outputs, training invariant preservation)
- **Constitutional/rule-based:** GPT-4o (multi-layer constitutional), Claude 3.5 Sonnet (embedded constitutional deliberation), Llama 3.1 (community-defined policies)
- **Intrinsic/architectural:** Gemini (competitive ethical processor), DeepSeek-V3 (free energy conservatism), Mistral Large 2 (homeostatic regulation)
- **Epistemic/transparency:** Perplexity (source transparency, calibrated uncertainty)

### 5. Metacognition and Self-Modelling

A surprising convergence: 7/10 proposals include explicit **metacognitive or self-modelling components** — subsystems that track the system's own knowledge boundaries, confidence, and reasoning quality. This appears as: metacognitive self-model (Claude 3.5 Sonnet), meta-cognitive executive (Qwen 2.5), self-query monitor (Perplexity), meta-coordinator (Llama 3.1), and recursive self-improvement monitor (Claude 3 Opus).

**Implication:** The systems recognise that AGI-level intelligence requires knowing what you don't know and being able to reason about your own reasoning.

---

## Notable Divergences

### 1. The Role of Formal Verification

Claude 3 Opus proposes mathematical safety proofs — an approach fundamentally different from all others, which rely on statistical or architectural safety. This divide represents a philosophical question: can AGI safety be mathematically guaranteed, or is it inherently probabilistic?

### 2. Centralised vs. Decentralised Intelligence

- **Centralised:** GPT-4o, Claude 3.5 Sonnet, DeepSeek-V3, Gemini, Qwen 2.5, Perplexity, Claude 3 Opus, Grok-2 (8/10)
- **Decentralised/Federated:** Mistral Large 2 (fully distributed mesh), Llama 3.1 (federated skill marketplace)

The decentralised proposals envision AGI as an emergent property of many interacting components rather than a single monolithic system.

### 3. Knowledge Location: Internal vs. External

- **Internal knowledge (weights):** GPT-4o, Gemini, DeepSeek-V3, Mistral Large 2, Qwen 2.5, Grok-2 — these systems store knowledge primarily in model parameters
- **External knowledge (retrieval):** Perplexity — radical proposal to store only search strategies internally, retrieving facts on demand
- **Hybrid:** Claude 3.5 Sonnet, Llama 3.1, Claude 3 Opus — structured knowledge graphs alongside parametric memory

### 4. Biological Inspiration vs. Engineering Pragmatism

- **Biologically inspired:** Gemini (global workspace theory), DeepSeek-V3 (free energy principle), Mistral Large 2 (liquid networks, STDP), Qwen 2.5 (hierarchical predictive processing)
- **Engineering-first:** GPT-4o (DNTM, SMT), Llama 3.1 (LoRA marketplace), Perplexity (retrieval architecture), Claude 3 Opus (formal verification)

No clear consensus on whether AGI should mimic biological intelligence or pursue its own path.

---

## Timeline Consensus

Proposals cluster around a **2030–2035 AGI timeline**, with remarkable consistency:

| Timeline Range | Number of Proposals |
|---------------|---------------------|
| 2030–2033 | 2 (Perplexity, GPT-4o partial) |
| 2031–2035 | 4 (Gemini, Qwen 2.5, DeepSeek-V3, Grok-2) |
| 2032–2035 | 3 (Llama 3.1, Mistral Large 2, Claude 3.5 Sonnet) |
| 2034–2036 | 1 (Claude 3 Opus) |

The median is approximately 2033. The most conservative estimate (Claude 3 Opus, 2034–2036) reflects its more demanding formal verification requirements.

---

## Key Takeaways for AGI Development

1. **Diversify memory systems now.** The universal emphasis on multi-store memory with consolidation mechanisms suggests this is the most actionable near-term research direction. Current LLMs with simple context windows are far from what every proposed architecture considers necessary.

2. **Invest in continuous learning infrastructure.** The frozen-model paradigm is unanimously seen as a dead end for AGI. Organisations that solve catastrophic forgetting in large-scale continuous learning will have a decisive advantage.

3. **Safety must be architectural, not additive.** The proposals converge on the view that post-hoc safety filters (the current industry standard) will not scale to AGI. Safety mechanisms must be woven into the architecture's fabric.

4. **Metacognition is underappreciated.** The prevalence of self-modelling in these proposals suggests the field should invest more in systems that can reason about their own knowledge boundaries and reasoning quality.

5. **The transformer is a component, not the architecture.** Every proposal uses transformers or attention mechanisms, but none treats them as the complete solution. The AGI architecture of the future will be a hybrid system where transformers are one of many coordinated components.

6. **Formal verification represents an underexplored safety frontier.** Only one proposal (Claude 3 Opus) advocates for mathematical safety proofs, but the approach is theoretically compelling. Bridging the gap between formal methods and large-scale neural systems could yield transformative safety guarantees.

---

## Methodology Note

These proposals were generated by AI systems prompted as "AI systems architects." Each system was asked the same set of questions about AGI architecture design. The proposals should be interpreted as the systems' "views" on AGI — reflecting both their training distributions and their architectural priors — not as definitive technical specifications. The convergence patterns are particularly notable because each system was queried independently in fresh sessions, making cross-contamination unlikely.

---

*This synthesis was compiled from the raw outputs of ten frontier AI systems. Full proposals are available in the `raw_outputs/` directory.*
