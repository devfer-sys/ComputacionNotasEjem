from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Estudiante, init_db
from app.load_data import cargar_estudiantes_si_base_vacia
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'clave_secreta_escuela_primaria'

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'escuela.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)
    cargar_estudiantes_si_base_vacia(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/buscar', methods=['POST'])
    def buscar():
        ci = request.form.get('ci')
        estudiante = Estudiante.query.filter_by(ci=ci).first()
        if estudiante:
            return render_template('report.html', estudiante=estudiante)
        else:
            return render_template('index.html', error="No se encontró ningún estudiante con ese CI.")

    @app.route('/print/<ci>')
    def mostrar_boletin(ci):
        estudiante = Estudiante.query.filter_by(ci=ci).first()
        if estudiante:
            return render_template('print.html', estudiante=estudiante)
        else:
            flash('No se encontró ningún estudiante con ese CI', 'error')
            return redirect(url_for('index'))

    return app

# Esta línea expone la app para Vercel
app = create_app()
