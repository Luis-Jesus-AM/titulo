import flet as ft
from clientes import vista_clientes
from pedidos import vista_pedidos
from resumen import vista_resumen
from proveedores import vista_proveedores   # 👈 importar proveedores

def main(page: ft.Page):
    page.title = "App Emprendedores"
    page.window_width = 1000
    page.window_height = 650
    page.bgcolor = "#F5F7FA"

    # 🔥 crear vistas UNA sola vez
    vista1 = vista_pedidos(page)
    vista2 = vista_clientes(page)
    vista3 = vista_resumen(page)
    vista4 = vista_proveedores(page)   # 👈 nueva vista

    contenido = ft.Container(content=vista1, expand=True)

    def cambiar_vista(e):
        if e.control.selected_index == 0:
            contenido.content = vista1
        elif e.control.selected_index == 1:
            contenido.content = vista2
        elif e.control.selected_index == 2:
            contenido.content = vista3
        elif e.control.selected_index == 3:   # 👈 manejar proveedores
            contenido.content = vista4

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
                label="Ventas"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PEOPLE,
                label="Clientes"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.BAR_CHART,
                label="Resumen"
            ),
            ft.NavigationRailDestination(   # 👈 nuevo destino
                icon=ft.Icons.WORK,
                label="Proveedores"
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
