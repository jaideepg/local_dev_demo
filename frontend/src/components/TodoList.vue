<template>
  <div class="todo-list-container">
    <div class="todo-list-tablewrapper">
      <DataTable :value="todos" class="modern-todo-table" v-if="todos.length">
        <Column field="title" header="Title" />
        <Column field="dueDate" header="Due Date">
          <template #body="slotProps">
            <span class="todo-date-chip">{{ slotProps.data.dueDate }}</span>
          </template>
        </Column>
        <Column header="Actions">
          <template #body="slotProps">
            <button class="table-delete-btn" @click="$emit('delete', slotProps.data.id)" aria-label="Delete">
              <svg viewBox="0 0 24 24" width="22" height="22" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="5.5" y="8.5" width="13" height="10" rx="2" fill="#fff" opacity="0.85"/>
                <path d="M9 11V16M15 11V16" stroke="#ff7675" stroke-width="1.8" stroke-linecap="round"/>
                <rect x="8" y="5" width="8" height="2.5" rx="1.25" fill="#ff7675"/>
                <rect x="3" y="8" width="18" height="1.7" rx="0.85" fill="#ff7675" opacity="0.8"/>
              </svg>
            </button>
          </template>
        </Column>
      </DataTable>
      <div v-else class="todo-empty">No to-dos yet.</div>
    </div>
  </div>
</template>

<script setup>
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'

const props = defineProps({
  todos: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.todo-list-container {
  margin-top: 36px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.todo-list-tablewrapper {
  width: 100%;
  max-width: 950px;
  margin: 0 auto;
  border-radius: 20px;
  background: rgba(38, 40, 44, 0.82);
  box-shadow: 0 8px 32px rgba(0,0,0,0.19);
  padding: 24px 18px;
  min-height: 220px;
}

/* DataTable Modern Styling */
.modern-todo-table {
  background: transparent;
  border-radius: 18px;
  overflow: hidden;
  font-family: 'Inter', 'Roboto', Arial, sans-serif;
}

.modern-todo-table .p-datatable-thead > tr > th {
  background: rgba(255,255,255,0.05);
  color: #fff;
  font-size: 1.12rem;
  font-weight: 600;
  border: none;
  padding: 14px 10px;
}

.modern-todo-table .p-datatable-tbody > tr {
  background: transparent;
  border-bottom: 1px solid rgba(255,255,255,0.03);
  transition: background 0.18s;
}
.modern-todo-table .p-datatable-tbody > tr:hover {
  background: rgba(67,233,123,0.08);
}
.modern-todo-table .p-datatable-tbody > tr > td {
  color: #eaeaea;
  font-size: 1.08rem;
  border: none;
  padding: 16px 10px;
  vertical-align: middle;
}

/* Date chip for due date column */
.todo-date-chip {
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  color: #1a1c1e;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 14px;
  font-size: 1rem;
  letter-spacing: 0.03em;
  box-shadow: 0 2px 8px rgba(67,233,123,0.19);
  display: inline-block;
}

/* Circular modern delete button with trashcan SVG */
.table-delete-btn {
  background: #ff7675;
  border: none;
  border-radius: 50%;
  width: 42px;
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(255,118,117,0.13);
  cursor: pointer;
  transition: background 0.18s, box-shadow 0.18s, transform 0.18s;
  min-width: 42px;
  min-height: 42px;
}
.table-delete-btn:hover,
.table-delete-btn:focus {
  background: #d63031;
  transform: scale(1.10) rotate(-8deg);
  box-shadow: 0 4px 16px rgba(255,118,117,0.24);
}
.table-delete-btn svg {
  width: 22px;
  height: 22px;
  display: block;
  margin: auto;
}

/* Empty state */
.todo-empty {
  color: #aaa;
  text-align: center;
  padding: 28px 0;
  font-size: 1.12rem;
  font-weight: 400;
  letter-spacing: 0.03em;
}
</style>