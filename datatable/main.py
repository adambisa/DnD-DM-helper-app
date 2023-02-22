import flet as ft
from header import AppHeader
from form import AppForm

def main(page:ft.Page):
    page.bgcolor='#fdfdfd'
    page.padding=20
    page.add(
        ft.Column(
            expand=True,
            controls=[
                AppHeader(),
                ft.Divider(height=2, color='transparent'),
                AppForm()
            ]
        )
    )
    page.update()
ft.app(target=main)