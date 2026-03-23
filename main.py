from pathlib import Path

import questionary
import typer
from rich.console import Console
from rich.markdown import Markdown

import ollama_integration
import render
import transcript_pull

app = typer.Typer()


@app.command()
def generate(id: str):
    transcipt = transcript_pull.pull(id)
    ollama_integration.chat(transcipt)


@app.command()
def summarize():
    #    note = questionary.path("select").ask()
    vault = Path("/home/rishav/obsidian_notes")
    notes = [str(f) for f in vault.glob("**/*.md")]
    selected = questionary.select("Choose a note:", choices=notes).ask()
    summary = str(ollama_integration.summarize_note(selected))
    summary = Markdown(summary)
    console = Console()
    console.print(summary)


@app.command()
def hello():
    render.render()


if __name__ == "__main__":
    app()
