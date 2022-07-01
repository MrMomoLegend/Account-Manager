from pickle import load, dump
from tkinter import *
from os import getcwd as dire

path = dire() + r'\\savefile.dat'

# User Interface
win = Tk()
win.title("Account Manager")
win.geometry('450x200')

# Input from the user
nvar = StringVar()
pvar = StringVar()
rpvar = StringVar()

# importing the passwords and usernames and storing in variable
with open(fr'{path}', 'wb+') as x:
    try:
        data = load(x)
        print(data)
        d = data
    except EOFError:
        d = {}


# --------------------------------------------------------------------
# Frontend


def signin():
    clear()
    head = Label(text="Signin")
    head.pack()
    Label(text='Username:').place(x=40, y=40)
    Label(text='Password:').place(x=40, y=80)
    Entry(width=30, textvariable=nvar).place(x=130, y=40)  # username
    Entry(width=30, textvariable=pvar, show='*').place(x=130, y=80)  # password
    Button(text='Submit', command=lambda: out('signin')).place(x=140, y=130)
    Button(text='Signup', command=signup).place(x=240, y=130)


def signup():
    clear()
    head = Label(text="Signup")
    head.pack()
    Label(text='Username:').place(x=40, y=40)
    Label(text='Password:').place(x=40, y=80)
    Label(text='Re-Enter Password:').place(x=20, y=120)
    Entry(width=30, textvariable=nvar).place(x=130, y=40)  # username
    Entry(width=30, textvariable=pvar, show='*').place(x=130, y=80)  # password
    Entry(width=30, textvariable=rpvar, show='*').place(x=130, y=120)  # re enter password
    Button(text='Submit', command=lambda: out('signup')).place(x=140, y=150)
    Button(text='Signin', command=signin).place(x=240, y=150)


# --------------------------------------------------------------------------------
def out(inorup):
    username = nvar.get()
    password = pvar.get()
    repas = rpvar.get()
    temp = {}
    if inorup == 'signup':
        if username not in d:
            if password == repas:
                temp[username] = password
                d.update(temp)
                with open(fr'{path}', 'wb') as da:
                    dump(d, da)
                clear()
                signin()
            else:
                Label(text='password does not match', font=('Arial', 8), fg='red').place(x=130, y=100)
                rpvar.set('')
        else:
            Label(text='username already exists', font=('Arial', 8), fg='red').place(x=130, y=20)
            pvar.set('')
            rpvar.set('')

    elif inorup == 'signin':
        if username in d:
            a = d[username]

            if a == password:
                clear()
                Label(text='The Secret message is ______', font=25).place(x=50, y=70)
                print("Working")
            else:
                Label(text='wrong password. try again', font=('Arial', 8), fg='red').place(x=130, y=60)
                pvar.set('')
                print('wrong password')
        else:
            Label(text='no username found. try again', font=('Arial', 8), fg='red').place(x=130, y=20)
            print('no username')
            nvar.set('')
            pvar.set('')


def clear():
    for i in win.winfo_children():
        i.destroy()

    nvar.set('')
    pvar.set('')
    rpvar.set('')


if d == {}:
    signup()
else:
    signin()
win.mainloop()
