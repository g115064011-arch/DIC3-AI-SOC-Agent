# AI SOC Analyst Agent (DIC3 Proposal Refactor)

> **DIC3 個人作業**：以 OpenSpec 規格驅動開發（Spec-Driven Development）進行專題 Proposal 重構與規格設計。  
> **專案主題**：結合 Machine Learning、MITRE ATT&CK、LLM Agent、SHAP 與資安領域知識的資安維運中心（SOC）智慧代理人。

---

## 專案來源與致謝（Original Team Attribution）

本專案沿用小組期末專題主題，並於個人 Repository 進行獨立研究深化、提案重構與 OpenSpec 規格設計。

- **原始小組專案**：[https://github.com/susuannie/proposal.git](https://github.com/susuannie/proposal.git)
- **原始專題作者**：期末專案第 16 組（Group 16）
  - 蘇恩平
  - 周妤
  - 袁靖淇
  - 蕭宥瑄
- **原始提案存檔**：[`docs/original/`](docs/original/)（包含原始 `proposal.md`、簡報 PDF 與 PPTX）

---

## 專題核心資訊

Agent 針對資安事件提供 **TP（True Positive） / BP（Benign Positive） / FP（False Positive）** 三級分級、ATT&CK 攻擊鏈對應與處置建議，每個結論皆附有可驗證的證據鏈；當信心度不足、結論衝突、高風險或證據不足時，主動交由分析師複核（Human-in-the-loop）。

### 系統核心架構

```
① 分析師 / 告警佇列 → ② 事件輸入 → ③ Planner & Reasoning Agent
   ↔ ④ 證據取得（事件資料、Log 查詢）
   ↔ ⑤ 分析引擎（分級模型、SHAP、相似事件）
   ↔ ⑥ 領域知識（MITRE ATT&CK、NIST SP 800-61 Rev. 3、D3FEND）
→ ⑦ 決策融合與升級判斷 → ⑧ 事件報告 / Dashboard
```

- **主資料集**：Microsoft GUIDE（真實 SOC 事件與分析師分級標籤）
- **評測基準**：ExCyTIn-Bench（LLM Agent 資安調查能力基準）
- **領域知識庫**：MITRE ATT&CK (v14/v15)、NIST SP 800-61 Rev. 3

---

## 專案目錄結構

```
DIC3-AI-SOC-Agent/
├── README.md
├── DESIGN.md                     # 系統設計總覽（含 OpenSpec Mapping）
├── docs/
│   ├── proposal.md               # 唯一正式 Proposal 版本
│   ├── OPEN_SPEC_GUIDE.md        # OpenSpec 指南與 SDD 工作流程說明
│   ├── ABSTRACT_REFACTOR.md      # Abstract A–F 重構紀錄
│   ├── DEEP_RESEARCH.md          # 5 Mindsets + 3 Controversies + 10 Questions
│   ├── INTRODUCTION_REFACTOR.md  # Introduction A–F 重構紀錄
│   ├── RELATED_WORK_REFACTOR.md  # Related Work 重構紀錄與文獻摘要表
│   ├── DIC3_CHECKLIST.md         # DIC3 作業檢核表
│   └── original/                 # 小組原始 proposal.md 與簡報存檔
├── research/
│   └── sources.md                # 已查證學術與產業來源
├── data/
│   └── README.md                 # 資料集說明與放置指引
├── experiments/
│   ├── e0_profile_guide.py       # GUIDE 資料檢查腳本（已實作）
│   └── results/                  # 實驗剖析輸出
├── src/soc_agent/                # SOC Agent 原始碼（後續實作階段）
└── openspec/                     # OpenSpec 專案規範與變更管理
    ├── project.md                # OpenSpec 專案脈絡設定
    ├── specs/                    # 系統規格庫
    └── changes/                  # Active Changes (refactor-ai-soc-agent-proposal)
```

---

## DIC3 作業進度與執行

詳細說明與 OpenSpec SDD 流程請參閱 [`docs/OPEN_SPEC_GUIDE.md`](docs/OPEN_SPEC_GUIDE.md)。

- **目前分支**：`dic3-refactor`
- **正式交付分支**：`main`（待確認後合併）
