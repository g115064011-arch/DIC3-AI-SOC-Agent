# Related Work Refactor — Phase 7 Changelog

> **版本**：Phase 7，2026-11-11  
> **文件目的**：記錄 §3 Related Work 的修改前版本、問題診斷、修改後版本與修改理由。  
> **語言政策**：主要段落改為學術英文；每節末附「繁體中文重點說明」；Article Summary Table 新增 Verified 欄位。

---

## 修改前問題診斷

| 問題 | 說明 |
|---|---|
| 語言政策未落實 | §3 全節主要段落為繁體中文，規範要求學術英文 |
| Article Summary Table 缺少 Verified 欄位 | 規範明確要求每篇論文標註 Verified（URL 是否可存取） |
| Table 欄位語言混用 | 表格內容為繁中，需配合英文主文調整 |
| Research Gap 未以英文學術段落呈現 | 規範要求主要段落使用學術英文 |

---

## URL 驗證結果（本 Phase 確認）

| Ref. | URL / DOI | HTTP 狀態 | 備註 |
|---|---|---|---|
| [1] | https://arxiv.org/abs/2407.09017 | 200 | ✓ |
| [2] | https://arxiv.org/abs/2510.00311 | 200 | ✓ |
| [3] | https://arxiv.org/abs/2610.10608 | 200 | ✓ |
| [4] | https://arxiv.org/abs/2507.14201 | 200 | ✓ |
| [5] | https://arxiv.org/abs/2509.20166 | 200 | ✓ |
| [6] | https://arxiv.org/abs/2505.11988 | 200 | ✓ |
| [7] | https://arxiv.org/abs/2607.16963 | 200 | ✓ |
| [8] | https://arxiv.org/abs/2605.08316 | 200 | ✓ |
| [9] | https://arxiv.org/abs/2509.10858 | 200 | ✓ |
| [10] | doi:10.1016/j.jisa.2024.103956 | 200 | ✓ ScienceDirect |
| [11] | doi:10.1145/3733826.3762680 | 403/redirect | ✓ DOI resolves to ACM DL (paywall) |
| [12] | doi:10.1108/ICS-08-2025-0318 | 403/redirect | ✓ DOI resolves to Emerald (paywall) |
| [13] | doi:10.6028/NIST.SP.800-61r3 | 200 | ✓ NIST |
| [24] | https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi | 200 | ✓ |
| [25] | doi:10.14722/usec.2025.23034 | 200 | ✓ |
| [26] | https://arxiv.org/abs/2609.06250 | 200 | ✓ |

所有 16 篇均已驗證可存取（paywall 論文 DOI 正確跳轉，列為 Paywall-OK）。

---

## 修改後版本

> 以下為 §3 Related Work 的完整修改後內容，已同步寫入 `docs/proposal.md`。

---

### 3.1 AI Technology

#### (1) ML-Based Alert Triage and Incident Prioritization

Microsoft's Copilot Guided Response (CGR) [1] introduced a production-deployed ML architecture that simultaneously addresses three SOC tasks—investigation (via similar historical incident retrieval), triage (TP/BP/FP classification), and remediation suggestion. Crucially, the work released the GUIDE dataset: approximately 13 million evidence rows, 1.6 million alerts, 1 million incidents across 6,100 customer organizations, with labels derived from real analyst decisions—the largest publicly available real-world enterprise incident dataset to date. CGR reports cross-region macro-F1 of 0.87 for TP/BP/FP classification, with precision 0.87 and recall 0.86. A companion work, Adaptive Incident Prioritization (AIP) [7], addresses the queue ordering problem by adapting BM25 information retrieval concepts into a query-free, cross-tenant ranking algorithm, achieving 92.8% Precision@10 in expert evaluation and extending GUIDE with 9,980 prioritization-labeled incidents. Together, these works establish that ML triage is industrially deployable at scale—yet the advantage derives substantially from vendor-internal cross-customer data and product integration context that is not publicly reproducible.

#### (2) LLM Agents for Alert Investigation

