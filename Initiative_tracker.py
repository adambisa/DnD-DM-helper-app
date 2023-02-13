import flet as ft


def main(page:ft.Page):
    def add_init(t):
        page.add(ft.Checkbox(label=name_init_dex.value))
        name_init_dex.value=''
        page.update()
    name_init_dex=ft.TextField(hint_text='Who goes next?What is their AC?What is their Dex mod?')
    adder=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_init)
    page.add(name_init_dex,adder)
ft.app(target=main)