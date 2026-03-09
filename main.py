from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Habilitar CORS (ajusta allow_origins en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir el frontend: index.html en la raíz y archivos estáticos en /static
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/", StaticFiles(directory=".", html=True), name="root")

from google import genai
client = genai.Client()


@app.get("/LM/{promt}")
async def read_root(promt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=promt,
    )
    return {"Respuesta": response.text}


