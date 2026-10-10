"""Your first autonomous AI agent: a Research Analyst built with CrewAI + Google Gemini.

What it does, on its own:
  1. reads a web page with a scraping tool,
  2. decides what matters,
  3. writes a clear summary to output/summary.md with a file-writing tool.

Setup (see README.md):
  python -m venv .venv
  source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
  pip install -r requirements.txt
  copy .env.example to .env and paste your free Gemini API key
  python research_agent.py
"""

import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai_tools import FileWriterTool, ScrapeWebsiteTool
from dotenv import load_dotenv

# 1. Load your Gemini API key from the .env file (never hard-code keys).
load_dotenv()
if not os.getenv("GEMINI_API_KEY"):
    raise SystemExit(
        "GEMINI_API_KEY is missing. Copy .env.example to .env and add your key."
    )

# 2. The brain: a free Gemini model.
#    Check aistudio.google.com for current model names.
llm = LLM(model=os.getenv("GEMINI_MODEL", "gemini/gemini-3.8-flash"), temperature=0.3)

# 3. The tools: one to read a web page, one to write a file.
PAGE_URL = os.getenv("PAGE_URL", "https://docs.crewai.com/en/introduction")
scrape_tool = ScrapeWebsiteTool(website_url=PAGE_URL)
write_tool = FileWriterTool()

# 4. The agent: a role, a goal and a backstory.
researcher = Agent(
    role="Research Analyst",
    goal="Read the given web page and explain its key ideas for complete beginners",
    backstory=(
        "You are a patient teacher who turns technical pages into short, accurate notes. "
        "You only use facts found on the page and never invent anything."
    ),
    tools=[scrape_tool, write_tool],
    llm=llm,
    max_iter=5,  # safety limit so the agent cannot loop forever
    verbose=True,  # print the agent's thinking and tool use
)

# 5. The task: what to do and what the result should look like.
summary_task = Task(
    description=(
        f"Use the scraping tool to read {PAGE_URL}. "
        "Then write a beginner-friendly summary with a one-line definition "
        "and five bullet points. Save it with the file writer tool "
        "as filename 'summary.md' in directory 'output'."
    ),
    expected_output=(
        "A markdown summary saved to output/summary.md, "
        "plus the same text as your answer."
    ),
    agent=researcher,
)

# 6. The crew runs the task and the agent works autonomously until it is done.
crew = Crew(
    agents=[researcher],
    tasks=[summary_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n=== FINAL ANSWER ===\n")
    print(result)
