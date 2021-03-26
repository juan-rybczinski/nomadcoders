const todoForm = document.querySelector(".js-todo-form"),
  todoInput = todoForm.querySelector("input"),
  todoList = document.querySelector(".js-todo-list");

const TODO_LS = "todos";

function paintTodos(text) {
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.innerText = text;
  const button = document.createElement("button");
  button.innerText = "❌";
  li.appendChild(button);
  li.appendChild(span);
  todoList.appendChild(li);
}

function handleSubmitTodos(event) {
  event.preventDefault();
  const currentValue = todoInput.value;
  paintTodos(currentValue);
  todoInput.value = "";
}

function loadTodos() {
  const todos = localStorage.getItem(TODO_LS);
  if (todos !== null) {
  }
}

function init() {
  loadTodos();
  todoForm.addEventListener("submit", handleSubmitTodos);
}

init();
