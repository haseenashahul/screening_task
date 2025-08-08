# HASEENA S - TANDEMLOOP Screening Test Submission

##  Language Used
- **Python 3**

##  How to Run the Programs

To run each problem file, follow these steps:

### 1. Install Required Tools
Make sure you have the following installed:
- Python 3
- Visual Studio Code (VS Code)
- Code Runner extension in VS Code

> 💡 You can install Code Runner by searching in the **Extensions tab** (Ctrl + Shift + X) in VS Code, then search for **Code Runner** by Jun Han and click **Install**.

---

### 2. ▶️ Running the Code

Each problem is saved as a separate Python file:

To run a program:
1. Open the file (e.g., `Problem-1.py`) in VS Code.
2. Click the **"Run Code"** button in the top-right or use the shortcut:
3. Configure Code Runner to use Terminal
To make `input()` work (e.g., for user prompts), you need to run your code in the **integrated terminal**, not the output window.

#### 👉 Steps:
1. Press `Ctrl + Shift + P` → Select **Preferences: Open Settings (JSON)**
2. Add the following to your settings:

```json
"code-runner.runInTerminal": true,
"code-runner.executorMap": {
  "python": "python -u"
}
