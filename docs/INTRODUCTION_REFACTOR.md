# Introduction Refactor — Phase 6 Changelog

> **版本**：Phase 6，2026-11-11  
> **文件目的**：記錄 §2 Introduction 的修改前版本、問題診斷、修改後版本與修改理由。  
> **語言政策**：主要段落改為學術英文；每節末附「繁體中文重點說明」。

---

## 修改前問題診斷

| 問題 | 說明 |
|---|---|
| 語言政策未落實 | §2 全節為繁體中文，規範要求主要段落使用學術英文 |
| 國安局數字混用風險 | 原文「每日約 263 萬次」緊接 SOC 告警討論，讀者可能誤解為告警量；需明確標示為「網路侵擾嘗試次數」（cyber probes / intrusion attempts） |
| 繁中說明缺漏 | 原文直接用繁中寫正文，沒有按節拆出對應的繁中重點說明區塊 |
| §2.5 表格欄位語言 | Innovation 比較表全為繁中，應配合英文主文 |
| §2.6 貢獻項目 | 全為繁中，應轉為英文正式段落 |

---

## 修改後版本

> 以下為 §2 Introduction 的完整修改後內容，已同步寫入 `docs/proposal.md`。

### 2.1 Attention Getter: The Widening Gap Between Attack Scale and Defender Response

Modern enterprises face an unprecedented surge in cyber threats that far outpaces the capacity of human defenders. According to Taiwan's National Security Bureau (NSB) 2026 disclosure, adversaries launched approximately 2.63 million daily cyber probe and intrusion attempts against Taiwan's critical infrastructure in 2025—a 6% increase from 2024 [23]. These figures represent the volume of externally originating network probes and attack attempts, not the number of alerts processed within enterprise SOC queues; the distinction is critical for avoiding misinterpretation of the operational burden on analysts.

The economic and temporal consequences of successful intrusions are severe. The IBM Cost of a Data Breach Report 2026 reveals an all-time high average breach cost of \$4.99 million (+12% year-over-year), with an average breach lifecycle of 247 days from initial compromise to containment [14]. Organizations that extensively deployed AI and automation in their security workflows achieved average savings of \$1.93 million per breach and shortened their response cycle by 65 days compared to those with no AI deployment [14]. Concurrently, Mandiant M-Trends 2026 reports a global median attacker dwell time of 14 days in 2025—an increase from 11 days in 2024—with cyber espionage campaigns and North Korean IT worker cases extending median dwell times to 122 days [15]. These metrics collectively underscore a fundamental tension: while the scale and sophistication of threats continue to escalate, the speed of detection and containment remains the decisive factor in limiting operational and financial damage.

#### 繁體中文重點說明

- **攻擊規模**：國安局 2026 年揭露，2025 年每日遭受約 263 萬次「網路侵擾嘗試」（cyber probe/intrusion attempts），較 2024 年增加 6%。**重要澄清**：此數字為外部對關鍵基礎設施的侵擾次數，非 SOC 內部告警量，兩者不可混用。
- **外洩代價**：IBM 2026 報告顯示，全球平均資料外洩成本創 499 萬美元新高（+12%），從發生到圍堵平均需 247 天；大量使用 AI 與自動化的組織可節省 193 萬美元、縮短 65 天。
- **潛伏時間**：Mandiant M-Trends 2026 指出，2025 年攻擊者全球潛伏時間中位數為 14 天（較 2024 年的 11 天延長），間諜攻擊與北韓 IT 人員案件達 122 天。
- **核心論點**：偵測與回應速度直接決定損失大小，AI 有機會在此發揮關鍵作用。

---

### 2.2 Background: How Modern SOCs Operate

A Security Operations Center (SOC) is an organization's centralized function for monitoring, detecting, analyzing, and responding to cybersecurity incidents on a continuous basis. Detection feeds originate from a diverse ecosystem of security controls—endpoint protection platforms, email gateways, identity management systems, cloud workload protections, and network sensors—each generating alerts according to their configured detection rules. These alerts are aggregated and correlated by Security Information and Event Management (SIEM) or Extended Detection and Response (XDR) platforms before reaching analysts.

