# Prompts Used for AGI Architecture Collection

## Standardized Base Prompt

The following prompt was used across all AI systems. Minor adaptations were made only when required by the system's interface (e.g., character limits, formatting constraints). All adaptations are documented below.

### Base Prompt

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

## System-Specific Adaptations

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

## Collection Method

- All prompts were submitted between July 29-31, 2026
- Raw outputs were minimally cleaned (removed conversational artifacts, preserved technical content)
- Each system was queried independently in fresh sessions
- Responses were collected within 24 hours to ensure temporal consistency