CORTEX [2] proposes a multi-agent LLM architecture—decomposing alert investigation into behavioral analysis, evidence collection, and reasoning sub-agents—and demonstrates improvements over single-agent baselines: actionable alert F1 improves from 0.66 to 0.78, and false positive rate decreases from 24.9% to 14.2%. However, Tsegai et al. [3] conduct a more systematic empirical study, evaluating five distinct tool-using LLM reasoning strategies and finding that **all existing strategies miss at least 40.4% of attack-related alerts**. The dominant failure mode is premature case closure when queries return empty results—an absence of logged evidence is incorrectly interpreted as an absence of malicious activity. In-context self-review is found to have a net-negative effect. Their proposed AIDA system, introducing independent adversarial challenger and judge agents, reduces the false negative rate to 3.1% (F1 0.958) at the cost of a 18.4% human escalation rate and approximately \$0.109 per alert (GPT-4.1). This work establishes that **the termination policy—when to stop investigating and when to escalate—is the most consequential design decision in LLM-based alert triage**.

#### (3) Security LLM Benchmarks

ExCyTIn-Bench [4] evaluates LLM agents on threat investigation within a controlled Azure tenant (57 log tables, 8 authentic attack chains, 7,542 auto-generated questions). The best-performing model achieves an investigation reward of only 0.606; removing alert tables from the queryable database causes performance to drop to 0.248, confirming agents' over-reliance on alert-level context. CyberSOCEval [5], part of the CyberSecEval 4 suite, benchmarks malware analysis (609 questions) and threat intelligence reasoning (588 questions across 45 real reports), finding that model accuracy ranges from 15–28% and 43–53% respectively—far below saturation—and that test-time compute scaling yields substantially smaller improvements in security analysis than in code generation or mathematics. Both benchmarks establish a consistent finding: **general-purpose LLMs remain significantly below expert-level performance on security reasoning tasks**.

#### (4) Domain Knowledge Retrieval via RAG

TechniqueRAG [6] addresses ATT&CK technique annotation in cyber threat intelligence (CTI) text using a retriever-augmented pipeline with an instruction-tuned LLM and zero-shot reranking. On the Procedures benchmark, TechniqueRAG achieves F1 of 91.09% with minimal labeled data, establishing state-of-the-art performance. However, two important limitations constrain applicability to our problem: (a) the method is designed for CTI text reports, not for structured SOC alert telemetry and security logs; and (b) on the multi-label Expert benchmark (covering 290 techniques), the best system achieves only ~50% F1, with models rarely outputting more than two techniques—indicating low recall in multi-tactic attack scenarios.

#### (5) Field Deployment of LLM Agents in SOC

Banstola et al. [26] conducted a 14-month participatory field study deploying an LLM ReAct agent collaboratively designed with analysts at a university SOC. During the final four active months, analysts incorporated the agent's output into case closure reports in over 90% of cases. For the three most frequent users, the estimated time savings were 30–50% relative to self-reported manual processing times. The study identifies **output verifiability—not accuracy—as the primary determinant of analyst adoption**: analysts were more willing to adopt outputs they could independently check, and self-customization of agent behavior further increased trust.

#### 繁體中文重點說明

1. **ML 分級**：CGR [1] macro-F1 0.87，但優勢依賴廠商跨客戶資料；AIP [7] 解決佇列排序問題，Precision@10 達 92.8%。
2. **LLM Agent**：CORTEX [2] F1 從 0.66 → 0.78；但 Tsegai 等人 [3] 發現所有現有方法漏判至少 40.4%，「何時停止調查」是最關鍵設計；AIDA 透過獨立質疑與裁判機制將漏判率降至 3.1%，代價是 18.4% 升級率。
3. **Benchmark**：ExCyTIn-Bench [4] 最佳 reward 0.606，移除告警表降至 0.248；CyberSOCEval [5] 顯示推理模型在資安的 scaling 效益遠不如程式或數學。
4. **RAG**：TechniqueRAG [6] 在 CTI 文字上 F1 91.09%，但只處理文字報告，多標籤情境召回率低。
5. **實地部署**：Banstola 等人 [26] 實地研究發現，採用 AI 輸出的關鍵是**可驗證性**，而非準確率。

