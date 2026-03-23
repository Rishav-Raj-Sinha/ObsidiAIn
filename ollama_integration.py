from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM


def chat(transcript: str):
    prompt = PromptTemplate(
        template="generate a summary in markdown format for the given transcript : {transcript} ",
        input_variables=["transcript"],
    )

    model = OllamaLLM(model="phi4-mini:3.8b")

    chain = prompt | model

    result = chain.invoke({"transcript": transcript})

    try:
        with open("file.md", "x", encoding="utf-8") as f:
            f.write(result)
            print("file created")

    except FileExistsError:
        print("file.txt already exists, exclusive creation aborted.")


def summarize_note(note: str):
    with open(note, "r") as file:
        note_content = file.read()
    prompt = PromptTemplate(
        template="generate a summary in markdown format for the given note focus on the most important parts and give proper headings and titles : {note_content} ",
        input_variables=["note_content"],
    )

    model = OllamaLLM(model="phi4-mini:3.8b")

    chain = prompt | model

    result = chain.invoke({"note_content": note_content})
    return result
    # print(result)
