# 🐍 Python AI Debugging Workflow: AI-Powered Code Optimization (Datacom Simulation)

**🔗 Dedicated Repository:** [github.com/lajordan09/python-ai-debugging-workflow](https://github.com/lajordan09/python-ai-debugging-workflow/tree/main)

![Status](https://img.shields.io/badge/Task_1-Completed-brightgreen)
![Status](https://img.shields.io/badge/Task_2-In_Progress-yellow)
![Status](https://img.shields.io/badge/Task_3-Upcoming-lightgrey)

This folder houses the documentation, source files, and architectural roadmaps for my participation in the **Datacom Automation AI Accelerator: From Co-pilot to Autonomous Agent** program on Forage. This simulation focuses on an advanced technical track—moving from hands-on, test-driven debugging up to macro-level autonomous system architecture.

---

## 🚦 Simulation Roadmap & Status

* **[COMPLETED] Task 1: AI-Powered Debugging and Refactoring (The "AI Pilot" Phase)**
  * *Objective:* Acted as a core developer utilizing conversational AI IDEs to execute root-cause analysis, perform test-driven development (TDD), and refactor inefficient legacy Python pipelines to meet strict enterprise performance SLAs.
* **[IN PROGRESS] Task 2: Process Automation Design & Flow Mapping (The "AI Architect" Phase)**
  * *Objective:* Translating complex client business requirements into visual, machine-executable process flows, focusing on continuous process improvement and logical automation mapping.
* **[UPCOMING] Task 3: Spec-Driven Development & Autonomous Agent Design (The "Business Strategist" Phase)**
  * *Objective:* Designing a comprehensive functional specification for an autonomous AI agent capable of orchestrating full development lifecycles and resolving end-to-end business challenges from scratch.

---

## 🎯 Core Technical Competencies Demonstrated (Task 1)

* **Algorithmic Optimization:** Diagnosed a legacy script (`process_data.py`) failing performance targets due to an $O(N^2)$ nested loop bottleneck. Successfully refactored the pipeline logic into a highly performant $O(N)$ linear-time execution model.
* **Test-Driven Development (TDD):** Engineered a dedicated, isolated unit testing suite (`test_cases.py`) using the Python `unittest` framework to reliably replicate production failures in a sandbox environment before deploying code modifications.
* **Root-Cause Analysis (RCA):** Parsed and diagnosed intermittent production script crashes by isolating data state failures within raw system tracebacks and error logs (`error.log`).
* **AI Prompt Engineering:** Maintained a transparent audit log (`DEBUG_LOG.md`) documenting specific context boundaries, system constraints, and prompt engineering sequences utilized with GitHub Copilot and Google Gemini.

---

## 🛠️ Tools & Technologies Used

* **Languages:** Python 3.x
* **Testing Architecture:** Python Standard Library `unittest` Framework
* **IDEs & AI Co-Pilots:** Visual Studio Code (VS Code), GitHub Copilot Chat, Google Gemini
* **Core Frameworks:** Test-Driven Development (TDD), Log Analytics, Algorithmic Complexity Management ($O(N)$ Scaling)

---

## 📂 Folder Architecture

To review the production codebase, tests, and prompt engineering logs, navigate to the dedicated repository or explore the folder structure below:

```text
job-simulations/python-ai-debugging/
├── process_data.py         # Original legacy script with algorithmic bottleneck
├── refactored_function.py  # Optimized linear-time production script ($O(N)$ efficiency)
├── test_cases.py           # Unit tests engineered to reproduce and isolate the bug
├── error.log               # Sample production log used for root-cause diagnosis
├── DEBUG_LOG.md            # Transparent journal tracking AI prompts and technical logic
└── README.md               # Main project documentation and overview
