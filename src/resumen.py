import flet as ft

def vista_resumen():
    return ft.Column([
        ft.Text("Resumen de Ventas", size=25, weight="bold"),
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Ventas del día: $1200"),
                    ft.Text("Pendiente por cobrar: $850"),
                ]),
                padding=15
            )
        )
    ])