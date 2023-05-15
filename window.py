import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from pokeclass import Grass, Water, Fire
from time import sleep




janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.bulb = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\bulbasauro.png")
        self.bulb_img = ImageTk.PhotoImage(self.bulb)
        self.charm = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\charmander.png")
        self.charm_img = ImageTk.PhotoImage(self.charm)
        self.squir = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\squirtle.png")
        self.squir_img= ImageTk.PhotoImage(self.squir)
        self.tela()
        self.home()
        janela.mainloop()


    # def test(self):
    #     self.pokemons = Grass(self.bulb_img, 45, 45, )
    def tela(self):
        """
        cria tela do tkinter
        """
        self.janela.title('POKEMON')
        self.janela.geometry('700x700')
        self.janela.configure(background='#000')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=700)
        self.janela.minsize(width=700, height=700)

    def home(self):
        self.imghome = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\initial.png")
        self.imagem_home = ImageTk.PhotoImage(self.imghome)
        self.frame_0 = Label(self.janela, image=self.imagem_home, )
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.botoes()
    #
    def botoes(self):
        fonte = ('Inter', 12, 'bold')
        self.bul = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\mini_bulbasauro.png")
        self.bul_img = ImageTk.PhotoImage(self.bul)
        self.squirt = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\mini_squirtle.png")
        self.squirt_img = ImageTk.PhotoImage(self.squirt)
        self.char = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\mini_char.png")
        self.char_img = ImageTk.PhotoImage(self.char)
        self.bt_bul = Button(self.frame_0, text='Bulbasaur', image=self.bul_img, compound=LEFT, font=fonte, fg='#78A75A', background='white', relief='flat',command=lambda m="Bulbasaur": self.battle(m))
        self.bt_bul.place(relx=0.10, rely=0.535, relwidth=0.20, relheight=0.07)
        self.bt_squir = Button(self.frame_0, text='Squirtle', image=self.squirt_img, compound=LEFT, font=fonte, fg='#52A3A9', background='white', relief='flat', command=lambda m="Squirtle": self.battle(m))
        self.bt_squir.place(relx=0.40, rely=0.535, relwidth=0.20, relheight=0.07)
        self.bt_char = Button(self.frame_0, text='Charmander', image=self.char_img, compound=LEFT, font=fonte, fg='#F47932', background='white', relief='flat', command=lambda m="Charmander": self.battle(m))
        self.bt_char.place(relx=0.69, rely=0.535, relwidth=0.22, relheight=0.07)
        self.bt_info = Button(self.frame_0, text='See poke infos', font=fonte, fg='#F47932', background='white', relief='flat', command=self.poke_infos)
        self.bt_info.place(relx=0.345, rely=0.68, relwidth=0.325, relheight=0.07)

    def battle(self, m):
        if m == 'Bulbasaur':
            self.poke_player = Grass(self.bulb_img, 45, 45, 'player')
        elif m == 'Squirtle':
            self.poke_player = Water(self.squir_img, 43, 44, 'player')
        elif m == 'Charmander':
            self.poke_player = Fire(self.charm_img, 65, 39, 'player')
        poke1, poke2, poke3 = self.bulb_img, self.charm_img, self.squir_img
        lista_pokes = [poke1, poke2, poke3]
        self.poke_img_bot = random.choice(lista_pokes)
        if self.poke_img_bot == poke1:
            self.poke_bot = Grass(poke1, 45, 45, 'bot')
        elif self.poke_img_bot == poke2:
            self.poke_bot = Fire(poke2, 65, 39, 'bot')
        else:
            self.poke_bot = Water(poke3, 43, 44, 'bot')
        self.imgfight = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\fight.png")
        self.imagem_fight = ImageTk.PhotoImage(self.imgfight)
        self.frame_0 = Label(self.janela, image=self.imagem_fight)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.label_bulb = Label(self.frame_0, image=self.poke_player.name)
        self.label_bulb.place(relx=0.13, rely=0.30, relwidth=0.25, relheight=0.25)
        self.label_bot = Label(self.frame_0, image=self.poke_img_bot)
        self.label_bot.place(relx=0.62, rely=0.32, relwidth=0.25, relheight=0.25)
        if self.poke_player.speed == self.poke_bot.speed:
            yn = ['p', 'b']
            chose = random.choice(yn)
            if chose == 'p':
                self.janela.after(3000, self.you_start)
            else:
                self.janela.after(3000, self.bot_start)
        elif self.poke_player.speed < self.poke_bot.speed:
            self.janela.after(3000, self.bot_start)
        elif self.poke_player.speed > self.poke_bot.speed:
            self.janela.after(3000, self.you_start)


    def bot_start(self):
        self.imgfight = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\op_start.png")
        self.imagem_fight = ImageTk.PhotoImage(self.imgfight)
        self.frame_0 = Label(self.janela, image=self.imagem_fight)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.label_bulb = Label(self.frame_0, image=self.poke_bot.name)
        self.label_bulb.place(relx=0.38, rely=0.30, relwidth=0.25, relheight=0.25)
    def you_start(self):
        self.imgfight = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\you_start.png")
        self.imagem_fight = ImageTk.PhotoImage(self.imgfight)
        self.frame_0 = Label(self.janela, image=self.imagem_fight)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.label_bulb = Label(self.frame_0, image=self.poke_player.name)
        self.label_bulb.place(relx=0.38, rely=0.30, relwidth=0.25, relheight=0.25)

    def poke_infos(self):
        self.seta = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\seta.png")
        self.seta_img = ImageTk.PhotoImage(self.seta)
        self.imagem = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\pokeinfo.png")
        self.imagem_tk = ImageTk.PhotoImage(self.imagem)
        frame = Frame(self.janela, background='#000')
        frame.place(relheight=0.9, relwidth=1.0, relx=0.0, rely=0.02)
        self.label_imagem = Label(frame, image=self.imagem_tk)
        self.label_imagem.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.bt_back = Button(self.label_imagem, fg='#F47932', image=self.seta_img, background='white', relief='flat', command=self.home)
        self.bt_back.place(relx=0.895, rely=0.855, relwidth=0.05, relheight=0.045)




    #
    #Button(root, text = 'Click Me !', image = photoimage,
                    # compound = LEFT).pack(side = TOP)
    # def home(self):78A75A
    # 52A3A9
    # F47932
    #     """
    #     exibe aba(tela) "home" do tkinter
    #     """
    #     self.cria_navbar()
    #     self.imagem = Image.open("home.png")
    #     self.imagem_tk = ImageTk.PhotoImage(self.imagem)
    #     frame = Frame(self.janela, background='#000')
    #     frame.place(relheight=0.9, relwidth=1.0, relx=0.0, rely=0.1)
    #     self.label_imagem = Label(frame, image=self.imagem_tk)
    #     self.label_imagem.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
    #
    # def command_brand(self):
    #     """
    #     exibe tela "brands" quando o usuario clicar no botão,
    #     mostra tvs de acordo com a marca
    #     """
    #     self.tvsframe = Frame(self.janela, background='#f0f0f0')
    #     self.tvsframe.place(relheight=0.9, relwidth=1.0, relx=0.0, rely=0.09)
    #     self.search = Image.open("search.png")
    #     self.search_tk = ImageTk.PhotoImage(self.search)
    #     label = Label(self.tvsframe, image=self.search_tk)
    #     label.place(relx=0, relwidth=1.0, relheight=0.1)
    #     self.frame_combo = Frame(label, background='#000')
    #     self.frame_combo.place(rely=0.31, relx=0.47, relheight=0.4, relwidth=0.3)
    #     self.combobox = ttk.Combobox(self.frame_combo,
    #                                  values=['Samsung', 'LG', 'TCL', 'Multilaser'], state="readonly", width=21, font=('sans-serif', 12), background='#fff')
    #     self.combobox.place( width=0.7)
    #     self.combobox.grid(column=0, row=1)
    #     self.combobox.current(1)
    #     self.bt = Image.open("lupa.png")
    #     self.bt_tk = ImageTk.PhotoImage(self.bt)
    #     self.btSearch = Button(label, image=self.bt_tk, relief='flat', background='#0087FD', command=self.tabela)
    #     self.btSearch.place(rely=0.21, relx=0.8, relheight=0.5, relwidth=0.04)
    #     self.btvalues = Button(self.tvsframe, text='Pegar valores em tempo real', font=('Inter', 8, 'bold'), fg='white', relief='groove', background='#0087FD', command=self.webscrapp_marcas)
    #     self.btvalues.place(rely=0.12, relx=0.05, relheight=0.05, relwidth=0.3)
    #
    # def webscrapp_marcas(self):
    #     """
    #     Inicia webscrap das marcas das tvs caso solicitado
    #     """
    #     j = Marcas()
    #
    # def webscrapp_tvs(self):
    #     """
    #     Inicia webscrap das tvs caso solicitado
    #     """
    #     j = Tvs()
    #
    # def tabela(self):
    #     """
    #     Cria tabela de acordo com as marcas
    #     """
    #     self.lista_frame2(True)
    #     self.selecionar_opcao()
    #
    # def command_tvs(self):
    #     """
    #     cria aba(tela) quando o botão tvs é clicado, feito pra mostrar as 10 primeiras tvs do site
    #     """
    #     self.cria_navbar()
    #     self.alltvsframe = Frame(self.janela, background='#f0f0f0')
    #     self.alltvsframe.place(relheight=0.9, relwidth=1.0, relx=0.0, rely=0.1)
    #     self.btvalues_tvs = Button(self.alltvsframe, text='Pegar valores em tempo real', font=('Inter', 8, 'bold'), fg='white', relief='groove', background='#0087FD', command=self.webscrapp_tvs)
    #     self.btvalues_tvs.place(rely=0.2, relx=0.16, relheight=0.05, relwidth=0.3)
    #     self.btatualiza = Button(self.alltvsframe, text='Atualizar', font=('Inter', 8, 'bold'), fg='white', relief='groove', background='#0087FD', command=self.tabela_2)
    #     self.btatualiza.place(rely=0.2, relx=0.05, relheight=0.05, relwidth=0.1)
    #     self.lista_frame2(False)
    #     self.selecionar_tvs()
    #
    # def tabela_2(self):
    #     """
    #     cria tabela das 10 primeiras tvs mostradas no site
    #     """
    #     self.lista_frame2(False)
    #     self.selecionar_tvs()
    #
    # def lista_frame2(self, s):
    #     """
    #     cria tabela de acordo com a variavel enviada como parametro, se s for true, entao a tabela é de acordo com marca,
    #     se s for false, então a tabela mostra todas as 10 primeiras tvs
    #     :param s: valida qual tabela será criada, valores true ou false
    #     """
    #     if s:
    #         self.listatvs = ttk.Treeview(self.tvsframe, height=3,
    #                                      columns=('col1',
    #                                               'col2',
    #                                               'col3'))
    #     else:
    #         self.listatvs = ttk.Treeview(self.alltvsframe, height=3,
    #                                      columns=('col1',
    #                                               'col2',
    #                                               'col3'))
    #     self.listatvs.heading('#0', text='')
    #     self.listatvs.heading('#1', text='NOME')
    #     self.listatvs.heading('#2', text='PREÇO')
    #
    #     self.listatvs.column('#0', width=5)
    #     self.listatvs.column('#1', width=530)
    #     self.listatvs.column('#2', width=80)
    #
    #     self.listatvs.place(rely=0.3, relx=0.03,
    #                         relwidth=0.93, relheight=0.4)
    #
    # def selecionar_opcao(self):
    #     """
    #     Insere dados do banco na tabela, de acordo com a marca escolhida
    #     """
    #     self.brand = self.combobox.get()
    #     print(self.brand)
    #     self.listatvs.delete(*self.listatvs.get_children())
    #     cursor.execute(f"Select nome, preco from {self.brand}")
    #     linhas = cursor.fetchall()
    #     for i in linhas:
    #         self.listatvs.insert(parent='', index=0, values=i)
    #
    # def selecionar_tvs(self):
    #     """
    #     Insere dados do banco na tabela, das 10 primeiras tvs do site
    #     """
    #     self.listatvs.delete(*self.listatvs.get_children())
    #     cursor.execute(f"Select nome, preco from tvs")
    #     linhas = cursor.fetchall()
    #     for i in linhas:
    #         self.listatvs.insert(parent='', index=0, values=i)


jan = Aplicacao()
jan.tela()