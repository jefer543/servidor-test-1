from dbconfig import db

class Mensagem(db.Model):
    __tablename__ = 'mensagens'

    id = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    conteudo = db.Column(db.String(255), nullable = False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def to_dict(self):
        return {
        'id': self.id,
        'conteudo': self.conteudo
        }