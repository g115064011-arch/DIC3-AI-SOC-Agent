# OpenSpec 與規格驅動開發（SDD）指南

> **專案**：AI SOC Analyst Agent — DIC3 Proposal Refactor  
> **文件版本**：1.0.0  
> **適用環境**：Google Antigravity / OpenSpec CLI 1.17.0+  

---

## 一、什麼是規格驅動開發（Spec-Driven Development, SDD）？

**規格驅動開發（Spec-Driven Development, SDD）** 是一種以「形式化、可驗證、機器可讀且人類可審查的規格（Specification）」作為核心驅動力的軟體工程典範。

### 傳統開發與 AI 輔助開發的痛點
在傳統開發或純 Prompt-based 的 AI 輔助開發（Prompt-and-Pray）中，工程師常面臨以下挑戰：
1. **規格漂移（Spec Drift）**：系統實作與原始 Proposal 或 Design 漸行漸遠，文檔與程式碼脫節。
2. **AI 幻覺與過度承諾（Hallucination & Scope Creep）**：AI 代理人容易在對話中自由發揮，產出與架構設計不符或未經論證的程式碼。
3. **驗證缺乏客觀標準**：缺乏可機器校驗（Machine-verifiable）的需求場景，導致測試與驗收依賴人工主觀判斷。

### SDD 的核心原則
SDD 將**規格視為第一公民（First-Class Citizen）**：
- **規格先於實作（Spec Before Code）**：在撰寫任何實作程式碼之前，先以結構化的 RFC 形式定義明確需求與驗收場景。
- **可驗證性（Verifiability）**：每條需求（Requirement）必須使用 RFC 2119 規範（如 `SHALL`、`MUST`），並搭配明確的行為場景（`Scenario: WHEN ... THEN ...`）。
- **變更即規格差異（Change as Spec Delta）**：每次系統演進都以「變更（Change）」的形式發起，明確標記新增（`ADDED`）、修改（`MODIFIED`）或移除（`REMOVED`）的需求。

---

## 二、OpenSpec 如何幫助本專題？

本專案的主題為 **AI SOC Analyst Agent**，致力於結合機器學習（GUIDE 資料集）、MITRE ATT&CK 知識圖譜、SHAP 可解釋特徵、LLM Planner 證據推理與人機協同（Human-in-the-loop），打造專業的資安維運中心輔助分析代理人。

在高度重視風險與精確性的資安維運（SOC）領域，OpenSpec 為本專案帶來以下關鍵價值：

1. **嚴謹的資安責任邊界**：
   SOC 面臨「非對稱錯誤成本（Asymmetric Error Cost）」——漏報（False Negative）的代價遠高於誤報（False Positive）。透過 OpenSpec 定義明確的決策規格，強制 Agent 在低信心、高風險或證據不足時啟動升級機制（SHALL escalate to human analyst），避免 AI 擅自採取高風險自動處置。
2. **多模組協同契約（Contract-first Architecture）**：
   本系統包含 ①～⑧ 個核心模組（分級、檢索、推理、知識庫整合、升級決策、可解釋報告等）。OpenSpec 的 Capability Specs（例如 `incident-triage`、`evidence-retrieval`、`domain-knowledge-reasoning` 等）建立了跨模組的資料與行為契約，杜絕接口不合與邏輯矛盾。
3. **學術提案與系統實作的一致性**：
   將 Proposal 與 `DESIGN.md` 中的設計藍圖轉化為可被靜態校驗（`openspec validate`）的工程規格，確保研究構想能無縫銜接至後續的程式碼實作。

---

## 三、Proposal、Specs、Design、Tasks 的本質差異

OpenSpec 將變更拆解為四個職責分明的工件（Artifacts），各司其職且互為支撐：

| 工件 (Artifact) | 核心回答的問題 | 焦點與層次 | 包含內容範例 |
|---|---|---|---|
| **Proposal** (`proposal.md`) | **Why** & **What changes** | 商業/研究目標、動機、背景與痛點 | 研究動機、現有方案限制、預期研究效益、範圍（Scope）。 |
| **Design** (`design.md`) | **How (Architecture)** | 技術架構、系統架構、元件關係與折衷決策 | 系統架構 ①～⑧ 模組、資料流圖、Mermaid 流程圖、演算法 Pseudocode、技術選型決策。 |
| **Specs** (`specs/<capability>/spec.md`) | **What the system SHALL do** | 系統行為契約、精確功能規範與驗收條件 | 使用 `SHALL`/`MUST` 敘述之 Requirement，以及 `WHEN... THEN...` 驗收情境（Scenario）。 |
| **Tasks** (`tasks.md`) | **How to implement & verify** | 具體工程執行清單與驗證步驟 | 檔案修改清單、逐步實作內容、單元/整合測試指令、狀態（Already Implemented / Planned）。 |

---

## 四、OpenSpec 的標準生命週期工作流程

OpenSpec 採用標準的四階段生命週期：

```
+-----------+     +------------+     +----------+     +-----------+
|  Propose  | --> |  Validate  | --> |  Apply   | --> |  Archive  |
+-----------+     +------------+     +----------+     +-----------+
  建立變更提案       嚴格語法校驗       實作與測試       歸檔合流規格
```

