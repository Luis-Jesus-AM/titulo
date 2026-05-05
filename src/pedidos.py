import flet as ft
from data_store import pedidos, clientes
from datetime import datetime

def vista_pedidos(page: ft.Page):

    # 🎨 colores
    AZUL = "#2563EB"
    FONDO = "#F5F7FA"
    BLANCO = "#FFFFFF"
    GRIS = "#6B7280"

    lista = ft.Column(spacing=10)

    def actualizar_lista():
        lista.controls.clear()

        for p in pedidos:
            lista.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.Column([
                                    ft.Text(p["cliente"], weight="bold"),
                                    ft.Text(p["producto"], size=12, color=GRIS),
                                ]),
                                ft.Text(f"${p['precio']:.2f}", weight="bold")
                            ],
                            alignment="spaceBetween"
                        ),
                        padding=15
                    )
                )
            )

        page.update()

    def agregar_pedido(e):
        if cliente.value == "" or producto.value == "" or precio.value == "":
            return
        
        pedidos.append({
            "cliente": cliente.value,
            "producto": producto.value,
            "precio": float(precio.value),
            "fecha": datetime.now().date()
        })

        cliente.value = ""
        producto.value = ""
        precio.value = ""

        actualizar_lista()

        # 🔥 feedback pro
        page.snack_bar = ft.SnackBar(ft.Text("venta agregado"))
        page.snack_bar.open = True
        page.update()

    # 🎨 inputs modernos
    cliente = ft.TextField(label="Cliente", border_radius=10, filled=True)
    producto = ft.TextField(label="Producto", border_radius=10, filled=True)
    precio = ft.TextField(label="Precio", border_radius=10, filled=True)

    # 🔥 formulario en tarjeta
    formulario = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Registrar venta", size=18, weight="bold"),
                cliente,
                producto,
                precio,
                ft.ElevatedButton(
                    "Agregar Venta",
                    bgcolor=AZUL,
                    color="white",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                    on_click=agregar_pedido
                )
            ], spacing=10),
            padding=20,
            width=350
        )
    )

    # 🔥 lista de ventas en tarjeta
    lista_ventas = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Ventas recientes", size=18, weight="bold"),
                lista
            ]),
            padding=20,
            expand=True
        )
    )

    # inicializar lista
    actualizar_lista()

    # 🎯 layout PRO (lado a lado)
    return ft.Container(
        bgcolor=FONDO,
        expand=True,
        padding=20,
        content=ft.Column([
            ft.Text("Pedidos", size=30, weight="bold"),

            ft.Row(
                [
                    formulario,
                    lista_ventas
                ],
                spacing=20,
                expand=True
            )
        ])
    )