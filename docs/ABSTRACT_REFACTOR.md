# Abstract A–F 重構紀錄（ABSTRACT REFACTOR）

> **專案**：AI SOC Analyst Agent — DIC3 Proposal Refactor  
> **關聯檔案**：[`docs/proposal.md`](proposal.md) §1  
> **最後更新日期**：2026 年 11 月  

---

## 一、原始版本（Original Version）

> 取自小組原始提案文件 `docs/original/proposal.md` 之第 1 節：

```markdown
## 1. Abstract

**【A. Attention Getter】** 資安攻擊的規模與代價持續攀升。依國安局報告，2025 年中共對我國關鍵基礎設施的網路侵擾平均每日約 263 萬次，較 2024 年增加 6% [23]；IBM 2026 年報告指出，資料外洩的全球平均成本創新高，達 499 萬美元（較前一年增加 12%），從發生到偵測、圍堵平均需要 247 天 [14]。站在第一線的資安維運中心（SOC）每天面對數以萬計的告警，其中只有一小部分對應真實攻擊 [2]。

**【B. But】** 大量誤報與良性觸發造成告警疲勞，讓分析師可能漏看真正的威脅 [8][24]。現有解法各有限制：ML 分級模型可大規模部署 [1][7]，但較少說明告警在攻擊鏈中的意義；LLM Agent 能調查與解釋，但近期研究發現，五種主流 LLM 推理策略都漏判至少 40.4% 的攻擊告警 [3]，在資安調查 benchmark 上最佳模型也只達到 0.606 的 reward [4]。此外，自動化程度提高會讓分析師降低監控、更依賴自動化結果 [12]。

**【C. Cure】** 為了解決上述問題，本專題提出一個結合 ML 分級、MITRE ATT&CK 領域知識與 LLM 推理的 **AI SOC Analyst Agent**，對資安事件提供有證據、可解釋，並且「知道何時該交給人」的分級與處置建議。

**【D. Development】** 系統以 LLM 作為規劃與推理核心，透過工具取得事件證據；以 Gradient Boosted Trees 預測事件為真陽性（TP）、良性陽性（BP）或誤報（FP）的機率，並用 SHAP 解釋；以向量資料庫檢索 ATT&CK 技術知識與 NIST SP 800-61 Rev. 3 處置流程；最後由證據融合模組整合 ML、LLM 與攻擊鏈規則的結論。當信心不足、結論衝突、證據不足或攻擊推進到後段階段時，系統會主動升級給人工複核。

**【E. Experiments】** 本專題以 Microsoft GUIDE（約 100 萬起真實事件，標籤由資安分析師標註）評估分級表現，並以 ExCyTIn-Bench 評估 Agent 查詢 log 進行調查的能力。比較對象包括多數類別、Detector 歷史誤報率規則、純 GBDT 及純 LLM；指標包括 Macro-F1、TP 漏判率、人工升級率、ATT&CK 對應準確率、報告品質與成本，並以消融實驗檢驗各模組的貢獻。

**【F. Expected Outcomes】** 本專題尚未進行實驗。我們預期：（1）整合領域知識與升級機制後，TP 漏判率將低於純 GBDT 與純 LLM baseline；（2）漏判率與升級率之間的取捨可被量化呈現，作為實務設定門檻的依據；（3）ATT&CK 知識檢索可提升攻擊技術對應的正確性與報告的可解釋性。實際結果將於期末報告中呈現。

**關鍵字**：Security Operations Center、Alert Triage、LLM Agent、MITRE ATT&CK、Retrieval-Augmented Generation、Human-in-the-loop
```

---

## 二、原始版本問題診斷（Identified Issues）

1. **語言政策不符作業規範**：
   - 根據期末專題規範，正式提案文檔之 Abstract、Introduction 與 Related Work 正式段落應使用標準學術英文（Academic English），且各章節需附繁體中文重點說明。原始版本全為中文，缺乏英文學術段落。
2. **數據脈絡之區隔性需強化（避免混淆）**：
   - Attention Getter 引述國安局每日 263 萬次侵擾 [23]，需在英文論述中明確釐清該數據為「外部威脅探測與侵擾（Cyber Probes/Intrusions）」，而非組織內部「SOC Alert 數量」，嚴格遵守「不可把網路攻擊次數當成 SOC 告警量」的評分原則。
3. **研究限制（But）與方法論（Development）之學術表述精準度**：
   - 原始版本雖點出 40.4% 漏判率 [3] 與 0.606 reward [4]，但未清楚連結「為何 Agent 會漏判」（例如：在 tool-using 調查時因 SQL 查無紀錄而過早宣告無害）。
   - Development 模組對應應更明確與系統架構 ①–⑧ 呼應（GBDT 機率校準、TreeSHAP 特徵歸因、RAG 向量知識檢索、多輪 Log 檢索、證據融合與升級邏輯）。
