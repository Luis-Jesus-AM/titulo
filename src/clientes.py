import flet as ft

def vista_clientes():

    lista_clientes = ft.Column()

    def agregar_cliente(e):
        lista_clientes.controls.append(
            ft.Text(f"{nombre.value} - {telefono.value}")
        )
        nombre.value = ""
        telefono.value = ""
        lista_clientes.update()

    nombre = ft.TextField(label="Nombre")
    telefono = ft.TextField(label="Teléfono")

    return ft.Column([
        ft.Text("Clientes", size=25, weight="bold"),
        nombre,
        telefono,
        ft.ElevatedButton("Agregar Cliente", on_click=agregar_cliente),
        ft.Divider(),
        lista_clientes
    ])