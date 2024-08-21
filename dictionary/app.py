from flask import Flask, request, jsonify
from model.bdHandler import corresp_exata, corresp_aproximada

app = Flask(__name__)
@app.route("/")
def index():
    """
        Rota Default:
        Este método irá:
        1. Prover para o usuário instruções de como
        formatar a entrada em json para que ele realize
        a requisição de uma palavra do dicionário
    """   

    response = {"uso": "/dict?palavra=<string>"}
    return jsonify(response)

@app.route("/dict")
def dict():
    """

        Rota "dict" vai prover:
        1. Aceita uma palavra como requisição do usuário
        2. Tenta encontrar uma correspondência exata
        3. Retorna a correspondência se encontrar
        4. Se não for encontrada, encontra correspondência aproximada e retorna
    
    """
    palavra = request.args.get("palavra")
    if not palavra:
        return jsonify({"Status": "Erro", "Dado": "Palavra inválida"})
    
    definicao = corresp_exata(palavra)
    if definicao:
        return jsonify({"Status": "Sucesso", "Dado": definicao})
    definicao = corresp_aproximada(palavra)
    if definicao:
        return jsonify({"Status": "Parcial", "Dado": definicao})
    else:
        return jsonify({"Status": "Erro", "Dado": "Palavra não encontrada"})



if __name__ == "__main__":
    app.run()