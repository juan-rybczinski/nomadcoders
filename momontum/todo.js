const todoForm = document.querySelector(".js-todo-form"),
  todoInput = todoForm.querySelector("input"),
  todoList = document.querySelector(".js-todo-list");

const TODO_LS = "todos";

const todos = [];

function saveTodos(params) {
  localStorage.setItem(TODO_LS, JSON.stringify(todos));
}

function paintTodos(text) {
  const li = document.createElement("li");
  const span = document.createElement("span");
  const button = document.createElement("button");
  const newId = todos.length + 1;

  span.innerText = text;
  button.innerText = "❌";
  li.id = newId;
  li.appendChild(button);
  li.appendChild(span);
  todoList.appendChild(li);

  const todoObject = {
    id: newId,
    todo: text,
  };
  todos.push(todoObject);
  saveTodos();
}

function handleSubmitTodos(event) {
  event.preventDefault();
  const currentValue = todoInput.value;
  paintTodos(currentValue);
  todoInput.value = "";
}

function loadTodos() {
  const loadTodos = localStorage.getItem(TODO_LS);
  if (loadTodos !== null) {
    console.log(loadTodos);
    const parsedTodos = JSON.parse(loadTodos);
    console.log(parsedTodos);
    parsedTodos.forEach(function (todoObject) {
      paintTodos(todoObject.todo);
    });
  }
}

function init() {
  loadTodos();
  todoForm.addEventListener("submit", handleSubmitTodos);
}

init();
