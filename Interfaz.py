from tkinter import *
from tkinter import messagebox

def abrir_toplevel_filtro():
    global toplevel_filtro
    toplevel_filtro = Toplevel()
    toplevel_filtro.title("Filtro")
    toplevel_filtro.resizable(False, False)
    toplevel_filtro.geometry("400x400")
    toplevel_filtro.config(bg="white")

    # etiqueta para valor en centigrados
    lb_c = Label(toplevel_filtro, text="Filtro")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18, "bold"))
    lb_c.place(x=20, y=20)

    # caja de texto para valor en centigrados
    entry_c = Entry(toplevel_filtro, textvariable=f)
    entry_c.config(bg="#E0E0E0", fg="black", font=("Arial", 14), relief="solid", borderwidth=1)
    entry_c.focus_set()
    entry_c.place(x=100, y=25)




ventana_principal = Tk()
ventana_principal.title("Proyecto")
ventana_principal.geometry("700x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="#FFA07A")  


#Variables
f = StringVar()

#Frame para titulo
frame_titulo = Frame(ventana_principal)
frame_titulo.config(bg="gray", width=680, height=80, relief="solid", borderwidth=2)
frame_titulo.place(x=10, y=10)

# etiqueta para el titulo del proyecto
lb_t = Label(frame_titulo, text="App")
lb_t.config(bg="gray", fg="black", font=("Helvetica", 18, "bold"), padx=10, pady=5, relief="solid", borderwidth=2)
lb_t.place(x=310, y=20)

#Frame para titulo
frame_entrada= Frame(ventana_principal)
frame_entrada.config(bg="gray", width=680, height=390, relief="solid", borderwidth=2)
frame_entrada.place(x=10, y=100)



# boton para abrir Toplevel del filtro
bt_filtro = Button(frame_entrada, text="Filtro", command=abrir_toplevel_filtro)
bt_filtro.config(width=15, height=3, bg="#FFA07A", fg="Black", font=("Arial", 12, "bold"), relief="raised", borderwidth=3)
bt_filtro.place(x=20, y=20)




ventana_principal.mainloop()
