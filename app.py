import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests

load_dotenv()

app = Flask(__name__)

# Configurações
GIPHY_API_KEY = 'i79REf8l0POTGSold8qOJ1Re4zrDm7En'
GIPHY_URL = "https://api.giphy.com/v1/gifs/search"


@app.route('/', methods=['GET', 'POST'])
def index():
    gifs = []
    search_term = ""

    if request.method == 'POST':
        search_term = request.form.get('search_term', '').strip()
        if search_term:
            params = {
                'api_key': GIPHY_API_KEY,
                'q': search_term,
                'limit': 5,  # Número de GIFs a retornar
                'rating': 'g'  # Filtro de conteúdo
            }
            response = requests.get(GIPHY_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                gifs = data.get('data', [])

    return render_template('index.html', gifs=gifs, search_term=search_term)


if __name__ == '__main__':
    app.run(debug=True)