class Todo:
    def __init__(self):
        self.title = None
        self.date = None
        self.notes = None
        self.location = None
        #self.list = None

class TodoManager:
    def __init__(self):
        self.selecttodo = None
        self.todos = []
    def addTodo(self):
        td = Todo()
        td.title = input("td title:")
        td.date = input("td date:")
        td.notes = input("td notes:")
        td.location = input("td location:")
        self.todos.append(td)
    def removeTodo(self):
        title = input('which todo <title>:')
        for i in range(len(self.todos)):
            if title == self.todos[i].title:
                self.todos.pop(i)
                break
    def checkTodo(self):
        for i in self.todos:
            print('Title:'+i.title+' Date:'+i.date+' Notes:'+i.notes+' Location:'+i.location)

class List():
    def __init__(self):
        self.title = None
        self.color = None
        self.manager = TodoManager()

class ListManager():
    def __init__(self):
        self.selectlis = None
        self.lists = []
    def createList(self):
        lis = List()
        lis.title = input('Title: ')
        lis.color = input('Color: ')
        self.lists.append(lis)
    def deleteList(self):
        title = input('which list <title>:')
        for i in range(len(self.lists)):
            if title == self.lists[i].title:
                self.lists.pop(i)
                break
    def showlist(self):
        for i in self.lists:
            print(i.title)


lisman = ListManager()
while True:
    cmd = input("ListManager <showlis/crelis/sellis/dellis>: ")
    if cmd == 'crelis':
        lisman.createList()
    elif cmd == 'dellis':
        lisman.deleteList()
    elif cmd == 'showlis':
        lisman.showlist()
    elif cmd == 'sellis':
        title = input("which list <title>:")
        for i in lisman.lists:
            if title == i.title:
                print(i.manager.todos)
                while True:
                    cmd = input('TodoManager <addtd/removetd/checktd>:')
                    if cmd == 'addtd':
                        i.manager.addTodo()
                    elif cmd == 'removetd':
                        i.manager.removeTodo()
                    elif cmd == 'checktd':
                        i.manager.checkTodo()
                    elif cmd == 'exit':
                        break
    elif cmd == 'exit':
        break

