from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from todo.models import Todo

def index(request):
    itens = Todo.objects.all()
    return render(request, 'index.html', {'itens': itens})

@csrf_exempt
@require_http_methods(["GET"])
def get_task(request, task_id):
    try:
        task = Todo.objects.get(id=task_id)
        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        })
    except Todo.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)

@csrf_exempt
@require_http_methods(["POST"])
def update_task_status(request):
    try:
        data = json.loads(request.body)
        task = Todo.objects.get(id=data["id"])
        task.status = data["status"]
        task.save()
        return JsonResponse({"message": "Task status updated successfully"})
    except (KeyError, Todo.DoesNotExist):
        return JsonResponse({"error": "Invalid task data"}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def update_task(request):
    try:
        data = json.loads(request.body)
        task = Todo.objects.get(id=data["id"])
        task.title = data["title"]
        task.description = data["description"]
        task.status = data["status"]
        task.save()
        return JsonResponse({"message": "Tarefa atualizada com sucesso"})
    except (KeyError, Todo.DoesNotExist):
        return JsonResponse({"error": "Dados da tarefa inválidos"}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_task(request):
    data = json.loads(request.body)
    task = Todo.objects.get(id=data["id"])
    task.delete()
    return JsonResponse({"message": "Tarefa deletada com sucesso"})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')

        # Criar a nova tarefa
        Todo.objects.create(title=title, description=description, status=status)

        # Redirecionar para o quadro Kanban
        return redirect('index')