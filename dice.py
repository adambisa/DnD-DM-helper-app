import flet
from flet import Page,border_radius,UserControl,Text,colors,TextField,IconButton,ElevatedButton,Container,Row,Column,GridView,TextAlign,alignment,MainAxisAlignment,icons
from random import randint


class DiceRoller(UserControl):
    def build(self):
        #self.reset()
        self.result = Text(value='0', color=colors.WHITE, size=20)
        self.txt_number = Text(value='1', color=colors.WHITE, size=20)
        return Container(
            width=350,
            bgcolor=colors.AMBER,
            border_radius=border_radius.all(20),
            content=Column(
                [
                Row([
                     Text('ROLL SOME DICE!', color=colors.WHITE, size=42)
                ]),
                Row([ElevatedButton(text='D4', on_click=self.roll_num, data='4'),
                              ElevatedButton(text='D6', on_click=self.roll_num, data='6'),
                              ElevatedButton(text='D8', on_click=self.roll_num, data='8'),
                        ], alignment=MainAxisAlignment.CENTER),
                Row([ElevatedButton(text='D10', on_click=self.roll_num, data='10'),
                              ElevatedButton(text='D12', on_click=self.roll_num, data='12'),
                              ElevatedButton(text='D20', on_click=self.roll_num, data='20')], alignment=MainAxisAlignment.CENTER),
                Row([IconButton(icons.REMOVE, on_click=self.minus_click),self.txt_number,IconButton(icons.ADD, on_click=self.plus_click)], alignment=MainAxisAlignment.CENTER),
                Row([Text('You rolled a : ', size=42, color=colors.WHITE), self.result])
          
                    
                ]
            )
        )
    def roll_num(self,d):
        res=0
        for i in range(int(self.txt_number.value)):
            res+=randint(1, int(d.control.data))
        self.result.value=res
        self.update()

    def minus_click(self,e):
        
        if int(self.txt_number.value)>1:   
            self.txt_number.value = str(int(self.txt_number.value) - 1)
        self.update()

    def plus_click(self,e):
        self.txt_number.value = str(int(self.txt_number.value) + 1)
        self.update()
        
def main(page:Page):
    page.title='Dice Roller'
    roller=DiceRoller()
    page.add(roller)
flet.app(target=main)