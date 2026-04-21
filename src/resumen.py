import flet as ft
from data_store import pedidos
from datetime import datetime

def vista_resumen(page: ft.Page):

    # 🎨 colores
    AZUL = "#2563EB"
    VERDE = "#16A34A"
    ROJO = "#DC2626"
    FONDO = "#F5F7FA"

    total = sum(p["precio"] for p in pedidos)
    cantidad = len(pedidos)

    # ⚠️ por ahora todo es pendiente (puedes mejorar luego)
    pendiente = sum(p["precio"] for p in pedidos)

    # 🔥 función corte del día
    def corte_del_dia(e):
        hoy = datetime.now().date()

        total_hoy = sum(
            p["precio"] for p in pedidos
            if p.get("fecha") == hoy
        )

        dialog = ft.AlertDialog(
            title=ft.Text("Corte del día"),
            content=ft.Text(f"Ganancias de hoy: ${total_hoy:.2f}"),
            actions=[
                ft.TextButton(
                    "Cerrar",
                    on_click=lambda e: cerrar_dialog(dialog)
                )
            ]
        )

        page.dialog = dialog
        dialog.open = True
        page.update()

    def cerrar_dialog(dialog):
        dialog.open = False
        page.update()

    # 🎯 cards reutilizables
    def card_titulo_valor(titulo, valor, color):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text(titulo, size=14),
                    ft.Text(valor, size=22, weight="bold", color=color)
                ]),
                padding=20,
                width=200
            )
        )

    return ft.Container(
        bgcolor=FONDO,
        expand=True,
        padding=20,
        content=ft.Column([
            ft.Text("Resumen", size=30, weight="bold"),

            # 🔥 métricas
            ft.Row([
                card_titulo_valor("Ventas totales", f"${total:.2f}", AZUL),
                card_titulo_valor("Pedidos", f"{cantidad}", VERDE),
                card_titulo_valor("Pendiente", f"${pendiente:.2f}", ROJO),
            ], spacing=20),

            ft.Divider(),

            # 🔥 botón corte del día
            ft.ElevatedButton(
                "Corte del día",
                bgcolor=AZUL,
                color="white",
                on_click=corte_del_dia
            ),

            ft.Divider(),

            # 🔥 actividad reciente
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Actividad reciente", size=18, weight="bold"),
                        ft.Column([
                            ft.Text(
                                f"{p['cliente']} compró {p['producto']} - ${p['precio']}"
                            )
                            for p in pedidos[-5:]
                        ])
                    ]),
                    padding=20
                )
            )
        ])
    )