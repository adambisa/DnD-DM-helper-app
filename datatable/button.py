import flet as ft
from controls import add_to_control_reference,return_control_reference

control_map=return_control_reference()

def return_form_button():
    return ft.IconButton(icon=ft.icons.SEND_SHARP)