### 1. Propose（提案階段）
- **指令**：在 IDE 中執行 `/opsx-propose "change-name"` 或使用 CLI。
- **產出**：在 `openspec/changes/<change-name>/` 目錄下建立變更提案骨架，包含 `proposal.md`、`design.md`、`tasks.md` 與能力規格目錄 `specs/<capability>/spec.md`。
- **原則**：明確定義變更動機與需求增減（`ADDED Requirements`）。

### 2. Validate（校驗階段）
- **指令**：
  ```bash
  openspec validate <change-name> --strict
  ```
- **目的**：執行語意與結構靜態檢查，確保：
  - 需求符合 RFC 2119 規範（必含 `SHALL` 或 `MUST`）。
  - 每個 Requirement 皆包含至少一個可驗證的 Scenario（`WHEN` / `THEN`）。
  - 各工件之結構與 OpenSpec Schema 完全一致。

### 3. Apply（套用/實作階段）
- **指令**：在 IDE 中執行 `/opsx-apply`。
- **目的**：開發者或 AI Agent 根據 `tasks.md` 列出的具體任務，逐步實作原始碼、撰寫測試並驗證執行結果，實作完成後將任務狀態標記為完成。

### 4. Archive（歸檔階段）
- **指令**：在 IDE 中執行 `/opsx-archive` 或 `openspec archive <change-name>`。
- **目的**：當 `tasks.md` 中所有項目皆已實作且驗收通過，將該變更移動至 `openspec/changes/archive/`，並自動將該變更的規格 Delta 同步（Sync）併入全域規格庫 `openspec/specs/` 中，成為系統當前最新的單一事實來源。

---

## 五、本專題為何在 DIC3 階段「暫不執行 Archive」？

在 DIC3 作業階段中，明確規定 **禁止執行 `openspec archive`**，原因如下：

1. **專案處於 Proposal 與規格藍圖階段**：
   DIC3 的核心目標是「Proposal Refactor 與 OpenSpec 規格規劃」，而非完整 AI 系統與模型的實作部署。
2. **符合 SDD 的真確性原則**：
   在 OpenSpec 架構中，一旦變更被 `archive`，其內含的 Delta Specs 就會被視為**已在系統中實現的全域正式規格**。如果將尚未撰寫程式碼、尚未訓練完成的規格強制歸檔，將違反規格與實作一致性的原則，造成「虛假實作（Phantom Implementation）」。
3. **保持 Change 處於 Active 狀態以供追蹤**：
   將變更維持在 `openspec/changes/refactor-ai-soc-agent-proposal/` 的 Active 狀態，能夠清楚呈現該變更對應的研究動機、架構設計與尚未完成的任務清單（`Planned`）。
4. **未來正式實作完成後的 Archive 流程**：
   待後續期末專案開發階段，完成以下要件後始得進行歸檔：
   - 完成資料集載入與特徵工程管道。
   - 完成 GUIDE ML 模型訓練與 SHAP 解釋器。
   - 建立 MITRE ATT&CK 檢索模組與 LLM Planner。
   - 執行並通過所有單元測試與端到端評測。
   - 依序更新 `tasks.md` 狀態，執行：
     ```bash
     openspec validate refactor-ai-soc-agent-proposal --strict
     openspec archive refactor-ai-soc-agent-proposal
     ```

---

## 六、本機環境實際安裝資訊與 Init 輸出摘要

### 1. 執行環境資訊
- **作業系統**：Windows 11 (64-bit)
- **Node.js**：`v22.14.0`（符合官方要求 Node.js ≥ 20.19.0）
- **npm**：`10.9.2`
- **Python**：`3.14.7`
- **Git**：`2.55.0.windows.5`
- **OpenSpec CLI**：`1.17.0`（套件：`@fission-ai/openspec@latest`）

### 2. 初始化指令與參數
在專案根目錄下以非互動模式執行初始化，並指定支援 Google Antigravity：
```bash
openspec init --tools antigravity --no-animation
```

### 3. 初始化輸出摘要
```text
- Creating OpenSpec structure...
▌ OpenSpec structure created
- Setting up Antigravity...
√ Setup complete for Antigravity

OpenSpec Setup Complete

Created: Antigravity
6 skills and 6 commands in .agents/
Config: openspec/config.yaml (schema: spec-driven)

Getting started:
  Start your first change: /opsx-propose "your idea"
```

### 4. 產生之檔案結構
初始化成功建立以下檔案與目錄：

```text
DIC3-AI-SOC-Agent/
├── .agents/
│   ├── skills/
│   │   ├── .openspec-target
│   │   ├── openspec-apply-change/SKILL.md
│   │   ├── openspec-archive-change/SKILL.md
│   │   ├── openspec-explore/SKILL.md
│   │   ├── openspec-propose/SKILL.md
│   │   ├── openspec-sync-specs/SKILL.md
│   │   └── openspec-update-change/SKILL.md
│   └── workflows/
│       ├── opsx-apply.md
│       ├── opsx-archive.md
│       ├── opsx-explore.md
│       ├── opsx-propose.md
│       ├── opsx-sync.md
│       └── opsx-update.md
└── openspec/
    ├── config.yaml
    ├── specs/
    │   └── .gitkeep
    └── changes/
        └── archive/
            └── .gitkeep
```
