# -*- coding: utf-8 -*-

import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser

# CRIAÇÃO DE UMA JANELA
janela = ctk.CTk()
janela.geometry("380x335")
janela.title("Localiza UFF")

# FUNÇÃO DO BOTÃO
def confirma(codigo_entry, turma_entry, codigo_rotulo, titulo, codigo_exemplo, turma_rotulo, btn_confirma, turma_exemplo):
    #TRANSFORMA AS ENTRADAS DO USUÁRIO EM STRINGS
    cod = codigo_entry.get()
    tur = turma_entry.get()

    # BANCO DE DADOS
    c1, c2, c3, c4, c5 = "TCC00296", "GAN00167", "GGM00137", "TCC00308", "TCC00346"
    t1, t2, t3, t4, t5, t6, t7, t8 = "A1", "B1", "C1", "D1", "E1", "AA", "BA", "CA"

    # VERIFICAÇÃO
    if cod == '' or tur == '':
        messagebox.showerror(title='Verificação', message="Preencha todos os campos corretamente!")
    elif cod != c1 and cod != c2 and cod != c3 and cod != c4 and cod != c5 or tur != t1 and tur != t2 and  tur != t3 and tur != t4 and tur != t5 and tur != t6 and tur != t7 and tur != t8:
        messagebox.showerror(title='Verificação', message='Matéria ou turma não cadastrada no sistema.')
    
    # MOSTRAR INFORMAÇÕES
    else:
        # Destruindo os wiggets da tela anterior
        codigo_rotulo.destroy()
        titulo.destroy()
        codigo_exemplo.destroy()
        codigo_entry.destroy()
        turma_rotulo.destroy()
        turma_entry.destroy()
        btn_confirma.destroy()
        turma_exemplo.destroy()
        nova_tela(cod, tur, c1, c2, c3, c4, c5, t1, t2, t3, t4, t5, t6, t7, t8)

# RETORNAR A TELA INICIAL DO APP
def retorna_original(disciplina, instituto, turma, horario, btn_local, btn_retorno):
    disciplina.destroy()
    instituto.destroy()
    turma.destroy()
    horario.destroy()
    btn_local.destroy()
    btn_retorno.destroy()
    
    titulo = ctk.CTkLabel(master=janela, text="Encontre sua sala de aula", font=('Roboto', 20))
    titulo.pack(padx=10, pady=10)

    codigo_rotulo = ctk.CTkLabel(master=janela, text='Digite o código da matéria:', font=('Roboto', 12))
    codigo_rotulo.pack()
    codigo_exemplo = ctk.CTkLabel(master=janela, text='Exemplo: TCC00296',font=('Roboto',8.45))
    codigo_exemplo.pack()
    codigo_entry = ctk.CTkEntry(master=janela, placeholder_text='Código da matéria')
    codigo_entry.pack(padx = 10)

    turma_rotulo = ctk.CTkLabel(master=janela, text='Digite a sua turma:', font=('Roboto', 12))
    turma_rotulo.pack()
    turma_entry = ctk.CTkEntry(master=janela, placeholder_text='Turma')
    turma_entry.pack(padx=10)
    turma_exemplo = ctk.CTkLabel(master=janela, text='Exemplo: A1',font=('Roboto', 10))
    turma_exemplo.pack()

    #BOTÃO
    btn_confirma = ctk.CTkButton(master=janela, text='Confirmar', command=lambda: confirma(codigo_entry, turma_entry, codigo_rotulo, titulo, codigo_exemplo, turma_rotulo, btn_confirma, turma_exemplo))
    btn_confirma.pack()

#######################################################################################

# SEGUNDA TELA

#######################################################################################

