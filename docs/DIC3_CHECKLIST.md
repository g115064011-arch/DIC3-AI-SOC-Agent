# DIC3 作業檢核表（DIC3 Checklist）

> **專案名稱**：AI SOC Analyst Agent — DIC3 Proposal Refactor  
> **專案位置**：`DIC3-AI-SOC-Agent/`  
> **交付分支**：`dic3-refactor`（合併至 `main`）  
> **更新時間**：2026-11-11  

本檢核表對照課程教師之五項核心要求，逐一列出對應的完成成果、量化證據與檔案位置，供專案審查與口試檢閱。

---

## 檢核表總覽矩陣（Requirements Matrix）

| 編號 | 教師要求項目 | 審查重點 | 完成狀態 | 核心檔案位置 |
|:---:|---|---|:---:|---|
| **REQ-1** | **Abstract & Introduction 重構** | A–F 架構、學術英文＋繁中重點、數據嚴謹性、創新比較表 | **已完成** | [`docs/ABSTRACT_REFACTOR.md`](ABSTRACT_REFACTOR.md)<br>[`docs/INTRODUCTION_REFACTOR.md`](INTRODUCTION_REFACTOR.md)<br>[`docs/proposal.md`](proposal.md) §1, §2 |
| **REQ-2** | **Related Work 文獻回顧** | AI / Domain 各約 50%、Summary Table (含 Verified)、零虛構數據、Research Gap | **已完成** | [`docs/RELATED_WORK_REFACTOR.md`](RELATED_WORK_REFACTOR.md)<br>[`research/sources.md`](../research/sources.md)<br>[`docs/proposal.md`](proposal.md) §3, §6 |
| **REQ-3** | **Deep Research 領域深度解析** | 5 大思維 (對應 ①–⑧)、3 大專業爭論 (辯證架構)、10 大深度問題 | **已完成** | [`docs/DEEP_RESEARCH.md`](DEEP_RESEARCH.md)<br>[`docs/proposal.md`](proposal.md) §4 |
| **REQ-4** | **系統設計與 OpenSpec SDD 規格** | 八大模組架構、RFC 2119 SHALL/MUST、Gherkin 情境、Active 變更驗證通過 | **已完成** | [`DESIGN.md`](../DESIGN.md)<br>[`docs/OPEN_SPEC_GUIDE.md`](OPEN_SPEC_GUIDE.md)<br>[`openspec/`](../openspec/) |
| **REQ-5** | **實驗評測設計與可重現性** | 雙公開資料集、GroupKFold 防外洩、e0 剖析驗證、無機密無大型檔案 | **已完成** | [`experiments/e0_profile_guide.py`](../experiments/e0_profile_guide.py)<br>[`experiments/results/guide_train_profile.json`](../experiments/results/guide_train_profile.json)<br>[`docs/proposal.md`](proposal.md) §5 |

---

## 詳細檢核項目與佐證

### REQ-1. Abstract & Introduction 結構化與學術品質

