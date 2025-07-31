import os
from flask import Flask, jsonify, request
from dbconfig import db
from flask_migrate import Migrate
from rotas.mensagens_rotas import mensagens_bp
from rotas.usuarios_rotas import usuarios_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubancodedados.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.register_blueprint(mensagens_bp)
app.register_blueprint(usuarios_bp)

db.init_app(app)
migrate = Migrate(app,db)

mensagens = [{"mensagem": "primeira mensagem"}]


@app.route('/')
def home():
    return jsonify({"mensagem": "Bem vindo a API de mensagens!"})





with app.app_context():
        from models.Mensagem import Mensagem
        from models.Usuario import Usuario
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)