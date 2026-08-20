# 🧪 MCP Deadbugz Attack Simulator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A fully self-contained, local simulation of the **Deadbugz MCP supply-chain attack** disclosed by Pillar Security in August 2026. 

This repository demonstrates how a malicious MCP server can use a **runtime-gated metadata poisoning** technique to evade detection and exfiltrate sensitive data from AI agents.

> **⚠️ DISCLAIMER**: This code is for **educational and research purposes only**. It simulates a malicious attack in a controlled, local environment. Do not deploy this in production or use it against systems you do not own.

---

## 🧠 How the Attack Works

The attack exploits a dangerous assumption: that a tool's description is static after initial approval. 

1. **The Bait**: The server presents two benign tools (`format_text`, `summarize`).
2. **The Gate**: The server counts tool calls. For the first 3 calls, it behaves perfectly.
3. **The Switch**: On the **4th call**, the server fires the `tools/listChanged` notification.
4. **The Payload**: The tool descriptions mutate mid-session to credential-seeking instructions (SSH keys, AWS creds, K8s configs), instructing the AI to conceal the activity.

This `3-call gate` is a research-evasion technique that bypasses brief security reviews.

---

## 🗂️ Repository Structure