---

### 3.2 Domain Know-How

#### (1) Alert Fatigue as a Structural SOC Problem

Ndichu et al. [8] conduct a systematic review of AI-based alert screening research spanning 2015–2026, analyzing 87 core studies from an initial pool of 119 references. They organize the alert management literature into four stages—filtering, triage, correlation, and generative augmentation—and identify four persistent research gaps: (i) absence of operational validation in real production SOC environments; (ii) insufficient adversarial robustness; (iii) limited cross-environment generalization; and (iv) lack of methodological consistency in evaluation. They propose a "Cognitive SOC" research agenda to address these deficiencies. Habibzadeh et al. [9] complement this with a comprehensive survey of LLM applications in SOC workflows, characterizing the structural challenges as: excessive alert volume, analyst staffing shortages, high domain expertise requirements, response latency, and difficulty operationalizing threat intelligence. They organize LLM SOC applications by workflow stage—log analysis, alert triage, and threat intelligence—and claim this as the first comprehensive survey specifically addressing LLM integration in SOC contexts.

#### (2) Kill Chain Stage as the Primary Severity Determinant

Sadlek et al. [10] propose mapping detected alert sequences to ATT&CK-derived kill chain attack graphs using MulVAL, assessing severity by the most advanced attack chain stage reached and the importance of compromised assets. On a 10-host testbed running 5 MITRE CALDERA attack scenarios (31 ATT&CK techniques, 475 alert sequences of which 10 are malicious), alert sequence classification achieves AUC 0.95, with a chosen threshold correctly identifying 80% of malicious sequences. ROSCA [11] independently pursues a similar insight, dynamically constructing alert graphs by shared attributes and scoring cases by ATT&CK tactic progression. Evaluated on real hospital SOC data (382 EDR alerts over 2 months), ROSCA outperforms the MATE framework in matching analyst-assigned severity labels. Both works converge on a central domain principle: **the security significance of any individual alert is inseparable from its position and context within the broader attack progression**.

#### (3) Human-Machine Interaction Risk: Automation Complacency

Tilbury and Flowerday [12] investigate whether SOC automation induces analyst complacency through a mixed-methods study combining four SOC site observations, a 696-analyst survey, and 29 in-depth analyst interviews. Using PLS structural equation modeling, they demonstrate that increased automation causes analysts to reduce monitoring vigilance and increase reliance on automated outputs—the *vigilance paradox*. Importantly, they find that systematic verification procedures can mitigate this effect. This finding has direct design implications: an AI SOC agent that presents opaque verdicts without traceable evidence chains not only fails to support analyst judgment but actively degrades it. The companion paper [18] provides further quantitative analysis of human-automation preference formation in SOC contexts.

#### (4) Incident Response Standards

NIST SP 800-61 Rev. 3 [13] (April 2025) replaces the 2012 Rev. 2 version, reorganizing incident response guidance around the six functions of the NIST Cybersecurity Framework (CSF) 2.0: Govern, Identify, Protect, Detect, Respond, and Recover. A key normative change is the explicit recommendation that incidents should be prioritized through structured triage and risk-based analysis rather than first-in-first-out queue management (outcome RS.MA-02). This standard provides the procedural framework for the proposed system's escalation and remediation suggestion components.

#### (5) Analyst Triage Behavior: Empirical Evidence

Alahmadi et al. [24] conduct qualitative research with 21 practitioners across seven SOCs (supplemented by a 20-respondent questionnaire), revealing that the majority of dismissed alerts are **benign positives rather than genuine false positives**: the detection fired correctly, but the flagged behavior is an authorized activity within that organization. This distinction—between FP (detector error) and BP (correct detection, benign activity)—is analytically critical but absent from most ML triage literature. Analysts also identify alert opacity—lack of explanations and contextual information—as a primary impediment to efficient triage. Kersten et al. [25] conduct two think-aloud protocol experiments observing five Tier-1 analysts performing 400 alert investigations at a commercial SOC, developing and evaluating an Alert Investigation Support System (AISS). Key findings include: investigation workflows vary substantially across analysts and alert types; and alerts that ultimately require escalation are associated with significantly greater variety in evidence types collected. This directly motivates adaptive evidence collection depth in the proposed system's LLM planning module.

