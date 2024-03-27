from tkinter import *
from tkinter import ttk
import os

root = Tk()
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("800x600+400+100")


style = ttk.Style(root)
style.configure('Treeview', font=('Bold', 14))

drives = ['C://']

valid_drives = []

browse_dir = []

def i_drives():
    for i in side_tab.get_children():
        side_tab.delete(i)

    for r in range(len(valid_drives)):
        side_tab.insert(parent='', iid=r, text='', values=[valid_drives[r]], index='end')

def f_v_drives():
    for drive in drives:
        if os.path.exists(drive):
            valid_drives.append(drive)

    i_drives()


def insert_folders(path):
    global browse_dir
    for i in main_tab.get_children():
        main_tab.delete(i)

    folders = os.listdir(path)

    browse_dir = []

    for r in range(len(folders)):
        main_tab.insert(parent='', iid=r, text='', values=[folders[r]], index='end')
        browse_dir.append(str(path) + '/' + folders[r])

def open_d():
    index = int(side_tab.selection()[0])

    path = valid_drives[index]
    insert_folders(path)

    root.title(path)

def insert_files(path):
    global browse_dir
    for i in main_tab.get_children():
        main_tab.delete(i)

    files = os.listdir(path)

    browse_dir = []

    for r in range(len(files)):
        main_tab.insert(parent='', iid=r, text='', values=[files[r]], index='end')
        browse_dir.append(str(path) + '/' + files[r])

def open_f():
    index = int(main_tab.selection()[0])

    path = browse_dir[index]

    if os.path.isdir(path):
        insert_files(path)
        root.title(path)
    else:
        os.system('"%s"' % path)

def get_back():
    global browse_dir
    for i in main_tab.get_children():
        main_tab.delete(i)

    path = root.title()
    gi = path[::-1]
    i = gi.find("/")
    ne = gi[i + 1:]
    path = ne[::-1]
    files = os.listdir(path)

    browse_dir = []

    for r in range(len(files)):
        main_tab.insert(parent='', iid=r, text='', values=[files[r]], index='end')
        browse_dir.append(str(path) + '/' + files[r])

    root.title(path)

def sozdat(entry, radio_get, nw):
    result = entry.get("1.0", "end")
    new_res = result[:-1]
    path = root.title()
    if radio_get == 1:
        with open(path + '/' + new_res + ".txt", 'w') as fil:
            pass
    elif radio_get == 2:
        path1 = path + "/" + new_res
        os.mkdir(path1)
    nw.destroy()
    insert_files(path)

def pereimenovat(entry, path, nw):
    result = entry.get("1.0", "end")
    new_res = result[:-1]
    path1 = root.title()
    if os.path.isdir(path):
        path2 = path1 + "/" + new_res
        os.rename(path, path2)
    else:
        path2 = path1 + "/" + new_res + ".txt"
        os.rename(path, path2)
    nw.destroy()
    insert_files(path1)

def create_file():
    radio = IntVar()
    newWindow = Toplevel(root)
    newWindow.geometry(f'300x200+1000+200')
    newWindow.title("Окно создания файла")
    labNew = Label(newWindow, text="Выберите что будете создавать")
    r1 = Radiobutton(newWindow, text="Файл", variable=radio, value=1)
    r2 = Radiobutton(newWindow, text="Дирректорию", variable=radio, value=2)
    lab1 = Label(newWindow, text="Напишите название")
    entry = Text(newWindow)
    buttonExample = Button(newWindow, text="Создать", command=lambda: sozdat(entry, radio.get(), newWindow))
    labNew.place(x=50, y=0, width=200, height=50)
    r1.place(x=30, y=40, width=100, height=40)
    r2.place(x=140, y=40, width=100, height=40)
    lab1.place(x=50, y=70, width=200, height=40)
    entry.place(x=50, y=100, width=200, height=40)
    buttonExample.place(x=50, y=150, width=200, height=40)

def delete():
    index = int(main_tab.selection()[0])

    path = browse_dir[index]

    if os.path.isdir(path):
        os.rmdir(path)
    else:
        os.remove(path)
    path1 = root.title()
    insert_files(path1)

def rename():
    index = int(main_tab.selection()[0])
    path = browse_dir[index]
    newWindow = Toplevel(root)
    newWindow.geometry(f'300x150+1000+200')
    newWindow.title("Окно переименования файла файла")
    lab1 = Label(newWindow, text="Напишите новое название")
    entry = Text(newWindow)
    buttonExample = Button(newWindow, text="Переименовать", command=lambda: pereimenovat(entry, path, newWindow))
    lab1.place(x=50, y=0, width=200, height=50)
    entry.place(x=50, y=40, width=200, height=40)
    buttonExample.place(x=50, y=100, width=200, height=40)

def svoistva():
    index = int(main_tab.selection()[0])

    path = browse_dir[index]
    newWindow = Toplevel(root)
    if os.path.isdir(path):
        lab1 = Label(newWindow, text=("Название:", browse_dir[index]))
        lab2 = Label(newWindow, text=("Тип: Директория"))
        lab3 = Label(newWindow, text=("Путь:", path))
        lab4 = Label(newWindow, text=("Размер Дирректории:", os.stat(path).st_size, "Байт"))
        lab5 = Label(newWindow, text=("Время последнего изменения:", os.stat(path).st_mtime))
        lab1.pack()
        lab2.pack()
        lab3.pack()
        lab4.pack()
        lab5.pack()

    else:
        lab1 = Label(newWindow, text=("Название:", browse_dir[index]))
        lab2 = Label(newWindow, text=("Тип: Файл"))
        lab3 = Label(newWindow, text=("Путь:", path))
        lab4 = Label(newWindow, text=("Размер Дирректории:", os.stat(path).st_size, "Байт"))
        lab5 = Label(newWindow, text=("Время последнего изменения:", os.stat(path).st_mtime))
        lab1.pack()
        lab2.pack()
        lab3.pack()
        lab4.pack()
        lab5.pack()


side_tab = ttk.Treeview(root)
side_tab['column'] = ['Drives']
side_tab.column('#0', anchor=W, width=0, stretch=NO)
side_tab.column('Drives', anchor=W, width=200)
side_tab.heading('Drives', text='Drives', anchor=W)
side_tab.pack(side=LEFT, anchor=W, fill=Y)
side_tab.bind('<<TreeviewSelect>>', lambda e: open_d())

main_tab = ttk.Treeview(root)
main_tab['column'] = ['Files']
main_tab.column('#0', anchor=W, width=0, stretch=NO)
main_tab.column('Files', anchor=W, width=500)
main_tab.heading('Files', text='Files', anchor=W)
main_tab.pack(side=LEFT, anchor=W, fill=Y)
main_tab.bind('<Double-Button-1>', lambda e: open_f())
main_tab.bind('<BackSpace>', lambda e: get_back())

btn = ttk.Button(text="Back", command=lambda: get_back()).pack()
btn1 = ttk.Button(text="Создать файл", command=lambda: create_file()).pack()
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Удалить", command=delete)
context_menu.add_command(label="Переименовать", command=rename)
context_menu.add_separator()
context_menu.add_command(label="Своийства", command=svoistva)
root.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))

f_v_drives()
root.mainloop()
