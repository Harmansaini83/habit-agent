import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from tools import log_habit_tool, analyze_habit_tool
from db import init_db

load_dotenv()
init_db()

gemini_llm = LLM(
    model="gemini/gemini-3.6-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

logger_agent = Agent(
    role="Habit Logger",
    goal="Extract the habit name and status (done/missed) from the user's message and log it accurately",
    backstory="You are meticulous about correctly identifying habits and whether they were completed.",
    tools=[log_habit_tool],
    llm=gemini_llm,
    verbose=True
)

analyst_agent = Agent(
    role="Habit Analyst",
    goal="Calculate accurate streaks and completion statistics for the logged habit",
    backstory="You are a data analyst specializing in behavior pattern tracking.",
    tools=[analyze_habit_tool],
    llm=gemini_llm,
    verbose=True
)

coach_agent = Agent(
    role="Motivational Coach",
    goal="Give short, personalized, encouraging feedback based on habit statistics",
    backstory="You are a supportive coach who keeps feedback short, positive, and specific.",
    llm=gemini_llm,
    verbose=True
)

def run_habit_crew(user_input: str) -> str:
    log_task = Task(
        description=f"From this message: '{user_input}', extract the habit name and status (done/missed), then log it using your tool.",
        expected_output="Confirmation of what habit and status was logged.",
        agent=logger_agent
    )

    analyze_task = Task(
        description="Using the habit name identified in the previous task, analyze its streak and completion % using your tool.",
        expected_output="Stats: total logs, completion percentage, current streak.",
        agent=analyst_agent,
        context=[log_task]
    )

    coach_task = Task(
        description="Based on the stats from the previous task, write a short 2-3 sentence motivational message.",
        expected_output="A short, encouraging, personalized message for the user.",
        agent=coach_agent,
        context=[analyze_task]
    )

    crew = Crew(
        agents=[logger_agent, analyst_agent, coach_agent],
        tasks=[log_task, analyze_task, coach_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return str(result)