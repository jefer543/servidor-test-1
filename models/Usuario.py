from dbconfig import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    db.relationship('Mensagem', backref='usuario', lazy=True)

    def to_dict(self):
        return {
        'id': self.id,
        'nome': self.nome,
        'email': self.email,
        'senha': self.senha

        }