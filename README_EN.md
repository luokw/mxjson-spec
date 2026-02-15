# MxJSON Protocol

> **MxJSON: A Universal Business Protocol for Enterprise AI Capability Packaging & Execution**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)]()

---

## What is MxJSON?

MxJSON is a **declarative AI business protocol** that packages prompts, workflows, and tool calls into standardized, portable, auditable, and monetizable capability assets (MXP).

**Core idea: Decouple business logic from execution environment.**

Like Docker decouples apps from OS, MxJSON decouples AI business logic from runtime engines. Build once, run anywhere.

---

## Why MxJSON?

| Capability | MxJSON | Traditional stacks |
|---|---|---|
| Human-in-the-loop | ✅ Native `human_review` node | ❌ Usually ad-hoc |
| Enterprise auditability | ✅ Native `audit` model | ❌ Extra custom layer needed |
| Commercialization-ready | ✅ Native `pricing` model | ❌ No standard pricing contract |
| Dynamic UI | ✅ Protocol-driven rendering | ❌ Front-end customization each time |

---

## 5-Minute Quick Start

### 1) Validate protocol artifacts

```bash
python scripts/validate_examples.py
```

### 2) Explore schema and examples

- Schema: [`schema/mxjson.schema.json`](./schema/mxjson.schema.json)
- Contract review example: [`examples/contract-review`](./examples/contract-review/)
- Translator example: [`examples/translator`](./examples/translator/)

### 3) Run with runtime engine (PHP)

```bash
composer require mxjson/runtime-php
```

```php
use MxJSON\Runtime;

$runtime = new Runtime();
$result = $runtime->execute('contract-review.mxjson', [
    'contract_text' => 'Your contract content...'
]);
```

---

## Quality & Validation

- JSON syntax checks are automated.
- Example-to-schema consistency checks are automated in CI.
- Local validation command:

```bash
python scripts/validate_examples.py
```

---

## Commercial & Ecosystem

- Commercialization and growth plan: [`mxjson新增.md`](./mxjson新增.md)
- Legal notice and licensing: [`LEGAL.md`](./LEGAL.md), [`LICENSE`](./LICENSE)

Contact: **luokongwei@gmail.com**

---

## Contributing

Contributions are welcome. See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

**If MxJSON helps your AI product roadmap, please star this repo ⭐**
