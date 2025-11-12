from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:123456@db:5432/tasksdb")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), default="ToDo")

@app.route("/")
def index():
    return jsonify({"message": "API de tareas funcionando correctamente 🚀"})

# 🟢 NUEVO ENDPOINT DE PRUEBA
@app.route("/health", methods=["GET"])
def health_check():
    try:
        db.session.execute(text("SELECT 1"))  # ✅ usando text()
        return jsonify({"status": "ok", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "status": t.status} for t in tasks])

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    new_task = Task(title=data["title"], status=data.get("status", "ToDo"))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Tarea creada"}), 201

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.json
    task = Task.query.get_or_404(id)
    task.status = data.get("status", task.status)
    db.session.commit()
    return jsonify({"message": "Tarea actualizada"})

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Tarea eliminada"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
