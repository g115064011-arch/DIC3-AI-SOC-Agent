# AI SOC Analyst Agent (DIC3 Proposal Refactor)

> **DIC3 個人作業**：以 OpenSpec 規格驅動開發（Spec-Driven Development, SDD）進行專題 Proposal 重構、深度研究與形式化系統規格設計。  
> **專案主題**：結合 Machine Learning、MITRE ATT&CK 領域知識、LLM Agent 推理、SHAP 特徵歸因與人機協同（Human-in-the-loop）的資安維運中心（SOC）智慧分級代理人。

---

## 一、專案目標與 DIC3 任務重點

本專案為國立中興大學資通安全相關課程 **DIC3 個人作業**。核心任務目標包含：
1. **研究品質學術化**：將期末專題提案導入嚴謹學術規範，落實雙語政策（主要章節採學術英文，文末附繁體中文重點說明）。
2. **數據嚴謹與零虛構（Zero Hallucination）**：所有引述文獻、DOI、數據皆經真實原文查核（Verified），杜絕 AI 幻覺，並嚴格區隔「外部網路探測侵擾嘗試」與「企業 SOC 內部告警量」。
3. **領域知識深度深化（5 + 3 + 10）**：系統性剖析 5 大資安思維、3 大核心專業爭論與 10 大深度技術難題，將資安專家直覺轉化為明確的系統架構決策。
4. **規格驅動開發（SDD）導入**：使用 [OpenSpec](openspec/) 建立形式化能力規格（RFC 2119 規範與 Gherkin 驗收情境），確保研究提案、系統架構與後續程式碼完全一致。

---

## 二、原始小組專案來源與致謝（Original Team Attribution）

本專案沿用小組期末專題主題，並於個人 Repository 進行獨立研究深化、提案重構與 OpenSpec 規格設計。

- **原始專題名稱**：AI SOC Analyst Agent
- **原始專題作者**：期末專案第 16 組（Group 16）
  - 蘇恩平
  - 周妤
  - 袁靖淇
  - 蕭宥瑄
