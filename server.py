from flask import Flask, render_template
import os 

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # Usa el puerto asignado por Railway
    app.run(host='0.0.0.0', port=port)