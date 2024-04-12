from flet import *
import flet as ft
from flet_route import Params,Basket




    


def login(page:Page,params:Params,basket:Basket):
    
   



    image = Container(

         height=180,
         image_src="assets/images/frente-igreja.jpeg",
            image_fit=ImageFit.COVER,
    )
    
    icone = Container(
         width=85,
         height=85,
         image_src="assets/icons/logo_igreja.jpg",
         border_radius=5,
         shadow=BoxShadow(blur_radius=8,color="grey"),
         clip_behavior=ClipBehavior.NONE,
         scale=Scale(scale=1.6),
         margin=Margin(bottom=15,top=-40,left=0,right=0),
        )

    usuario = TextField(
         height=40,
         border_radius=15,
         content_padding=Padding(8,0,8,0),
         text_style=TextStyle(
             color="black"
         )
         
                 
    )

    senha_usuario = TextField(
         height=40,
         border_radius=15,         
         content_padding=Padding(8,0,8,0),
         text_style=TextStyle(
            color="black"
         ),
         password=True,
         can_reveal_password=True,
          
    )

    btn_login = ElevatedButton(
         width=400,
         height=40,
         elevation=8,       
         bgcolor="brown",
         style=ButtonStyle(
            shadow_color="brown",
            shape=RoundedRectangleBorder(radius=10),
            
         ),
         content=Text("Login",color="white"),
         on_click=lambda _:page.go("/menu")
         
         
    )
    
   
    
    
    return ft.View(
            "/",               
                bgcolor="white",
                horizontal_alignment=CrossAxisAlignment.CENTER,
                vertical_alignment=MainAxisAlignment.CENTER,
                controls=[
                        Container(
                            width=300,
                            height=580,
                            bgcolor="white",
                            shadow=BoxShadow(blur_radius=8,color="black"),
                            border_radius=20,
                            content=Column(
                                scroll = ScrollMode.AUTO,
                                horizontal_alignment = CrossAxisAlignment.CENTER,
                                controls=[
                                    image,
                                    icone,
                                    Text("Login",
                                            style=TextStyle(
                                                size=32,
                                                color="black",
                                                weight=FontWeight.BOLD)),
                                    Container(
                                            width=230,
                                            height=250,        
                                            
                                            content=Column(                                             
                                                horizontal_alignment = CrossAxisAlignment.START,
                                                alignment = MainAxisAlignment.START,
                                                spacing=1,
                                                controls=[
                                                    Text("USUARIO",color="black"),
                                                    usuario,
                                                    Text("SENHA",color="black"),
                                                    senha_usuario,
                                                    Divider(height=40,opacity=0),
                                                    btn_login 
                                                ]
                                            )
                                    )
                                ]
                            )           
                
                        ) 
                ]  

        
        )




        
  

    
   
    

