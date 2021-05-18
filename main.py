from dbhelper import DBHelper

from tkinter import *

db = DBHelper()
root = Tk()
root.title('Quizlett')
root.geometry("700x550")
#root.resizable(width = False, height = False)


tk_ss = Entry(root, width = 30)
tk_ss.grid(row = 0, column = 1, padx = 20, pady = 5)
tk_ssLabel = Label(root, text = "New study set")
tk_ssLabel.grid(row = 0, column = 0)

tk_ssIdDel = Entry(root, width = 30)
tk_ssIdDel.grid(row = 2, column = 1, pady = 5)
tk_ssIdDelLabel = Label(root, text = "Study set ID")
tk_ssIdDelLabel.grid(row = 2, column = 0)

tk_ssIdUpd = Entry(root, width = 30)
tk_ssIdUpd.grid(row = 4, column = 1)
tk_ssIdUpdLabel = Label(root, text = "Study set ID")
tk_ssIdUpdLabel.grid(row = 4, column = 0)
tk_newSs = Entry(root, width = 30)
tk_newSs.grid(row = 5, column = 1, pady = 5)
tk_newSsLabel = Label(root, text = "Rename")
tk_newSsLabel.grid(row = 5, column = 0)

#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
tk_ssword = Entry(root, width = 30)
tk_ssword.grid(row = 0, column = 4, padx = 20, pady = 5)
tk_sswordLabel = Label(root, text = "Study set Id")
tk_sswordLabel.grid(row = 0, column = 3)
tk_word = Entry(root, width = 30)
tk_word.grid(row = 1, column = 4, pady = 5)
tk_wordLabel = Label(root, text = "Word")
tk_wordLabel.grid(row = 1, column = 3)
tk_def = Entry(root, width = 30)
tk_def.grid(row = 2, column = 4, pady = 5)
tk_defLabel = Label(root, text = "Definition")
tk_defLabel.grid(row = 2, column = 3)

tk_sswordIdDel = Entry(root, width = 30)
tk_sswordIdDel.grid(row = 4, column = 4, pady = 20)
tk_sswordIdDelLabel = Label(root, text = "Study set ID")
tk_sswordIdDelLabel.grid(row = 4, column = 3)
tk_wordIdDel = Entry(root, width = 30)
tk_wordIdDel.grid(row = 5, column = 4, pady = 5)
tk_wordIdDelLabel = Label(root, text = "Word ID")
tk_wordIdDelLabel.grid(row = 5, column = 3)


tk_sswordIdUpd = Entry(root, width = 30)
tk_sswordIdUpd.grid(row = 7, column = 4)
tk_sswordIdUpdLabel = Label(root, text = "Study set ID")
tk_sswordIdUpdLabel.grid(row = 7, column = 3)
tk_wordIdUpd = Entry(root, width = 30)
tk_wordIdUpd.grid(row = 8, column = 4, pady = 5)
tk_wordIdUpdLabel = Label(root, text = "Word ID")
tk_wordIdUpdLabel.grid(row = 8, column = 3)
tk_newWord = Entry(root, width = 30)
tk_newWord.grid(row = 9, column = 4, pady = 5)
tk_newWordLabel = Label(root, text = "New word")
tk_newWordLabel.grid(row = 9, column = 3)
tk_newDef = Entry(root, width = 30)
tk_newDef.grid(row = 10, column = 4, pady = 5)
tk_newDefLabel = Label(root, text = "New definition")
tk_newDefLabel.grid(row = 10, column = 3)

def submitAdd1():
    print(tk_ss.get())
    db.insert_studySet(tk_ss.get())
    tk_ss.delete(0, END)
    


def submitDel1():
    print(tk_ssIdDel.get())
    db.delete_studySet(tk_ssIdDel.get())
    tk_ssIdDel.delete(0, END)


def submitUpd1():
    print(tk_ssIdUpd.get())
    print(tk_newSs.get())
    db.update_studySet(tk_ssIdUpd.get(), tk_newSs.get())
    tk_ssIdUpd.delete(0, END)
    tk_newSs.delete(0, END)

def submitShow1():
    print("all")
    res = db.fetch_all_studySet()
    id = 0
    top = Toplevel()
    top.geometry("200x200")
    w = Label(top, text ='List of study sets', font = "50")
    w.pack()
    scroll_bar = Scrollbar(top)
    scroll_bar.pack( side = RIGHT, fill = Y)

    mylist = Listbox(top, yscrollcommand = scroll_bar.set)
    for r in res:
        mylist.insert(END, "Id: "+ str(r[0]))
        mylist.insert(END, "Title: "+ r[1])
        mylist.insert(END, "------------")
    mylist.pack(side = LEFT, fill = BOTH)

    scroll_bar.config(command = mylist.yview)

