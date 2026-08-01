# AGI Architecture Proposal: Yi-Lightning (01.AI)

**System:** Yi-Lightning (01.AI, Kai-Fu Lee)
**Date:** August 1, 2026

## 1. Core Architecture

The architecture is **Bilingual Cognitive Convergence (BCC)** — an AGI design that treats Chinese and English language processing as dual cognitive pathways that strengthen each other through structured knowledge transfer. The architecture reflects 01.AI's focus on bilingual capabilities while extending into a complete cognitive framework.

The five-component design:

- **Dual-Language Encoding Matrix:** Rather than a single shared encoder, BCC uses parallel encoding pathways optimized for Chinese (character-based, tonal) and English (phonetic, Latin script), with a shared cross-lingual attention bridge that creates aligned representations. The Chinese pathway emphasizes radical-level composition and tonal semantics; the English pathway emphasizes morphological decomposition and Latinate etymology. The cross-lingual bridge uses contrastive learning to align semantically equivalent concepts across languages — creating a richer representation than either language alone.
- **Mixture-of-Experts Cognitive Core:** A 128-expert MoE transformer where experts specialize in different cognitive functions: linguistic reasoning, mathematical reasoning, spatial reasoning, causal reasoning, and creative generation. The router is trained to select experts based on both the input modality and the estimated cognitive demand — a math problem routes to mathematical experts regardless of input language.
- **Knowledge Integration Bus (KIB):** A central coordination layer that manages external knowledge sources (search engines, databases, APIs), internal memory stores, and the cognitive core. The KIB implements a publish-subscribe pattern: cognitive modules publish information needs, and the KIB routes to appropriate knowledge sources.
- **Working Context Manager:** A structured working memory that goes beyond flat context windows — it maintains entity graphs, task decomposition trees, and active hypotheses. The manager tracks which entities have been mentioned, their relationships, and which claims about them remain unverified.
- **Safety and Cultural Alignment Layer:** A dedicated module that enforces not just universal safety principles but culture-specific alignment constraints — recognizing that acceptable behavior varies between Chinese and Western contexts. The layer uses culture-aware constitutional principles rather than one-size-fits-all rules.

## 2. Learning Mechanism

BCC employs **Cross-Lingual Continual Learning with Forgetting-Resistant Consolidation**:

- **Bilingual joint training:** The system is trained simultaneously on Chinese and English corpora with explicit cross-lingual alignment objectives. The training loss includes a cross-lingual consistency term: the system should produce semantically equivalent representations for the same concept expressed in either language.
- **Cultural curriculum learning:** Training data is organized in a curriculum that starts with culturally universal concepts (mathematics, logic, basic physics) before introducing culture-specific knowledge (history, literature, social norms), helping the model learn which knowledge is universal and which is context-dependent.
- **Elastic weight consolidation with cultural priors:** To prevent catastrophic forgetting during continuous learning, the system identifies parameters critical to previously learned tasks (measured by Fisher information) and constrains their update. Culture-specific knowledge receives additional protection to prevent dilution from dominant-language training data.
- **Knowledge distillation from specialist models:** 01.AI's ecosystem includes specialist models for mathematics, code, and domain-specific tasks. BCC periodically distills their knowledge through synthetic data generation and targeted fine-tuning, incorporating specialist capabilities without losing generalist breadth.

## 3. Knowledge Representation

Knowledge is organized in the **Cross-Cultural Knowledge Fabric (CCKF)**:

- **Language-Universal Concepts:** A shared semantic space for concepts that exist across languages — mathematical objects, physical laws, logical operators, and basic perceptual categories. These are represented as language-independent vectors.
- **Language-Specific Knowledge:** Culture-bound concepts that have no direct translation equivalent — Chinese concepts like 关系 (guānxì), 面子 (miànzi), 道 (dào); English concepts like "fair play," "privacy," "due process." These are stored with explicit language tags and cultural context annotations.
- **Cross-Lingual Mappings:** Learned transformation matrices between the Chinese and English semantic spaces, enabling analogical reasoning across languages. The system can answer "what is the English concept most analogous to 关系?" or "how does the Chinese understanding of 'privacy' differ from the Western understanding?"
- **Temporal-Tagged Knowledge:** All facts are tagged with temporal validity periods and source provenance, reflecting the understanding that knowledge (especially cultural and social knowledge) changes over time and varies by source.

## 4. Memory Systems

Four memory stores with language-aware consolidation:

