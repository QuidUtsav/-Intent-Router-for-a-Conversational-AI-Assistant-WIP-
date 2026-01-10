# 🧠 Intent Router for a Conversational AI Assistant (WIP)

This repository contains the **early brain of a Jarvis-style personal assistant** — an intent router that decides *how* the assistant should respond to user input.

Instead of blindly replying to everything like a chatbot, this system **classifies user intent** and routes queries to the appropriate capability (conversation vs information lookup).

> ⚠️ **Work in Progress**: This project is actively evolving. The current code represents an early but functional prototype. Major updates and extensions are planned.

---

## ✨ What This Project Does

Given a user input like:

* "Hi"
* "How are you?"
* "Who invented Python?"
* "Tell me about Nepal"

The system decides whether the user is:

* 💬 Engaging in **social conversation**, or
* 🔎 Requesting **factual information lookup**

This decision is made using a **hybrid approach**:

* Rule-based intent overrides (high confidence patterns)
* Zero-shot classification using a Hugging Face transformer model
* A confidence threshold with a safe fallback strategy

This is a foundational component of a larger assistant system.

---

## 🧩 Why This Matters

Most chatbot demos jump straight to text generation.

Real assistants (like Jarvis-style systems) need **decision-making layers**:

* Should I chat or search?
* Should I call a tool?
* Should I ask a clarification question?

This project focuses on **that missing layer** — the *intent routing brain*.

---

## 🏗️ Current Architecture

1. **Input normalization** (lowercasing)
2. **Rule-based intent detection** (greetings, thanks, question keywords)
3. **Zero-shot intent classification** using MNLI
4. **Confidence-based fallback** (defaults to search when uncertain)
5. **Explicit final decision output**

The system is designed to be:

* Deterministic
* Explainable
* Easy to extend

---

## 🤖 Model Used

* `typeform/distilbert-base-uncased-mnli`
* Zero-shot classification with semantic labels:

  * `social conversation`
  * `factual information lookup`

The model choice prioritizes:

* Simplicity
* Interpretability
* Rapid prototyping

---

## 🚧 Current Limitations (By Design)

* No real search engine integration yet
* No memory or multi-turn context
* Keyword matching is substring-based
* Not optimized for edge cases

These are **intentional** — the focus is on building a solid core before scaling.

---

## 🛣️ Planned Updates

* 🔌 Plug in a real search backend (Wikipedia / web search)
* 🧠 Add more intent classes (tasks, commands, clarifications)
* 🧾 Improve rule system (token-aware / regex-based)
* 🔄 Multi-turn intent refinement
* 🤖 Integration into a full conversational assistant

This repository will evolve step by step.

---

## 🎯 Long-Term Vision

This project is part of a larger goal:

> Building a **Jarvis-like intelligent assistant** — capable of reasoning, tool use, and natural interaction.

This intent router is the **first cognitive layer** of that system.

---

## 🧑‍💻 About the Author

Computer Engineering student with a focus on:

* Natural Language Processing
* Applied AI systems
* Assistant and agent architectures

Built as part of a long-term, project-based NLP journey.

---

## ⭐ Status

🟡 **Active Development**
Expect breaking changes, refactors, and new features.

Feedback, ideas, and discussions are welcome.

---

> *This is not a finished product — it’s a system growing in public.*