SOC analysts are typically organized in a tiered structure. Tier-1 analysts are responsible for initial alert triage: classifying each incident as a True Positive (TP, confirmed malicious activity), a Benign Positive (BP, correctly detected activity that is authorized or non-threatening within the organization's context), or a False Positive (FP, an alert fired erroneously by the detection logic) [24]. This TP/BP/FP taxonomy is analytically significant: empirical research on real-world SOC workflows demonstrates that the majority of dismissed alerts are actually BPs rather than genuine FPs—the detection fired correctly, but the flagged behavior is legitimate for that organization [24]. Tier-2 and Tier-3 analysts handle confirmed TP incidents that require deeper forensic investigation, containment, eradication, and recovery.

During triage, analysts consult security logs and telemetry, verify account and host context, and map alerts to attack knowledge frameworks such as MITRE ATT&CK to determine the stage of the attack progression [10][22]. Formal response procedures follow standards such as NIST SP 800-61 Rev. 3 [13], which—as of its April 2025 revision—reorganizes incident response around the six functions of the NIST Cybersecurity Framework (CSF) 2.0 and explicitly recommends that incidents should be prioritized through structured triage rather than processed in arrival order.

**Relevance to AIoT**: Internet of Things (IoT) and Operational Technology (OT) devices in enterprise networks typically cannot support endpoint protection agents; their anomalies surface in the SOC via network-layer and identity-layer alerts. The proposed system processes alerts at the incident level, integrating evidence from multiple detection sources and reasoning over ATT&CK tactics—a framework that also offers an ICS matrix for industrial control systems. This design is intentionally device-type agnostic, making it extensible to AIoT and OT monitoring contexts.

#### 繁體中文重點說明

- **SOC 架構**：SIEM/XDR 彙整各類偵測工具的告警，Tier-1 負責初步分級（TP/BP/FP），Tier-2/Tier-3 負責深入調查與應變。
- **BP ≠ FP 的重要性**：Alahmadi 等人 [24] 研究顯示，大量被稱為「誤報」的告警其實是良性觸發（BP），應分開衡量，本專題的三分類設計（TP/BP/FP）正確反映此實務。
- **分析師工作流程**：分級時需對照 MITRE ATT&CK 判斷攻擊階段，並依 NIST SP 800-61 Rev. 3 執行應變流程，不再依到達先後排序事件。
- **與 AIoT 關聯**：本專題以事件為單位整合多來源告警，ATT&CK 有 ICS 矩陣，可延伸至工控與 IoT 裝置的監控情境。

---

### 2.3 Problem: Alert Triage as the Critical Bottleneck

Enterprise SOCs are routinely overwhelmed by alert volumes far exceeding their analysts' processing capacity. Research on large-scale SOC operations reveals that analysts must simultaneously manage hundreds of queued incidents, yet queue ordering often relies on little more than alert arrival time or coarse severity scores—neither of which reliably reflects actual threat priority [7]. This volume problem is compounded by the composition of the alert stream: in the Microsoft GUIDE dataset—the largest publicly available real-world enterprise incident dataset—only 20.6% of incidents are TP, while 49.0% are BP and 30.4% are FP [1]. The practical consequence is pervasive **alert fatigue**: analysts overwhelmed by high volumes of non-actionable alerts risk desensitization to genuine threats [8][9].

The core problem this project addresses is therefore:

> **Can an AI Agent, integrating machine learning triage, cybersecurity domain knowledge, and LLM-based reasoning, produce evidence-grounded, explainable incident classifications—with a principled policy governing when cases must be escalated to human analysts?**

#### 繁體中文重點說明

- **告警量問題**：SOC 每天面對的告警中，真實惡意事件（TP）只佔 20.6%，良性觸發（BP）49%，誤報（FP）30.4%（GUIDE 資料集 [1]）。
- **排序問題**：大型 SOC 有數百起待處理事件，但排序多依到達時間或粗略嚴重度 [7]，優先順序不可靠。
- **告警疲勞**：大量非可行動告警導致分析師疲勞，真正的攻擊反而被忽略 [8][9]。
- **核心問題**：能否設計一個 AI Agent，結合 ML、領域知識與 LLM 推理，提供有依據、可解釋，且知道何時交給人的分級決策？

---

### 2.4 Existing Limitations of Current Approaches

Current approaches to automated SOC triage suffer from five critical gaps that this project aims to address:

**1. ML classifiers lack kill chain context.** ML-based triage systems, including Microsoft's large-scale Copilot Guided Response (CGR) [1] and Adaptive Incident Prioritization (AIP) [7], can achieve high accuracy at enterprise scale—CGR reports a cross-region macro-F1 of 0.87 for TP/BP/FP classification. However, these models primarily learn statistical similarity to historical TP patterns; they do not explicitly reason about what a given alert means within the progression of an attack chain. Kill chain context is precisely the information analysts rely on to assess severity and urgency [10][11].

**2. LLM Agents exhibit high false negative rates.** LLM agents offer flexible, query-driven investigation capabilities, but systematic empirical evaluation reveals critical failure modes: across five mainstream tool-using LLM reasoning strategies, every approach misses at least 40.4% of attack-related alerts, with false negatives occurring most frequently when queries return empty results—a "no evidence" finding is incorrectly treated as "no attack" [3]. On the ExCyTIn-Bench threat investigation benchmark (57 log tables, 8 real attack chains), the best-performing model achieves an investigation reward of only 0.606, with performance degrading substantially to 0.248 when alerts are removed from the query context [4]. Furthermore, test-time compute scaling—which yields marked improvements in code and mathematics—provides only marginal benefit for security analysis tasks [5].

**3. Domain knowledge is not integrated into triage pipelines.** Methods for mapping alerts to ATT&CK tactics predominantly address threat intelligence text reports [6] rather than raw SOC alerts and logs. Graph-based severity assessment methods that do incorporate kill chain context [10][11] operate as standalone rule systems without integration with ML classifiers or LLM reasoning.

**4. Human-in-the-loop design is neglected.** Most automated systems produce only a final verdict without an explicit policy for when and how to escalate to human review. Research on SOC automation demonstrates that increasing automation induces *automation complacency*: analysts reduce their monitoring vigilance and over-rely on automated outputs [12]. Critically, field deployment evidence shows that analyst adoption of AI outputs depends primarily on output *verifiability* rather than raw accuracy [26], and that systematic verification procedures can mitigate complacency [12].

**5. Evaluations lack reproducibility.** Systematic reviews of AI-based alert filtering identify persistent deficits in operational validation and methodological consistency [8]. Commonly used benchmark datasets carry significant quality concerns—for instance, over 20% of CICIDS2017 flows require reconstruction or re-labeling due to dataset construction artifacts [17]—while evaluation pitfalls in ML security research are broadly documented [16].

#### 繁體中文重點說明

1. **ML 缺少攻擊鏈脈絡**：CGR [1] 的 macro-F1 達 0.87，但主要學習「像不像過去的 TP」，不明確說明告警在攻擊鏈中的意義，而攻擊鏈位置是判斷嚴重度的關鍵 [10][11]。
2. **LLM 漏判率高**：五種主流 LLM 推理策略都漏判至少 40.4% 的攻擊告警 [3]；ExCyTIn-Bench 最佳 reward 僅 0.606 [4]；推理模型在資安的 scaling 效益遠不如程式或數學 [5]。
3. **領域知識未整合**：ATT&CK 對應方法多處理威脅情資文字 [6]，攻擊鏈圖方法 [10][11] 是獨立規則系統，沒有與 ML/LLM 整合。
4. **缺少人機協作設計**：自動化加劇分析師自滿偏誤 [12]；影響採用的關鍵是輸出是否容易驗證 [26]，而非準確率。
5. **評估難以重現**：缺乏一致的評估方法 [8]；CICIDS2017 超過 20% 流量需重建 [17]；ML 資安評估陷阱普遍存在 [16]。

---

### 2.5 Innovation: How This Project Differs

The proposed AI SOC Analyst Agent addresses the five limitations identified above through a principled integration of complementary approaches. The following comparison table contrasts existing methods with the proposed design across six dimensions:

| Dimension | Existing Approaches | Proposed AI SOC Analyst Agent |
|---|---|---|
| **Classification basis** | Standalone ML model, or standalone LLM | **Evidence fusion**: ML calibrated probability + LLM multi-step reasoning + ATT&CK kill chain rules |
| **Domain knowledge use** | Implicit in training data, or applied only to threat intelligence text | **Explicit integration** of ATT&CK knowledge base and kill chain rules; later-stage tactics systematically bias toward escalation |
| **Uncertainty handling** | Binary verdict output only | Explicit escalation when prediction confidence falls below threshold τ, ML/LLM conclusions conflict, high-risk kill chain rules trigger, or evidence is insufficient |
| **Insufficient evidence** | LLM may close the case [3] | Per **Assume Breach** doctrine: expand queries; escalate if budget exhausted with unresolved uncertainty |
| **Explainability** | Numerical score or brief rationale | Each verdict includes a **full evidence chain**: SHAP feature attributions, similar historical incidents, mapped ATT&CK techniques, and data source citations |
| **Evaluation** | Accuracy only | Reports both **TP False Negative Rate and Human Escalation Rate**; reproducible evaluation on two public datasets |
| **Comparison with AIDA [3]** | Reasoning, challenge, and judgment all performed by LLM; evaluated on single data series; ~34k tokens/alert | Triage probability from GBDT trained on real analyst labels; LLM cannot unilaterally decide; ATT&CK knowledge and kill chain rules as hard constraints; escalation policy encoded as auditable rules; evaluated on 6.1k-organization GUIDE dataset |

#### 繁體中文重點說明

- **證據融合**：本專題的核心創新是將三種方法（ML 機率、LLM 推理、ATT&CK 規則）整合，不讓任何一個單獨決定結果。
- **升級機制**：明確定義四種升級條件（信心不足、ML/LLM 衝突、高風險規則觸發、證據不足），並依 Assume Breach 原則擴大查詢。
- **可解釋性**：每個結論都附完整證據鏈（SHAP 特徵、相似事件、ATT&CK 技術、資料來源），讓分析師有依據可驗證。
- **評估**：同時報告漏判率與升級率，在兩個公開資料集上可重現，直接回應評估不一致的問題。
- **與 AIDA [3] 的差異**：本專題的分級機率來自在真實標籤上訓練的 GBDT，不完全依賴 LLM；ATT&CK 規則作為硬性約束，升級條件是可審核的規則，而非 LLM 自由裁量。

---

### 2.6 Contributions

This project makes the following five anticipated contributions:

**1. System contribution.** We design and implement a modular AI agent for SOC alert triage that integrates ML-based probability estimation, ATT&CK knowledge retrieval, and LLM-based multi-step evidence collection within a clearly defined eight-module architecture (modules ①–⑧), providing a reproducible and extensible reference implementation.

**2. Methodological contribution.** We propose evidence fusion and escalation algorithms (Algorithms 1 and 2) that operationalize domain principles—Assume Breach, kill chain context-awareness, and asymmetric error cost—as explicit, auditable decision rules rather than implicit model behaviors.

**3. Experimental contribution.** We conduct rigorous evaluation on two public datasets: Microsoft GUIDE (triage accuracy) and ExCyTIn-Bench (agentic log investigation), comparing against majority-class, rule-based, standalone GBDT, and standalone LLM baselines. Data splits respect organizational boundaries (GroupKFold by organization and incident ID) to prevent data leakage. Ablation studies quantify the marginal contribution of each component.

**4. Domain research contribution.** We synthesize five core SOC mindsets, three domain controversies, and ten deep-understanding questions that translate cybersecurity domain knowledge into concrete system design decisions—forming a reusable analytical framework for AI-augmented SOC research.

**5. Reproducibility and handover.** All source code, data processing pipelines, DESIGN.md, and READMEs are published to enable other researchers and developers to understand, execute, verify, and extend this work.

#### 繁體中文重點說明

1. **系統貢獻**：整合 ML + ATT&CK 知識庫 + LLM 的八模組 SOC 分級 Agent，架構清楚分工，可延伸。
2. **方法貢獻**：證據融合與升級演算法（Algorithm 1、2），將 Assume Breach、攻擊鏈脈絡、錯誤成本不對稱等領域原則轉為明確的可審核決策規則。
3. **實驗貢獻**：在 GUIDE 與 ExCyTIn-Bench 上對比多個 baseline，以組織為單位切分資料避免資料洩漏，消融實驗量化各模組貢獻。
4. **領域研究貢獻**：五個核心思維模式、三個專業爭論、十個深度理解問題，形成可重用的分析框架。
5. **可重現**：公開原始碼、資料流程與完整文件，確保可繼續開發。

---

## 修改理由摘要

| 修改項目 | 修改理由 |
|---|---|
| 全節主要段落轉為學術英文 | 語言政策要求 |
| 國安局 263 萬次加「網路侵擾嘗試」與「非 SOC 告警量」明確說明 | 規範明確禁止混用；§2.1 開頭段落已加 disclaimer |
| 新增各節末繁體中文重點說明 | 語言政策要求；幫助讀者快速理解關鍵數字與論點 |
| §2.5 Innovation 表格改為英文欄位 | 配合主文語言政策 |
| §2.6 Contributions 改為英文學術段落格式 | 配合主文語言政策 |
| 加入 GUIDE 資料集中的 TP/BP/FP 分布數字（§2.3） | 以實際資料量化告警組成問題，強化論點 |
| 加入 CGR macro-F1 0.87（§2.4 限制 1） | 客觀呈現 ML 方法的強項，再說明其不足 |
| ExCyTIn-Bench reward 降至 0.248（無告警表）（§2.4 限制 2） | 更完整呈現 LLM 局限性的證據 |

---

## 新增引用（本 Phase 未新增）

本 Phase 6 未新增任何引用。所有引用均取自原 §6 References [1]–[26]，皆為已驗證來源。

## Unverified 項目

本 Phase 6 無 `[Unverified]` 標記。所有數字均取自原 proposal.md 中已驗證的引用來源。

