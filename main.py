from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

from datos import *


class ProgressFormApp(App):
    login_name = ""
    login_password = ""
    login_email = ""
    login_birthdate = ""
    box = BoxLayout(orientation='vertical')
    lbl = Label(text="Usuario ya existente")
    btn = Button(text="Volver")
    box.add_widget(lbl)
    box.add_widget(btn)
    popupUsuarioExistente = Popup(title='Registro Login', content=box, auto_dismiss=False, size_hint=(.6, .8))
    btn.bind(on_press=popupUsuarioExistente.dismiss)

    def crear_tabla(self):
        return ProgressDao.crear_tabla()

    def agregar_usuario(self, nombre, contrasenia, mail, nacimiento):
        filaModificada = ProgressDao.agregar_usuario(nombre, contrasenia, mail, nacimiento)
        if filaModificada != 0:
            self.login_name = nombre
            self.login_password = contrasenia
            self.login_email = mail
            self.login_birthdate = nacimiento

    def login(self, name, password):
        user = ProgressDao.login(name, password)
        if user:
            self.login_name = user[0]
            self.login_password = user[1]
            self.login_email = user[2]
            self.login_birthdate = user[3]
        return user

    def find_user(self, name):
        user = ProgressDao.find_user(name)
        return user

    def update_usuario(self, nombre, contrasenia, mail, fecha_nacimiento):
        filaModificada = ProgressDao.update_usuario(nombre, contrasenia, mail, fecha_nacimiento)
        user = ProgressDao.login(nombre, contrasenia)
        if user:
            self.login_name = user[0]
            self.login_password = user[1]
            self.login_email = user[2]
            self.login_birthdate = user[3]
        return filaModificada

    def delete_user(self, nombre):
        filaModificada = ProgressDao.delete_user(nombre)
        return filaModificada


if __name__ == '__main__':
    ProgressFormApp().run()
