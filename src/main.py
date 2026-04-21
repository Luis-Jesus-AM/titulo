import flet as ft
from clientes import vista_clientes
from pedidos import vista_pedidos
from resumen import vista_resumen

def main(page: ft.Page):
    page.title = "App Emprendedores"
    page.window_width = 1000
    page.window_height = 650
    page.bgcolor = "#F5F7FA"

    # 🔥 crear vistas UNA sola vez
    vista1 = vista_pedidos(page)
    vista2 = vista_clientes(page)
    vista3 = vista_resumen(page)

    contenido = ft.Container(content=vista1, expand=True)

    def cambiar_vista(e):
        if e.control.selected_index == 0:
            contenido.content = vista1
        elif e.control.selected_index == 1:
            contenido.content = vista2
        elif e.control.selected_index == 2:
            contenido.content = vista3

        page.update()

    menu = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=80,
        extended=True,
        bgcolor="#FFFFFF",
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.SHOPPING_CART,
                label="Pedidos"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PEOPLE,
                label="Clientes"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.BAR_CHART,
                label="Resumen"
            ),
        ],
        on_change=cambiar_vista
    )

    page.add(
        ft.Row(
            [
                menu,
                ft.VerticalDivider(width=1),
                contenido
            ],
            expand=True
        )
    )

ft.app(target=main)