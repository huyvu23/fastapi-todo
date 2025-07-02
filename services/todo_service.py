array_todos = []

def create_new_todo(value):
    new_todo = {
        "id":len(array_todos)+1,
        "title":value.title,
    }
    array_todos.append(new_todo)
    return new_todo

def get_all_todo():
    return array_todos
    