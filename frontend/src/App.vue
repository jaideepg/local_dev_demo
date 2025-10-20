<script setup>
import { onMounted } from 'vue'
import TodoInput from './components/TodoInput.vue'
import TodoList from './components/TodoList.vue'
import { useTodoStore } from './stores/todo'

const todoStore = useTodoStore()

onMounted(todoStore.fetchTodos)
</script>

<template>
  <div class="app-bg">
    <div class="app-center-card">
      <TodoInput @add="todoStore.addTodo" />
      <TodoList :todos="todoStore.todos" @delete="todoStore.deleteTodo" />
    </div>
  </div>
</template>

<style scoped>
.app-bg {
  min-height: 100vh;
  background: #181818;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 48px;
}

.app-center-card {
  width: 100%;
  max-width: 700px;
  margin: 0 auto;
  background: transparent; /* Let child cards show their own backgrounds */
  box-shadow: none;
  border-radius: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 36px; /* Reduce the gap between TodoInput and TodoList! */
}
</style>