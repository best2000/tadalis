import json
import sys
import os
import shutil

class Todo:
    def __init__(self):
        self.title = None
        self.date = None
        self.notes = None
        self.location = None
        #self.list = None
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class TodoManager:
    def __init__(self):
        self.selecttodo = None
    def addTodo(self):
        td = Todo()
        td.title = input("td title:")
        td.date = input("td date:")
        td.notes = input("td notes:")
        td.location = input("td location:")
        with open('liss/'+ listitle + '/' + td.title + '.json', 'w') as lisf:
            lisf.write(td.toJSON())
    def removeTodo(self):
        try:
            os.remove("liss/" + listitle + '/' + tdtitle + '.json')
        except:
            print("error!")
    def checkTodo(self):
        pass

class List():
    def __init__(self):
        self.title = None
        self.color = None
        self.manager = lisman
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class ListManager():
    def __init__(self):
        self.selectlis = None 
    def createList(self):
        lis = List()
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
        cmd = input("waht u wanna do with list <dellis/showtd/addtd/seltd>:")
        if cmd == 'showtd':
            todoman.checkTodo() #################
        elif cmd == 'dellis':
            lisman.deleteList()
        elif cmd == 'addtd':
            todoman.addTodo() ###################
        elif cmd == 'seltd':
            tdtitle = input("which td <title>:")
            todoman.selecttodo = tdtitle 
            cmd = input("waht u wanna do with td <deltd>:")
            if cmd == 'deltd':
                todoman.removeTodo() #################
            else:
                pass
        else:
            pass

    elif cmd == 'exit':
        sys.exit()
    else:
        print('Command not found!!!')
        