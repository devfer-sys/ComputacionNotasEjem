from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Estudiante(db.Model):
    __tablename__ = 'estudiantes'
    
    id = db.Column(db.Integer, primary_key=True)  # Clave interna de la BD
    ci = db.Column(db.String(20), unique=True, nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    grado = db.Column(db.String(10), nullable=False)
    
    primer_trimestre = db.Column(db.Float, nullable=True)
    segundo_trimestre = db.Column(db.Float, nullable=True)
    tercer_trimestre = db.Column(db.Float, nullable=True)
    promedio_anual = db.Column(db.Float, nullable=True)

    def calcular_promedio(self):
        notas = [n for n in [self.primer_trimestre, self.segundo_trimestre, self.tercer_trimestre] if n is not None]
        if notas:
            self.promedio_anual = round(sum(notas) / len(notas), 2)
        else:
            self.promedio_anual = None

    def to_dict(self):
        self.calcular_promedio()
        return {
            'ci': self.ci,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'grado': self.grado,
            'primer_trimestre': self.primer_trimestre,
            'segundo_trimestre': self.segundo_trimestre,
            'tercer_trimestre': self.tercer_trimestre,
            'promedio_anual': self.promedio_anual
        }

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()