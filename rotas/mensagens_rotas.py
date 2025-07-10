from flask import Blueprint, jsonify, request
from dbconfig import db
from models.Mensagem import Mensagem

mensagens_bp = Blueprint('mensagens_bp', __name__, url_prefix='/mensagens')

@mensagens_bp.route('/')
def ler_mensagens():
    mensagens = Mensagem.query.all()
    mensagens = [mensagem.to_dict() for mensagem in mensagens]
    return jsonify(mensagens), 200


@mensagens_bp.route('/criar', methods=['POST'])
def criar_mensagem():
    dados = request.get_json()
    conteudo = dados['conteudo']

    novaMensagem = Mensagem(conteudo=conteudo)

    db.session.add(novaMensagem)
    db.session.commit()

    return jsonify(novaMensagem.to_dict()), 201


@mensagens_bp.route('/editar/<id>', methods=['PUT'])
def atualizar_mensagem(id):
    dados = request.get_json()
    conteudo = dados['conteudo']
 
    mensagem = Mensagem.query.get_or_404(id)

    mensagem.conteudo = conteudo
    db.session.commit()

    return jsonify(mensagem.to_dict()), 200




@mensagens_bp.route('/excluir/<id>', methods=['DELETE'])
def excluir_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id)
    db.session.delete(mensagem)
    db.session.commit()
    return jsonify({"mensagem": "Mensagem excluida com sucesso!"}), 200