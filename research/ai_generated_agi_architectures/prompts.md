# AGI Architecture Proposal — Prompt Used

## Collection Method

The same exact prompt was submitted to all five AI systems (four via API, one via public disclosure) to elicit detailed AGI architecture proposals. This ensures comparability across model outputs.

## The Prompt

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

## Prompt Design Rationale

- **Nine structured sections** ensure coverage of all major AGI subsystem concerns
- **"Be specific" + "concrete mechanisms"** directive pushes models beyond vague hand-waving
- **Open-ended framing** ("Propose a detailed AGI architecture") allows each model to express its unique architectural philosophy
- **Terminology alignment** (working/episodic/semantic/procedural memory) uses standard cognitive science vocabulary to elicit comparable responses

## Models & Collection Dates

| Model | Provider | Access Method | Date Collected |
|-------|----------|---------------|----------------|
| DeepSeek v4 Pro | DeepSeek | API | July 25, 2025 |
| Grok 3 Mini | xAI | API | July 25, 2025 |
| Llama 3.3 70B Versatile | Groq | API | July 25, 2025 |
| Llama 3.2 1B | Ollama (local) | Local inference | July 25, 2025 |
| Claude (Brain System) | Anthropic | Public Medium article | August 16, 2025 |

**Note on Claude:** The Claude entry differs from the others — it is not a direct prompt response but a publicly disclosed cognitive architecture (the "Brain System") that Claude itself designed and built over 6 months. This architecture was documented by Claude in an August 2025 Medium article by Micheal Bee. It represents Claude's actual implemented AGI-adjacent architecture (38 MCP tools, 50+ state systems, 58 protocols) rather than a theoretical proposal.