- [x] **A–F 結構完整性**：
  - Abstract 完整落實 Attention Getter (A)、But (B)、Cure (C)、Development (D)、Experiments (E)、Expected Outcomes (F) 六段標準結構。
  - 佐證檔案：[`docs/ABSTRACT_REFACTOR.md`](ABSTRACT_REFACTOR.md)、[`docs/proposal.md`](proposal.md#1-abstract)。
- [x] **雙語政策嚴格落實**：
  - 主要論述採用高標準學術英文（Academic English），文末均附「繁體中文重點說明」區塊。
- [x] **數據脈絡精確界定**：
  - 國安局 2026 年揭露之「每日 263 萬次」明確標記為外部關鍵基礎設施「網路探測與侵擾嘗試（cyber probes/intrusion attempts）」，並加註警語明確與組織內部「SOC 告警量」劃清界線，杜絕概念混淆。
- [x] **創新性比較表與貢獻條列**：
  - §2.5 提供與傳統方案及先進研究（如 AIDA [3]）之全方位對比表格。
  - §2.6 明確條列五大研究貢獻（系統、方法、實驗、領域研究、可重現性）。
  - 佐證檔案：[`docs/INTRODUCTION_REFACTOR.md`](INTRODUCTION_REFACTOR.md)、[`docs/proposal.md`](proposal.md#2-introduction)。

---

### REQ-2. Related Work 文獻回顧與真實性查證

- [x] **主題篇數與篇幅對稱（各 50%）**：
  - **AI Technology**（8 篇）：CGR [1]、CORTEX [2]、AIDA [3]、ExCyTIn-Bench [4]、CyberSOCEval [5]、TechniqueRAG [6]、AIP [7]、Banstola [26]。
  - **Domain Know-how**（8 篇）：Ndichu [8]、Habibzadeh [9]、Sadlek [10]、ROSCA [11]、Tilbury [12]、NIST SP 800-61r3 [13]、Alahmadi [24]、Kersten [25]。
  - 實際統計：文獻篇數 50.0% : 50.0%（8 篇 vs 8 篇）；英文詞數比例 49.4% : 50.6%；字元數比例 49.2% : 50.8%，嚴格符合約各 50% 要求。
- [x] **Article Summary Table 與可驗證性**：
  - 包含 16 篇文獻之全英文結構化對比表（Ref, Year, Problem, AI Method, Domain Knowledge, Dataset, Key Findings, Limitation, Verified）。
  - 逐篇實測 URL 與 DOI：全部 16 篇均為 HTTP 200 或資料庫正常跳轉（Paywall-OK），無任何 `[Unverified]` 標記。
- [x] **零虛構文獻與數據抽查實測**：
  - 抽查 8 篇原文驗證年份與數值，全數真實無訛；在 CyberSOCEval [5] 抽查過程中，更進一步對照 Figure 8 與原文將草稿誤植之 23–34% 更正為真實數據 15–28%（TI 43–53%）。
- [x] **Research Gap 梳理**：
  - 明確總結現有四大技術限制，並具體提出本專案之五大互補應對架構。
  - 佐證檔案：[`docs/RELATED_WORK_REFACTOR.md`](RELATED_WORK_REFACTOR.md)、[`research/sources.md`](../research/sources.md)、[`docs/proposal.md`](proposal.md#3-related-work)。

---

### REQ-3. Deep Research 領域深度解析（5 + 3 + 10）

- [x] **五大核心思維模式（Five Core Mindsets）**：
  - 完整分析 M1 Assume Breach、M2 Context Awareness、M3 Asymmetric Error Cost、M4 Pyramid of Pain、M5 Human-in-the-Loop。
  - **每個思維模式皆明確對應系統架構模組編號（①～⑧）** 與權威文獻佐證。
- [x] **三大專業爭論（Three Core Controversies）**：
  - C1：告警分級該依賴 ML 還是 LLM？（View A ↔ View B）
  - C2：自動化自滿 vs. 分析師監督（View A ↔ View B）
  - C3：公開 Benchmark vs. 專有遙測實證（View A ↔ View B）
  - 採用完整的辯證骨架：正反論點 ↔ 實證依據 ↔ 業界共識 ↔ 未解挑戰 ↔ 本專案設計決策。
- [x] **十大深度理解問題（Ten Deep-Understanding Questions）**：
  - 深入解答包含「為何以 incident 而非單一 alert 為處理單位」、「為何單純擴大 test-time compute 無法解決資安推理」、「日誌中斷時如何避免偽陽性/偽陰性結案」等十項關鍵專業難題。
  - 佐證檔案：[`docs/DEEP_RESEARCH.md`](DEEP_RESEARCH.md)、[`docs/proposal.md`](proposal.md#4-deep-research)。

---

### REQ-4. 系統設計與 OpenSpec 規格驅動開發（SDD）

- [x] **模組化系統架構設計**：
  - 定義 ① 使用者/佇列、② 告警輸入、③ Planner、④ 證據取得、⑤ 分析引擎、⑥ 領域知識、⑦ 決策融合、⑧ 報告/介面 八大模組。
  - 具備完整資料流圖、Mermaid 流程圖、Algorithm 1（證據蒐集與終止）與 Algorithm 2（多模態融合與升級）。
  - 佐證檔案：[`DESIGN.md`](../DESIGN.md)、[`docs/proposal.md`](proposal.md#5-system-design)。
- [x] **OpenSpec 變更與形式化規格設計**：
  - 建立 Active Change：`openspec/changes/refactor-ai-soc-agent-proposal/`。
  - 涵蓋五大核心 Capabilities 規格，全面採用 RFC 2119 規範詞彙（`SHALL` / `MUST`）與 Gherkin 風格驗證情境（`Scenario: WHEN ... THEN ...`）：
    - `incident-triage`
    - `evidence-retrieval`
    - `domain-knowledge-reasoning`
    - `risk-escalation`
    - `explainability-reporting`
- [x] **生命週期原則落實**：
  - 恪遵 SDD 真實性原則，**在 Proposal 與藍圖規劃階段禁止執行 `openspec archive`**，避免產生虛假歸檔。
  - 嚴格校驗指令：執行 `npx @fission-ai/openspec validate refactor-ai-soc-agent-proposal --strict` 檢驗全數通過（Valid）。
  - 佐證檔案：[`docs/OPEN_SPEC_GUIDE.md`](OPEN_SPEC_GUIDE.md)、[`openspec/`](../openspec/)。

---

### REQ-5. 實驗評測設計、可重現性與資安防護

- [x] **雙公開資料集評測設計**：
  - Microsoft GUIDE：1,300 萬證據、100 萬事件、6,100 企業組織真實分析師標籤。
  - ExCyTIn-Bench：57 張 log 表、8 條真實攻擊鏈，評測多輪 SQL 調查能力。
- [x] **防止資料外洩之嚴格資料切分**：
  - 規劃以客戶組織（`OrgId`）與事件（`IncidentId`）為單位的 GroupKFold 切分，杜絕同企業相似事件跨入測試集。
- [x] **營運指標周全性**：
  - 同時評估並繪製「TP False Negative Rate」與「Human Escalation Rate」的營運取捨曲線。
- [x] **真實資料剖析腳本可執行驗證**：
  - 實作 [`experiments/e0_profile_guide.py`](../experiments/e0_profile_guide.py)，成功剖析 GUIDE 訓練集（707,108 事件、5,769 組織、9,516,837 筆證據列），產出完整結構化報表 [`experiments/results/guide_train_profile.json`](../experiments/results/guide_train_profile.json)。
- [x] **安全與輕量檢驗**：
  - 全專案通過密鑰掃描，無任何 API Token、金鑰或密碼洩漏。
  - 大型資料檔（`.csv`、`.parquet`）已透過 [`.gitignore`](../.gitignore) 排除，未納入 Git 追蹤。
