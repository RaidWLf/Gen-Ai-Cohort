# 01: 🔑 Prompt Engineering Basics

This directory contains the code examples and materials for **Day 02** of the **GenAI Cohort**, focusing on different prompt engineering techniques and styles.

## 📅 Topics Learned (August 20, 2025)

### 1️⃣ Initial Tokens

-   ✍️ Writing simple prompts like: _"Write a code to add two numbers"_
-   🧑‍💻 Always try to use **humanly written prompts** instead of AI auto-generated prompts.

### 2️⃣ Types & Styles of Prompts

#### 🦙 Alpaca Prompt

-   📌 Format → **Instruction → Input → Response**
-   💡 Example: _Perform arithmetical operations on user input → 2 + 2 → 4_

#### 🦙➡️ LLaMA-2 INST Format

-   🏷️ Structure → `[INST] User Prompt [/INST]`
-   ⚙️ Supports **System Messages**: `<<SYS>> ... <</SYS>>`
-   💡 Example: `[INST] What is an LRU Cache ? [/INST]`

#### 🤖 ChatML (OpenAI)

-   📌 JSON-like role/content format.
-   💡 Example: `{role: "system", content: "You are an assistant"}`

### 3️⃣ Prompting Techniques

-   🎯 **Zero-Shot Prompting** → Model responds without any examples.
-   🎯 **Few-Shot Prompting** → Provide a few examples to guide the model.
-   ⚡ **System Prompt** → Defines initial context for the model (very important).
-   🙋 **User Prompt** → The actual query asked by the user.
-   🔗 **Chain of Thought** → Encourages step-by-step reasoning.
-   🔄 **Self-Consistency Prompting** → Generates multiple responses and selects the most consistent/common one.
    -   💡 Example Query: _Which is greater, 9.8 or 9.11?_
-   🧑‍🎭 **Persona-Based Prompting** → Model behaves like a specific person/character.

---

## 📝 Key Takeaways

-   🌟 Good prompts = Better outputs.
-   🔧 Different formats exist (Alpaca, INST, ChatML).
-   🧠 Techniques like **Chain of Thought** and **Self-Consistency** improve reasoning.
-   🎭 System & persona-based prompts help control the model’s behavior.

---
