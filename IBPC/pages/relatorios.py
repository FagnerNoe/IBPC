from flet import *
from flet_route import Params,Basket




titulo = Container(
   width=500,
   height=120,
   bgcolor=colors.BROWN_600,
   border_radius=BorderRadius(0,0,0,60),
   padding=Padding(20,30,50,20),
   content=Text("Relatórios",          
                size=34,
                color="White",
                text_align=TextAlign.END,
                style=TextStyle(
                   font_family="Poppins",
                   weight=FontWeight.BOLD,
                   decoration=TextDecoration.UNDERLINE)
               )
   )

corpo = Container(  
   margin=Margin(25,0,20,0),
   width=790,
   height=400,   
   content=Column(
               spacing=2,
               alignment=MainAxisAlignment.SPACE_BETWEEN,
               controls=[
                    Container(                     
                              bgcolor="white",
                             
                              border_radius=BorderRadius(0,0,10,10),
                              padding=Padding(0,0,0,10),
                                          content=Column(                                                
                                             spacing=4,
                                             alignment=MainAxisAlignment.CENTER,
                                             controls=[
                                                Container(
                                                   width=300,
                                                  
                                                   height=500,
                                                   offset=Offset(0,1),                                                  
                                                   bgcolor="grey"
                                                ) 
                                                   
               ]
   )

)  
               ]
   )
)

              
                         
                         

               
               
               
              



def relatorios(page:Page,params:Params,basket:Basket):
    


  


   janela=Container(
         width=830,
         height=680,
         content=(
            Column(
               controls=[
                     titulo,
                     corpo                  
 
               ]
            )
         )     
      )


   return janela
    