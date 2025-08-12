from ..models.Mensagem import Message
from .. import db

def listar_mensagens():
    return Message.query.all()

def obter_mensagem(message_id):
    return Message.query.get(message_id)  

def criar_mensagem(dados):
    nova = Message(**dados)
    db.session.add(nova)
    db.session.commit()
    return nova

def atualizar_mensagem(message, dados):
    for chave, valor in dados.items():
        setattr(message, chave, valor)
    db.session.commit()
    return message

def deletar_mensagem(message):
    db.session.delete(message)
    db.session.commit()