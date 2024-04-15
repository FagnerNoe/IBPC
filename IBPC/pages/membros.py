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



corpo = Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(
                text="Pessoal",
                icon=icons.PERSON,
                content=Container(
                    padding=padding.all(10),
                    content=Column(
                        spacing=4,
                        controls=[
                            Row(
                            controls=[
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("CÓDIGO",color="black"),
                                    TextField(
                                        width=80,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("NOME",color="black"),
                                    TextField(
                                        width=550,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("DATA NASCIMENTO",color="black"),
                                    TextField(
                                        width=150,
                                        height=30,
                                        content_padding=5,
                                    )]),
                            ]
                        ),
                            Row(
                            controls=[
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("SEXO",color="black"),
                                    TextField(
                                        width=60,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("ENDEREÇO",color="black"),
                                    TextField(
                                        width=500,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("BAIRRO",color="black"),
                                    TextField(
                                        width=220,
                                        height=30,
                                        content_padding=5,
                                    )]),
                            ]
                        ),
                            Row(
                            controls=[
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("CIDADE",color="black"),
                                    TextField(
                                        width=250,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("CEP",color="black"),
                                    TextField(
                                        width=120,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("UF",color="black"),
                                    TextField(
                                        width=60,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                 Column(
                                    spacing=0,
                                    controls=[
                                    Text("TELEFONE",color="black"),
                                    TextField(
                                        width=160,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                 Column(
                                    spacing=0,
                                    controls=[
                                    Text("CELULAR",color="black"),
                                    TextField(
                                        width=170,
                                        height=30,
                                        content_padding=5,
                                    )]),
                            ]
                        ),
                            Row(
                            controls=[
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("PROFISSÃO",color="black"),
                                    TextField(
                                        width=350,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("EMAIL",color="black"),
                                    TextField(
                                        width=440,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                
                            ]
                        ),
                            Row(
                            controls=[
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("MEMBRO",color="black"),
                                    TextField(
                                        width=200,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("ATIVO",color="black"),
                                    TextField(
                                        width=150,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("PROFISSÃO DE FÉ",color="black"),
                                    TextField(
                                        width=430,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                
                            ]
                        ),
                         Row(
                            controls=[
                                Column(
                                    spacing=0,
                                    controls=[ 
                                    Text("HABILIDADES",color="black"),                                   
                                    TextField(
                                        width=800,
                                        height=30,                                        
                                        content_padding=5,
                                    )]),
                        ])
                        


                        ]
                    )
                ),
            ),
            Tab(
                text="Familia",
                icon=icons.PEOPLE,
                content=Container(
                    padding=padding.all(10),
                    content=Column(
                        spacing=4,
                        controls=[
                            Row(
                            controls=[
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("NOME DO PAI",color="black"),
                                    TextField(
                                        width=330,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("NOME DA MÃE",color="black"),
                                    TextField(
                                        width=330,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("ESTADO CIVIL",color="black"),
                                    TextField(
                                        width=130,
                                        height=30,
                                        content_padding=5,
                                    )]),
                            ]
                        ),
                            Row(
                            controls=[
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("NOME DO CONJUGE",color="black"),
                                    TextField(
                                        width=600,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                Column(
                                    spacing=0,
                                    controls=[
                                    Text("TEM FILHOS?",color="black"),
                                    TextField(
                                        width=200,
                                        height=30,
                                        content_padding=5,
                                    )]),
                                
                            ]
                        ),
                        
                        ]
                    )
                )
            ),
            Tab(            
                tab_content=Icon(icons.SEARCH),                
                content=Container(
                    padding=padding.all(10),
                    content=Column(
                        controls=[
                            Row(
                                controls=[TextField(width=620,
                                          height=30),
                                TextButton(text="LOCALIZAR MEMBROS")
                        ]),
                           DataTable(
                         width=800,
                         height=300,
                         show_bottom_border=True,
                         border_radius=8,
                         vertical_lines=BorderSide(width=1,color="black"),
                         data_row_max_height=28,                        
                         heading_row_height=25,
                         horizontal_lines=BorderSide(width=1,color=colors.GREY_100),
                         border=Border(
                            top=BorderSide(1,color="black"),
                            right=BorderSide(1,color="black"),
                            left=BorderSide(1,color="black"),
                            bottom=BorderSide(1,color="black"),
                            ),
                            columns=[DataColumn(label=Text("CÓDIGO",color="black"),
                                                numeric=True),
                                     DataColumn(label=Text("MEMBRO",color="black"))
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
                               DataRow(
                               cells=[
                                  DataCell(Text()),
                                  DataCell(Text()),
                               ]),
                        ]
                    )
                        ]
                    )
                ),
            ),
        ],
        expand=1,
    )
       
   


def membros(page:Page,params:Params,basket:Basket):
    


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
    