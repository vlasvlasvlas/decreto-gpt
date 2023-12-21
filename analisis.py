import os
from dotenv import load_dotenv
import openai
import PyPDF2

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Ahora puedes acceder a las variables de entorno usando la función `os.getenv()`
api_key = os.getenv("API_KEY")
pdf_file = os.getenv("FILE_PDF")


# Configurar OpenAI
openai.api_key = api_key


def leer_pdf(ruta):
    with open(ruta, "rb") as pdf_file_obj:
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

        texto = ""

        # Utiliza len(pdf_reader.pages) en lugar de pdf_reader.numPages
        for num_pagina in range(len(pdf_reader.pages)):
            pagina = pdf_reader.pages[num_pagina]  # Utiliza pdf_reader.pages
            texto += (
                pagina.extract_text()
            )  # Utiliza extract_text() en lugar de extractText()

    return texto


# gpt-4-1106-preview
# gpt-3.5-turbo-1106
# gpt-3.5-turbo
# ai_model = 'gpt-3.5-turbo-1106'

ai_model = "gpt-4-1106-preview"


# Hacer una pregunta al texto
def hacer_pregunta(texto, pregunta):
    respuesta = openai.ChatCompletion.create(
        model=ai_model,
        messages=[
            {
                "role": "system",
                "content": "Estás analizando un decreto de necesidad de urgencia de la República Argentina. Comportate como el mejor analista económico-político de historia Argentina. Tenes que ser muy serio y preciso. Si hay algo que no sabes o no tenes la respuesta bien clara, tenés que decir que no lo sabes. Tu mirada sobre el tema debe ser neutra. Siempre que puedas, contextualizá tu respuesta.",
            },
            {"role": "user", "content": texto},
            {"role": "user", "content": pregunta},
        ],
    )
    return respuesta["choices"][0]["message"]["content"].strip()


#############

# Leer el PDF
ruta = pdf_file  # Reemplaza esto con la ruta a tu archivo PDF
texto = leer_pdf(ruta)

# Hacer una pregunta al texto!
pregunta = "¿Cuál es el tema principal del documento?"  # Reemplaza esto con tu pregunta
respuesta = hacer_pregunta(texto, pregunta)
print("Respuesta:", respuesta)
