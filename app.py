from flask import Flask, jsonify, request

app = Flask(__name__)

mensagens = [{"mensagem": "primeira mensagem"}]


@app.route('/')
def home():
    return jsonify({"mensagem": "Bem vindo a API de mensagens!"})


@app.route('/mensagens')
def ler_mensagens():
    return jsonify(mensagens)


@app.route('/mensagens/criar', methods=['POST'])
def criar_mensagem():
    dados = request.get_json()
    conteudo = dados['conteudo']

    mensagens.append({"mensagem":conteudo})

    return jsonify({"mensagem": "mensagem criada com sucesso"}), 201


@app.route('/mensagens/editar/<id>', methods=['PUT'])
def atualizar_mensagem(id):
    dados = request.get_json()
    conteudo = dados['conteudo']
    indice = int(id)

    if len(mensagens) < indice:
        return jsonify({"erro": "Indice maior que lista de mensagens"}), 400
    if mensagens[indice] is None:
        return jsonify( {"erro": "Mensagem inexistente!"}), 400

    mensagens[indice] = {"conteudo": conteudo}
    return jsonify({"mensagem": "Mensagem atualizar com sucesso"}), 200




@app.route('/mensagens/exluir/<id>', methods=['DELETE'])
def excluir_mensagem(id):
    indice = int(id)

    if indice > len(mensagens):
        return jsonify({"erro": "Indice maior que tamanho da lista de mensagens"}), 400

    if mensagens[indice] is None:
        return jsonify( {"erro": "Mensagem inexistente!"}), 400
    
    del mensagens[indice]

    return jsonify({"mensagem": "Mensagem excluida com sucesso!"}), 200

    
app.run(debug=True)