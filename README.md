# agentchat-streamlit

About
-----

A lightweight Streamlit-based wrapper for conversational agents. This project demonstrates a simple agent architecture (in `agent.py`) with a Streamlit frontend (`main.py`) so you can prototype chat-style workflows locally. It uses environment configuration via `python-dotenv` and YAML for config where needed.

Key technologies: Python, Streamlit, python-dotenv, PyYAML

Small Python project containing `agent.py` and `main.py`.

## Quick start

1. Install Python 3.10+ and create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # zsh/bash
```

2. Install dependencies:

- If your project has a `requirements.txt`, run:

```bash
pip install -r requirements.txt
```

- Otherwise install common dependencies used by this project:

```bash
pip install python-dotenv PyYAML streamlit
```

3. Run the app:

- If this is a Streamlit app:

```bash
streamlit run main.py
```

- Otherwise run directly with Python:

```bash
python main.py
```

## Files

- `main.py` - application entrypoint
- `agent.py` - agent-related code
- `.gitignore` - ignores build artifacts and environment files

## Troubleshooting

- "Import 'dotenv' could not be resolved": install `python-dotenv` (see step 2).
- "Import 'yaml' could not be resolved": install `PyYAML`.
- "Import 'autogen_agentchat.agents' could not be resolved": confirm the correct package name and install it, or ensure the module is available in your workspace or virtual environment.
- If VS Code still reports unresolved imports, make sure the Python interpreter points to the virtual environment (`.venv`) in the bottom-left of VS Code.

## Notes

- Add a `requirements.txt` when you have a fixed set of dependencies.
- Consider adding a `LICENSE` and more detailed docs if you plan to publish the project.

