import os
import sys
import sqlite3

# subir un nivel para encontrar models.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from models import db, Estudiante


def cargar_estudiantes_si_base_vacia(app):
    with app.app_context():
        if Estudiante.query.count() == 0:
            ruta_sql = os.path.join(
                os.path.dirname(__file__),
                '../inserts/estudiantes.sql'
            )

            if not os.path.exists(ruta_sql):
                print("⚠ Archivo estudiantes.sql no encontrado.")
                return

            db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace(
                'sqlite:///', ''
            )

            with open(ruta_sql, 'r', encoding='utf-8') as archivo:
                sql = archivo.read()

            with sqlite3.connect(db_path) as conn:
                conn.executescript(sql)

            print("✔ Estudiantes cargados desde SQL.")
        else:
            print("ℹ La base ya tiene estudiantes.")