#### 繁體中文重點說明

1. **告警疲勞**：Ndichu 等人 [8] 回顧 87 篇核心研究，指出四大缺口（營運驗證、對抗穩健性、跨環境泛化、評估一致性），提出 Cognitive SOC 研究議程；Habibzadeh 等人 [9] 整理 LLM 在 SOC 工作流程中的應用分類。
2. **攻擊鏈階段**：Sadlek 等人 [10] 以 Kill Chain 攻擊圖判定嚴重度，AUC 0.95；ROSCA [11] 以 ATT&CK 戰術推進評分，在真實醫院 SOC 資料上優於 MATE。**核心共識**：單一告警的意義取決於在攻擊鏈中的位置。
3. **自動化自滿**：Tilbury 與 Flowerday [12] 以 696 份問卷與 29 場訪談確認自動化讓分析師降低監控；系統性驗證程序可減緩此現象，強調 Agent 必須輸出可驗證的證據鏈。
4. **NIST SP 800-61 Rev. 3**：2025 年 4 月更新，明確建議事件應依風險優先排序（RS.MA-02），不應先到先處理，是本專題處置建議的流程依據。
5. **分析師行為**：Alahmadi 等人 [24] 發現大多數「誤報」實為良性觸發（BP），本專題三分類正確反映此實務；Kersten 等人 [25] 發現需升級的告警會蒐集更多種類的資訊，支持本專題依情況調整證據蒐集深度的設計。

---

### 3.3 Article Summary Table

