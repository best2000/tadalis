import json
import sys
import os
import shutil

class Todo:
    def __init__(self, title , date, notes, location, List, progress):
        self.title = title
        self.date = date
        self.notes = notes
        self.location = location
        self.list = List
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class TodoManager:
    def __init__(self):
        self.selecttodo = None
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
        os.mkdir('liss/' + lis.title)
        with open("liss/"+ lis.title + "/info.json", 'w') as lisf:
            lisf.write(lis.toJSON())
    def deleteList(self):
        try:
            shutil.rmtree("liss/" + self.selectlis)
        except:
            print("error!")

while True:
    cmd = input("command input:")
    lisman = ListManager() #main lisman
    todoman = TodoManager() #main todoman

    if cmd == 'showlis':
        lisdir = os.listdir('liss')
        for i in lisdir:
            with open('liss/' + i + '/info.json', 'r') as jf:
                jstr = jf.read()
            jdic = json.loads(jstr)
            print(jdic['title'], jdic['color'])
    elif cmd == 'crelis':
        lisman.createList()
    elif cmd == 'sellis':
        listitle = input("which list <title>:")
        lisman.selectlis = listitle
        #show list info
        tddir = os.listdir('liss/'+listitle) 
        print(tddir)
        cmd = input("waht u wanna do with list <dellis/showtd/addtd/deltd>:")
        if cmd == 'showtd':
            pass
        elif cmd == 'dellis':
            lisman.deleteList()
        elif cmd == 'addtd':
            pass
        elif cmd == 'deltd':
            pass
        else:
            pass

    elif cmd == 'exit':
        sys.exit()
    else:
        print('Command not found!!!')
        


#jsere = me.toJSON()
#print(jsere)