4. **預期成果（Expected Outcomes）真確性**：
   - 原始版本已注意未宣稱實驗結果，但其預期假說（Hypotheses）的理論依據可更深入扣緊「Assume Breach」與「非對稱錯誤成本（Asymmetric Error Cost）」等核心思維。

---

## 三、修改後正式版本（Refactored Academic English & Traditional Chinese）

```markdown
## 1. Abstract

**[A. Attention Getter]** Modern Security Operations Centers (SOCs) are overwhelmed by tens of thousands of alerts daily, of which only a small fraction represent actual malicious intrusions. Global breach metrics highlight this acute operational pressure: the IBM Cost of a Data Breach Report 2026 reveals an all-time high average breach cost of $4.99 million (+12% year-over-year) and an average lifecycle of 247 days from breach to containment, while Mandiant M-Trends 2026 reports a global median attacker dwell time of 14 days (surging to 122 days in cyber espionage incidents). Concurrently, national telemetry, such as Taiwan National Security Bureau's 2026 disclosure of 2.63 million daily cyber probes targeting critical infrastructure (+6% from 2024), underscores the relentless barrage of external threats. In this high-stakes environment, rapid and reliable triage is the critical bottleneck in preventing catastrophic organizational damages.

**[B. But]** Massive volumes of false positives and benign triggers lead to pervasive analyst alert fatigue, creating substantial risks of overlooking genuine intrusions. Existing automated triage solutions suffer from critical shortcomings: standalone Machine Learning (ML) classifiers scale well across enterprise telemetry but lack Kill Chain semantic context; conversely, recent empirical evaluations demonstrate that five mainstream tool-using LLM agent strategies suffer from a false negative rate of at least 40.4% on attack-related alerts, primarily due to premature termination when queries yield empty results. Furthermore, on the ExCyTIn-Bench benchmark, state-of-the-art LLMs achieve an investigation reward of only 0.606. Moreover, increased opaque automation induces automation complacency among analysts, diminishing human vigilance.

**[C. Cure]** To overcome these foundational limitations, we propose the **AI SOC Analyst Agent**—a domain-specific AI system that orchestrates Machine Learning classification, MITRE ATT&CK contextual reasoning, and LLM agentic planning. The system provides evidence-grounded, explainable triage for security incidents across True Positive (TP), Benign Positive (BP), and False Positive (FP) categories, equipped with a rigorous human-in-the-loop escalation policy that knows precisely when an incident must be handed over to human analysts.

**[D. Development]** The agent employs an eight-module architecture. A Gradient Boosted Decision Tree (GBDT) model, trained on analyst-labeled enterprise telemetry, computes calibrated incident probabilities (TP/BP/FP) accompanied by TreeSHAP local feature explanations. Simultaneously, a vector database retrieves formal MITRE ATT&CK techniques and NIST SP 800-61 Rev. 3 incident handling playbooks. An LLM planner conducts multi-step evidence gathering and hypothesis verification via structured SQL log query tools. Finally, an evidence fusion engine reconciles ML predictions, ATT&CK tactical kill-chain rules, and LLM reasoning. Grounded in the "Assume Breach" and "Asymmetric Error Cost" doctrines, the system systematically escalates incidents to human analysts whenever prediction confidence falls below threshold $\tau$, conclusions conflict, investigative evidence is insufficient, or late-stage tactics (e.g., Exfiltration) are detected.

**[E. Experiments]** We evaluate the proposed system on two benchmark suites: Microsoft GUIDE (encompassing ~1 million real-world enterprise incidents across 6,100 customer organizations) for triage accuracy, and ExCyTIn-Bench (57 log tables, 8 authentic attack chains) for agentic multi-hop log investigation. Baselines include majority-class heuristic, detector-level historical false positive rules, standalone GBDT, and standalone LLM without knowledge retrieval. Primary evaluation metrics comprise Macro-F1, TP False Negative Rate (FNR), Human Escalation Rate, ATT&CK mapping accuracy, report qualitative scoring, and execution cost (token usage and latency). Ablation studies isolate the quantitative contributions of knowledge retrieval, ML probability priors, and escalation logic.

**[F. Expected Outcomes]** As this project is currently in the proposal phase, empirical evaluations are pending. We hypothesize: (1) integrating domain knowledge constraints and calibrated escalation rules will significantly reduce TP False Negative Rates compared to standalone ML and LLM baselines; (2) the operational trade-off curve between Miss Rate and Human Escalation Rate can be quantitatively mapped to provide actionable tuning for tiered SOC teams; and (3) structured ATT&CK retrieval will demonstrably improve tactic mapping precision and report verifiability for Tier-1 analysts. All empirical validations will be executed and documented in the final capstone deliverable.

**Keywords**: Security Operations Center (SOC), Alert Triage, LLM Agent, MITRE ATT&CK, Explainable AI (SHAP), Human-in-the-Loop, Spec-Driven Development.

### 繁體中文重點說明

1. **研究動機（Attention Getter）**：
   - 整合 2026 最新官方與產業實證數據：IBM 2026 報告指出全球資料外洩成本創 499 萬美元新高、偵測至圍堵週期長達 247 天；Mandiant M-Trends 2026 指出攻擊者潛伏期中位數為 14 天（間諜攻擊達 122 天）；國安局 2026 數據顯示關鍵基礎設施每日面臨 263 萬次侵擾。強調第一線 SOC 告警分級是圍堵災情最嚴峻的瓶頸。
2. **現有方法瓶頸與 Research Gap（But）**：
   - 告警疲勞源於誤報與良性觸發（BP）；純 ML 缺少攻擊鏈脈絡；LLM Agent 在查無紀錄時易誤判提前結案，主流策略漏判率高達 40.4% [3]，在 ExCyTIn-Bench 基準評測僅得 0.606 reward [4]；過度自動化更造成分析師自滿偏誤（Automation Complacency）[12]。
3. **解決方案（Cure）**：
   - 提出結合 ML 分級、MITRE ATT&CK 知識圖譜與 LLM 推理的 **AI SOC Analyst Agent**，提供具備證據鏈、可解釋性，且「知所進退（明確升級給人類）」的智慧代理人。
4. **系統方法論（Development）**：
   - 以系統架構 ①–⑧ 為基礎：GBDT 預測 TP/BP/FP 機率並搭配 TreeSHAP 解釋；向量知識庫檢索 ATT&CK 與 NIST 應變指引；LLM 執行 Log 證據收集；證據融合模組於低信心、衝突、證據不足或晚期戰術時觸發升級機制。
5. **實驗設計（Experiments）**：
   - 使用 Microsoft GUIDE（100 萬起真實事件、6.1k 組織）與 ExCyTIn-Bench（57 張 Log 表、8 條攻擊鏈）。評估指標包含 Macro-F1、TP 漏判率、升級率、ATT&CK 對應準確率與 Token 成本，並進行消融實驗。
6. **預期成果（Expected Outcomes）**：
   - 遵守真實性原則，標明為預期成果：預期漏判率顯著低於純 GBDT 與純 LLM；能繪出「漏判率 vs. 升級率」取捨曲線；提升報告可驗證性與可解釋性。
```

