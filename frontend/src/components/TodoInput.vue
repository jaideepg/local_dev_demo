<template>
  <div class="todo-input-outer">
    <div class="todo-input-card">
      <form @submit.prevent="addTodo" class="todo-input-form">
        <InputText
          v-model="title"
          placeholder="Add to list.."
          class="todo-input"
          required
        />
        <DatePicker
          v-model="dueDate"
          showIcon
          iconDisplay="input"
          class="todo-date"
        />
        <button
          type="submit"
          class="add-btn"
          aria-label="Add"
        >
          <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
            <path d="M14 8V20M8 14H20" stroke="white" stroke-width="3.2" stroke-linecap="round"/>
          </svg>
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import InputText from 'primevue/inputtext'
import DatePicker from 'primevue/datepicker'

const title = ref('')
const dueDate = ref(null)

const emit = defineEmits(['add'])

function addTodo() {
  if (!title.value || !dueDate.value) return
  emit('add', { title: title.value, dueDate: dueDate.value })
  title.value = ''
  dueDate.value = null
}
</script>

<style scoped>
.todo-input-outer {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 30vh;
}

.todo-input-card {
  background: rgba(44, 46, 54, 0.85);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.15);
  padding: 32px 24px;
  min-width: 500px;
}

.todo-input-form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}
@media (min-width: 768px) {
  .todo-input-form {
    flex-direction: row;
    align-items: center;
    gap: 20px;
  }
}

/* InputText styling */
.todo-input {
  border-radius: 16px;
  font-size: 1.3rem;
  padding: 18px 24px;
  background: rgba(255,255,255,0.07);
  color: #f3f3f3;
  border: none;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  transition: background 0.15s, box-shadow 0.15s;
  width: 100%;
  min-width: 320px;
  max-width: 420px;
  height: 54px;
}
.todo-input:focus {
  background: rgba(255,255,255,0.12);
  box-shadow: 0 4px 12px rgba(67,233,123,0.15);
}

.todo-input::placeholder {
  color: #aaa;
}

/* DatePicker input styling to match InputText */
.todo-date .p-inputtext {
  border-radius: 16px;
  font-size: 1.3rem;
  padding: 18px 24px;
  background: rgba(255,255,255,0.07) !important;
  color: #f3f3f3 !important;
  border: none !important;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  transition: background 0.15s, box-shadow 0.15s;
  height: 54px;
}

.todo-date .p-inputtext:focus {
  background: rgba(255,255,255,0.12) !important;
  box-shadow: 0 4px 12px rgba(67,233,123,0.15);
}

.todo-date .p-inputtext::placeholder {
  color: #aaa !important;
}

/* DatePicker icon color */
.todo-date .pi-calendar {
  color: #f3f3f3 !important;
  opacity: 0.8;
}

/* Remove border on the datepicker input, if present */
.todo-date .p-inputtext,
.todo-date .p-datepicker .p-inputtext {
  border: none !important;
}

/* Popup datepicker styling for consistency (optional, for modern look) */
.todo-date .p-datepicker {
  background: #222326;
  color: #fff;
  border-radius: 16px;
  border: none;
  box-shadow: 0 8px 32px rgba(0,0,0,0.15);
}
.todo-date .p-datepicker-calendar {
  background: transparent;
}
.todo-date .p-datepicker-header {
  background: #232526;
  color: #43e97b;
  border-bottom: 1px solid rgba(67,233,123,0.25);
}
.todo-date .p-datepicker-title {
  color: #43e97b;
}
.todo-date .p-datepicker .p-highlight {
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  color: #fff;
  border-radius: 8px;
}
.todo-date .p-datepicker .p-disabled {
  opacity: 0.5;
}

/* Rounded, perfectly circular button */
.add-btn {
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  border-radius: 50%;
  width: 56px;
  height: 56px;
  aspect-ratio: 1/1;
  color: #fff;
  border: none;
  box-shadow: 0 2px 12px 0 rgba(56,249,215,0.10), 0 1px 6px 0 rgba(67,233,123,0.14);
  display: flex;
  align-items: center;
  justify-content: center;
  transition:
    box-shadow 0.22s cubic-bezier(.37,1.28,.64,.98),
    background 0.18s,
    transform 0.16s;
  margin-left: 20px;
  position: relative;
  outline: none;
  cursor: pointer;
  min-width: 56px;
  min-height: 56px;
  max-width: 56px;
  max-height: 56px;
}

.add-btn svg {
  width: 28px;
  height: 28px;
}

.add-btn:hover, .add-btn:focus {
  background: linear-gradient(135deg, #38f9d7 0%, #43e97b 100%);
  box-shadow: 0 4px 24px 0 rgba(56,249,215,0.22), 0 2px 8px 0 rgba(67,233,123,0.22);
  transform: scale(1.08);
}

.add-btn:active {
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  box-shadow: 0 1px 4px 0 rgba(56,249,215,0.10), 0 0.5px 3px 0 rgba(67,233,123,0.10);
  transform: scale(0.95);
}
</style>