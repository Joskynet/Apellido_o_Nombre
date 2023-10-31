from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv("environment.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detectar', methods=['POST'])
def detectar():
    palabra = request.form['palabra']
    resultado = detectar_nombre_o_apellido(palabra)
    return render_template('result.html', palabra=palabra, resultado=resultado)

def detectar_nombre_o_apellido(palabra):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "ULTRA_PROMPT"
            },
            {
                "role": "user",
                "content": f"SECRET_SAUCE"
            }
        ]
    )

    respuesta = response['choices'][0]['message']['content'].strip().lower()

    if "first name" in respuesta:
        return "Nombre"
    elif "surname" in respuesta:
        return "Apellido"
    else:
        return "Indeterminado"

if __name__ == "__main__":
    app.run(debug=True)
