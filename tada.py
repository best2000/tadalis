import json
import sys
import os

class Todo:
    def __init__(self, title , date, notes, location, List, progress):
        self.title = title
        self.date = date
        self.notes = notes
        self.location = location
        self.list = List
class TodoManager:
    def __init__(self, TodoObj):
        self.Todo = TodoObj
    def addTodo(self):
        pass
    def removeTodo(self):
        pass    
    def checkTodo(self):
        pass
class List():
    def __init__(self, title, color):
        self.title = title
        self.color = color
        self.manager = lisman

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class ListManager():
    def __init__(self):
        self.selectlis = None 
            
    def createList(self):
        lis = List("title", "color")
        lis.title = input('Title: ')
        lis.color = input('Color: ')
        with open("liss/"+ lis.title + ".json", 'w') as lisf:
            lisf.write(lis.toJSON())

    def deleteList(self):
        rmlis = input("which one? '<listitle>.json':")
        try:
            os. remove("liss/" + rmlis)
        except:
            print("file not found!")

while True:
    cmd = input("command input:")
    lisman = ListManager() #main lisman
    if cmd == 'showlis':
        pass
    elif cmd == 'createlis':
        lisman.createList()
    elif cmd == 'dellis':
        lisman.deleteList()
    #elif cmd == 'selectlist':
     #   lis = input("which list:")
      #  lisman.selectlis = lis
        #show list info
       # cmd = input("waht u wanna do with list:")
        #if cmd == 'remove':
         #   lisman.deleteList()
        #else:
         #   pass

    elif cmd == 'exit':
        sys.exit()
    else:
        print('Command not found!!!')
        


#jsere = me.toJSON()
#print(jsere)