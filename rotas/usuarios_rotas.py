from flask import Blueprint, request, jsonify
from models.Usuario import Usuario
from dbconfig  import db
from werkzeug.security import generate_password_hash, check_password_hash
from generate_token import gerar_token
from token_decorator import requer_token

usuarios_bp = Blueprint('usuarios_bp', __name__, url_prefix='/usuarios')

@usuarios_bp.route('/login', methods=['post'])
def login():
    dados = request.get_json()
    email = dados['email']
    senha = dados['senha']

    usuario = Usuario.query.filter_by(email=email).first()

    if usuario is None:
        return jsonify({"erro": "Email ou senha incorretos!"}), 400
    
    token = gerar_token(usuario.id)

    if usuario is not None and check_password_hash(usuario.senha, senha):
        return jsonify({"token":token}), 200

    return jsonify({"erro": "Email ou senha incorretos!"}), 400

@usuarios_bp.route('/register', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    nome = dados['nome']
    email = dados['email']
    senha = dados['senha']

    senhaCriptografada = generate_password_hash(senha)

    usuario_existente = Usuario.query.filter_by(email=email).first()
    if usuario_existente:
        return jsonify({"erro": "Email já cadastrado!"}), 400
    
    novo_usuario = Usuario(nome=nome, email=email, senha=senhaCriptografada)

    db.session.add(novo_usuario)
    db.session.commit()

    token = gerar_token(novo_usuario.id)

    return jsonify({"token": token}), 201

@usuarios_bp.route('/')
def ler_usuarios():
    usuarios = Usuario.query.all()
    usuarios = [usuario.to_dict() for usuario in usuarios]
    return jsonify(usuarios), 200


@usuarios_bp.route('/editar/<int:id_usuario>', methods=['PUT'])
@requer_token
def editar_usuario(id_usuario):
    dados = request.get_json()
    
    print(id_usuario)

    if id_usuario == request.id_usuario:
        usuario = Usuario.query.get_or_404(id_usuario)
    else:
        return jsonify({"erro": "Operação inválida!"}), 401
    
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
@requer_token
def excluir_usuario(id):
    if id == request.id_usuario:
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({"msg": "Usuário excluído com sucesso!"}), 200

    return jsonify({"erro": "Você não tem permissão para excluir este usuário!"}), 403