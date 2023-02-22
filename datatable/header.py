import flet as ft
from controls import add_to_control_reference,return_control_reference


control_map=return_control_reference()

class AppHeader(ft.UserControl):
    def __init__(self):
        super().__init__()
    def app_header_instance(self):
        add_to_control_reference('AppHeader', self)
        
        
    def app_header_brand(self):
        return ft.Container(
            content=ft.Text('Initiative Tracker', size=15, color=ft.colors.WHITE)
            
        )
        
    def app_header_search(self):
        return ft.Container(
            width=320,
            bgcolor=ft.colors.WHITE10,
            border_radius=6,
            padding=8,
            content=ft.Row(
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[ft.Icon(ft.icons.SEARCH, size=17, opacity=0.85),
                          ft.TextField(hint_text='Search', border_color='transparent',height=20,text_size=14,content_padding=0,cursor_color='white',cursor_width=1,color='white'
                                       #on_change=lambda e:self.filter_data_table(e)
                                       )],
                
            )
            
        )
    def app_header_avatar(self):
        return ft.Container(
            content=ft.IconButton(ft.icons.PERSON)
        )
    def show_searchbar(self, e):
        if e.data=='true':
            self.controls[0].content.controls[1].opacity=1
            self.controls[0].content.controls[1].update()
        else:
            self.controls[0].content.controls[1].content.controls[1].value =''
            self.controls[0].content.controls[1].opacity=0
            self.controls[0].content.controls[1].update()
            
    def build(self):
        self.app_header_instance()
        return ft.Container(
            expand=True,
            on_hover=lambda e:self.show_searchbar(e),
            height=60,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.only(topLeft=15, topRight=15),
            padding=ft.padding.only(left=15,right=15),
            content=ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[self.app_header_brand(),self.app_header_search(),self.app_header_avatar()],
            )
        )