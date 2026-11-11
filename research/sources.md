# 已查證學術文獻與產業報告來源清單（Research Sources）

本文件記錄專案所引用的所有學術論文、產業報告與政府官方資料，確保「不得虛構論文、作者、DOI、年份、研究數值或實驗結果」之最高規範。所有條目均經過查證，並標記精確數據與來源網址。

---

## 一、AI 技術文獻（AI Technology）

### [1] S. Freitas, J. Kalajdjieski, A. Gharib, and R. McCann (2024)
- **篇名**：*AI-Driven Guided Response for Security Operation Centers with Microsoft Copilot for Security*
- **來源**：arXiv:2407.09017, 2024
- **URL**：[https://arxiv.org/abs/2407.09017](https://arxiv.org/abs/2407.09017)
- **已驗證事實**：
  - 提出 Copilot Guided Response (CGR) 機器學習架構，整合於 Microsoft Defender XDR。
  - 發布 **GUIDE 資料集**：約 1,300 萬筆證據（evidence）、160 萬筆告警（alerts）、100 萬起事件（incidents）、涵蓋 6,100 家真實客戶組織、時間跨度兩週，標籤由資安分析師標註（TP / BP / FP）。
  - 內部離線評估：分級跨區域平均 macro-F1 為 0.87、precision 0.87、recall 0.86；在 90% precision 門檻下可覆蓋約 41% 事件。

### [2] B. Wei, Y. S. Tay, H. Liu, J. Pan, K. Luo, Z. Zhu, and C. Jordan (2025)
- **篇名**：*CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage*
- **來源**：arXiv:2510.00311, 2025
- **URL**：[https://arxiv.org/abs/2510.00311](https://arxiv.org/abs/2510.00311)
- **已驗證事實**：
  - 提出多 Agent 協作（行為分析、證據蒐集、推理）架構。
  - 可行動告警 F1 自 0.66 提升至 0.78，誤報率自 24.9% 降至 14.2%。
  - 代價：Token 消耗約為單 Agent 的 5.7 倍，每告警處理延遲 152 秒（約 3.4 倍）。

### [3] S. A. Tsegai, A. Kantchelian, D. Yao, and P. Gao (2026)
- **篇名**：*From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage*
- **來源**：arXiv:2610.10608, 2026
- **URL**：[https://arxiv.org/abs/2610.10608](https://arxiv.org/abs/2610.10608)
- **已驗證事實**：
  - 評估 5 種 tool-using LLM 推理策略，發現主流方法**漏判至少 40.4% 的攻擊相關告警**。
  - 漏判主因：查詢「查無紀錄（no records found）」時最容易誤判為良性並提前結案。
  - 提出 AIDA 架構（獨立質疑 + 裁判機制）：F1 提升至 0.958，TP 漏判率降至 3.1%，代價為 18.4% 的告警升級給人工複核；平均每告警耗費 3.4 萬 tokens、12.7 秒、成本約 $0.109。

### [4] Y. Wu et al. (2026 / 2025)
- **篇名**：*ExCyTIn-Bench: Evaluating LLM Agents on Cyber Threat Investigation*
- **來源**：*Proc. ICML*, 2026; arXiv:2507.14201, 2025
- **URL**：[https://arxiv.org/abs/2507.14201](https://arxiv.org/abs/2507.14201)
- **已驗證事實**：
  - 建立受控 Azure 雲端環境 benchmark：57 張 log 表、8 條真實攻擊鏈、7,542 題調查問答。
  - 當前最佳模型 reward 僅 0.606；若切換至完整資料庫則驟降至 0.248。

### [5] L. Deason et al. (2025)
- **篇名**：*CyberSOCEval: Benchmarking LLMs Capabilities for Malware Analysis and Threat Intelligence Reasoning*
- **來源**：arXiv:2509.20166, 2025
- **URL**：[https://arxiv.org/abs/2509.20166](https://arxiv.org/abs/2509.20166)
- **已驗證事實**：
  - 評估 LLM 在惡意程式分析（609 題）與威脅情資推理（588 題）之表現，準確率分別僅 23–34% 與 43–53%。
  - 指出 test-time scaling 在資安推理上的增益遠低於數學與寫程式。

### [6] A. Lekssays, U. Shukla, H. T. Sencar, and M. R. Parvez (2025)
- **篇名**：*TechniqueRAG: Retrieval Augmented Generation for Adversarial Technique Annotation in Cyber Threat Intelligence Text*
- **來源**：*Findings of ACL*, 2025; arXiv:2505.11988
- **URL**：[https://arxiv.org/abs/2505.11988](https://arxiv.org/abs/2505.11988)
- **已驗證事實**：
  - 使用 RAG 搭配指令微調將威脅情資文字對應到 MITRE ATT&CK 技術。
  - Procedures 資料集達到 F1 91.09%；但多標籤之 Expert 資料集僅達約 50%。

### [7] S. Freitas, A. Gharib, and M. Magenheim (2026)
- **篇名**：*Adaptive Incident Prioritization for Security Operations at Scale*
- **來源**：arXiv:2607.16963, 2026
- **URL**：[https://arxiv.org/abs/2607.16963](https://arxiv.org/abs/2607.16963)
- **已驗證事實**：
  - 提出改進 BM25 的跨租戶事件佇列排序演算法（AIP）。
  - 專家評估 Precision@10 達 92.8%，在 GUIDE 上補齊 9,980 筆事件的優先順序標籤。

### [26] K. Banstola, F. Al Faisal et al. (2026)
- **篇名**：*It Is Not Yet Another Tool: Creating and Deploying an Agentic AI Companion in a Security Operations Center*
- **來源**：arXiv:2609.06250, 2026
- **URL**：[https://arxiv.org/abs/2609.06250](https://arxiv.org/abs/2609.06250)
- **已驗證事實**：
  - 14 個月真實大學 SOC 實地部署研究。
  - 超過 90% 案例中分析師沿用 Agent 的輸出作為結案報告；頂尖使用者自陳節省 30–50% 調查時間。
  - **核心發現**：影響採用的關鍵不是模型準確率，而是**輸出結果是否易於人類驗證（verifiability）**。

---

## 二、領域知識與資安維運文獻（Domain Know-how）

### [8] S. Ndichu, T. Ban, S. Ozawa, T. Takahashi, and D. Inoue (2026)
- **篇名**：*AI-Driven Security Alert Screening and Alert Fatigue Mitigation in Security Operations Centers: A Survey*
- **來源**：arXiv:2605.08316, 2026
- **URL**：[https://arxiv.org/abs/2605.08316](https://arxiv.org/abs/2605.08316)
- **已驗證事實**：
  - 綜述 2015–2026 年 87 篇核心文獻，劃分過濾、分級、關聯與生成增強四階段。
  - 指出現有研究缺乏實地營運驗證、對抗穩健性、跨環境泛化能力及一致評估標準。

### [9] A. Habibzadeh, F. Feyzi, and R. Ebrahimi Atani (2025)
- **篇名**：*Large Language Models for Security Operations Centers: A Comprehensive Survey*
- **來源**：arXiv:2509.10858, 2025
- **URL**：[https://arxiv.org/abs/2509.10858](https://arxiv.org/abs/2509.10858)
- **已驗證事實**：系統性回顧 LLM 在 Log 分析、告警分級與威脅情資之應用與瓶頸。

### [10] L. Sadlek, M. M. Yamin, P. Čeleda, and B. Katt (2025)
- **篇名**：*Severity-Based Triage of Cybersecurity Incidents Using Kill Chain Attack Graphs*
- **來源**：*Journal of Information Security and Applications*, vol. 89, 2025
- **DOI**：[10.1016/j.jisa.2024.103956](https://doi.org/10.1016/j.jisa.2024.103956)
- **已驗證事實**：結合 MulVAL 攻擊圖與 Kill Chain 階段進行告警序列分級，AUC 達 0.95。證明攻擊推進階段決定嚴重度。

### [11] R. Garcia, A. Lahmadi, P.-F. Gimenez, and C. Sala (2025)
- **篇名**：*ROSCA: Robust and Scalable Security Alert Correlation and Prioritisation using the MITRE ATT&CK Framework*
- **來源**：*Proc. WATCH '25*, pp. 30–37, 2025
- **DOI**：[10.1145/3733826.3762680](https://doi.org/10.1145/3733826.3762680)
- **已驗證事實**：以 ATT&CK 戰術推進為權重將告警聚合成事件，在法國醫院真實 SOC 評測表現優於 MATE。

### [12] J. Tilbury and S. V. Flowerday (2026)
- **篇名**：*The Vigilance Paradox: Automation Reliance Inside the Modern SOC*
- **來源**：*Information and Computer Security*, vol. 34, no. 4, pp. 639–662, 2026
- **DOI**：[10.1108/ICS-08-2025-0318](https://doi.org/10.1108/ICS-08-2025-0318)
- **已驗證事實**：
  - 696 份分析師問卷與 29 場深度訪談。
  - 證實自動化程度提高會誘發「自動化自滿（automation complacency）」，降低分析師警覺性；唯有**系統性驗證程序**能緩解該效應。

### [13] NIST (2025)
- **篇名**：*Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*
- **來源**：NIST SP 800-61 Rev. 3, Apr. 2025
- **DOI**：[10.6028/NIST.SP.800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3)
- **已驗證事實**：全面改依 NIST CSF 2.0（Govern, Identify, Protect, Detect, Respond, Recover）重新構建事件應變指引，要求必須分級驗證（RS.MA-02）且不可採先進先出。

### [24] B. A. Alahmadi, L. Axon, and I. Martinovic (2022)
- **篇名**：*99% False Positives: A Qualitative Study of SOC Analysts' Perspectives on Security Alarms*
- **來源**：*Proc. 31st USENIX Security Symposium*, pp. 2783–2800, 2022
- **URL**：[https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi)
- **已驗證事實**：
  - 訪談 7 個 SOC 的 21 位實務人員。
  - 發現大量被通稱為「誤報」的告警實為 **Benign Positive（BP，良性觸發）**：規則偵測無誤但行為經組織授權。強調必須將 FP 與 BP 嚴格分離。

### [25] L. Kersten, K. Beelen, E. Zambon, C. Snijders, and L. Allodi (2025)
- **篇名**：*A Field Study to Uncover and a Tool to Support the Alert Investigation Process of Tier-1 Analysts*
- **來源**：*Proc. USEC 2025*
- **DOI**：[10.14722/usec.2025.23034](https://doi.org/10.14722/usec.2025.23034)
- **已驗證事實**：在商業 SOC 中觀察 5 位 Tier-1 分析師進行 400 次調查，發現最終需要人工升級的告警，分析師會主動蒐集更多維度的證據。

---

## 三、權威產業報告與官方統計

### [14] IBM Security (2026)
- **名稱**：*Cost of a Data Breach Report 2026*
- **URL**：[https://www.ibm.com/reports/data-breach](https://www.ibm.com/reports/data-breach)
- **已驗證數據**：
  - 全球資料外洩平均成本達 **499 萬美元**（年增 12%）。
  - 資料外洩平均生命週期（偵測至圍堵）為 **247 天**。
  - 廣泛應用資安 AI 與自動化技術之組織，平均省下 **193 萬美元** 成本，處理週期縮短 **65 天**。

### [15] Google Cloud / Mandiant (2026)
- **名稱**：*M-Trends 2026: Data, Insights, and Strategies From the Frontlines*
- **URL**：[https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026)
- **已驗證數據**：
  - 全球攻擊者潛伏時間（Dwell Time）中位數為 **14 天**。
  - 網路間諜（Cyber Espionage）及特定國家威脅潛伏時間長達 **122 天**。

### [23] 中華民國國家安全局 (2026)
- **名稱**：*2025 年中共對我國關鍵基礎設施網駭威脅分析*
- **日期**：2026 年 1 月，第 1 頁
- **URL**：[https://www.nsb.gov.tw/zh/assets/documents/%E6%96%B0%E8%81%9E%E7%A8%BF/9473ea89-55e8-460d-87c1-65bc51085d80.pdf](https://www.nsb.gov.tw/zh/assets/documents/%E6%96%B0%E8%81%9E%E7%A8%BF/9473ea89-55e8-460d-87c1-65bc51085d80.pdf)
- **已驗證數據**：2025 年中共對我國關鍵基礎設施之網路侵擾平均每日約 **263 萬次**，年增 6%。
