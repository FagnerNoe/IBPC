from flet import *
import flet as ft
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
   width=840,
   height=400,
   padding=padding.all(10),
   content=Row(
      alignment=MainAxisAlignment.SPACE_BETWEEN,
      controls=[
         Container(
            width=400,
            height=400,
            clip_behavior=ClipBehavior.NONE,
            bgcolor=ft.colors.BLACK38,
            border_radius=10,
            padding=padding.all(8),
            content=(
               Column(
                  alignment= MainAxisAlignment.START,
                  horizontal_alignment=CrossAxisAlignment.CENTER,
                  controls=[
                      Container(width=150,
                               offset=Offset(0,-0.6),
                               height=35,
                               border_radius=5,
                               gradient=LinearGradient(colors=["black","brown"]),
                               content=Text("MEMBROS",
                                            color="white",
                                            size=16,
                                            weight=FontWeight.BOLD,
                                            text_align=TextAlign.CENTER)),
                     Row(
                     alignment=MainAxisAlignment.SPACE_EVENLY,
                     controls=[               
                     Column(
                        controls=[                    
                           Checkbox(label="ANIVERSARIANTES"),
                           Checkbox(label="MULHERES"),
                           Checkbox(label="HOMENS"),
                           Checkbox(label="CRIANÇAS"),
                           Checkbox(label="ADOLESCENTES"),
                           Checkbox(label="JOVENS"),
                           Checkbox(label="MEMBROS ATIVOS"),        
                        ]
                     ),
                     Column(
                        controls=[
                           Checkbox(label="MEMBROS NÃO ATIVOS"),
                           Checkbox(label="SEXO FEMININO"),
                           Checkbox(label="SEXO MASCULINO"),
                           Checkbox(label="PROFISSÃO DE FÉ - SIM"),
                           Checkbox(label="PROFISSÃO DE FÉ - NÃO"),
                           Checkbox(label="TODOS OS MEMBROS"),
                           Dropdown(width=180, 
                                    content_padding=5,                                                                   
                                    text_style=TextStyle(
                                       size=14,
                                      
                                       ),
                                    hint_text="ESTADO CIVIL",
                                    hint_style=TextStyle(size=14, color="WHITE"),                                   
                                    height=35,                                                                     
                                    options=[                                      
                                       dropdown.Option("CASADO"),
                                       dropdown.Option("SOLTEIRO"),
                                       dropdown.Option("DIVORCIADO"),
                                       dropdown.Option("VIÚVO"),
                                    ])
                        ]
                     ),
                     ]
                     
                  )
                        ]
                     )
            )
         ),
         Column(
            spacing=25,
            controls=[
            Container(
               width=320,
               height=60,
               margin=Margin(5,0,30,0),               
               clip_behavior=ClipBehavior.NONE,
               bgcolor=ft.colors.BLACK38,
               border_radius=10,                                        
               content=
               Column(
                  spacing=0,
                  alignment=MainAxisAlignment.START,
                  horizontal_alignment=CrossAxisAlignment.START,                  
                  controls=[ 
                      Container(
                               width=150,                              
                               height=35,
                               margin=Margin(50,-15,0,0),
                               border_radius=5,
                               gradient=LinearGradient(colors=["black","brown"]),
                               content=Text("MINISTÉRIOS",
                                            color="white",
                                            size=16,
                                            weight=FontWeight.BOLD,
                                            text_align=TextAlign.CENTER)
                     ),                                        
                     Checkbox(label="MINISTÉRIOS")
                     ]),
            ),
            Container(
               width=320,
               height=60,
               margin=Margin(5,0,30,0),               
               clip_behavior=ClipBehavior.NONE,
               bgcolor=ft.colors.BLACK38,
               border_radius=10,                                        
               content=
               Column(
                  spacing=0,
                  alignment=MainAxisAlignment.START,
                  horizontal_alignment=CrossAxisAlignment.START,                  
                  controls=[ 
                      Container(
                               width=150,                              
                               height=35,
                               margin=Margin(50,-15,0,0),
                               border_radius=5,
                               gradient=LinearGradient(colors=["black","brown"]),
                               content=Text("PATRIMÔNIOS",
                                            color="white",
                                            size=16,
                                            weight=FontWeight.BOLD,
                                            text_align=TextAlign.CENTER)
                     ),                                        
                     Checkbox(label="PATRIMÔNIOS")
                     ]),
            ),
            Container(
               width=320,
               height=90,
               margin=Margin(5,0,30,0),               
               clip_behavior=ClipBehavior.NONE,
               bgcolor=ft.colors.BLACK38,
               border_radius=10,                                        
               content=
               Column(
                  spacing=0,
                  alignment=MainAxisAlignment.START,
                  horizontal_alignment=CrossAxisAlignment.START,                  
                  controls=[ 
                      Container(
                               width=210,                              
                               height=35,
                               margin=Margin(50,-15,0,0),
                               border_radius=5,
                               gradient=LinearGradient(colors=["black","brown"]),
                               content=Text("ATIVIDADES DA IGREJA",
                                            color="white",
                                            size=16,
                                            weight=FontWeight.BOLD,
                                            text_align=TextAlign.CENTER)
                     ),                                        
                     Checkbox(label="ATIVIDADES"),
                     Row(
                        alignment=MainAxisAlignment.SPACE_AROUND,
                        controls=[
                              Dropdown(width=160, 
                                             content_padding=5,                                                                   
                                             text_style=TextStyle(
                                                size=14,                                      
                                                ),                                    
                                             hint_style=TextStyle(size=14, color="WHITE"),                                   
                                             height=26,                                                                     
                                             options=[                                      
                                                dropdown.Option("SEGUNDA"),
                                                dropdown.Option("TERÇA"),
                                                dropdown.Option("QUARTA"),
                                                dropdown.Option("QUINTA"),
                                                dropdown.Option("SEXTA"),
                                                dropdown.Option("SABADO"),
                                                dropdown.Option("DOMINGO"),
                                             ]),
                              Text("DIA DA SEMANA",color='white',size=16)

                              ]),

                     ])
            ),
            Container(
               width=320,
               height=100,
               margin=Margin(5,0,30,0),               
               clip_behavior=ClipBehavior.NONE,
               bgcolor=ft.colors.BLACK38,
               border_radius=10,                                        
               content=
               Column(
                  spacing=0,
                  alignment=MainAxisAlignment.START,
                  horizontal_alignment=CrossAxisAlignment.START,                  
                  controls=[ 
                      Container(
                               width=150,                              
                               height=35,
                               margin=Margin(50,-15,0,-5),
                               border_radius=5,
                               gradient=LinearGradient(colors=["black","brown"]),
                               content=Text("EVENTOS",
                                            color="white",
                                            size=16,
                                            weight=FontWeight.BOLD,
                                            text_align=TextAlign.CENTER)
                     ),                                        
                     Checkbox(label="EVENTOS"),
                     Row(
                        alignment=MainAxisAlignment.SPACE_EVENLY,
                        
                        controls=[
                           Column(
                              spacing=0,
                              controls=[
                              Text("DATA INICIO"),
                              TextField(width=150,height=26,content_padding=5)
                           ]),
                           Column(
                              spacing=0,
                              controls=[
                              Text("DATA FIM"),
                              TextField(width=150,height=26,content_padding=5)
                           ]),
                        ]
                     )
                     ]),
            ),
           
            
         ])
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
    