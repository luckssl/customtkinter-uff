import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

janela = ctk.CTk()
janela.geometry("500x300")
janela.title("Localiza UFF")

# NOVA JANELA
def nova_tela(cod, tur, c1, c2, c3, c4, c5, t1, t2, t3, t4, t5, t6, t7, t8):
    nova_janela = ctk.CTk()
    nova_janela.geometry("500x350")
    nova_janela.title("Informações")

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
                    sala == "lab 307"
            elif tur == t8:
                hor = "09h às 11h"
                dsem = "Segundas"
                sala = "lab 303"
        else:
            mat = "Progamação de Computadores I"
            if tur == t1 or tur == t2:
                hor == "11h às 13h"
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

    # Mostrando as informações na tela
    disciplina = ctk.CTkLabel(master=nova_janela, text=mat, font=('Roboto', 20))
    disciplina.pack()
    instituto = ctk.CTkLabel(master=nova_janela, text=inst, font=('Roboto', 12))
    instituto.pack()
    turma = ctk.CTkLabel(master=nova_janela, text=tur, font=('Roboto', 12))
    turma.pack()
    horario = ctk.CTkLabel(master=nova_janela, text=(f"Sua aula será às {dsem} das {hor} na(s) sala(s) {sala}"), font=('Roboto', 12))
    horario.pack()


            








    nova_janela.mainloop()
    

#FUNÇÃO DO BOTÃO
def confirma():
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
        nova_tela(cod, tur, c1, c2, c3, c4, c5, t1, t2, t3, t4, t5, t6, t7, t8)




# TELA INICIAL DO APLICATIVO

# VARIÁVEIS
mat = 0
inst = 0
dsem = 0
hor = 0
sala = 0

#TÍTULO
titulo = ctk.CTkLabel(master=janela, text="Encontre sua sala de aula", font=('Roboto', 20))
titulo.pack(padx=10, pady=10)

#CÓDIGO DA MATÉRIA
codigo_rotulo = ctk.CTkLabel(master=janela, text='Digite o código da matéria:', font=('Roboto', 12))
codigo_rotulo.pack()
codigo_entry = ctk.CTkEntry(master=janela, placeholder_text='Código da matéria')
codigo_entry.pack(padx = 10)

#CÓDIGO DA TURMA
turma_rotulo = ctk.CTkLabel(master=janela, text='Digite a sua turma:', font=('Roboto', 12))
turma_rotulo.pack()
turma_entry = ctk.CTkEntry(master=janela, placeholder_text='Turma')
turma_entry.pack(padx=10)

#BOTÃO
btn_confirma = ctk.CTkButton(master=janela, text='Confirmar', command=confirma)
btn_confirma.pack()






janela.mainloop()