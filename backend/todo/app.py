from flask import Flask, request, jsonify
import psycopg2
import os
from flask_cors import CORS  

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Database connection settings
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'postgres')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'password')

# Helper to get DB connection
def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/todos', methods=['GET'])
def get_todos():
    print("Running /todos GET endpoint")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, title, completed FROM todos ORDER BY id;')
    todos = [
        {'id': row[0], 'title': row[1], 'completed': row[2]} for row in cur.fetchall()
    ]
    cur.close()
    conn.close()
    print("Successfully fetched todos:", todos)
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    title = data.get('title')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO todos (title, completed) VALUES (%s, %s) RETURNING id;', (title, False))
    todo_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': todo_id, 'title': title, 'completed': False}), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    title = data.get('title')
    completed = data.get('completed')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE todos SET title = %s, completed = %s WHERE id = %s;', (title, completed, todo_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': todo_id, 'title': title, 'completed': completed})

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM todos WHERE id = %s;', (todo_id,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204

if __name__ == '__main__':
    # import debugpy

    # Enable remote debugging    
    # debugpy.listen(("0.0.0.0", 5678 ))
    app.run(debug=True, host="0.0.0.0", port=5001)
