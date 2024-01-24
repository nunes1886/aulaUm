import flet as ft

def main(page: ft.Page):
    page.bgcolor = 'Blue'
    title = ft.Text(value='Nunes Sublimação', size='50', color='white', font_family='arial')
    subtitle = ft.Container(ft.Text(value='Caixa', size='35', color='white', font_family='arial'))
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(title, subtitle)
    page.title = 'Nunes Sublimação'
    

    page.update()

if __name__ == '__main__':
    ft.app(target=main)