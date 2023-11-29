from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import sys
import os

incorrect = ('!@#$%^&*+_-=|/?><~`[]±§')
passwords = []
logins = []
#!!!
data = []






def log():
    login_get = login.get()
    password_get = password.get()
    with open('users.json', 'r') as file:
        data = json.load(file)
        print("все что было в файле:", data)
        for l in data:
            if l['login'] == login_get and l['password'] == password_get:
                messagebox.showinfo(message='вы вошли')
                #sys.exit()
        
def reg():
    global data
    login_check = False
    password_check = False
    login_get = login.get()
    password_get = password.get()
    if login_get in logins or login_get in data:
        print('iahsbduyabsuydb')
        messagebox.showinfo(message='такой пользователь уже есть, войдите если это вы')
    else:
        if len(login_get) < 5:
            print('Длинна логина должна быть не менее 5 символов!')
            login_check = False
        else:
            for i in login_get:
                if i not in incorrect:
                    login_check = True
                else:
                    print('Недопустимый символ в логине=> ' +  i)
                    login_check = False
                    break
            else:
                login_check = True
        if len(password_get) < 6:
            print('Пароль должен быть длинной не менее 6 символов!')
            password_check = False
        else:
            for j in password_get:
                if j not in incorrect:
                    password_check = True
                else:
                    print('Недопустимый символ в пароле=> ' +  j)
                    password_check = False
                    break
            else:
                if password_check == True and login_check == True:
                    logins.append(login_get)
                    print('Логин: ', logins)
                    passwords.append(password_get)
                    print('Пароль: ', passwords)


                    

                    for x, y in zip(logins, passwords):
                        if x not in 'users.json':
                            data.append({'login': x, 'password': y})
                        with open('users.json', 'w') as file:
                            json.dump(data, file)
                else:
                    pass

        
            

root = Tk()
root.title('hihi')
root.geometry("400x400")
root.resizable(width=False, height=False)

log_label = ttk.Label(text='Логин')
log_label.pack()
login = Entry(root)
login.pack()

password_label = ttk.Label(text='Пароль')
password_label.pack()
password = Entry(root)
password.pack()

btn_log = Button(root, text='Войти', command=log)
btn_log.pack()

btn_reg = Button(root, text='Зарегестрироваться', command=reg)
btn_reg.pack()

root.mainloop()