- **原始小組 Repository**：[https://github.com/susuannie/proposal.git](https://github.com/susuannie/proposal.git)
- **原始提案存檔**：[`docs/original/`](docs/original/)（包含原始小組版 `proposal.md`、簡報 PDF 與 PPTX 原始檔）

---

## 三、個人 Refactor 核心升級內容

相較於小組原始版本，個人在本次 DIC3 作業中完成以下重大升級與深化：

1. **章節規格重構與雙語政策**：
   - **Abstract（§1）**：改寫為標準 **A–F 結構**（Attention Getter, But, Cure, Development, Experiments, Expected Outcomes），英文學術主文搭配繁中摘要。詳見 [`docs/ABSTRACT_REFACTOR.md`](docs/ABSTRACT_REFACTOR.md)。
   - **Introduction（§2）**：釐清國安局 263 萬次為「外部威脅探測與侵擾」，非 SOC 內部告警；新增與 SOTA（如 AIDA [3]）之創新對比表，明確列出五大具體研究貢獻。詳見 [`docs/INTRODUCTION_REFACTOR.md`](docs/INTRODUCTION_REFACTOR.md)。
   - **Related Work（§3）**：AI 技術與 Domain 知識文獻比例達到各 50%（8 篇 : 8 篇）；建立包含 16 篇實測已驗證（Verified）之文獻摘要表；提出明確四大研究限制與五大互補應對架構。詳見 [`docs/RELATED_WORK_REFACTOR.md`](docs/RELATED_WORK_REFACTOR.md)。
2. **Deep Research 領域深度解析（5 + 3 + 10）**：
   - **5 大核心思維（Mindsets）**：M1 Assume Breach、M2 Context Awareness、M3 Asymmetric Error Cost、M4 Pyramid of Pain、M5 Human-in-the-Loop，每個思維皆明確綁定至系統架構模組編號（①～⑧）。
   - **3 大核心爭論（Controversies）**：以「View A ↔ View B → 實證 → 共識 → 未解挑戰 → 本專案決策」之嚴謹辯證架構探討 ML vs LLM、自動化自滿與評測 Benchmark 選擇。
   - **10 大深度問題（Questions）**：深入分析以 incident 為單位的理由、非對稱成本量化、測試時推理 Scaling 限制、日誌中斷處理等專業議題。詳見 [`docs/DEEP_RESEARCH.md`](docs/DEEP_RESEARCH.md)。
3. **OpenSpec 規格驅動開發藍圖**：
   - 將系統完整映射為 5 大核心 Capabilities、15 條 RFC 2119 規範與 15 組可驗證驗收情境。詳見 [`docs/OPEN_SPEC_GUIDE.md`](docs/OPEN_SPEC_GUIDE.md)。

---

## 四、系統核心架構與 OpenSpec 規格對應

Agent 針對資安事件提供 **TP（True Positive） / BP（Benign Positive） / FP（False Positive）** 三級分級、ATT&CK 攻擊鏈對應與處置建議，每個結論皆附有可驗證的證據鏈；當信心度不足、結論衝突、高風險或證據不足時，主動交由分析師複核（Human-in-the-loop）。

### 八大核心模組架構

```
① 分析師 / 告警佇列 → ② 事件輸入 → ③ Planner & Reasoning Agent
   ↔ ④ 證據取得（事件資料、Log 查詢）
   ↔ ⑤ 分析引擎（分級模型、SHAP、相似事件）
   ↔ ⑥ 領域知識（MITRE ATT&CK、NIST SP 800-61 Rev. 3、D3FEND）
→ ⑦ 決策融合與升級判斷 → ⑧ 事件報告 / Dashboard
```

### OpenSpec 規格對應關係表

詳細架構設計與演算法虛擬碼請參閱 [`DESIGN.md`](DESIGN.md)。

| 系統架構模組 | OpenSpec Capability | 規格檔案位置 | 形式化需求（RFC 2119） |
|---|---|---|---|
| ② 事件輸入 / ⑤ 分級模型 | `incident-triage` | [`openspec/.../incident-triage/spec.md`](openspec/changes/refactor-ai-soc-agent-proposal/specs/incident-triage/spec.md) | Ingestion Validation, Multi-Class Prediction |
| ③ Planner / ④ 證據取得 | `evidence-retrieval` | [`openspec/.../evidence-retrieval/spec.md`](openspec/changes/refactor-ai-soc-agent-proposal/specs/evidence-retrieval/spec.md) | Multi-Hop Acquisition, Query Budget, Assume Breach Check |
| ⑥ 領域知識庫 | `domain-knowledge-reasoning` | [`openspec/.../domain-knowledge-reasoning/spec.md`](openspec/changes/refactor-ai-soc-agent-proposal/specs/domain-knowledge-reasoning/spec.md) | ATT&CK Retrieval, Kill Chain Rules (R1–R5), Playbook Alignment |
| ⑦ 決策融合與升級 | `risk-escalation` | [`openspec/.../risk-escalation/spec.md`](openspec/changes/refactor-ai-soc-agent-proposal/specs/risk-escalation/spec.md) | Multi-Modal Evidence Fusion, Human Escalation Policy |
| ⑤ SHAP / ⑧ 報告介面 | `explainability-reporting` | [`openspec/.../explainability-reporting/spec.md`](openspec/changes/refactor-ai-soc-agent-proposal/specs/explainability-reporting/spec.md) | TreeSHAP Attribution, Dual-Format Audit Reports, Feedback Ingestion |

---

## 五、專案目錄結構

```
DIC3-AI-SOC-Agent/
├── README.md                     # 專案總覽與作業指引（本文件）
├── DESIGN.md                     # 系統架構設計藍圖、流程圖、演算法與 OpenSpec 映射
├── docs/
│   ├── proposal.md               # 唯一正式學術提案版本（§1–§6 完整內容）
│   ├── DIC3_CHECKLIST.md         # DIC3 作業檢核表（對照老師五項要求）
│   ├── OPEN_SPEC_GUIDE.md        # OpenSpec 與規格驅動開發完整指南
│   ├── ABSTRACT_REFACTOR.md      # Abstract A–F 結構重構紀錄與診斷
│   ├── INTRODUCTION_REFACTOR.md  # Introduction 重構紀錄、創新對比與貢獻
│   ├── RELATED_WORK_REFACTOR.md  # Related Work 16 篇實測查證與重構紀錄
│   ├── DEEP_RESEARCH.md          # 5 Mindsets + 3 Controversies + 10 Questions
│   └── original/                 # 第 16 組原始提案存檔（proposal.md、簡報 PDF/PPTX）
├── research/
│   └── sources.md                # 16 篇已查證學術文獻與產業報告清單
├── data/
│   └── README.md                 # GUIDE 與 ExCyTIn-Bench 資料集放置指引與授權說明
├── experiments/
│   ├── e0_profile_guide.py       # GUIDE 資料集實測剖析腳本
│   └── results/
│       └── guide_train_profile.json # GUIDE 訓練集剖析產出結果
├── src/soc_agent/                # SOC Agent 原始碼目錄（規劃實作階段）
└── openspec/                     # OpenSpec 專案規範與 Active 變更管理
    ├── project.md                # 專案脈絡與技術堆疊定義
    ├── config.yaml               # OpenSpec 設定與 SDD 規則
    └── changes/
        └── refactor-ai-soc-agent-proposal/ # Active Change 工件
            ├── proposal.md       # Change 動機與範圍
            ├── design.md         # 系統技術設計
            ├── tasks.md          # 具體任務執行清單（1.1–6.2）
            └── specs/            # 5 大 Capabilities 形式化規格
```

---

## 六、如何驗證（How to Verify）

本專案所有規格與實測腳本皆可於本機環境重現與驗證：

### 1. 執行 OpenSpec 規格靜態校驗（Strict Validation）
確認所有規格檔案符合 RFC 2119 與 Gherkin 驗收語意：
```bash
npx @fission-ai/openspec validate refactor-ai-soc-agent-proposal --strict
```
> **輸出預期**：`Change 'refactor-ai-soc-agent-proposal' is valid`

### 2. 執行 GUIDE 資料集實測剖析腳本
驗證已完成之 Task 1.1 資料前處理與統計腳本：
```bash
python experiments/e0_profile_guide.py
```
> 輸出結構化分析指標（涵蓋 707,108 起事件、5,769 家企業組織、9,516,837 筆證據列），結果保存於 [`experiments/results/guide_train_profile.json`](experiments/results/guide_train_profile.json)。

### 3. 查驗文獻真實性與可連結性
查閱 [`research/sources.md`](research/sources.md) 與 [`docs/RELATED_WORK_REFACTOR.md`](docs/RELATED_WORK_REFACTOR.md)，所有 16 篇文獻皆附有可點擊之官方 DOI / arXiv URL，並通過原文比對確認。

---

## 七、專案進度：已完成與後續規劃（Progress & Roadmap）

### 已完成事項（DIC3 Proposal Refactor 階段）
- [x] **Phase 1**：專案環境初始化、目錄骨架建置、第 16 組原案存檔。
- [x] **Phase 2**：OpenSpec CLI 與 Antigravity 規格驅動開發環境設定。
- [x] **Phase 3**：Abstract A–F 結構重構與學術英文化（[`docs/ABSTRACT_REFACTOR.md`](docs/ABSTRACT_REFACTOR.md)）。
- [x] **Phase 4**：Deep Research 深化（5 Mindsets + 3 Controversies + 10 Questions）（[`docs/DEEP_RESEARCH.md`](docs/DEEP_RESEARCH.md)）。
- [x] **Phase 5**：系統設計與 OpenSpec Active Change 規格化（[`DESIGN.md`](DESIGN.md)、[`openspec/`](openspec/)）。
- [x] **Phase 6**：Introduction 重構、數據脈絡釐清、創新比較與貢獻確立（[`docs/INTRODUCTION_REFACTOR.md`](docs/INTRODUCTION_REFACTOR.md)）。
- [x] **Phase 7**：Related Work 16 篇文獻實測查核、比例平衡與文獻摘要表重構（[`docs/RELATED_WORK_REFACTOR.md`](docs/RELATED_WORK_REFACTOR.md)）。
- [x] **Phase 8**：DIC3 檢核表建立（[`docs/DIC3_CHECKLIST.md`](docs/DIC3_CHECKLIST.md)）、全專案連結檢核、OpenSpec 驗證與分支交付。

### 後續實作事項（期末專題實作階段，見 `tasks.md`）
- [ ] **Task 1.2**：Canonical 事件載入管道與 Pydantic 資料模型實作。
- [ ] **Task 2.1–2.2**：LightGBM/XGBoost 分級模型訓練與 TreeSHAP 特徵歸因引擎。
- [ ] **Task 3.1–3.2**：DuckDB 證據資料庫、唯讀 SQL 工具與 ReAct 調查 Planner。
- [ ] **Task 4.1–4.3**：Chroma MITRE ATT&CK STIX 2.1 向量知識庫與 NIST Playbooks。
- [ ] **Task 5.1–5.2**：多模態證據融合（Algorithm 2）與四大人工作業升級規則引擎。
- [ ] **Task 6.1–6.2**：雙格式（JSON/Markdown）審核報告產生器與 Streamlit 分析師儀表板。
- [ ] **全功能歸檔**：待上述功能均實作且通過端到端測試後，始執行 `openspec archive`。

---

## 八、版本控制與交付分支說明

- **工作與審查分支**：`dic3-refactor`
- **正式交付分支**：`main`（已合併最新 Refactor 成果）
- **作業檢核清單**：請參閱完整對照表 [`docs/DIC3_CHECKLIST.md`](docs/DIC3_CHECKLIST.md)。
