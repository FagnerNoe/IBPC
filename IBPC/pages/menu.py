
from flet import *
import flet as ft

from flet_route import Params,Basket
from datetime import datetime
import time
from pages.membros import membros as membros_page
from pages.ministerios import ministerios as ministerio_page  
from pages.patrimonio import patrimonio as patrimonio_page  
from pages.atividades import atividades as atividades_page  
from pages.agenda import agenda as agenda_page  
from pages.relatorios import relatorios as relatorios_page  
   





    

    

data = datetime.now()
data_atual = data.today().strftime('%d/%m/%Y')
hora_atual = data.time().strftime('%H:%M:%S')           
time.sleep(1)
        

     



def menu(page:Page,params:Params,basket:Basket):

                
            
    
                    
    def modal_membros(e):
        page.dialog = janela_membros
        janela_membros.open = True
        page.update()   

    def modal_ministerios(e):
        page.dialog = janela_ministerios
        janela_ministerios.open = True
        page.update()  

    def modal_patrimonio(e):
        page.dialog = janela_patrimonio
        janela_patrimonio.open = True
        page.update() 

    def modal_atividades(e):
        page.dialog = janela_atividades
        janela_atividades.open = True
        page.update() 

    def modal_agenda(e):
        page.dialog = janela_agenda
        janela_agenda.open = True
        page.update() 

    def modal_relatorio(e):
        page.dialog = janela_relatorio
        janela_relatorio.open = True
        page.update()      


    



    def sair(e):
        page.dialog =caixa_dialogo
        caixa_dialogo.open = True
        page.update()


    def sim(e):
        page.window_destroy()

     

    caixa_dialogo = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirme..."),
        content=ft.Text("Você quer realmente fechar o sistema?"),
        actions=[
            ft.ElevatedButton("Sim", on_click=sim),
            ft.ElevatedButton("Não", on_click=lambda _: page.close_dialog()),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    
    janela_membros = AlertDialog(
        content_padding=Padding(0,0,0,0),
        actions_padding=Padding(0,0,0,0),
        modal=True,
        content=Stack(
                    controls=[
                        Container(
                                width=840,
                                height=530,
                                bgcolor="white",
                                border_radius=BorderRadius(10,10,0,0),
                                content=membros_page(page=View,params=Params,basket=Basket))                                         
                                   ]                                   
                                   ),

                                   actions=[ 
                                        Container(                                            
                                            bgcolor="white",
                                            border_radius=BorderRadius(0,0,10,10),
                                            padding=Padding(0,0,0,10),
                                            content=Row(
                                                spacing=4,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[

                                                    Container(
                                                        width=130,
                                                        height=95,                                                        
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                           
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("ADICIONAR",
                                                             color="green"),
                                                        Image(
                                                            src="assets/icons/icons_telas/adicionar-user.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                        width=130,
                                                        height=95,                                                         
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("ALTERAR",
                                                             color="Blue"),
                                                        Image(src="assets/icons/icons_telas/editar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(                                                        
                                                        width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("DELETAR",
                                                             color="red"),
                                                        Image(src="assets/icons/icons_telas/deletar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(                                                         
                                                        width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("CANCELAR",
                                                             color=colors.BLUE_600),
                                                        Image(src="assets/icons/icons_telas/cancelar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                         width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("IMPRIMIR",
                                                             color="bROWN"),
                                                        Image(src="assets/icons/icons_telas/imprimir.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                        width=130,
                                                        height=95,
                                                         on_click=lambda _:page.close_dialog(), 
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("FECHAR",
                                                             color=colors.BLUE_500),
                                                        Image(src="assets/icons/icons_telas/fechar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                ]
                                            )
                                            ) 
                                                ]

                                            
                                        
                                            ) 

    janela_ministerios = AlertDialog(
        content_padding=Padding(0,0,0,0),
        actions_padding=Padding(0,0,0,0),
        modal=True,
        content=Stack(
                    controls=[
                        Container(
                                width=840,
                                height=530,
                                bgcolor="white",
                                border_radius=BorderRadius(10,10,0,0),
                                content=ministerio_page(page=View,params=Params,basket=Basket))                                         
                                   ]                                   
                                   ),

                                   actions=[ 
                                        Container(                                            
                                            bgcolor="white",
                                            border_radius=BorderRadius(0,0,10,10),
                                            padding=Padding(0,0,0,10),
                                            content=Row(
                                                spacing=4,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[

                                                    Container(
                                                        width=130,
                                                        height=95,                                                        
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                           
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("ADICIONAR",
                                                             color="green"),
                                                        Image(
                                                            src="assets/icons/icons_telas/adicionar-user.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                        width=130,
                                                        height=95,                                                         
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("ALTERAR",
                                                             color="Blue"),
                                                        Image(src="assets/icons/icons_telas/editar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(                                                        
                                                        width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("DELETAR",
                                                             color="red"),
                                                        Image(src="assets/icons/icons_telas/deletar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(                                                         
                                                        width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("CANCELAR",
                                                             color=colors.BLUE_600),
                                                        Image(src="assets/icons/icons_telas/cancelar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                         width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("IMPRIMIR",
                                                             color="bROWN"),
                                                        Image(src="assets/icons/icons_telas/imprimir.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                        width=130,
                                                        height=95,
                                                         on_click=lambda _:page.close_dialog(), 
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("FECHAR",
                                                             color=colors.BLUE_500),
                                                        Image(src="assets/icons/icons_telas/fechar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                ]
                                            )
                                            ) 
                                                ]

                                            
                                        
                                            )                                
    
    janela_patrimonio = AlertDialog(
        content_padding=Padding(0,0,0,0),
        actions_padding=Padding(0,0,0,0),
        modal=True,
        content=Stack(
                    controls=[
                        Container(
                                width=840,
                                height=530,
                                bgcolor="white",
                                border_radius=BorderRadius(10,10,0,0),
                                content=patrimonio_page(page=View,params=Params,basket=Basket))                                         
                                   ]                                   
                                   ),

                                   actions=[ 
                                        Container(                                            
                                            bgcolor="white",
                                            border_radius=BorderRadius(0,0,10,10),
                                            padding=Padding(0,0,0,10),
                                            content=Row(
                                                spacing=4,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[

                                                    Container(
                                                        width=130,
                                                        height=95,                                                        
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                           
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("ADICIONAR",
                                                             color="green"),
                                                        Image(
                                                            src="assets/icons/icons_telas/adicionar-user.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                        width=130,
                                                        height=95,                                                         
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("ALTERAR",
                                                             color="Blue"),
                                                        Image(src="assets/icons/icons_telas/editar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(                                                        
                                                        width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("DELETAR",
                                                             color="red"),
                                                        Image(src="assets/icons/icons_telas/deletar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(                                                         
                                                        width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("CANCELAR",
                                                             color=colors.BLUE_600),
                                                        Image(src="assets/icons/icons_telas/cancelar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                         width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("IMPRIMIR",
                                                             color="bROWN"),
                                                        Image(src="assets/icons/icons_telas/imprimir.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                        width=130,
                                                        height=95,
                                                        on_click=lambda _:page.close_dialog(),                                                                                              
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("FECHAR",
                                                             color=colors.BLUE_500),
                                                        Image(src="assets/icons/icons_telas/fechar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                ]
                                            )
                                            ) 
                                                ]

                                            
                                        
                                            )                                
   
    janela_atividades = AlertDialog(
        content_padding=Padding(0,0,0,0),
        actions_padding=Padding(0,0,0,0),
        modal=True,
        content=Stack(
                    controls=[
                        Container(
                                width=840,
                                height=530,
                                bgcolor="white",
                                border_radius=BorderRadius(10,10,0,0),
                                content=atividades_page(page=View,params=Params,basket=Basket))                                         
                                   ]                                   
                                   ),

                                   actions=[ 
                                        Container(                                            
                                            bgcolor="white",
                                            border_radius=BorderRadius(0,0,10,10),
                                            padding=Padding(0,0,0,10),
                                            content=Row(
                                                spacing=4,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[

                                                    Container(
                                                        width=130,
                                                        height=95,                                                        
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                           
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("ADICIONAR",
                                                             color="green"),
                                                        Image(
                                                            src="assets/icons/icons_telas/adicionar-user.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                        width=130,
                                                        height=95,                                                         
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("ALTERAR",
                                                             color="Blue"),
                                                        Image(src="assets/icons/icons_telas/editar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(                                                        
                                                        width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("DELETAR",
                                                             color="red"),
                                                        Image(src="assets/icons/icons_telas/deletar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(                                                         
                                                        width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("CANCELAR",
                                                             color=colors.BLUE_600),
                                                        Image(src="assets/icons/icons_telas/cancelar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                         width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("IMPRIMIR",
                                                             color="bROWN"),
                                                        Image(src="assets/icons/icons_telas/imprimir.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                        width=130,
                                                        height=95,
                                                        on_click=lambda _:page.close_dialog(),                                                                                              
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("FECHAR",
                                                             color=colors.BLUE_500),
                                                        Image(src="assets/icons/icons_telas/fechar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                ]
                                            )
                                            ) 
                                                ]

                                            
                                        
                                            )                                
    
    janela_agenda = AlertDialog(
        content_padding=Padding(0,0,0,0),
        actions_padding=Padding(0,0,0,0),
        modal=True,
        content=Stack(
                    controls=[
                        Container(
                                width=840,
                                height=530,
                                bgcolor="white",
                                border_radius=BorderRadius(10,10,0,0),
                                content=agenda_page(page=View,params=Params,basket=Basket))                                         
                                   ]                                   
                                   ),

                                   actions=[ 
                                        Container(                                            
                                            bgcolor="white",
                                            border_radius=BorderRadius(0,0,10,10),
                                            padding=Padding(0,0,0,10),
                                            content=Row(
                                                spacing=4,
                                                alignment=MainAxisAlignment.CENTER,
                                                controls=[

                                                    Container(
                                                        width=130,
                                                        height=95,                                                        
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                           
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("ADICIONAR",
                                                             color="green"),
                                                        Image(
                                                            src="assets/icons/icons_telas/adicionar-user.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                        width=130,
                                                        height=95,                                                         
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("ALTERAR",
                                                             color="Blue"),
                                                        Image(src="assets/icons/icons_telas/editar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(                                                        
                                                        width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("DELETAR",
                                                             color="red"),
                                                        Image(src="assets/icons/icons_telas/deletar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(                                                         
                                                        width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("CANCELAR",
                                                             color=colors.BLUE_600),
                                                        Image(src="assets/icons/icons_telas/cancelar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                         width=130,
                                                         height=95,
                                                        border=Border(
                                                            None,BorderSide(2,color="grey"),None,None),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("IMPRIMIR",
                                                             color="bROWN"),
                                                        Image(src="assets/icons/icons_telas/imprimir.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    Container(
                                                        width=130,
                                                        height=95,
                                                        on_click=lambda _:page.close_dialog(),                                                                                              
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("FECHAR",
                                                             color=colors.BLUE_500),
                                                        Image(src="assets/icons/icons_telas/fechar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                ]
                                            )
                                            ) 
                                                ]

                                            
                                        
                                            )                                
    
    janela_relatorio = AlertDialog(
        content_padding=Padding(0,0,0,0),
        actions_padding=Padding(0,0,0,0),
        modal=True,
        content=Stack(
                    controls=[
                        Container(                                
                                width=840,
                                height=530,
                                bgcolor="white",                                
                                border_radius=BorderRadius(10,10,0,0),
                                content=relatorios_page(page=View,params=Params,basket=Basket))                                         
                                   ]                                   
                                   ),

                                   actions=[                                                                                
                                           Container(
                                               clip_behavior=ClipBehavior.NONE,                                               
                                               width=840,                                                           
                                               bgcolor="white",
                                               border_radius=BorderRadius(0,0,10,10),
                                               content=Row(
                                                    alignment=MainAxisAlignment.END,
                                                    spacing=0,
                                                   controls=[                                                       
                                                    Container(
                                                        width=130,
                                                        height=100,
                                                        bgcolor="white",
                                                        border=Border(
                                                            BorderSide(None),None,BorderSide(2,color="grey"),BorderSide(2,color="grey")),                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("IMPRIMIR",
                                                             color="BROWN"),
                                                        Image(src="assets/icons/icons_telas/imprimir.png",
                                                            width=90,
                                                            height=80)
                                                    ])),                                        
                                                    Container(                                                         
                                                        width=130,
                                                         height=100,
                                                        border=Border(
                                                            None,None,BorderSide(2,color="grey"),BorderSide(2,color="grey")),
                                                            
                                                            content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("CANCELAR",
                                                             color=colors.BLUE_600),
                                                        Image(src="assets/icons/icons_telas/cancelar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                    
                                                    Container(
                                                        width=130,
                                                        height=100,
                                                          border=Border(
                                                            None,None,None,BorderSide(2,color="grey")),
                                                        on_click=lambda _:page.close_dialog(),                                                                                              
                                                        content=
                                                              Column(
                                                                  spacing=0,
                                                                  alignment=MainAxisAlignment.CENTER,
                                                                  horizontal_alignment=CrossAxisAlignment.CENTER,
                                                                  controls=[
                                                        Text("FECHAR",
                                                             color=colors.BLUE_500),
                                                        Image(src="assets/icons/icons_telas/fechar.png",
                                                            width=90,
                                                            height=80)
                                                    ])),
                                                   ]
                                               )
                                           ) 
                                                ],
                                                actions_alignment=MainAxisAlignment.END,
                                            )
                                            
                                                
                                                

                                            
                                        
                                                                         
                                          
        
    
    

       
         
    
    


    image = Container(
        height=160,
       
        content=Image(
            src="assets/icons/logo_menu.png",
            width=250,
            color_blend_mode=BlendMode.NONE,
            fit=ImageFit.CONTAIN
        )        
    )

    opcoes = Container(
        height=370,        
        content=Column(
            alignment=MainAxisAlignment.START,
            spacing=2,
            controls=[            
                Row(                    
                    width=200,
                    spacing=0,                   
                    controls=[
                        Image(
                            src="assets/icons/icons_menu/membros.png",
                            width=50,
                            height=50,
                            fit=ImageFit.CONTAIN
                        ),
                        TextButton(
                                   content=Text("MEMBROS",
                                                size=18,
                                                color="white"),
                                    on_click=modal_membros,               
                                    
                                    style=ButtonStyle(
                                        overlay_color=ft.colors.with_opacity(0.3,"white"),
                                        
                                    )                                  
                                  )                                       
                            ]),
                    Divider(height=1,color="Brown"),
                Row(
                    width=200,
                    spacing=0,
                    controls=[
                        Image(
                            src="assets/icons/icons_menu/icon-ministerios.png",
                            width=50,
                            height=50,
                            fit=ImageFit.CONTAIN
                        ),
                        TextButton(
                            content=Text("MINISTÉRIOS",
                                         size=18,
                                         color="white"),
                            on_click=modal_ministerios,
                             style=ButtonStyle(
                                        overlay_color=ft.colors.with_opacity(0.3,"white"),
                                    )         
                                         )
                            ]),
                            Divider(height=1,color="Brown"),
                Row(
                    width=200,
                    spacing=0,   
                    controls=[
                        Image(
                            src="assets/icons/icons_menu/icon-patrimonio.png",
                            width=50,
                            height=50,
                            fit=ImageFit.CONTAIN
                        ),
                        TextButton(
                            on_click=modal_patrimonio,
                            content=Text("PATRIMÔNIO",size=18,color="white"),
                                    style=ButtonStyle(
                                        overlay_color=ft.colors.with_opacity(0.3,"white"),
                                    ))
                            ]),
                            Divider(height=1,color="Brown"),
                Row(
                   width=200,
                    spacing=0,                     
                    controls=[
                        Image(
                            src="assets/icons/icons_menu/edit.png",
                            width=50,
                            height=40,
                            fit=ImageFit.CONTAIN
                        ),
                        TextButton(
                                   on_click=modal_atividades,
                                   content=Text("ATIVIDADES",size=18,color="white"),
                                   style=ButtonStyle(
                                        overlay_color=ft.colors.with_opacity(0.3,"white"),
                                    ))
                            ]),
                            Divider(height=1,color="Brown"),
                Row(
                    width=200,
                    spacing=0,  
                    controls=[
                        Image(
                            src="assets/icons/icons_menu/agenda.png",
                            width=50,
                            height=50,
                            fit=ImageFit.CONTAIN
                        ),
                        TextButton( 
                                    on_click=modal_agenda,
                                    content=Text("AGENDA",size=18,color="white"),
                                    style=ButtonStyle(
                                        overlay_color=ft.colors.with_opacity(0.3,"white"),
                                    ))
                            ]),
                            Divider(height=1,color="Brown"),
                Row(
                   width=200,
                    spacing=0,  
                    controls=[
                        Image(
                            src="assets/icons/icons_menu/icon-relatorio.png",
                            width=50,
                            height=50,
                            fit=ImageFit.CONTAIN
                        ),
                        TextButton(
                                    on_click=modal_relatorio,
                                    content=Text("RELATÓRIO",size=18,color="white"),
                                    style=ButtonStyle(
                                        overlay_color=ft.colors.with_opacity(0.3,"white"),
                                    ))
                            ]),
                            Divider(height=1,color="Brown"),
                Row(
                    width=200,
                    spacing=0,  
                    
                    controls=[
                        Image(
                            src="assets/icons/icons_menu/sair.png",
                            width=50,
                            height=40,
                            fit=ImageFit.CONTAIN
                        ),
                        TextButton(
                            content=Text("SAIR",
                                         size=18,
                                         color="white"),
                            on_click=sair,                  
                            style=ButtonStyle(
                                    overlay_color=ft.colors.with_opacity(0.3,"white"),
                                    
                                    )
                                        
                                                                           )
                            ]),
            ]
        )
    )

    data_hora_caixa = Container(
        margin=margin.only(top=10),
        height=100,
        padding=8,
        content=Column(
            spacing=0,
            controls=[
                Row(
                    controls=[
                        Text("DATA :",
                             size=16,
                             color="white",
                             weight=FontWeight.BOLD),
                        Text(value=data_atual,
                             size=16,
                             color="white",
                             
                             )
            ]),
                Row(
                    controls=[
                        Text("HORA :",
                             size=16,
                             color="white",
                             weight=FontWeight.BOLD),
                        Text(value=hora_atual,
                             size=16,
                             color="white",
                             )
                    ]
                ),
            ]
        )
        
    )

    return ft.View(
        "/menu", 
        fullscreen_dialog=True, 
        padding=Padding(0,0,0,0),    
         controls=[
             Stack(                 
                 controls=[ 
                    ShaderMask(
                        shader=LinearGradient(colors=[
                            colors.with_opacity(0.9,"#ffc291"),
                            colors.with_opacity(0.4,"#ffc291")
                        ]), 
                        
                        
                        content=Image(
                                    src="assets/images/frente-igreja.jpeg",
                                    width=3000,
                                    height=800,                       
                                    fit=ImageFit.COVER,
                                    
                                    ),
                        
                        ),               
                        
                        Container(
                            width=240,
                            height=670,
                            
                            gradient=LinearGradient(colors=[
                                colors.with_opacity(0.97,"#ffc291"),
                                colors.with_opacity(1,"#5b2b04"),
                                
                            ]),
                            border_radius=BorderRadius(top_left=0, bottom_right=40, bottom_left=0,top_right=0),
                            content=Column(
                                horizontal_alignment = CrossAxisAlignment.START,
                                spacing =2,
                                controls=[
                                    image,
                                    Container(height=15,width=220,gradient=LinearGradient(
                                        colors=['#5b1b04','#825129']
                                    )),
                                    opcoes,
                                    Container(height=15,width=220,gradient=LinearGradient(
                                        colors=['#5b1b04','#825129']
                                    )),
                                    data_hora_caixa
                                ]
                            )

                        ),
                        Container(
                            width=300,
                            height=130,                           
                            top=680,
                            bottom=0,
                            left=10,
                            padding=10,
                            content=Text("Software IBPC",
                                         size=28,
                                         weight=FontWeight.BOLD,                                        
                                            
                                         ),
                        )
                                
                 ],
                 width=2500,
                 height=1000,
                 
    ),
         ]

    )                  
                    
        
                        



    
        
    
                                          
   
    
            
    