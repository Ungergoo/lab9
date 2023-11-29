from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import json
import sys
import os

incorrect = ('!@#$%^&*+_-=|/?><~`[]±§')
passwords = []
logins = []
data = []

try:
    with open('users.json', 'r') as file:
        data = json.load(file)
except:
    pass

def log():
    login_get = login.get()
    password_get = password.get()
    try:
        with open('users.json', 'r') as file:
            data = json.load(file)
            print(data)
            for l in data:
                if l['login'] == login_get and l['password'] == password_get:
                    messagebox.showinfo(message='вы вошли')
                    sys.exit()
                    break
                    
            else:
                messagebox.showinfo(message='неправильный логин или пароль')
    except FileNotFoundError:
        print('Базы данных не создана, для начала зарегестрируйтесь')
        
def reg():
    global data
    login_check = False
    password_check = False
    login_get = login.get()
    password_get = password.get()
    for items in data:
        if items['login'] == login_get:
            messagebox.showwarning(message='такой пользователь уже есть, войдите если это вы')
            break
    else:
        if len(login_get) < 5:
            messagebox.showinfo(message='Длинна логина должна быть не менее 5 символов!')
            login_check = False
        else:
            for i in login_get:
                if i not in incorrect:
                    login_check = True
                else:
                    messagebox.showinfo(message='Недопустимый символ в логине=> ' +  i)
                    login_check = False
                    break
            else:
                login_check = True
        if len(password_get) < 6:
            messagebox.showinfo(message='Пароль должен быть длинной не менее 6 символов!')
            password_check = False
        else:
            for j in password_get:
                if j not in incorrect:
                    password_check = True
                else:
                    messagebox.showinfo(message='Недопустимый символ в пароле=> ' +  j)
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
root.title('Вход/регистрация')
root.geometry("400x150")
root.resizable(width=False, height=False)
root.configure(bg = '#009999')

log_label = tk.Label(bg = '#009999', text='Логин')
log_label.pack()
login = Entry(root, bg = '#006363')
login.pack()

password_label = tk.Label(bg = '#009999', text='Пароль')
password_label.pack()
password = Entry(root, bg = '#006363')
password.pack()

btn_log = Button(root, text='Войти', bg = '#006363', fg = 'white', command=log)
btn_log.pack()

btn_reg = Button(root, text='Зарегестрироваться', bg = '#006363', fg = 'white', command=reg)
btn_reg.pack()

root.mainloop()