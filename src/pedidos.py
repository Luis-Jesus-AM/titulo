import flet as ft

def vista_pedidos():

    lista_pedidos = ft.Column()

    def agregar_pedido(e):
        lista_pedidos.controls.append(
            ft.Text(f"{cliente.value} - {producto.value} - ${precio.value}")
        )
        cliente.value = ""
        producto.value = ""
        precio.value = ""
        lista_pedidos.update()

    cliente = ft.TextField(label="Cliente")
    producto = ft.TextField(label="Producto")
    precio = ft.TextField(label="Precio")

    return ft.Column([
        ft.Text("Pedidos", size=25, weight="bold"),
        cliente,
        producto,
        precio,
        ft.ElevatedButton("Agregar Pedido", on_click=agregar_pedido),
        ft.Divider(),
        lista_pedidos
    ])