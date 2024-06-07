from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

def get_openhermes_response(user_input):
    try:
        # Usar ollama.chat para obtener la respuesta del modelo openhermes
        response = ollama.chat(model='openhermes', messages=[{'role': 'user', 'content': user_input}])
        
        # Imprimir la respuesta completa para depuración
        print("Respuesta completa del modelo:", response)
        
        # Ajusta según la estructura observada
        if 'message' in response and 'content' in response['message']:
            return response['message']['content']
        else:
            return "Error: Respuesta inesperada del modelo."
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response_text = get_openhermes_response(user_input)
    return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
