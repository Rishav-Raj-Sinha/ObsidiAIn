import typer
import transcript_pull
import ollama_integration

def generate(id: str):
    transcript = (transcript_pull.pull(id))
    (ollama_integration.chat(transcript))

if __name__ == "__main__":
    typer.run(generate)
