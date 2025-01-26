

function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}

function drop(event) {
    event.preventDefault();
    const data = event.dataTransfer.getData("text");
    const task = document.getElementById(data);
    const column = event.target.closest('.kanban-column');
    const status = column.querySelector('h3').innerText;

    // Map status text to status code
    const statusMap = {
        "Para Fazer": "O",
        "Em Progresso": "N",
        "Feito": "C"
    };

    const newStatus = statusMap[status];
    if (newStatus) {
        column.appendChild(task);

        // Update task status via AJAX
        fetch(updateTaskStatusUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}"
            },
            body: JSON.stringify({
                id: data.split('-')[1], // Extract task ID
                status: newStatus
            })
        }).then(response => {
            if (!response.ok) {
                console.error("Failed to update task status.");
            }
        }).catch(error => {
            console.error("Error:", error);
        });
    }
}

function openModal() {
    document.getElementById("addTaskModal").classList.add("show");
}

function closeModal() {
    document.getElementById("addTaskModal").classList.remove("show");
}

function openUpdateModal(taskId) {
    fetch(`/get-task/${taskId}`)
        .then(response => response.json())
        .then(data => {
            // Populate the modal fields with the fetched data
            document.getElementById('updateTitle').value = data.title;
            document.getElementById('updateDescription').value = data.description;
            document.getElementById('updateStatus').value = data.status;

            // Attach the taskId to the form submission
            document.getElementById('updateTaskForm').onsubmit = function(event) {
                event.preventDefault();
                updateTask(taskId);
            };

            // Set the delete button's onclick handler
            document.getElementById('deleteTaskButton').onclick = function() {
                deleteTask(taskId);
            };

            // Show the modal
            document.getElementById('updateTaskModal').classList.add("show");
        })
        .catch(error => {
            console.error("Error fetching task details:", error);
        });
}

// Função para fechar o modal
function closeUpdateModal() {
    document.getElementById('updateTaskModal').style.display = 'none';
}

function updateTask(taskId) {
    const title = document.getElementById('updateTitle').value;
    const description = document.getElementById('updateDescription').value;
    const status = document.getElementById('updateStatus').value;

    fetch(updateTaskUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": "{{ csrf_token }}"
        },
        body: JSON.stringify({
            id: taskId,
            title: title,
            description: description,
            status: status
        })
    }).then(response => {
        if (!response.ok) {
            console.error("Falha ao atualizar a tarefa.");
        } else {
            // Atualizar a tarefa na interface ou recarregar a página
            window.location.reload();
        }
    }).catch(error => {
        console.error("Erro:", error);
    });
}

function deleteTask(taskId) {
        fetch(deleteTaskUrl, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}"
            },
            body: JSON.stringify({ id: taskId })
        }).then(response => {
            if (!response.ok) {
                console.error("Falha ao deletar a tarefa.");
            } else {
                window.location.reload()
            }
        }).catch(error => {
            console.error("Erro:", error);
        });
}


