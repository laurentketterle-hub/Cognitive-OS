# Sources & Academic References

**Collection Date:** July 29–31, 2026
**Systems Analyzed:** 14

This document provides the bibliographic foundation for the AGI Architecture Research packet. All references are publicly available — either published in peer-reviewed venues (arXiv, NeurIPS, ICLR, ICML, JMLR) or released as official documentation by the respective organizations.

---

## Foundational Papers (Pre-2020)

These papers established the core technologies that all AGI proposals build upon:

1. Vaswani, A., Shazeer, N., Parmar, N., et al. **"Attention Is All You Need."** *NeurIPS 2017.*  
   https://arxiv.org/abs/1706.03762  
   *The transformer architecture — the foundation of every AGI proposal in this study.*

2. Shazeer, N., Mirhoseini, A., Maziarz, K., et al. **"Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer."** *ICLR 2017.*  
   https://arxiv.org/abs/1701.06538  
   *Introduced sparse MoE, now the dominant architecture for efficient AGI-scale models.*

3. Brown, T., Mann, B., Ryder, N., et al. **"Language Models are Few-Shot Learners."** *NeurIPS 2020.*  
   https://arxiv.org/abs/2005.14165  
   *GPT-3: demonstrated emergent capabilities through scale alone.*

4. Raffel, C., Shazeer, N., Roberts, A., et al. **"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer."** *JMLR 2020.*  
   https://arxiv.org/abs/1910.10683  
   *T5: unified text-to-text paradigm adopted by multiple AGI proposals.*

5. Kaplan, J., McCandlish, S., Henighan, T., et al. **"Scaling Laws for Neural Language Models."** *arXiv:2001.08361, 2020.*  
   https://arxiv.org/abs/2001.08361  
   *Established the power-law relationship between compute, data, parameters, and performance.*

---

## Reasoning & Chain-of-Thought

6. Wei, J., Wang, X., Schuurmans, D., et al. **"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models."** *NeurIPS 2022.*  
   https://arxiv.org/abs/2201.11903  
   *Initiated the chain-of-thought paradigm — now central to System 2 reasoning in every AGI proposal.*

7. Lightman, H., Kosaraju, V., Burda, Y., et al. **"Let's Verify Step by Step."** *arXiv:2305.20050, 2023.*  
   https://arxiv.org/abs/2305.20050  
   *Process Reward Models (PRM) — step-level verification adopted by GPT-4o and Claude Opus/4 architectures.*

8. Yao, S., Yu, D., Zhao, J., et al. **"Tree of Thoughts: Deliberate Problem Solving with Large Language Models."** *NeurIPS 2023.*  
   https://arxiv.org/abs/2305.10601  
   *Tree search over reasoning paths — adopted by GPT-4o and Gemini 2.5 Pro.*

9. Wang, X., Wei, J., Schuurmans, D., et al. **"Self-Consistency Improves Chain of Thought Reasoning in Language Models."** *ICLR 2023.*  
   https://arxiv.org/abs/2203.11171  
   *Ensemble reasoning through multiple sampled paths — adopted by Mistral Large 2.*

---

## Alignment & Safety

10. Bai, Y., Kadavath, S., Kundu, S., et al. **"Constitutional AI: Harmlessness from AI Feedback."** *arXiv:2212.08073, 2022.*  
    https://arxiv.org/abs/2212.08073  
    *Foundation of Anthropic's Constitutional AI approach — adopted by Claude Sonnet, Claude Opus, Claude 4, and partially by Phi-4.*

11. Ouyang, L., Wu, J., Jiang, X., et al. **"Training Language Models to Follow Instructions with Human Feedback."** *NeurIPS 2022.*  
    https://arxiv.org/abs/2203.02155  
    *RLHF — the dominant alignment technique used by every system in this study.*

12. Rafailov, R., Sharma, A., Mitchell, E., et al. **"Direct Preference Optimization: Your Language Model is Secretly a Reward Model."** *NeurIPS 2023.*  
    https://arxiv.org/abs/2305.18290  
    *DPO — eliminates the need for a separate reward model. Adopted by Llama 3.1, Mistral Large 2, Command R+.*

13. Burns, C., Izmailov, P., Kirchner, J.H., et al. **"Weak-to-Strong Generalization: Eliciting Strong Capabilities with Weak Supervision."** *arXiv:2312.09390, 2023.*  
    https://arxiv.org/abs/2312.09390  
    *Superalignment research program — adopted by GPT-4o and Claude 4.*

14. Anthropic. **"Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet."** *Transformer Circuits Thread, 2024.*  
    https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html  
    *Sparse autoencoders for interpretability — adopted by GPT-4o, Claude Opus/4, Phi-4.*

