from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # O token exato configurado no painel da Meta
        MEU_TOKEN = "bot_despesas_123"
        
        token_recebido = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        # A Meta só valida se o servidor devolver o challenge intacto
        if token_recebido == MEU_TOKEN:
            return challenge, 200
        return 'Falha na verificação', 403

    if request.method == 'POST':
        # Logica futura para processar as despesas
        dados = request.get_json()
        print("Nova mensagem recebida:", dados)
        return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    app.run(port=5000)