from flet import*
import flet as ft
from pages.login import login as login_page
from pages.menu import menu as menu_page
from flet_route import Routing,path





def main(page:Page): 
    
    page.fonts = {
        "Poppins":"assets/fonts/Poppins-Bold.ttf",
        "Ailerons":"assets/fonts/Ailerons-Typeface.otf",
        "DMSans":"assets/fonts/DMSans-VariableFont_opsz,wght.ttf",
    }
    

    

    routes = [
       path(url="/",clear=True, view=login_page),   
       path(url="/menu",clear=True, view=menu_page), 
    ]

    Routing(page=page,
            app_routes=routes)




    page.go(page.route)




ft.app(target=main)    
    













       

                
             
    
     












    






