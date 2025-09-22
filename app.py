import flet as ft

def main(page:ft.Page):
    page.tittle = "финансовый трекер"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1200
    page.window_height = 800
    page.update()

    ft.app(target=main)