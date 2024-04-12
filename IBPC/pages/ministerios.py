from flet import *
import flet as ft
from flet_route import Params,Basket




titulo = Container(
   width=800,
   height=120,
   bgcolor=colors.BROWN_600,
   border_radius=BorderRadius(0,0,0,60),
   padding=Padding(20,30,30,20),
   content=Text("Cadastro de Ministérios",          
                size=34,
                color="White",
                text_align=TextAlign.CENTER,
                style=TextStyle(
                   font_family="Poppins",
                   weight=FontWeight.BOLD,
                   decoration=TextDecoration.UNDERLINE))
   )
        
corpo = Container(
   margin=Margin(25,0,20,0),
   width=790,
   height=400,  
  
   content=Column(
               spacing=2,
               alignment=MainAxisAlignment.SPACE_BETWEEN,
               controls=[
               Row(
                  controls=[
               Column(spacing=0,controls=[
               Text("CODIGO",
                    color="black",
                    weight=FontWeight.W_600),
               TextField( 
                  height=30,
                  width=150,
                  content_padding=Padding(8,0,8,0),
                  text_size=16,                  
                  text_style=TextStyle(color="black"),                  
                  cursor_color="brown",
                  
                  keyboard_type=KeyboardType.NUMBER,
                  
                  )
               ]),

               Column(spacing=0,controls=[
               Text("MINISTÉRIO",
                    color="black",
                    weight=FontWeight.W_600),
               TextField(
                  height=30,
                  width=620,
                  content_padding=Padding(8,6,2,0),
                  text_size=16,                  
                  text_style=TextStyle(color="black"),                  
                  cursor_color="brown",
                  keyboard_type=KeyboardType.TEXT,
                  capitalization=TextCapitalization.CHARACTERS,
                  )
               ])
               ]),
               Row(
                  controls=[
               Column(spacing=0,controls=[
               Text("MINISTÉRIO",
                    color="black",
                    weight=FontWeight.W_600),
               TextField( 
                  height=30,
                  width=460,
                  content_padding=Padding(8,0,8,0),
                  text_size=16,                  
                  text_style=TextStyle(color="black",
                                       ),                  
                  cursor_color="brown",                  
                  keyboard_type=KeyboardType.TEXT,
                  capitalization=TextCapitalization.CHARACTERS,
                  )
               ]),

               Column(spacing=3,
                      controls=[
               Divider(height=10,opacity=0),
               ElevatedButton(
                  height=35,
                  width=310,
                  bgcolor=ft.colors.BROWN_800,                  
                  content=Row(
                     alignment=MainAxisAlignment.SPACE_AROUND,
                     controls=[
                     Icon(name=icons.SEARCH,color="white",size=30),
                     Text("LOCALIZAR MINISTÉRIO",color="white",size=18)
                  ]),
                  style=ButtonStyle(
                     shape=RoundedRectangleBorder(
                        radius=8
                     )
                                                       
                  )
               )
               ])
               ]),
               DataTable(width=780,
                         height=250,
                         border_radius=8,
                         vertical_lines=BorderSide(width=1,color="black"),
                         data_row_max_height=28,                        
                         heading_row_height=25,
                         horizontal_lines=BorderSide(width=1,color=ft.colors.GREY_100),
                         border=Border(
                            top=BorderSide(1,color="black"),
                            right=BorderSide(1,color="black"),
                            left=BorderSide(1,color="black"),
                            bottom=BorderSide(1,color="black"),
                            ),
                            columns=[DataColumn(label=Text("CÓDIGO",color="black"),
                                                numeric=True),
                                     DataColumn(label=Text("MINISTÉRIO",color="black"))
                            ],
                            rows=[
                               DataRow(
                               cells=[
                                  DataCell(Text()),
                                  DataCell(Text()),
                               ]),
                               DataRow(
                               cells=[
                                  DataCell(Text()),
                                  DataCell(Text()),
                               ]),
                               DataRow(
                               cells=[
                                  DataCell(Text()),
                                  DataCell(Text()),
                               ]),
                               DataRow(
                               cells=[
                                  DataCell(Text()),
                                  DataCell(Text()),
                               ]),
                               DataRow(
                               cells=[
                                  DataCell(Text()),
                                  DataCell(Text()),
                               ]),
                               DataRow(
                               cells=[
                                  DataCell(Text()),
                                  DataCell(Text()),
                               ]),
                               DataRow(
                               cells=[
                                  DataCell(Text()),
                                  DataCell(Text()),
                               ]),
                               DataRow(
                               cells=[
                                  DataCell(Text()),
                                  DataCell(Text()),
                               ]),
                               
                               
                               ]
                           
                              )
                         
                         

               ]
               ),
               
              

)      

   



     

def ministerios(page:Page,params:Params,basket:Basket):
   

  
      


    
   
   janela=Container(
         width=840,
         height=680,
         content=(
            Column(
               controls=[
                     titulo,
                     corpo,                   
 
               ]
            )
         )     
      )



   return janela


     










      

      
         
      
     
      
     
   
  
   
   
  
    
   
  
   
      
     