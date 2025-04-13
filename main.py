import marimo

__generated_with = "0.12.4"
app = marimo.App(width="medium")


@app.cell
def _():
    from agno.agent import Agent
    from agno.models.google import Gemini
    return Agent, Gemini


@app.cell
def _(Agent, Gemini):
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash-thinking-exp-01-21"),
        tools=[],
        instructions=[
            "Show data in list format"
        ],
        markdown=True,
    )

    return (agent,)


@app.cell
def _(agent):
    agent.print_response("Which are the 10 best cities in Europe?")
    return


if __name__ == "__main__":
    app.run()
