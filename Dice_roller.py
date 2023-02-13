import flet as ft
from random import randint

def main(page:ft.Page):
    page.title='DM TOOLz'
    headercont=ft.Container(content=ft.Text('DM TOOLz',size=46,color=ft.colors.WHITE,),bgcolor=ft.colors.AMBER, height=140)
    headercont.alignment=ft.alignment.center
    result=ft.Text(value=' ', color=ft.colors.WHITE, size=42)
    def roll_num(d):
        
        result.value=str(randint(1,int(d.control.data)))
        page.update()
    
        
    dice=ft.GridView(expand=2,
        runs_count=3,
        max_extent=150,
        child_aspect_ratio=1.9,
        spacing=10,
        run_spacing=3,
        padding=10)

    dice.controls.append(ft.ElevatedButton(text='D4', on_click=roll_num, data='4'))
    dice.controls.append(ft.ElevatedButton(text='D6', on_click=roll_num, data='6'))
    dice.controls.append(ft.ElevatedButton(text='D8', on_click=roll_num, data='8'))
    dice.controls.append(ft.ElevatedButton(text='D10', on_click=roll_num, data='10'))
    dice.controls.append(ft.ElevatedButton(text='D12', on_click=roll_num, data='12'))
    dice.controls.append(ft.ElevatedButton(text='D20', on_click=roll_num, data='20'))
    dice_header=ft.Container(content=ft.Text('ROLL SOME DICE!', size=28, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER), bgcolor=ft.colors.AMBER, height=56, width=350, border_radius=10)
    dice_options=ft.Container(content=dice,bgcolor=ft.colors.AMBER, height=350, width=350, border_radius=10)
    dice_result=ft.Container(content=ft.Row([ft.Text('You rolled a : ',color=ft.colors.WHITE, size=44),result]),bgcolor=ft.colors.AMBER, height=140, width=350, border_radius=10)
    dicecolumn=ft.Column([dice_header,dice_options,dice_result],col=6)
    
    


    page.add(headercont,dicecolumn)
ft.app(target=main)
