import flet as ft
from data_store import clientes

def vista_clientes(page: ft.Page):

    # 🎨 colores consistentes
    AZUL = "#2563EB"
    FONDO = "#F5F7FA"
    GRIS = "#6B7280"

    lista = ft.Column(spacing=10)

    def actualizar_lista():
        lista.controls.clear()

        for c in clientes:
            lista.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.Column([
                                    ft.Text(c["nombre"], weight="bold"),
                                    ft.Text(c["telefono"], size=12, color=GRIS),
                                ]),
                                ft.Icon(ft.Icons.PERSON, color=AZUL)
                            ],
                            alignment="spaceBetween"
                        ),
                        padding=15
                    )
                )
            )

        page.update()

    def agregar_cliente(e):
        if nombre.value == "" or telefono.value == "":
            return

        clientes.append({
            "nombre": nombre.value,
            "telefono": telefono.value
        })

        nombre.value = ""
        telefono.value = ""

        actualizar_lista()

        # 🔥 feedback visual
        page.snack_bar = ft.SnackBar(ft.Text("Cliente agregado"))
        page.snack_bar.open = True
        page.update()

    # 🎨 inputs modernos
    nombre = ft.TextField(label="Nombre", border_radius=10, filled=True)
    telefono = ft.TextField(label="Teléfono", border_radius=10, filled=True)

    # 🔥 formulario en card
    formulario = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Registrar cliente", size=18, weight="bold"),
                nombre,
                telefono,
                ft.ElevatedButton(
                    "Agregar Cliente",
                    bgcolor=AZUL,
                    color="white",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10)
                    ),
                    on_click=agregar_cliente
                )
            ], spacing=10),
            padding=20,
            width=350
        )
    )

    # 🔥 lista en card
    lista_clientes = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Clientes registrados", size=18, weight="bold"),
                lista
            ]),
            padding=20,
            expand=True
        )
    )

    # inicializar
    actualizar_lista()

    # 🎯 layout profesional
    return ft.Container(
        bgcolor=FONDO,
        expand=True,
        padding=20,
        content=ft.Column([
            ft.Text("Clientes", size=30, weight="bold"),

            ft.Row(
                [
                    formulario,
                    lista_clientes
                ],
                spacing=20,
                expand=True
            )
        ])
    )