---

## 四、修改理由與查證來源對照

| 段落標籤 | 修改重點 | 理論與實證依據（Verified Sources） |
|---|---|---|
| **A. Attention Getter** | 區分外部威脅侵擾（263 萬次/日）與內部 SOC 告警量；補齊 2026 年最新損失金額（$4.99M）與潛伏天數（14 天/122 天）。 | 國安局報告 [23]；IBM Cost of a Data Breach 2026 [14]；Mandiant M-Trends 2026 [15]。 |
| **B. But** | 明確點出 LLM Agent 失敗機制（查無紀錄時過早結案导致漏判率 $\ge 40.4\%$），並引述人因研究指出自動化自滿。 | Tsegai et al. (AIDA) [3]；ExCyTIn-Bench [4]；Tilbury & Flowerday (2026) [12]；Alahmadi et al. [24]。 |
| **C. Cure** | 定位為領域專用 AI Agent（Domain AI Agent），突出 TP/BP/FP 分級、證據鏈與人機協同決策邊界。 | 呼應期末專題規範核心原則（AI Agent + Domain Knowledge + Data Analytics + Real-World Application）。 |
| **D. Development** | 具體展開 GBDT、TreeSHAP、ATT&CK STIX RAG、SQL Log 調查工具、證據融合演算法之技術堆疊。 | GUIDE [1]；TechniqueRAG [6]；NIST SP 800-61 Rev. 3 [13]；DESIGN.md 架構 ①–⑧。 |
| **E. Experiments** | 跨資料集評測（GUIDE + ExCyTIn-Bench），量化「漏判率–升級率」取捨，設計消融實驗。 | GUIDE [1]；ExCyTIn-Bench [4]；Arp et al. [16]（防範評估陷阱）。 |
| **F. Findings** | 恪守「Expected Outcomes」規範，嚴禁假造實驗數據，以三個具體假說呈現期末預期驗證方向。 | 期末專題規範第二節與第六節。 |