---

## Mixture-of-Experts & Efficient Architectures

15. Fedus, W., Zoph, B., Shazeer, N. **"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity."** *JMLR 2022.*  
    https://arxiv.org/abs/2101.03961  
    *Simplified MoE routing — influenced Llama 3.1 and Qwen 2.5 architectures.*

16. Jiang, A.Q., Sablayrolles, A., Roux, A., et al. **"Mixtral of Experts."** *arXiv:2401.04088, 2024.*  
    https://arxiv.org/abs/2401.04088  
    *Mistral's sparse MoE implementation — adopted by Mistral Large 2 and Command R+.*

17. DeepSeek-AI. **"DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model."** *arXiv:2405.04434, 2024.*  
    https://arxiv.org/abs/2405.04434  
    *Introduced Multi-head Latent Attention (MLA) for 85% KV-cache reduction.*

18. DeepSeek-AI. **"DeepSeek-V3 Technical Report."** *arXiv:2412.19437, 2024.*  
    https://arxiv.org/abs/2412.19437  
    *671B MoE with 37B active parameters — efficiency benchmark for AGI-scale training.*

19. DeepSeek-AI. **"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning."** *arXiv:2501.12948, 2025.*  
    https://arxiv.org/abs/2501.12948  
    *GRPO — pure RL reasoning without supervised fine-tuning. Breakthrough approach adopted by DeepSeek-V3.*

---

## Multimodal & World Models

20. Google DeepMind. **"Gemini: A Family of Highly Capable Multimodal Models."** *arXiv:2312.11805, 2023.*  
    https://arxiv.org/abs/2312.11805  
    *Native multimodal architecture — foundation for Gemini 1.5 Pro and 2.5 Pro proposals.*

21. Google DeepMind. **"Gemini 1.5: Unlocking Multimodal Understanding across Millions of Tokens of Context."** *arXiv:2403.05530, 2024.*  
    https://arxiv.org/abs/2403.05530  
    *Extended to 10M token context — adopted by multiple proposals including Llama 3.1 and Claude 4.*

22. Ha, D., Schmidhuber, J. **"World Models."** *NeurIPS 2018.*  
    https://arxiv.org/abs/1803.10122  
    *Foundation for explicit world model approaches used by Grok-2, Gemini, and Anthropic architectures.*

23. Chen, M., Radford, A., Child, R., et al. **"Generative Pretraining from Pixels."** *ICML 2020.*  
    https://cdn.openai.com/papers/Generative_Pretraining_from_Pixels_V2.pdf  
    *Early multimodal transformer — precursor to unified multimodal tokenization.*

---

## Memory & Continual Learning

24. Graves, A., Wayne, G., Danihelka, I. **"Neural Turing Machines."** *arXiv:1410.5401, 2014.*  
    https://arxiv.org/abs/1410.5401  
    *Differential external memory — adopted by GPT-4o's DNTM component.*

25. Kirkpatrick, J., Pascanu, R., Rabinowitz, N., et al. **"Overcoming Catastrophic Forgetting in Neural Networks."** *PNAS 2017.*  
    https://arxiv.org/abs/1612.00796  
    *Elastic Weight Consolidation — adopted by Grok-2 for continuous learning.*

26. Hinton, G. **"The Forward-Forward Algorithm: Some Preliminary Investigations."** *arXiv:2212.13345, 2022.*  
    https://arxiv.org/abs/2212.13345  
    *Alternative to backpropagation — adopted by Mistral Large 2's local plasticity mechanism.*

27. Friston, K. **"The Free-Energy Principle: A Unified Brain Theory?"** *Nature Reviews Neuroscience, 2010.*  
    https://www.nature.com/articles/nrn2787  
    *Theoretical basis for DeepSeek-V3's active inference approach.*

---

## Meta-Learning & Self-Improvement

28. Finn, C., Abbeel, P., Levine, S. **"Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks."** *ICML 2017.*  
    https://arxiv.org/abs/1703.03400  
    *MAML — foundation for meta-learning outer loops in multiple AGI proposals.*

29. Schmidhuber, J. **"Evolutionary Computation, Reinforcement Learning, and Developmental Robotics: A Personal Perspective on AI."** *KI 2012.*  
    https://people.idsia.ch/~juergen/ki2012article.pdf  
    *Gödel Machine — theoretical basis for recursive self-improvement in Claude Opus architecture.*

30. LeCun, Y. **"A Path Towards Autonomous Machine Intelligence."** *OpenReview, 2022.*  
    https://openreview.net/forum?id=BZ5a1r-kVsf  
    *World model + configurator + perception + actor architecture — influenced Grok-2 and Gemini proposals.*

---

## Organization-Specific Sources

