# Your First Autonomous AI Agent (CrewAI + Google Gemini)

A beginner-friendly **Research Analyst** agent. It reads a web page on its own, decides what
matters, and writes a summary file - no complex code.

## What you need
- Python **3.10 to 3.13** (CrewAI requirement) - check with `python3 --version`
- A **free** Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

## Steps
```bash
git clone https://github.com/aakash0780/first-ai-agent-crewai-gemini.git
cd first-ai-agent-crewai-gemini
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # Windows: copy .env.example .env
# open .env and paste your key after GEMINI_API_KEY=
python research_agent.py
```
Your summary appears in `output/summary.md`.

## How it works
| Part | In the code | Meaning |
|---|---|---|
| Brain | `LLM(model="gemini/...")` | The language model that thinks and decides |
| Tools | `ScrapeWebsiteTool`, `FileWriterTool` | What the agent can *do*: read a page, write a file |
| Agent | `role`, `goal`, `backstory` | Who it is and what it is trying to achieve |
| Task | `description`, `expected_output` | The job and what "done" looks like |
| Crew | `crew.kickoff()` | Runs the agent's loop: think -> use a tool -> observe -> repeat |

## Common problems
- **`GEMINI_API_KEY is missing`** - create `.env` from `.env.example` and add your key.
- **429 / quota errors** - the free tier has limits; wait and try again later.
- **Model not found** - model names change; pick a current Flash model in AI Studio and set
  `GEMINI_MODEL=gemini/<model-name>` in `.env`.
- **Agent keeps looping** - `max_iter=5` stops it; make the task description more specific.

## Safety
Never commit your `.env` file (it is in `.gitignore`). The agent only uses facts from the page,
but always check its output - AI models can still make mistakes.

Sources: [CrewAI installation](https://docs.crewai.com/en/installation) ·
[CrewAI LLMs (Gemini)](https://docs.crewai.com/en/concepts/llms) ·
[Agents](https://docs.crewai.com/en/concepts/agents) · [Tasks](https://docs.crewai.com/en/concepts/tasks) ·
[ScrapeWebsiteTool](https://docs.crewai.com/en/tools/web-scraping/scrapewebsitetool) ·
[FileWriterTool](https://docs.crewai.com/en/tools/file-document/filewritetool)

## Example output
`example_output/summary.md` is the real file the agent wrote in our demo run (2026-10-10).

## Video
Built step by step on the **AI Agents Pro** YouTube channel.

## License
MIT - see `LICENSE`.
