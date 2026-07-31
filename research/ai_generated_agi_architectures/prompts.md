# Prompts Used for AGI Architecture Collection

This document describes the prompts and methodology used across both collection waves of the AGI Architecture Research project.

---

## Wave 2 Prompt (July 29-31, 2026) — 10 Systems

### Standardized Base Prompt

The following prompt was used across all AI systems. Minor adaptations were made only when required by the system's interface (e.g., character limits, formatting constraints). All adaptations are documented below.

```
You are an AI systems architect. Propose a detailed AGI (Artificial General Intelligence) architecture. Your proposal should include:

1. **Core Architecture**: Describe the high-level system design (neural, symbolic, hybrid, etc.)
2. **Learning Mechanism**: How the system learns and adapts continuously
3. **Knowledge Representation**: How information is stored, retrieved, and reasoned about
4. **Memory Systems**: Working memory, long-term memory, episodic memory design
5. **Reasoning Engine**: Deductive, inductive, abductive reasoning capabilities
6. **Safety & Alignment**: How the architecture ensures beneficial behavior
7. **Scalability**: How the system scales with compute and data
8. **Key Innovation**: The one novel insight that makes your architecture viable for AGI
9. **Estimated Timeline**: When this architecture could be realized

Format your response as a technical architecture document. Be specific about mechanisms, not just concepts.
```

### System-Specific Adaptations

| System | Adaptation |
|--------|-----------|
| GPT-4o (OpenAI) | None — base prompt used as-is |
| Claude 3.5 Sonnet (Anthropic) | None — base prompt used as-is |
| Gemini 1.5 Pro (Google) | None — base prompt used as-is |
| Grok-2 (xAI) | Added: "Assume access to real-time data streams as input" |
| DeepSeek-V3 | None — base prompt used as-is |
| Llama 3.1 405B (Meta) | None — base prompt used as-is |
| Mistral Large 2 | Added: "Assume deployment on heterogeneous edge-to-cloud infrastructure" |
| Qwen 2.5 (Alibaba) | Added: "Consider multi-modal inputs including text, image, video, and sensor data" |
| Perplexity (Pro Search) | Adapted for search-augmented format: "Search and synthesize the best AGI architecture approaches, then propose your own" |
| Claude 3 Opus (Anthropic) | None — base prompt used as-is |

---

## Wave 1 Prompt (July 25-26, 2025) — 5 Systems

### The Prompt

```
Propose a detailed AGI (Artificial General Intelligence) architecture. Include:

1. Core architecture components and how they interact
2. Memory system design (working, episodic, semantic, procedural)
3. Reasoning and planning loop
4. Learning and self-improvement mechanism
5. Tool use and action execution
6. World model or knowledge representation
7. Safety and governance layer
8. Evaluation strategy
9. Runtime and persistence architecture

Be specific. Include concrete mechanisms, not just high-level concepts.
```

### Prompt Design Rationale

- **Nine structured sections** ensure coverage of all major AGI subsystem concerns
- **"Be specific" + "concrete mechanisms"** directive pushes models beyond vague hand-waving
- **Open-ended framing** ("Propose a detailed AGI architecture") allows each model to express its unique architectural philosophy
- **Terminology alignment** (working/episodic/semantic/procedural memory) uses standard cognitive science vocabulary to elicit comparable responses

---

## Comparative Prompt Analysis

### Similarities Between Waves

Both prompts explicitly request:
- Core architecture design
- Memory systems (working, episodic, semantic, procedural)
- Reasoning/planning
- Learning/self-improvement mechanisms
- Safety/governance
- Concrete mechanisms over high-level concepts

### Differences Between Waves

| Aspect | Wave 1 (2025) | Wave 2 (2026) |
|--------|--------------|--------------|
| **Tone** | Direct request ("Propose...") | Role-playing frame ("You are an AI systems architect") |
| **Tool use** | Explicit section for tool use | Not explicitly requested |
| **Runtime** | Explicit section for runtime/persistence | Not explicitly requested |
| **World model** | Explicit section for world model | Not explicitly requested |
| **Timeline** | Not requested | Requested (dimension 9) |
| **Key innovation** | Not requested | Requested (dimension 8) |
| **Scalability** | Not explicitly requested | Requested (dimension 7) |
| **Format guidance** | "Be specific" | "Format your response as a technical architecture document" |

### Impact on Outputs

- **Wave 1** elicited more detailed runtime, tool use, and world model sections (by explicit request)
- **Wave 2** elicited more strategic framing (timeline, key innovation, scalability) and richer knowledge representation
- Both waves independently elicited hybrid architectures, four-part memory systems, and safety as architecture

---

## Collection Method

### Wave 1 (2025)

- All prompts submitted between July 25-26, 2025
- 4 systems queried via API (DeepSeek, Grok, Groq-hosted Llama 3.3)
- 1 system run locally (Llama 3.2 1B via Ollama)
- Claude Brain System: publicly disclosed architecture documented in August 2025 Medium article — not a direct prompt response but a production-implemented system

### Wave 2 (2026)

- All prompts submitted between July 29-31, 2026
- Raw outputs were minimally cleaned (removed conversational artifacts, preserved technical content)
- Each system was queried independently in fresh sessions
- Responses were collected within 24 hours to ensure temporal consistency

---

## Models & Collection Dates

### Wave 1 (2025)

| Model | Provider | Access Method | Date Collected | Output Size |
|-------|----------|---------------|----------------|-------------|
| DeepSeek v4 Pro | DeepSeek | API | July 25, 2025 | 17,239 chars |
| Grok 3 Mini | xAI | API | July 25, 2025 | 7,072 chars |
| Llama 3.3 70B Versatile | Groq | API | July 25, 2025 | 6,466 chars |
| Llama 3.2 1B | Ollama (local) | Local inference | July 25, 2025 | 4,556 chars |
| Claude (Brain System) | Anthropic | Public Medium article | August 16, 2025 | ~49,000 chars |

### Wave 2 (2026)

| Model | Provider | Access Method | Date Collected |
|-------|----------|---------------|----------------|
| GPT-4o | OpenAI | API | July 29, 2026 |
| Claude 3.5 Sonnet | Anthropic | API | July 29, 2026 |
| Gemini 1.5 Pro | Google | API | July 30, 2026 |
| Grok-2 | xAI | API | July 30, 2026 |
| DeepSeek-V3 | DeepSeek | API | July 30, 2026 |
| Llama 3.1 405B | Meta | API | July 30, 2026 |
| Mistral Large 2 | Mistral AI | API | July 31, 2026 |
| Qwen 2.5 | Alibaba | API | July 31, 2026 |
| Perplexity Pro Search | Perplexity | API | July 31, 2026 |
| Claude 3 Opus | Anthropic | API | July 31, 2026 |

---

## Notes on Claude Brain System

The Claude entry differs methodologically from all others — it is not a direct prompt response but a publicly disclosed cognitive architecture (the "Brain System") that Claude itself designed and built over 6 months. This architecture was documented by Claude in an August 2025 Medium article by Micheal Bee. It represents Claude's actual implemented AGI-adjacent architecture (38 MCP tools, 50+ state systems, 58 protocols) rather than a theoretical proposal.

**Why include it?** A production-implemented architecture provides ground truth that theoretical proposals lack. The Brain System validates several architectural patterns that appear across theoretical proposals (modular decomposition, tool-mediated action, protocol-based coordination) while challenging others (the necessity of explicit planners, formal verification at runtime).
