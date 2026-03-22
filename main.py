import typer
import ollama_integration
import transcript_pull
import questionary
import render

app = typer.Typer()

@app.command()
def generate(id: str):
    transcipt = (transcript_pull.pull(id))
    ollama_integration.chat(transcipt)

@app.command()
def summarize():
    note = questionary.path("select").ask()
    ollama_integration.summarize_note(note)

@app.command()
def hello():
    render.render()    

if __name__ == "__main__":
    app()
