# MxJSON Protocol

> **MxJSON: A Universal Business Protocol for Enterprise AI Capability Packaging & Execution**
> 
> 面向企业级 AI 能力封装与执行的万能业务协议

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)]()

---

[English Version](./README_EN.md)

## 🎯 What is MxJSON?

MxJSON 是一种**声明式 AI 业务协议**，它将 AI 能力（提示词、工作流、工具调用）封装为**可移植、可定价、可审计**的标准化资产包（MXP）。

**核心理念：逻辑与环境解耦**

就像 Docker 将应用与操作系统解耦一样，MxJSON 将 AI 业务逻辑与执行引擎解耦。一次编写，随处执行。

---

## 🏆 Why MxJSON? (四大核心壁垒)

| 特性 | MxJSON | 传统方案 (Dify/Coze/GPTs) |
|------|--------|--------------------------|
| **确定性人机协作** | ✅ 内置 `human_review` 节点，精准控制人工介入点 | ❌ 黑盒流程，难以嵌入审批 |
| **企业级审计** | ✅ 原生 `audit` 支持，敏感字段自动脱敏 | ❌ 需额外开发审计层 |
| **商业化就绪** | ✅ 内置 `pricing` 计费逻辑，人人可卖 AI 能力 | ❌ 无标准化定价机制 |
| **动态 UI 渲染** | ✅ 协议驱动界面，无需前端开发 | ❌ 每个场景需定制开发 |

---

## 📦 MXP Package Structure (资产包规范)

```
my-capability.mxp/
├── manifest.mxjson      # 能力声明文件
├── prompts/             # 提示词资产
├── tools/               # 工具定义
├── schemas/             # 数据结构
└── ui/                  # 界面配置
```

---

## 🚀 Quick Start

### 1. 安装运行时引擎

```bash
composer require mxjson/runtime-php
```

### 2. 执行一个 MxJSON 能力包

```php
use MxJSON\Runtime;

$runtime = new Runtime();
$result = $runtime->execute('contract-review.mxjson', [
    'contract_text' => '合同内容...'
]);
```

---

## 📚 Documentation

- [完整协议规范 v1.0](./docs/spec_v1.0.md) - 21 章详细规范
- [JSON Schema 定义](./schema/mxjson.schema.json)
- [示例：合同审核](./examples/contract-review/)
- [示例：智能翻译](./examples/translator/)
- [商业化升级与增长规划](./mxjson新增.md)
- [English README](./README_EN.md)

---


## ✅ Quality & Validation

```bash
python scripts/validate_examples.py
```

该命令会校验示例与协议 Schema 的一致性（本地安装了 `jsonschema` 时走完整校验）。

---

## 💼 Commercial Licensing

**协议规范 (Schema & Docs)**: MIT License - 完全开源

**企业版引擎**: 以下场景需商业授权：
- 企业私有化部署
- 高并发执行引擎
- 深度行业方案包（法律版、医疗版等）

📧 商业咨询：luokongwei@gmail.com

---

## 📜 Legal

**Software Copyright Registration Number**: 2026R11L0140169;2026R11L0140165

本协议规范及核心实现已完成中国软件著作权登记。

详见 [LEGAL.md](./LEGAL.md)

---

## 🤝 Contributing

欢迎贡献代码和能力包！请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 📈 Roadmap

- [x] v1.0.0 - 核心协议规范发布
- [ ] v1.1.0 - Python 运行时引擎
- [ ] v1.2.0 - Node.js 运行时引擎
- [ ] v2.0.0 - 可视化编排器

---

## 🌟 Why This Project Is Star-worthy

- **可执行规范**：不仅有文档，还有可校验 JSON Schema 与完整示例能力包。
- **面向商业变现**：原生 `pricing`、`audit`、`human_review`，可直接用于企业交付。
- **跨运行时架构**：协议层稳定后可快速扩展到 PHP / Node.js / Python 等多引擎。

如果你也在做企业 AI Agent、工作流产品、AI 应用市场，欢迎 Star 与共建。

---

*MxJSON - Standardizing AI Capabilities for the Enterprise*

**Star ⭐ this repo if you find it useful!**
