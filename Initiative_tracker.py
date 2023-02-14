import flet as ft


def main(page:ft.Page):
    def add_init(t):
        turns.controls.append(ft.Draggable(content=ft.Container(content=ft.Row([ft.Text(name.value), ft.Text(init.value),ft.Text(dex.value)]), bgcolor=ft.colors.BLUE_GREY_100, width=100, height=25)))
        for i in [name,init,dex]:
            i.value=''
        page.update()
    def remove_init(t):
        #somehow remove last item, issue is Draggable is not iterable so we cant pop()
        page.update()
    name=ft.TextField(hint_text='State a name for the character')
    init=ft.TextField(hint_text='State the characters initiative roll')
    dex=ft.TextField(hint_text='State your characters exterity modifier')
    input_data=ft.Row([name,init ,dex])
    
    turns=ft.Column(controls=[])
    
    adder=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_init)
    deleter=ft.FloatingActionButton(icon=ft.icons.REMOVE, on_click=remove_init)
    nice_col=ft.Column([input_data,adder,deleter])
    
    page.add(nice_col, turns)
    '''
    Three text boxes  each for name dex init
    
    Table of data
    
    Sort descending order
    
    Next action button which highlights next fighter    
    '''
ft.app(target=main)