#>>>>>
def submitAdd2():
    print(tk_ssword.get())
    print(tk_word.get())
    print(tk_def.get())
    db.insert_word(tk_ssword.get(), tk_word.get(), tk_def.get())
    tk_ssword.delete(0, END)
    tk_word.delete(0, END)
    tk_def.delete(0, END)

def submitDel2():
    print(tk_sswordIdDel.get())
    print(tk_wordIdDel.get())
    db.delete_word(tk_sswordIdDel.get(), tk_wordIdDel.get())
    tk_sswordIdDel.delete(0, END)
    tk_wordIdDel.delete(0, END)

def submitUpd2():
    print(tk_sswordIdUpd.get())
    print(tk_wordIdUpd.get())
    print(tk_newWord.get())
    print(tk_newDef.get())
    db.update_word(tk_sswordIdUpd.get(), tk_wordIdUpd.get(), tk_newWord.get(), tk_newDef.get())
    tk_sswordIdUpd.delete(0, END)
    tk_wordIdUpd.delete(0, END)
    tk_newWord.delete(0, END)
    tk_newDef.delete(0, END)

def submitShow2():
    print("all")
    res = db.fetch_all_word()
    print(res)
    top = Toplevel()
    top.geometry("200x200")
    w = Label(top, text ='Wordlist', font = "50")
    w.pack()
    scroll_bar = Scrollbar(top)
    scroll_bar.pack(side = RIGHT, fill = Y)

    mylist = Listbox(top, yscrollcommand = scroll_bar.set)
    for r in res:
        mylist.insert(END, "ID: "+ str(r[0]))
        mylist.insert(END, "Study Set Id: "+ str(r[1]))
        mylist.insert(END, "Word: "+ r[2])
        mylist.insert(END, "Definition: "+ r[3])
        mylist.insert(END, "------------")
    mylist.pack( side = LEFT, fill = BOTH)

    scroll_bar.config(command = mylist.yview)

addButton1 = Button(root, text = "Add", command = submitAdd1, bg = '#3399FF', fg = 'white')
addButton1.grid(row = 1, column = 1, columnspan = 2, ipadx = 20)
deleteButton1 = Button(root, text = "Delete", command = submitDel1, bg = '#3399FF', fg = 'white')
deleteButton1.grid(row = 3, column = 1, columnspan = 2, ipadx = 20)
updateButton1 = Button(root, text = "Update", command = submitUpd1, bg = '#3399FF', fg = 'white')
updateButton1.grid(row = 6, column = 1, columnspan = 2, padx = 10, ipadx = 20)
showButton1 = Button(root, text = "Show all", command = submitShow1, bg = '#3399FF', fg = 'white')
showButton1.grid(row = 7, column = 1, columnspan = 2, pady = 5, padx = 10, ipadx = 20)

addButton2 = Button(root, text = "Add", command = submitAdd2, bg = '#FF6699', fg = 'white')
addButton2.grid(row = 3, column = 4, columnspan = 2, ipadx = 20)
deleteButton2 = Button(root, text = "Delete", command = submitDel2, bg = '#FF6699', fg = 'white')
deleteButton2.grid(row = 6, column = 4, columnspan = 2, pady = 5, ipadx = 20)
updateButton2 = Button(root, text = "Update", command = submitUpd2, bg = '#FF6699', fg = 'white')
updateButton2.grid(row = 11, column = 4, columnspan = 2, pady = 5, padx = 10, ipadx = 20)
showButton2 = Button(root, text = "Show all", command = submitShow2, bg = '#FF6699', fg = 'white')
showButton2.grid(row = 12, column = 4, columnspan = 2, pady = 5, padx = 10, ipadx = 20)

tk_topic = Entry(root, width = 30)
tk_topic.grid(row = 9, column = 1, pady = 5)
tk_topicLabel = Label(root, text = "Choose study set")
tk_topicLabel.grid(row = 9, column = 0)

def submitLearn():
    
    top = Toplevel()
    top.title('Quiz')
    top.geometry("100x100")
    top.resizable(width = False, height = False)
    data = db.fetch_one_word(int(tk_topic.get()))
    qs = data[0]
    ans = data[1]
    w = Label(top, text = qs, font = "30")
    w.pack()
    scroll_bar = Scrollbar(top)
    scroll_bar.pack( side = RIGHT, fill = Y)

    mylist = Listbox(top, yscrollcommand = scroll_bar.set)
    for i in range (0, 10):
        mylist.insert(END, " ")
    mylist.insert(END, "  " + ans)
    mylist.pack(side = LEFT, fill = BOTH)

    scroll_bar.config(command = mylist.yview)


learnButton = Button(root, text = "Learn", command = submitLearn, bg = '#FF9900', fg = 'white')
learnButton.grid(row = 10, column = 1, columnspan = 1, pady = 5, ipadx = 50)
mainloop()