from flask import Blueprint, request, jsonify
from models.Usuario import Usuario
from dbconfig  import db
usuarios_bp = Blueprint('usuarios_bp', __name__, url_prefix='/usuarios')

@usuarios_bp.route('/register', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    nome = dados['nome']
    email = dados['email']
    senha = dados['senha']

    usuario_existente = Usuario.query.filter_by(email=email).first()
    if usuario_existente:
        return jsonify({"erro": "Email já cadastrado!"}), 400
    
    novo_usuario = Usuario(nome=nome, email=email, senha=senha)

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"msg": "usuario criado!"}), 201

@usuarios_bp.route('/')
def ler_usuarios():
    usuarios = Usuario.query.all()
    usuarios = [usuario.to_dict() for usuario in usuarios]
    return jsonify(usuarios), 200

@usuarios_bp.route('/editar/<int:id>', methods=['PUT'])
def editar_usuario(id):
    dados = request.get_json()

    usuario = Usuario.query.get_or_404(id)

    if dados['nome']:
        usuario.nome = dados['nome']

    if dados['email']:
        email_existente = Usuario.query.filter_by(email = dados['email']).first()
        if email_existente:
            return jsonify({"erro": "Email existente"})
        usuario.email = dados['email']

    if dados['senha']:
        usuario.senha = dados['senha']

    db.session.commit()
    return jsonify({"msg": "usuario atualizado com sucesso!"})

@usuarios_bp.route('/excluir/<int:id>', methods=['DELETE']) # delete
def excluir_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"msg": "Usuário excluído com sucesso!"}), 200