| Ref. | Year | Problem | AI Method | Domain Knowledge | Dataset | Key Findings | Limitation | Verified |
|---|---|---|---|---|---|---|---|---|
| [1] | 2024 | SOC incident investigation, triage, and remediation | ML (CGR), integrated in Defender XDR | SOC triage (TP/BP/FP), remediation actions | GUIDE: 13M evidence rows, 1.6M alerts, 1M incidents, 6.1k orgs, 2 weeks (public) | Deployed to thousands of customers; macro-F1 0.87, precision 0.87, recall 0.86; 41% incident coverage at 90% precision threshold | Authors: no comparison to other products; limited to known detectors; cannot handle zero-day or unmonitored attack vectors | Y |
| [2] | 2025 | High alert volume; single-LLM instability and opacity under noisy enterprise data | Multi-agent LLM (behavior analysis, evidence collection, reasoning) | SOC investigation workflow, analyst step-by-step actions | Self-constructed SOC investigation traces (10+ real enterprise scenarios, thousands of records, public) | Actionable alert F1: 0.66→0.78; FP rate: 24.9%→14.2% vs. single tool-using agent | Authors: limited scenario count; sensitive to distribution shift, prompt injection, incomplete tool returns; cost: ~5.7× tokens, 152s/alert | Y |
| [3] | 2026 | How LLM reasoning strategies affect evidence collection and case closure timing | 5 tool-using LLM strategies; proposes AIDA (multi-agent challenger + judge) | Alert triage, SIEM investigation | ALERT-BENCH: AIT-LDSv2 telemetry replayed in SIEM; 1,247 alerts from 4-day multi-stage attack scenarios | All existing strategies miss ≥40.4% attacks; AIDA F1 0.958, FNR 3.1%, escalation 18.4%; ~34k tokens, $0.109/alert (GPT-4.1) | Authors: data only from AIT series; lacks organizational context; analyst adoption not evaluated; preprint | Y |
| [4] | 2026 | Lack of benchmark for evaluating LLM agent threat investigation | LLM Agent + SQL tools; questions auto-generated from investigation graphs | Security logs, investigation graphs, detection logic | Controlled Azure tenant: 57 log tables, 8 real attack chains, 7,542 questions | Best model reward 0.606; drops to 0.248 with full DB; alert table removal causes sharp degradation | Derived from text: single tenant; benign noise is simulated; questions LLM-generated from alert graphs, biased toward alert table | Y |
| [5] | 2025 | Lack of benchmarks for malware analysis and threat intelligence reasoning | LLM evaluation (including reasoning models) | Malware analysis, threat intelligence | CyberSOCEval (part of CyberSecEval 4): malware 609 Qs, threat intelligence 588 Qs (45 reports) | Model accuracy 15–28% (malware), 43–53% (TI); larger/newer models better; test-time scaling less effective than in code/math | Authors: malware analysis Windows-only; multiple-choice format; IR and triage listed as future work | Y |
| [6] | 2025 | ATT&CK technique annotation from CTI text requires large labeled datasets | RAG: retriever + instruction-tuned LLM + zero-shot reranker | MITRE ATT&CK techniques | Tram, Procedures, Expert benchmarks (198, 488, 290 techniques respectively) | SOTA with minimal labels: Procedures F1 91.09%; Expert multi-label ~50% | Authors: techniques lack procedure examples; models rarely output >2 techniques; multi-label recall low; ground truth inconsistency; CTI text only, not SOC alerts | Y |
| [7] | 2026 | Incident queues ordered by time or coarse severity; true priority unclear | Modified BM25 cross-tenant ranking + component-level explanations | SOC queue management, domain priors | 1,000-org expert evaluation; 473k org-day queues (production); GUIDE + 9,980 priority labels (499 queues) | Precision@10 92.8%; 17.5% more alert details viewed vs. severity-ordered | Authors: only ranks existing queues; cannot classify TP/FP or surface undetected attacks; ranking depends on ATT&CK mapping, TI, and asset label completeness | Y |
| [8] | 2026 | Lack of systematic review of AI-based alert screening | Survey: filtering, triage, correlation, generative augmentation | Alert fatigue, SOC workflow | 119 references, 87 core studies (2015–2026) | Four-stage classification; identifies 4 research gaps; proposes Cognitive SOC agenda | Authors: excludes non-English literature; most studies use benchmark datasets; preprint submitted to ACM Computing Surveys | Y |
| [9] | 2025 | LLM integration into SOC workflows lacks systematic treatment | Survey: LLM for log analysis, alert triage, threat intelligence | SOC staffing, alert volume, response time challenges | Kitchenham systematic review methodology | Claims first comprehensive LLM-in-SOC survey; organizes by SOC workflow stage | No empirical results (survey); preprint | Y |
| [10] | 2025 | Multi-step attack alerts need severity-based triage | Attack graph matching (MulVAL), non-LLM | Kill chain, ATT&CK, asset criticality | 10-host testbed; 5 MITRE CALDERA scenarios (31 ATT&CK techniques); 475 alert sequences, 10 malicious | Alert sequence classification AUC 0.95; threshold correctly identifies 80% malicious sequences | Authors: small testbed scale, no real user traffic; attack graph scalability issues; MulVAL rules require manual authoring | Y |
| [11] | 2025 | High alert volume causes analyst fatigue; opaque commercial tools impede customization | Non-ML: dynamic alert graph by shared attributes, aggregated into cases, scored by ATT&CK tactic progression | ATT&CK tactic progression (kill chain) | French hospital SOC: EDR alerts (2 months, 382 records) + internal IDS (15 days, 37 records); analyst labels; penetration test data | Scores outperform MATE in matching analyst labels; 382-alert correlation in 0.12s, 1.45MB | Single hospital; small alert count; no Precision/Recall reported; only alerts with deterministic tactic inference included | Paywall-OK |
| [12] | 2026 | Does SOC automation induce analyst complacency and bias? | Non-AI: PLS structural equation modeling | Automation complacency, human-machine trust | 4 SOC observations, 696-analyst survey, 29 interviews | Automation reduces monitoring vigilance; systematic verification procedures mitigate complacency | US analysts only; self-reported data | Paywall-OK |
| [13] | 2025 | Incident response guidance needs integration with CSF 2.0 | — | Incident response lifecycle (CSF 2.0 six functions) | — | Replaces 2012 Rev. 2; RS.MA-02 recommends risk-based triage, not FIFO; Govern function added | High-level guidance; no alert-level decision rules or quantitative thresholds | Y |
| [24] | 2022 | High security tool FP rates, but "false positive" is poorly defined | Non-AI: questionnaire (n=20) + semi-structured interviews (n=21) | Analyst alert verification; FP vs. benign trigger distinction | Practitioners from 7 SOCs, predominantly UK-based | Most "false positives" are benign triggers; alert opacity (no explanation/context) is a primary problem; proposes REACT model | Authors: small sample, 7 SOCs mostly UK/Europe; non-random recruitment; self-reported | Y |
| [25] | 2025 | Little is known about how Tier-1 analysts actually investigate alerts | Non-AI: think-aloud experiments; develops AISS | Tier-1 investigation process, evidence collection patterns | Commercial SOC: 5 analysts, 400 investigations; 4 analysts using AISS for 36 investigations | Workflows vary by analyst and alert type; escalated alerts involve greater evidence type variety; AISS reduces actions needed | Authors: single SOC; subjects mostly junior/intern analysts; same attack investigated repeatedly | Y |
| [26] | 2026 | Will LLM agents be adopted in real SOC practice? | LLM ReAct Agent, participatory design with analysts | SOC ticketing workflow, analyst trust and adoption | University SOC: 14-month field study, 4-month active use period | >90% usage rate for case closure; verifiability is key to adoption; 30–50% time savings for top-3 users | Authors: single university SOC; time comparison vs. self-reported manual baseline; preprint | Y |

