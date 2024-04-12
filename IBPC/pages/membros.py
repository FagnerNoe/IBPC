from flet import *
from flet_route import Params,Basket




titulo = Container(
   width=800,
   height=120,
   bgcolor=colors.BROWN_600,
   border_radius=BorderRadius(0,0,0,60),
   padding=Padding(20,30,30,20),
   content=Text("Cadastro de Membros",          
                size=34,
                color="White",
                text_align=TextAlign.CENTER,
                style=TextStyle(
                   font_family="Poppins",
                   weight=FontWeight.BOLD,
                   decoration=TextDecoration.UNDERLINE))
   )

def membros(page:Page,params:Params,basket:Basket):
    


    janela=Container(
         width=830,
         height=680,
         content=(
            Column(
               controls=[
                     titulo,                  
 
               ]
            )
         )     
      )


    return janela
    