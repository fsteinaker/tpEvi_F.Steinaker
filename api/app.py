from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@task_db:5432/tasks_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

# Ruta para obtener tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    result = [{'id': t.id, 'title': t.title, 'status': t.status} for t in tasks]
    return jsonify(result), 200

# Ruta para crear tarea
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json(force=True)  # 👈 fuerza a interpretar el body como JSON
        if not data:
            return jsonify({'error': 'No se recibió JSON'}), 400
        
        title = data.get('title')
        status = data.get('status')

        if not title or not status:
            return jsonify({'error': 'Faltan campos obligatorios (title, status)'}), 400

        new_task = Task(title=title, status=status)
        db.session.add(new_task)
        db.session.commit()

        return jsonify({'message': 'Tarea creada correctamente'}), 201
    
    except Exception as e:
        return jsonify({'error': f'Error procesando la solicitud: {str(e)}'}), 400

# Ruta raíz para testeo
@app.route('/')
def home():
    return "API Flask funcionando correctamente 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