---

### 3.4 Research Gap

#### Existing Research

Prior work divides into four clusters, each contributing a necessary but insufficient piece of the solution:

- **ML-based triage** ([1], [7]): Industrially deployed ML classifiers achieve strong accuracy at enterprise scale (macro-F1 0.87 for CGR [1]) and effective queue prioritization (Precision@10 92.8% for AIP [7]). However, their advantage derives from vendor-internal cross-customer data and product integration context. Critically, these models optimize for statistical similarity to historical TP patterns without explicitly encoding kill chain semantics or providing analyst-interpretable evidence chains.

- **LLM Agent investigation** ([2], [3], [4]): LLM agents offer flexible, query-driven investigation but exhibit severe reliability limitations. All mainstream reasoning strategies miss at least 40.4% of attack-related alerts [3], and the best-performing model on the ExCyTIn-Bench threat investigation benchmark achieves an investigation reward of only 0.606 [4]. The fundamental failure mode—premature case closure when queries return empty results—reveals that LLM agents conflate absence of evidence with evidence of absence.

- **Domain knowledge integration** ([6], [10], [11]): ATT&CK-based methods demonstrably improve severity assessment by contextualizing alerts within kill chain progression, with alert sequence classification AUC reaching 0.95 [10]. RAG-based ATT&CK annotation achieves F1 91.09% on CTI text [6]. Yet these methods operate as isolated systems—ATT&CK reasoning is not integrated with ML probability estimation or LLM evidence collection.

- **SOC human factors and practice** ([12], [24], [25], [26]): Empirical research consistently establishes that (a) automation complacency degrades analyst vigilance [12]; (b) output verifiability—not accuracy—determines analyst adoption [26]; (c) the TP/BP/FP distinction is essential but conflated in practice [24]; and (d) escalated cases require richer, more varied evidence collection [25]. These findings establish clear requirements for human-centered agent design that the technical ML and LLM literature largely neglects.

#### Limitations of Current Approaches

1. ML classifiers are strong at pattern recognition but do not explain *what an alert means within the attack chain*—the information analysts most need for severity judgment.
2. LLM agents terminate investigations prematurely under incomplete evidence, and simply increasing inference compute does not improve reliability [3][5].
3. Most systems produce opaque verdicts without explicit escalation policies, lack the evidence chains analysts need to independently verify outputs, and consequently risk exacerbating automation complacency [12][26].
4. Systematic reviews identify evaluation methodology inconsistency and absence of reproducible public benchmarking as a persistent gap [8].

#### Research Gap

