from fastapi import FastAPI

app = FastAPI()


@app.get("/LM/{promt}")
async def read_root(promt):
    from google import genai
    from dotenv import load_dotenv

    client = genai.Client()
    load_dotenv()

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=promt,
    )

    print(response.text)
    return {"Respuesta": response.text}


