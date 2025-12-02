# 📌 Project: FastAPI Board & Task Manager

This project provides a simple **Kanban-style Board Management API** built with **FastAPI** and  **MongoDB** .

You can create boards, lists inside boards, and tasks inside lists.

It also supports moving tasks between lists and deleting tasks.

---

## 🚀 Features

* Get all project boards
* Get lists and tasks of a specific board
* Get all tasks from a specific list
* Add a new task
* Move a task between lists
* Delete a task
* Auto-generated interactive API documentation using **Swagger UI**

---

## 📂 Project Structure (example)

<pre class="overflow-visible!" data-start="775" data-end="862"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>.
├── main.py
├── </span><span>database</span><span>.py
├── </span><span>schemas</span><span>.py
└── README.md
</span></span></code></div></div></pre>

---

## 🔧 Requirements

Make sure you have:

* Python 3.9+
* MongoDB running locally or remotely
* The following libraries installed:
  <pre class="overflow-visible!" data-start="1001" data-end="1055"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>pip</span><span> install fastapi uvicorn motor pydantic
  </span></span></code></div></div></pre>

---

## 🛠️ Running the Project

Start the FastAPI server with:

<pre class="overflow-visible!" data-start="1122" data-end="1169"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m uvicorn main:app --reload
</span></span></code></div></div></pre>

The API will start at:

<pre class="overflow-visible!" data-start="1195" data-end="1224"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>http:</span><span>//127.0.0.1:8000</span><span>
</span></span></code></div></div></pre>

---

## 📘 FastAPI Interactive Docs

FastAPI automatically generates two documentation UIs:

### ✔ Swagger UI (Recommended)

<pre class="overflow-visible!" data-start="1350" data-end="1384"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>http:</span><span>//127.0.0.1:8000/docs</span><span>
</span></span></code></div></div></pre>

This interface lets you:

* Try out  **GET** ,  **POST** ,  **PUT** , **DELETE** directly
* Fill request bodies in JSON format
* See response samples
* Test API behavior without needing Postman

### ✔ ReDoc

<pre class="overflow-visible!" data-start="1587" data-end="1622"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>http:</span><span>//127.0.0.1:8000/redoc</span><span>
</span></span></code></div></div></pre>

A cleaner, more text-based documentation page.

---

## 🗄️ API Endpoints

### ▶ Get all boards

<pre class="overflow-visible!" data-start="1720" data-end="1739"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>GET /boards
</span></span></code></div></div></pre>

### ▶ Get a specific board with its lists

<pre class="overflow-visible!" data-start="1783" data-end="1815"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>GET /boards/{board_name}
</span></span></code></div></div></pre>

### ▶ Get tasks from a specific list inside a board

<pre class="overflow-visible!" data-start="1869" data-end="1917"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>GET /boards/{board_name}/lists/{list_id}
</span></span></code></div></div></pre>

### ▶ Add a task to a board list

<pre class="overflow-visible!" data-start="1952" data-end="2001"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>POST /boards/{board_name}/lists/{list_id}
</span></span></code></div></div></pre>

**Request body (example):**

<pre class="overflow-visible!" data-start="2030" data-end="2127"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"id"</span><span>:</span><span></span><span>"task123"</span><span>,</span><span>
  </span><span>"title"</span><span>:</span><span></span><span>"My new task"</span><span>,</span><span>
  </span><span>"description"</span><span>:</span><span></span><span>"More details here"</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

### ▶ Move a task from one list to another

<pre class="overflow-visible!" data-start="2172" data-end="2261"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>PUT /boards/{board_name}/tasks/{task_id}/move?source_list_id=...&dest_list_id=...
</span></span></code></div></div></pre>

### ▶ Delete a task

<pre class="overflow-visible!" data-start="2283" data-end="2334"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>DELETE /boards/{board_name}/tasks/{task_id}
</span></span></code></div></div></pre>

---

## 🧪 Testing With Swagger UI

1. Start the server:
   <pre class="overflow-visible!" data-start="2396" data-end="2445"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>python -m uvicorn </span><span>main</span><span>:app --reload
   </span></span></code></div></div></pre>
2. Open:
   <pre class="overflow-visible!" data-start="2458" data-end="2498"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>http:</span><span>//127.0.0.1:8000/docs</span><span>
   </span></span></code></div></div></pre>
3. Choose any endpoint
4. Click **Try it out**
5. Fill required parameters
6. Click **Execute**