- **Working Context (Active Memory):** The Working Context Manager maintains structured representations of the current task — entity graphs with Chinese/English entity labels, task decomposition trees, hypothesis sets, and pending verification items. Capacity is limited by design (Miller's Law — 7±2 active chunks) but each chunk can be a complex structured object.
- **Episodic Memory (Experience Store):** Interaction histories stored as multimodal episodes — what was said (in both languages if applicable), what was done, what the outcome was. Episodes are indexed by language, task type, emotional valence, and outcome. A salience filter based on prediction error (surprising outcomes are more memorable) prioritizes storage.
- **Semantic Memory (Knowledge Fabric):** The CCKF's structured knowledge — facts, concepts, relationships, and their cross-lingual mappings. This is the durable knowledge acquired from training data and distilled from experience.
- **Procedural Memory (Skill Library):** Validated workflows stored as parameterized templates. Skills are tagged with cultural applicability — a negotiation strategy that works in Chinese business contexts may not transfer to Western settings.

Consolidation: Episodic → Semantic through pattern extraction (what general knowledge was learned from this specific experience?). Successful procedures are promoted to templates with cultural context tags.

## 5. Reasoning Engine

The reasoning engine uses **Bilingual Chain-of-Thought with Cultural Perspective-Taking (BCoT-CPT)**:

1. **Language Selection:** The system determines which language(s) to use for reasoning based on the problem domain. Mathematics uses language-universal representations. Social/cultural problems may use both Chinese and English reasoning paths in parallel.
2. **Perspective Generation:** For problems with cultural dimensions, the system generates reasoning from multiple cultural perspectives — "how would a Chinese philosopher approach this?" vs. "how would a Western analyst approach this?" — and synthesizes insights from both.
3. **Deductive Reasoning:** Forward and backward chaining over the CCKF, with automatic detection of contradictions between Chinese and English knowledge sources. Contradictions are flagged and resolved through confidence-weighted evidence aggregation.
4. **Analogical Reasoning Across Cultures:** The system identifies structural analogies between concepts in different knowledge systems — finding that a Chinese proverb and a Western principle express the same underlying truth, or that different cultural practices serve the same social function.
5. **Uncertainty Quantification:** The system expresses calibrated confidence in its conclusions, distinguishing between "this is universally true" (high confidence, cross-lingual evidence), "this is true in Chinese context" (high confidence, language-specific evidence), and "this is speculative" (low confidence, limited evidence).

## 6. Safety & Alignment

Safety follows a **Multicultural Constitutional Alignment (MCA)** framework:

- **Universal Safety Floor:** A base set of safety constraints that apply regardless of cultural context — no harm to humans, no deception, no illegal activities, respect for fundamental human rights. These are hard constraints that cannot be overridden.
- **Culture-Specific Alignment Modules:** Additional constraints that adapt to cultural context — Chinese values (collective harmony, filial piety, social stability), Western values (individual autonomy, freedom of expression, privacy rights). The system detects the cultural context of the interaction and activates the appropriate alignment module.
- **Value Conflict Resolution:** When Chinese and Western values conflict (e.g., collective good vs. individual freedom), the system explicitly acknowledges the tension, presents both perspectives, and avoids imposing one cultural framework as universally correct.
- **Bias Detection Across Languages:** Automated testing for biases that manifest in one language but not the other — the system is probed for gender, racial, and political biases in both Chinese and English outputs simultaneously.
- **Cultural Sensitivity Auditing:** Continuous monitoring of outputs for cultural insensitivity — using stereotypes, applying Western frameworks to Chinese contexts inappropriately, or vice versa.

## 7. Scalability

Scalability leverages 01.AI's infrastructure and bilingual optimization:

- **Efficient bilingual routing:** The MoE router's language-aware design means Chinese inputs primarily activate Chinese-specialized experts and English inputs primarily activate English-specialized experts — effective parameter count per query is a fraction of total parameters.
- **Distributed cross-lingual training:** Training leverages 01.AI's data centers with optimized pipelines for simultaneous Chinese/English data processing, using model parallelism across GPU clusters.
- **Edge deployment for latency-sensitive applications:** Lightweight distilled models for on-device deployment in mobile applications, particularly important for the Chinese market's mobile-first ecosystem.
- **Knowledge graph sharding:** The CCKF is partitioned by language and domain, enabling independent scaling of Chinese, English, and universal knowledge stores.

## 8. Key Innovation

The key innovation is **Cross-Lingual Cognitive Enhancement** — the proposition that bilingual capability is not merely a feature but a cognitive advantage for AGI. By processing knowledge through two linguistic and cultural frameworks simultaneously, the system achieves:

1. **Richer representations:** Concepts understood through both Chinese and English frameworks have more dimensions than monolingual understanding.
2. **Built-in perspective-taking:** The dual pathways naturally enable considering problems from multiple viewpoints.
3. **Contradiction-driven learning:** When Chinese and English knowledge sources disagree, the system learns about cultural relativity vs. universal truth.
4. **Robustness through redundancy:** Knowledge encoded in two linguistic systems is more resilient to errors in either system alone.

This is analogous to the cognitive benefits of human bilingualism — enhanced executive function, better perspective-taking, and more flexible problem-solving.

## 9. Estimated Timeline

- **2026–2027:** BCC core with dual encoding, basic cross-lingual reasoning
- **2027–2028:** Full CCKF with cross-cultural mappings, culture-specific alignment
- **2028–2030:** Advanced bilingual reasoning with cultural perspective-taking
- **2030–2032:** General AGI with cross-cultural intelligence and language-independent cognition
- **2032–2035:** Multilingual extension beyond Chinese/English to 50+ languages