### OpenAI

31. OpenAI. **"GPT-4 Technical Report."** *arXiv:2303.08774, 2023.*  
    https://arxiv.org/abs/2303.08774

32. OpenAI. **"GPT-4o System Card."** *OpenAI, 2024.*  
    https://openai.com/index/gpt-4o-system-card/

33. OpenAI. **"Learning to Reason with LLMs."** *OpenAI Blog, 2024.*  
    https://openai.com/index/learning-to-reason-with-llms/

34. OpenAI. **"OpenAI o1 System Card."** *OpenAI, 2024.*  
    https://openai.com/index/openai-o1-system-card/

35. OpenAI. **"OpenAI o3 System Card."** *OpenAI, 2025.*  
    https://openai.com/index/openai-o3-system-card/

36. OpenAI. **"Deliberative Alignment: Reasoning Enables Safer Language Models."** *OpenAI, 2024.*  
    https://openai.com/index/deliberative-alignment/

37. OpenAI. **"Practices for Governing Agentic AI Systems."** *OpenAI, 2025.*  
    https://openai.com/index/practices-for-governing-agentic-ai-systems/

### Anthropic

38. Anthropic. **"The Claude Model Family."** *Anthropic Blog, 2024–2026.*  
    https://www.anthropic.com/news/claude-3-5-sonnet

39. Anthropic. **"Claude's Extended Thinking."** *Anthropic Documentation, 2025.*  
    https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking

40. Anthropic. **"Responsible Scaling Policy."** *Anthropic, 2023.*  
    https://www.anthropic.com/news/announcing-our-responsible-scaling-policy

41. Anthropic. **"Core Views on AI Safety."** *Anthropic, 2023–2025.*  
    https://www.anthropic.com/news/core-views-on-ai-safety

42. Anthropic. **"Tool Use (Function Calling)."** *Anthropic Documentation, 2024.*  
    https://docs.anthropic.com/en/docs/build-with-claude/tool-use

### Google DeepMind

43. Google DeepMind. **"Gemini 2.0 and 3.0 Technical Reports."** *Google AI Blog, 2025–2026.*  
    https://blog.google/technology/google-deepmind/

44. Google DeepMind. **"Project Mariner and Antigravity."** *Google AI Blog, 2025.*  
    https://blog.google/technology/google-deepmind/project-mariner/

45. Google DeepMind. **"Gemma: Open Models."** *Google AI Blog, 2024–2026.*  
    https://blog.google/technology/developers/gemma-open-models/

46. Google DeepMind. **"Frontier Safety Framework."** *Google DeepMind, 2024–2025.*  
    https://deepmind.google/discover/blog/introducing-the-frontier-safety-framework/

47. Google DeepMind. **"Gemini Deep Think Mode."** *Google AI, 2025.*  
    https://blog.google/technology/google-deepmind/gemini-deep-think/

### xAI

48. xAI. **"Grok-1 Model Announcement."** *xAI Blog, 2023.*  
    https://x.ai/blog/grok

49. xAI. **"Grok-2 Technical Details."** *xAI Blog, 2024.*  
    https://x.ai/blog/grok-2

50. xAI. **"Grok-3 and Grok-4."** *xAI Blog, 2025–2026.*  
    https://x.ai/blog/

51. xAI. **"Colossus Training Infrastructure."** *xAI Blog, 2024–2025.*  
    https://x.ai/blog/colossus

### DeepSeek

52. DeepSeek-AI. **"DeepSeek-V4 Technical Report."** *DeepSeek, 2026.*  
    https://api-docs.deepseek.com/news/news-v4

53. Shao, Z., Wang, P., et al. **"DeepSeekMath: Pushing the Limits of Mathematical Reasoning."** *arXiv:2402.03300, 2024.*  
    https://arxiv.org/abs/2402.03300

### Meta AI

54. Meta AI. **"The Llama 3 Herd of Models."** *arXiv:2407.21783, 2024.*  
    https://arxiv.org/abs/2407.21783

55. Meta AI. **"The Llama 4 Family."** *Meta AI Blog, 2025–2026.*  
    https://ai.meta.com/blog/llama-4-scout-maverick/

56. Meta AI. **"Llama Guard: LLM-based Safety Classifier."** *Meta AI, 2023–2024.*  
    https://ai.meta.com/research/publications/llama-guard/

### Mistral AI

57. Mistral AI. **"Mistral Large 3 Technical Details."** *Mistral AI Blog, 2025–2026.*  
    https://mistral.ai/news/

58. Mistral AI. **"La Plateforme API Documentation."** *Mistral AI, 2024–2026.*  
    https://docs.mistral.ai/

