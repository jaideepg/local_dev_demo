import pytest
from unittest.mock import patch, MagicMock
from todo.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@patch('todo.app.get_db_connection')
def test_get_todos(mock_get_db_connection, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        (1, 'Task 1', False),
        (2, 'Task 2', True)
    ]
    mock_conn.cursor.return_value = mock_cursor
    mock_get_db_connection.return_value = mock_conn

    response = client.get('/todos')
    assert response.status_code == 200
    assert response.get_json() == [
        {'id': 1, 'title': 'Task 1', 'completed': False},
        {'id': 2, 'title': 'Task 2', 'completed': True}
    ]

@patch('todo.app.get_db_connection')
def test_add_todo(mock_get_db_connection, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = [42]
    mock_conn.cursor.return_value = mock_cursor
    mock_get_db_connection.return_value = mock_conn

    response = client.post('/todos', json={'title': 'New Task'})
    assert response.status_code == 201
    assert response.get_json() == {'id': 42, 'title': 'New Task', 'completed': False}

@patch('todo.app.get_db_connection')
def test_update_todo(mock_get_db_connection, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_get_db_connection.return_value = mock_conn

    response = client.put('/todos/5', json={'title': 'Updated Task', 'completed': True})
    assert response.status_code == 200
    assert response.get_json() == {'id': 5, 'title': 'Updated Task', 'completed': True}

@patch('todo.app.get_db_connection')
def test_delete_todo(mock_get_db_connection, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_get_db_connection.return_value = mock_conn

    response = client.delete('/todos/7')
    assert response.status_code == 204