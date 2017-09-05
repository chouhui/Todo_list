from utils import log
from routes import json_response
from models.todo import Todo


def all(request):
    todo_list = Todo.all()
    todos = [t.json() for t in todo_list]
    return json_response(todos)


def add(request):
    # 浏览器用 ajax 发送 json 格式的数据过来
    form = request.json()

    t = Todo.new(form)

    return json_response(t.json())


def delete(request):
    todo_id = int(request.query.get('id'))
    t = Todo.delete(todo_id)
    return json_response(t.json())


def update(request):
    form = request.form()
    todo_id = int(form.get('id'))
    t = Todo.update(todo_id, form)
    return json_response(t.json())


def route_dict():
    d = {
        '/api/todo/all': all,
        '/api/todo/add': add,
        '/api/todo/delete': delete,
        '/api/todo/update': update,
    }
    return d