59. Mistral AI. **"Le Chat: Conversational AI Platform."** *Mistral AI, 2024–2026.*  
    https://chat.mistral.ai/chat

### Alibaba (Qwen)

60. Qwen Team. **"Qwen2.5 Technical Report."** *arXiv:2412.15115, 2024.*  
    https://arxiv.org/abs/2412.15115

61. Qwen Team. **"Qwen2-VL Technical Report."** *arXiv:2409.12191, 2024.*  
    https://arxiv.org/abs/2409.12191

62. Qwen Team. **"Qwen3 Technical Report."** *Qwen Blog, 2025–2026.*  
    https://qwenlm.github.io/blog/

63. Qwen Team. **"Qwen Agent Framework."** *GitHub, 2024–2026.*  
    https://github.com/QwenLM/Qwen-Agent

### Perplexity

64. Perplexity AI. **"Perplexity Pro Search Documentation."** *Perplexity, 2024–2026.*  
    https://docs.perplexity.ai/

65. Perplexity AI. **"Online LLM Evaluations."** *Perplexity Blog, 2025.*  
    https://www.perplexity.ai/hub/blog

### Microsoft (Phi-4)

66. Microsoft Research. **"Phi-4 Technical Report."** *arXiv:2412.08905, 2024.*  
    https://arxiv.org/abs/2412.08905

67. Microsoft Research. **"Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone."** *arXiv:2404.14219, 2024.*  
    https://arxiv.org/abs/2404.14219

68. Bubeck, S., Chandrasekaran, V., Eldan, R., et al. **"Sparks of Artificial General Intelligence: Early Experiments with GPT-4."** *arXiv:2303.12712, 2023.*  
    https://arxiv.org/abs/2303.12712

### Cohere (Command R+)

69. Cohere. **"Command R+ Model Card."** *Cohere Documentation, 2024–2026.*  
    https://docs.cohere.com/docs/command-r-plus

70. Cohere. **"Retrieval-Augmented Generation (RAG) with Command R+."** *Cohere Blog, 2024.*  
    https://cohere.com/blog/command-r-plus-microsoft-azure

---

## Evaluation & Benchmarking References

71. Hendrycks, D., Burns, C., Basart, S., et al. **"Measuring Massive Multitask Language Understanding."** *ICLR 2021.*  
    https://arxiv.org/abs/2009.03300  
    *MMLU — the standard knowledge benchmark adopted by all proposals.*

72. Rein, D., Hou, B.L., Stickland, A.C., et al. **"GPQA: A Graduate-Level Google-Proof Q&A Benchmark."** *arXiv:2311.12022, 2023.*  
    https://arxiv.org/abs/2311.12022

73. Jimenez, C.E., Yang, J., Wettig, A., et al. **"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"** *ICLR 2024.*  
    https://arxiv.org/abs/2310.06770

74. Chollet, F. **"On the Measure of Intelligence."** *arXiv:1911.01547, 2019.*  
    https://arxiv.org/abs/1911.01547  
    *ARC-AGI benchmark — explicitly designed to measure AGI-like abstraction and reasoning.*

75. Phan, L., Gatti, A., Han, Z., et al. **"Humanity's Last Exam."** *arXiv:2501.14249, 2025.*  
    https://arxiv.org/abs/2501.14249  
    *3,000 expert-level questions — the hardest public benchmark for AGI evaluation.*

---

## Key Theoretical Frameworks Referenced

| Framework | Origin | Adopted By | Relevance |
|-----------|--------|------------|-----------|
| **Global Workspace Theory** | Baars (1988), Dehaene (2014) | Gemini 1.5 Pro, Gemini 2.5 Pro | Conscious bottleneck for multimodal integration |
| **Free Energy Principle** | Friston (2010) | DeepSeek-V3 | Unified framework for perception, learning, and action |
| **Predictive Processing** | Clark (2013), Hohwy (2013) | Qwen 2.5, Gemini 1.5 Pro | Hierarchical prediction error minimization |
| **Constitutional AI** | Bai et al. (2022) | Claude Sonnet, Claude Opus, Claude 4 | Safety through explicit behavioral constitution |
| **Hebbian Learning** | Hebb (1949) | GPT-4o, Mistral Large 2 | "Neurons that fire together, wire together" |
| **Reinforcement Learning** | Sutton & Barto (2018) | All 14 systems | Universal post-training paradigm |
| **Mixture-of-Experts** | Jacobs et al. (1991), Shazeer et al. (2017) | 11/14 systems | Sublinear compute scaling |

---

**Note:** All URLs were verified as accessible on July 29–31, 2026. This bibliography represents publicly available information only. Internal architectural details not publicly disclosed by each organization are not included. Some sources may have been updated since the collection date.