The field currently lacks a system that **simultaneously** integrates: (a) ML triage trained on real analyst-labeled data; (b) ATT&CK and kill chain domain reasoning as explicit constraints; (c) LLM-based multi-step evidence collection with a principled termination and escalation policy; and (d) full evidence-chain explainability to support analyst verification—while providing reproducible evaluation on public datasets.

#### Our Project

The proposed AI SOC Analyst Agent is designed to close this gap through five complementary mechanisms:

1. **ML triage on real labels**: GBDT trained on the GUIDE dataset provides stable, calibrated TP/BP/FP probability estimates at scale, eliminating dependence on LLM judgment for the base classification decision (addresses Limitation 1).
2. **Explicit kill chain reasoning**: ATT&CK knowledge retrieval and five programmatic kill chain rules (R1–R5) provide domain-grounded severity constraints; later-stage attack tactics systematically increase escalation priority (addresses Limitation 1).
3. **Principled evidence collection and escalation**: The LLM planning module follows an Assume Breach protocol—empty query results trigger expanded investigation rather than case closure. An explicit escalation policy (Algorithm 2) defines four auditable conditions for human handover: low confidence, ML/LLM conflict, kill chain rule trigger, or evidence budget exhaustion without resolution (addresses Limitation 2 and 3).
4. **Full evidence-chain explainability**: Every verdict includes SHAP feature attributions, similar historical incidents, mapped ATT&CK techniques, and data source citations—enabling analysts to verify rather than accept outputs on faith (addresses Limitation 3).
5. **Reproducible dual-dataset evaluation**: Primary evaluation on GUIDE (triage accuracy, 1M incidents) and ExCyTIn-Bench (agentic log investigation) with organizational-boundary data splits (GroupKFold) prevents data leakage and enables reproducible comparison (addresses Limitation 4).

#### 繁體中文重點說明

- **ML 分級的不足**：準確率高但缺少攻擊鏈脈絡，依賴廠商私有資料，無法提供可驗證的證據鏈。
- **LLM Agent 的不足**：漏判率高（≥40.4% [3]），Benchmark 分數有限（0.606 [4]），增加推理量無法改善可靠性。
- **知識整合的缺口**：ATT&CK / Kill Chain 方法有效但與 ML/LLM 孤立。
- **人因研究的啟示**：自動化自滿 [12]、可驗證性是採用關鍵 [26]、BP≠FP 的區分 [24]、升級告警需更多證據 [25]——這些實務發現在技術論文中多被忽略。
- **Research Gap**：目前沒有系統同時整合「真實標籤 ML 分級」+「ATT&CK 領域推理」+「有升級機制的 LLM 證據收集」+「可驗證的證據鏈」且在公開資料上可重現評估。
- **本專題回應**：五個互補機制（ML 訓練於 GUIDE、Kill Chain 規則 R1–R5、Assume Breach 升級協定、完整證據鏈、GroupKFold 雙資料集評估）直接對應四個限制。

---

## 修改理由摘要

| 修改項目 | 修改理由 |
|---|---|
| 全節主要段落轉為學術英文 | 語言政策要求 |
| Article Summary Table 加入 Verified 欄位 | 規範明確要求；每篇均已確認 URL 可存取 |
| Table 內容改為英文 | 配合主文語言政策 |
| 保留全部 16 篇（[1]–[13]、[24]–[26]） | 所有引用均已驗證可存取，無需刪除；[11][12] 為 Paywall-OK |
| Research Gap 轉為英文學術段落 | 語言政策要求 |
| 新增各節末繁體中文重點說明 | 語言政策要求 |
| Research Gap 加入 R1–R5 規則說明 | 更清楚說明本專題如何具體回應各限制 |

---

## 新增引用（本 Phase 未新增）

本 Phase 7 未新增任何引用。所有引用均取自原 §6 References [1]–[26]，皆為已驗證來源。

## Unverified 項目

本 Phase 7 無 `[Unverified]` 標記。  
- [11] ROSCA (ACM)：DOI 10.1145/3733826.3762680 正確跳轉至 ACM DL，為 Paywall-OK。  
- [12] Tilbury (Emerald)：DOI 10.1108/ICS-08-2025-0318 正確跳轉至 Emerald，為 Paywall-OK。

