from flask import Blueprint, jsonify, request
from dbconfig import db
from models.Mensagem import Mensagem
from token_decorator import requer_token

mensagens_bp = Blueprint('mensagens_bp', __name__, url_prefix='/mensagens')

@mensagens_bp.route('/usuario/<int:id_usuario>')
@requer_token
def ler_mensagens():
    mensagens = Mensagem.query.all()
    mensagens = [mensagem.to_dict() for mensagem in mensagens]
    return jsonify(mensagens), 200


@mensagens_bp.route('/criar', methods=['POST'])
@requer_token
def criar_mensagem():
    dados = request.get_json()
    conteudo = dados['conteudo']
    id_usuario = request.id_usuario

    novaMensagem = Mensagem(conteudo=conteudo, id_usuario=id_usuario)

    db.session.add(novaMensagem)
    db.session.commit()

    return jsonify(novaMensagem.to_dict()), 201


@mensagens_bp.route('/editar/<id>', methods=['PUT'])
@requer_token
def atualizar_mensagem(id):
    dados = request.get_json()
    conteudo = dados['conteudo']
 
    mensagem = Mensagem.query.get_or_404(id)

    mensagem.conteudo = conteudo
    db.session.commit()

    return jsonify(mensagem.to_dict()), 200




@mensagens_bp.route('/excluir/<id>', methods=['DELETE'])
@requer_token
def excluir_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id)
    db.session.delete(mensagem)
    db.session.commit()
    return jsonify({"mensagem": "Mensagem excluida com sucesso!"}), 200