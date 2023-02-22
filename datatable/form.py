import flet as ft 
from controls import add_to_control_reference


class AppForm(ft.UserControl):
    def __init__(self):
        super().__init__()
    
    
    def app_form_instance(self):
        add_to_control_reference('AppForm', self)
    
    def app_form_input_field(self,name:str,expand:int):
        return ft.Container(
            expand=expand,
            height=45,
            bgcolor=ft.colors.WHITE10,
            border_radius=6,
            padding=8,
            content=ft.Column(
                spacing=1,
                controls=[
                          ft.TextField(border_color='transparent',height=24,text_size=13,
                                       content_padding=0,cursor_color=ft.colors.BLACK,
                                       cursor_width=1,
                                       cursor_height=18,
                                       color=ft.colors.WHITE,
                                       bgcolor=ft.colors.BLACK,
                                       label=name,
                                       )
                          ]
            )
        )
    def build(self):
        self.app_form_instance()
        return ft.Container(
            expand=True,
            height=190,
            bgcolor=ft.colors.WHITE10,
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=8,
            padding=15,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(controls=[self.app_form_input_field('Name * ', 3)]),
                    ft.Row(controls=[self.app_form_input_field('Initiative * ', 1), self.app_form_input_field('Dex * ', 1),self.app_form_input_field('AC * ', 1)]),
                    ft.Row(alignment=ft.MainAxisAlignment.END, controls=[ft.Text('placeholder')])
                    
                ]
                
            )
        )
