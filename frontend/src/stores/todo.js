import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useTodoStore = defineStore('todo', () => {
  const todos = ref([])
  const API_URL = 'http://localhost:5003/todos'

  async function fetchTodos() {
    const res = await fetch(API_URL)
    todos.value = await res.json()
  }

  async function addTodo(todo) {
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: todo.title, due_date: todo.dueDate }),
    })
    if (res.ok) {
      await fetchTodos()
    }
  }

  async function deleteTodo(id) {
    const res = await fetch(`${API_URL}/${id}`, { method: 'DELETE' })
    if (res.ok) {
      await fetchTodos()
    }
  }

  return { todos, fetchTodos, addTodo, deleteTodo }
})
