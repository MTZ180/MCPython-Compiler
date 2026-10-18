# 🚀 MCPython Compiler

A modular, terminal-based compiler designed to support Redstone CPUs in Minecraft. The compiler is planned to take a high-level programming language named **MCPython** and convert it across various layers and formats, down to physical hardware representations or block schematics.

---

## 📌 Project Purpose

This project was born to bridge the gap between high-level software development and executing code on Redstone CPUs inside Minecraft.

The compiler is designed around a **strict separation of concerns (Modular Architecture)**: code is not compiled in a single monolithic pass, but rather flows through a chain of dedicated **Transformers**. Each transformer is responsible for a single conversion step from one strictly defined format to another. This separation provides maximum flexibility, clean maintainability, and seamless future extensibility.

### ⚙️ CPU Support & Future Expansion
* The compiler is planned to initially support the **`MTZ-8bit-001-CPU`** Redstone processor and its custom Instruction Set Architecture (ISA).
  * *Note:* The physical construction of the CPU in Minecraft is currently in progress. Once completed, a full schematic alongside a detailed ISA spreadsheet will be published here.
* In the future, the compiler is planned to support additional Redstone CPUs and varying instruction sets.
* Furthermore, a **Plugin Architecture** is planned to allow users to build custom modules, making it easy to adapt the compiler to any unique Redstone CPU design.

---

## 🏗️ Architecture & Pipeline

The compiler splits the transformation process into Visible Layers and Hidden Layers (intermediate representations) linked together by dedicated Transformers:

### 🔷 Layers
* **Visible Layers:**
  * **MCPython code:** High-level source code.
  * **Assembly code:** Human-readable assembly code.
  * **Hexadecimal:** Base-16 code representation.
  * **Binary:** Machine-level binary representation.
  * **Schem:** Minecraft block schematic file (`.schem`).
* **Hidden Layers (Intermediate Representations):**
  * **MCPython tokens:** Tokens produced after parsing MCPython code.
  * **Assembly tokens:** Tokens representing target assembly instructions.

---

### 🔄 Transformers

* **`A`:** Converts **MCPython code** to **MCPython tokens**.
* **`B`:** Converts **MCPython tokens** to **Assembly tokens**.
* **`C1`:** Bidirectional converter between **Assembly tokens** and **Assembly code**.
* **`C2`:** Bidirectional converter between **Assembly tokens** and **Binary**.
* **`D1`:** Converts **Binary** to **Schem** (Minecraft schematic file).
* **`D2`:** Bidirectional converter between **Binary** and **Hexadecimal**.

---

### ⚙️ Supported Conversion Modes

Thanks to the decoupled transformer pipeline, the system can perform various multi-step conversions:

* **`M2A`:** MCPython to Assembly code (`A > B > C1`)
* **`M2B`:** MCPython to Binary (`A > B > C2`)
* **`M2S`:** MCPython to Schem schematic file (`A > B > C2 > D1`)
* **`M2H`:** MCPython to Hexadecimal (`A > B > C2 > D2`)
* **`A2B`:** Assembly code to Binary (`C1 > C2`)
* **`A2S`:** Assembly code to Schem schematic file (`C1 > C2 > D1`)
* **`A2H`:** Assembly code to Hexadecimal (`C1 > C2 > D2`)
* **`B2A`:** Binary to Assembly code (`C2 > C1`)
* **`B2S`:** Binary to Schem schematic file (`D1`)
* **`B2H`:** Binary to Hexadecimal (`D2`)
* **`H2B`:** Hexadecimal to Binary (`D2`)
* **`H2S`:** Hexadecimal to Schem schematic file (`D2 > D1`)
* **`H2A`:** Hexadecimal to Assembly code (`D2 > C2 > C1`)

---

## 💻 User Interface (Terminal / Interactive Console)

The compiler is designed to run directly from the Terminal / Shell. The initial planned interface is an interactive console inspired by the Python REPL (featuring a `<<<` prompt) where commands can be entered to trigger transformations. In future versions, this is planned to upgrade into a full Command Line Interface (CLI) supporting flags and arguments directly from the command line.

*(Note: Detailed error reporting and debugging mechanisms are planned for future releases).*

---

## 🐍 The MCPython Language

**MCPython** is planned to be a high-level programming language tailored for writing programs for Redstone CPUs. It features a clean, readable, **Python-like syntax**.

MCPython is specifically designed to work within the constraints and characteristics of hardware processors and Redstone logic. The full syntax specification and documentation will be published in a separate document as development progresses.

---

## 🙏 Acknowledgements

* **Mattbatwings:** A huge thank you to the content creator and YouTuber Mattbatwings! His amazing videos, tutorials, and explanations on Redstone logic and building computers inside Minecraft provided the essential knowledge needed to design this CPU and compiler.  
  YouTube Channel Link: https://www.youtube.com/@mattbatwings
* **Python & Python Software Foundation:** Thank you to the Python team and community for creating a wonderful programming language that serves as the inspiration for MCPython's syntax and design.
* **Minecraft & Mojang Studios:** Thank you to Mojang Studios and Microsoft for creating Minecraft, providing a rich sandbox for research, engineering, and Redstone CPU development.
* **Future Plugin & Mod Developers:** Thank you in advance to all future developers and creators who will build plugins, modules, and extensions for this compiler and various Redstone processors — and to those reading this in hopes of joining their ranks!

---

## ⚠️ Legal Disclaimer

**Independence from Python:**
* **MCPython** and this project are **NOT** an official Python product, are **NOT** part of Python, and are not affiliated with, sponsored, endorsed, or approved by the **Python Software Foundation (PSF)**.
* The name **MCPython** is a portmanteau of *Minecraft* and *Python*, intended solely to describe a language with a Python-like syntax designed for Minecraft environments.
* All compiler code, transformers, and parsers are planned to be written completely from scratch independently.
* **Python®** is a registered trademark of the Python Software Foundation.

**Independence from Minecraft:**
* This project is **NOT** an official Minecraft product, and is not affiliated with, sponsored, endorsed, or approved by **Mojang Studios** or **Microsoft Corporation**.
* **Minecraft®** is a registered trademark of Mojang Synergies AB / Microsoft.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

*As of October 18, 2026.*