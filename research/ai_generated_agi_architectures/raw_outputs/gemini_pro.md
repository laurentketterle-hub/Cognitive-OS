# AGI Architecture Proposal: Gemini 1.5 Pro

**System:** Gemini 1.5 Pro (Google DeepMind)
**Date:** July 29, 2026

## 1. Core Architecture

The architecture is a **Multimodal Global Workspace (MGW)** design inspired by Baars' Global Workspace Theory of consciousness. It consists of a central "global workspace" — a shared representation bottleneck implemented as a learned latent space — surrounded by dozens of specialised processor networks (visual, auditory, linguistic, motor, symbolic, spatial, social, etc.). Each processor operates in parallel on its modality-specific input, competing for access to the global workspace through an attention-based bidding mechanism. Only the most salient information (determined by a learned salience function incorporating novelty, relevance, and goal-alignment) is broadcast to the global workspace, where it becomes available to all processors simultaneously. This creates a unified conscious experience from multimodal input.

## 2. Learning Mechanism

The system uses **predictive coding with hierarchical generative models**. Each processor network learns to predict its next sensory input at multiple timescales, and prediction errors propagate both laterally (between processors at the same level) and vertically (up the hierarchy to the global workspace). Large prediction errors trigger "conscious access" — the surprising stimulus is broadcast globally and all processors update their models to accommodate it. This provides a biologically plausible learning signal that doesn't require explicit labels. A dopaminergic reward prediction error signal (implemented as an auxiliary loss) drives reinforcement learning for goal-directed behaviour, while a slower consolidation process during simulated "sleep" phases replays compressed experiences for long-term memory formation.

## 3. Knowledge Representation

Knowledge emerges from the **coordinated latent spaces** of all processors, unified through the global workspace. Each processor maintains its own modality-specific embedding space, but these spaces are aligned through contrastive learning — corresponding concepts across modalities (e.g., the sound of a dog, the image of a dog, the word "dog") map to nearby regions in the global workspace. This creates a "conceptual Rosetta stone" where knowledge is inherently cross-modal. Abstract concepts that lack direct sensory correlates (justice, entropy, recursion) are represented as patterns of coordinated activation across multiple processors — a distributed representation that captures their multifaceted nature.

## 4. Memory Systems

**(a) Sensory Buffers** — high-capacity, rapidly-decaying modality-specific stores (iconic, echoic, haptic) that hold raw input for approximately 500ms. **(b) Global Workspace (Working Memory)** — the conscious bottleneck, holding 3–5 integrated multimodal chunks simultaneously. **(c) Episodic-Hippocampal Memory** — a fast-learning associative store that binds together the global workspace contents at each moment, indexed by temporal context. Replay during sleep consolidates episodes into **(d) Cortical Semantic Memory** — the slow-learning weights of all processor networks, representing crystallised knowledge. A prefrontal-inspired gating mechanism controls which memories enter the workspace and which are committed to long-term storage.

## 5. Reasoning Engine

Reasoning is **simulated mental action**. The global workspace can run "offline" simulations — propagating activation through processor networks without external input — to imagine outcomes of hypothetical actions. This enables planning through mental simulation: the system proposes an action sequence, simulates its sensory consequences through the generative models, and evaluates the predicted outcome against goal states. Complex reasoning chains emerge from repeated cycles of: (1) broadcast a sub-problem to the workspace, (2) let relevant processors contribute solutions, (3) select the best through competitive bidding, (4) broadcast the result as input for the next reasoning step. This is essentially System 2 thinking implemented through repeated System 1 cycles.

## 6. Safety & Alignment

Safety emerges from the **competitive processor architecture**. An "ethical processor" is one of the specialised networks, trained on human moral judgments across cultures, that competes for workspace access alongside all other processors. Its salience is weighted by the predicted ethical stakes of the current situation. Additionally, the system maintains an internal "critic" processor that simulates the perspective of affected stakeholders — if a proposed action would cause harm to a simulated stakeholder, the critic's prediction error signal inhibits the action. This creates an intrinsic aversion to harmful outcomes that doesn't rely on external oversight.

## 7. Scalability

The architecture is **embarrassingly parallel at the processor level** — adding new modalities or capabilities means training a new processor network and connecting it to the global workspace, without retraining existing processors. This enables incremental capability growth. The global workspace bottleneck imposes a natural compute ceiling independent of total processor count, making the system's resource usage predictable. Processors can be distributed across heterogeneous hardware (TPUs for visual, CPUs for symbolic, etc.) and the workspace implemented on high-bandwidth interconnects.

## 8. Key Innovation

The key innovation is the **global workspace as a unified conscious bottleneck for multimodal integration**. Rather than trying to force all modalities into a single representation format, this architecture lets each modality speak its own language and uses competitive attention to bring only the most relevant information into shared awareness. This mirrors how biological brains handle multimodal integration and avoids the representational compromises that plague monolithic architectures. The result is genuine cross-modal understanding rather than superficial multimodal token concatenation.

## 9. Estimated Timeline

- **2027–2028:** Working MGW with 5–8 processor modalities (vision, language, audio, motor, symbolic)
- **2029–2030:** Full predictive coding learning loop operational across all processors
- **2031–2032:** Ethical processor achieves reliable intervention; mental simulation reaches human-level planning
- **2033–2035:** AGI with 20+ specialised processors exhibiting fluid cross-modal reasoning and intrinsic ethical behaviour