# CRIAR UMA NOVA TELA
def nova_tela(cod, tur, c1, c2, c3, c4, c5, t1, t2, t3, t4, t5, t6, t7, t8):

    # ATUALIZANDO AS VARIÁVEIS
    if cod == c1 or cod == c4 or cod == c5:
        inst = "Instituto de Computação"
        local = "https://maps.app.goo.gl/tH1Tak8tBRePeGjF6"
        if cod == c1:
            mat = "Fundamentos de Arquitetura de Computadores"
            dsem = "Terças e quintas"
            hor = "11h às 13h"
            if tur == t1:
                sala = "206"
            elif tur == t2:
                sala = "213"
        elif cod == c4:
            mat = "Laboratório de Resolução de Problemas"
            if tur == t6 or tur == t7:
                hor = "09h às 11h"
                dsem = "Quartas"
                if tur == t6:
                    sala = "lab 303"
                else:
                    sala = "lab 307"
            elif tur == t8:
                hor = "09h às 11h"
                dsem = "Segundas"
                sala = "lab 303"
        else:
            mat = "Progamação de Computadores I"
            if tur == t1 or tur == t2:
                hor = "11h às 13h"
                dsem = "Segundas e quartas"
                if tur == t2:
                    sala = "313 na Segunda\nlab 303 na Quarta"
                elif tur == t1:
                    sala = "lab 304 na Segunda\n303 na Quarta"
    else:
        inst = "UFASA - BLOCO H"
        local = "https://maps.app.goo.gl/6u6FdQufmprA2H7B6"
        if cod == c2:
            mat = "Matemática Discreta"
            dsem = "Segundas e Quartas"
            hor = "14h às 16h"
            if tur == t2:
                sala = "404"
            elif tur == t3:
                sala = "403"
        else:
            mat = "Fundamentos de Cálculo e Geometria"
            dsem = "Terças e Quintas"
            hor = "09h às 11h"
            if tur == t4:
                sala = "303"
            elif tur == t5:
                sala = "501"



    # Comando do botao da localização
    def abrir():
        webbrowser.open(local)

    # Mostrando as informações na tela
    btn_retorno = ctk.CTkButton(master=janela, text='\u2190', command=lambda: retorna_original(disciplina, instituto, turma, horario, btn_local, btn_retorno))
    btn_retorno.pack(side=ctk.LEFT, anchor=ctk.NW, padx=5, pady=5)

    disciplina = ctk.CTkLabel(master=janela, text=mat, font=('Roboto', 20))
    disciplina.pack(padx=10)
    instituto = ctk.CTkLabel(master=janela, text=inst, font=('Roboto', 12))
    instituto.pack()
    turma = ctk.CTkLabel(master=janela, text=tur, font=('Roboto', 12))
    turma.pack()
    horario = ctk.CTkLabel(master=janela, text=(f"Sua aula será às {dsem} das {hor} na(s) sala(s) {sala}"), font=('Roboto', 12))
    horario.pack()

    # Botao para abrir o local no maps
    btn_local = ctk.CTkButton(master=janela, text='Mostrar local no maps', command = abrir)
    btn_local.pack()

#####################################################################################################

# TELA INICIAL DO APLICATIVO

####################################################################################################

# VARIÁVEIS
mat = 0
inst = 0
dsem = 0
hor = 0
sala = 0

#TÍTULO DA JANELA
titulo = ctk.CTkLabel(master=janela, text="Encontre sua sala de aula", font=('Roboto', 20, 'bold'))
titulo.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

#CÓDIGO DA MATÉRIA
codigo_rotulo = ctk.CTkLabel(master=janela, text='  Digite o código da matéria:', font=('Roboto', 12, 'bold'))
codigo_rotulo.grid(row=2, column=0, sticky="e", padx=10)
codigo_entry = ctk.CTkEntry(master=janela, placeholder_text='Código da matéria')
codigo_entry.grid(row=2, column=1, sticky="w", padx=10)
codigo_exemplo = ctk.CTkLabel(master=janela, text='Exemplo: TCC00296',font=('Roboto', 10))
codigo_exemplo.grid(row=3, column=1)

#CÓDIGO DA TURMA
turma_rotulo = ctk.CTkLabel(master=janela, text='Digite a sua turma:', font=('Roboto', 12, 'bold'))
turma_rotulo.grid(row=5, column=0)
turma_entry = ctk.CTkEntry(master=janela, placeholder_text='Turma')
turma_entry.grid(row=5, column=1, sticky="w", padx=10)
turma_exemplo = ctk.CTkLabel(master=janela, text='Exemplo: A1',font=('Roboto', 10))
turma_exemplo.grid(row=6, column=1, sticky='n')
# As classes CTkLabel e CTkEntry criam, respectivamente, um texto e uma caixa de entrada dentro da janela

# BOTÃO PARA COLETAR OS DADOS DE ENTRADA DO USUÁRIO E REALIZAR A VERIFICAÇÃO DE ACORDO COM O BANCO DE DADOS NO CÓDIGO
btn_confirma = ctk.CTkButton(master=janela, text='Confirmar', command=lambda: confirma(codigo_entry, turma_entry, codigo_rotulo, titulo, codigo_exemplo, turma_rotulo, btn_confirma, turma_exemplo))
btn_confirma.grid(row=10, column=0, columnspan=2, pady=20)
# Essa classe cria um botão dentro da janela que, ao ser clicado pelo usuário, chama a função confirma()






janela.mainloop()