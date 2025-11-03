from db import db

class Times(db.Model):
    __tablename__ = 'times'

    id = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(80), nullable=False)
    Genero = db.Column(db.String(80), nullable=False)
    Desenvolvidor = db.Column(db.String(80), nullable=False)
    Plataforma = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'Titulo': self.titulo,           
            'Genero': self.genero,    
            'Desenvolvidor': self.desenvolvidor,      
            'Plataforma': self.Plataforma,         
        }