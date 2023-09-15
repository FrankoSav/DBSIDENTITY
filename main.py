import tkinter as tk
import sqlite3


class DatabaseGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Base de Datos")
        self.pack(fill=tk.BOTH, expand=True)

        # Conexion a la base de datos
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, edad INTEGER, tarjeta_credito TEXT, dni TEXT, telefono TEXT, direccion TEXT)")

        # Widgets ! 
        self.nombre_label = tk.Label(self, text="Nombre:")
        self.nombre_label.grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        self.edad_label = tk.Label(self, text="Edad:")
        self.edad_label.grid(row=1, column=0, padx=5, pady=5)
        self.edad_entry = tk.Entry(self)
        self.edad_entry.grid(row=1, column=1, padx=5, pady=5)

        self.tarjeta_credito_label = tk.Label(self, text="Tarjeta de Crédito:")
        self.tarjeta_credito_label.grid(row=3, column=0, padx=5, pady=5)
        self.tarjeta_credito_entry = tk.Entry(self)
        self.tarjeta_credito_entry.grid(row=3, column=1, padx=5, pady=5)

        self.dni_label = tk.Label(self, text="DNI:")
        self.dni_label.grid(row=4, column=0, padx=5, pady=5)
        self.dni_entry = tk.Entry(self)
        self.dni_entry.grid(row=4, column=1, padx=5, pady=5)

        self.telefono_label = tk.Label(self, text="Teléfono:")
        self.telefono_label.grid(row=5, column=0, padx=5, pady=5)
        self.telefono_entry = tk.Entry(self)
        self.telefono_entry.grid(row=5, column=1, padx=5, pady=5)

        self.direccion_label = tk.Label(self, text="Dirección:")
        self.direccion_label.grid(row=6, column=0, padx=5, pady=5)
        self.direccion_entry = tk.Entry(self)
        self.direccion_entry.grid(row=6, column=1, padx=5, pady=5)

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.grid(row=7, column=0, columnspan=2, pady=10)
        
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=8, column=0, columnspan=3, padx=5, pady=5)
        # Final de widgets

        # Botones !
        self.agregar_btn = tk.Button(
            self.bottom_frame, text="Agregar", command=self.agregar_usuario)
        self.agregar_btn.grid(row=0, column=0, padx=5)

        self.mostrar_btn = tk.Button(
            self.bottom_frame, text="Mostrar", command=self.mostrar_usuarios)
        self.mostrar_btn.grid(row=0, column=1, padx=5)

        self.borrar_btn = tk.Button(
            self.bottom_frame, text="Borrar", command=self.borrar_usuario)
        self.borrar_btn.grid(row=0, column=2, padx=5)



    # Funcion para poder agregar usuarios
    def agregar_usuario(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        tarjeta_credito = self.tarjeta_credito_entry.get()
        dni = self.dni_entry.get()
        telefono = self.telefono_entry.get()
        direccion = self.direccion_entry.get()

        self.c.execute("INSERT INTO usuarios (nombre, edad, tarjeta_credito, dni, telefono, direccion) VALUES (?, ?, ?, ?, ?, ?)", (nombre, edad, tarjeta_credito, dni, telefono, direccion))
        self.conn.commit()
        self.nombre_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self.tarjeta_credito_entry.delete(0, tk.END)
        self.dni_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)

    # Funcion de mostrar los usuarios registrados en la listbox
    def mostrar_usuarios(self):
        usuarios = self.c.execute("SELECT * FROM usuarios").fetchall()
        # Limpiamos la Listbox antes de mostrar los datos
        self.listbox.delete(0, tk.END)
        for usuario in usuarios:
            info_usuario = "ID: {}, Nombre: {}, Edad: {}, Tarjeta de Crédito: {}, DNI: {}, Teléfono: {}, Dirección: {}".format(
                usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6])
            self.listbox.insert(tk.END, info_usuario)
            print(info_usuario)

    # Funcion para borrar un usuario desde la aplicacion
    def borrar_usuario(self):
        seleccionado = self.listbox.curselection()
        if seleccionado:
            index = seleccionado[0]
            usuario = self.listbox.get(index)
            id_usuario = int(usuario.split(',')[0].split(':')[1])
            self.c.execute("DELETE FROM usuarios WHERE id=?", (id_usuario,))
            self.conn.commit()
            self.listbox.delete(index)
        else:
            print("No se ha seleccionado ningún usuario para borrar seleccione 1.")


if __name__ == "__main__":
    root = tk.Tk()
    db_gui = DatabaseGUI(root)
    root.mainloop()
