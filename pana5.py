
from tkinter import Tk, Menu, messagebox, simpledialog

class MenuApp:
    def _init_(self, master):
        self.master = master
        self.crear_menu()
        
    def crear_menu(self):
                
        barra_menus = Menu(self.master)

        # Menú Cálculo en lugar de Excel
        menu_calculo = Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Cálculo", menu=menu_calculo)

        # Opciones dentro del menú Cálculo
        menu_calculo.add_command(label="Todos", command=self.mostrar_todos)
        menu_calculo.add_command(label="Nombre", command=self.mostrar_nombre)
        menu_calculo.add_command(label="Mayores de 18", command=self.mostrar_mayores_18)

        # Opción para salir
        menu_calculo.add_separator()
        menu_calculo.add_command(label="Salir", command=self.salir)

        self.master.config(menu=barra_menus)

    def mostrar_todos(self):
        messagebox.showinfo("Opción seleccionada", "Mostrar todos los datos.")

    def mostrar_nombre(self):
        nombre = simpledialog.askstring("Nombre", "Introduce tu nombre:")
        if nombre:
            messagebox.showinfo("Nombre ingresado", f"Tu nombre es: {nombre}")

    def mostrar_mayores_18(self):
        edad = simpledialog.askinteger("Edad", "Introduce tu edad:")
        if edad is not None:
            if edad >= 18:
                messagebox.showinfo("Acceso permitido", "Eres mayor de 18 años.")
            else:
                messagebox.showwarning("Acceso denegado", "Eres menor de 18 años.")

    def salir(self):
        self.master.quit()

class App:
    def _init_(self):
        self.root = Tk()
        self.root.title("Aplicación con Menú Cálculo")
        
        self.menu_app = MenuApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "_main_":
    app = App()
    app.run()