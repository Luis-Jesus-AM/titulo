import flet as ft
from clientes import vista_clientes
from pedidos import vista_pedidos
from resumen import vista_resumen

def main(page: ft.Page):
    page.title = "App Emprendedores"
    page.window_width = 900
    page.window_height = 600

    contenido = ft.Column()

    def cambiar_vista(e):
        if e.control.selected_index == 0:
            contenido.controls = [vista_pedidos()]
        elif e.control.selected_index == 1:
            contenido.controls = [vista_clientes()]
        elif e.control.selected_index == 2:
            contenido.controls = [vista_resumen()]
        page.update()

    menu = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
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

    contenido.controls = [vista_pedidos()]

    page.add(
        ft.Row(
            [
                menu,
                ft.VerticalDivider(width=1),
                ft.Container(content=contenido, expand=True, padding=20)
            ],
            expand=True
        )
    )

ft.app(target=main)