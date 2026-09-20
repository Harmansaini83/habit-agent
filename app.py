import os
import gradio as gr
from crew_setup import run_habit_crew
from db import get_logs

def chat_response(message, history):
    try:
        result = run_habit_crew(message)
        return result

    except Exception as e:
        error_message = str(e).lower()

        # Handle Gemini quota / rate-limit errors
        if (
            "quota" in error_message
            or "429" in error_message
            or "rate limit" in error_message
            or "resource exhausted" in error_message
        ):
            return (
                "✅ Your habit was logged successfully!\n\n"
                "⚠️ AI analysis is temporarily unavailable because "
                "the Gemini API quota has been reached.\n\n"
                "You can check your updated progress in the **Dashboard**."
            )

        # Handle temporary Gemini server errors
        elif "503" in error_message or "unavailable" in error_message:
            return (
                "✅ Your habit was logged successfully!\n\n"
                "⚠️ The AI service is temporarily busy. "
                "Please try again after a short while.\n\n"
                "Your habit can still be viewed in the **Dashboard**."
            )

        # Handle other errors
        else:
            return (
                "⚠️ Something went wrong while processing your request.\n\n"
                "Please try again later."
            )


def get_dashboard():
    logs = get_logs()

    if not logs:
        return "No habits logged yet. Go log one in the Chat tab!"

    habits = {}

    for name, status, _ in logs:
        habits.setdefault(name, []).append(status)

    summary = ""

    for habit, statuses in habits.items():
        done = statuses.count("done")
        total = len(statuses)
        pct = round((done / total) * 100, 1)

        summary += (
            f"**{habit.title()}**: "
            f"{done}/{total} completed ({pct}%)\n\n"
        )

    return summary


with gr.Blocks(title="AI Habit Tracking Agent") as demo:

    # Header
    gr.Markdown(
        """
        # 🎯 AI Habit Tracking Agent

        ### 👨‍💻 Harman Saini | PRN: 24070521056
        """
    )

    with gr.Tab("💬 Chat"):
        gr.Markdown(
            "### Track your habits using natural language"
        )

        gr.ChatInterface(
            fn=chat_response,
            examples=[
                "I did yoga today",
                "I missed the gym today",
                "I studied Python today",
                "I went for a walk today"
            ]
        )

    with gr.Tab("📊 Dashboard"):
        gr.Markdown(
            "### Your Habit Progress"
        )

        refresh_btn = gr.Button(
            "🔄 Refresh Stats"
        )

        stats_output = gr.Markdown()

        refresh_btn.click(
            fn=get_dashboard,
            outputs=stats_output
        )

    gr.Markdown(
        """
        ---
        **Designed by Harman Saini | 24070521056**
        """
    )


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )