import random
from tkinter import *
from PIL import ImageTk, Image
from pokeclass import Grass, Water, Fire
import pygame

janela = Tk()


class Aplicacao():
    def __init__(self):
        self.quadros = []
        self.janela = janela
        self.bot_life = ''
        self.player_life = ''
        self.lose= Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\lose.png")
        self.lose_img= ImageTk.PhotoImage(self.lose)
        self.won= Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\won.png")
        self.won_img= ImageTk.PhotoImage(self.won)
        self.b_life = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\bulbasauro_life.png")
        self.bulb_life = ImageTk.PhotoImage(self.b_life)
        self.c_life = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\charmander_life.png")
        self.charm_life = ImageTk.PhotoImage(self.c_life)
        self.s_life = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\squirtle_life.png")
        self.squir_life= ImageTk.PhotoImage(self.s_life)
        self.bulb = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\bulbasauro.png")
        self.bulb_img = ImageTk.PhotoImage(self.bulb)
        self.charm = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\charmander.png")
        self.charm_img = ImageTk.PhotoImage(self.charm)
        self.squir = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\squirtle.png")
        self.squir_img= ImageTk.PhotoImage(self.squir)
        self.tela()
        self.home()

        janela.mainloop()


    def song(self):
        pygame.mixer.init()
        pygame.mixer.music.load(r"C:/Users/47829927855/Desktop/poke-game-main/song/pokesong.wav")
        pygame.mixer.music.play()
    def tela(self):
        self.song()
        self.janela.title('POKEMON')
        self.janela.geometry('700x700')
        self.janela.configure(background='#000')
        self.janela.iconbitmap(r'C:\Users\47829927855\Desktop\poke-game-main\img\pokeball.ico')
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
        self.bt_bul = Button(self.frame_0, text='Bulbasaur', image=self.bul_img, compound=LEFT, font=fonte, fg='#78A75A', background='white', relief='flat', command=lambda m="Bulbasaur": self.define_1st_player(m))
        self.bt_bul.place(relx=0.10, rely=0.535, relwidth=0.20, relheight=0.07)
        self.bt_squir = Button(self.frame_0, text='Squirtle', image=self.squirt_img, compound=LEFT, font=fonte, fg='#52A3A9', background='white', relief='flat', command=lambda m="Squirtle": self.define_1st_player(m))
        self.bt_squir.place(relx=0.40, rely=0.535, relwidth=0.20, relheight=0.07)
        self.bt_char = Button(self.frame_0, text='Charmander', image=self.char_img, compound=LEFT, font=fonte, fg='#F47932', background='white', relief='flat', command=lambda m="Charmander": self.define_1st_player(m))
        self.bt_char.place(relx=0.69, rely=0.535, relwidth=0.22, relheight=0.07)
        self.bt_info = Button(self.frame_0, text='See poke infos', font=fonte, fg='#F47932', background='white', relief='flat', command=self.poke_infos)
        self.bt_info.place(relx=0.345, rely=0.68, relwidth=0.325, relheight=0.07)

    def define_1st_player(self, m):
        if m == 'Bulbasaur':
            self.poke_player = Grass(self.bulb_img, 45, 45, {'Razor Leaf': {'type': 'Physical', 'strenght': 10,  'movement': 'throwing blades \nat the opponent...'},
                'Stun Spore': {'type': 'Status', 'strenght': 10, 'movement': 'spreading cloud of\n numbing powder...'},
                'Absorb': {'type': 'Physical', 'strenght': 10, 'movement': 'draining the\n opponents ...'}}, 'player')
            self.player_life = self.bulb_life
        elif m == 'Squirtle':
            self.player_life = self.squir_life
            self.poke_player = Water(self.squir_img, 43, 44, {'Rain Dance': {'type': 'Status', 'strenght': 10, 'movement': 'Summoning rain...'},
                'Bubble Beam': {'type': 'Status', 'strenght': 10, 'movement': 'Throwing bubble\nspray at the opponent...'},
                'Razor Shell': {'type': 'Status', 'strenght': 10, 'movement': 'Slashing opponent \nwith shells...'}}, 'player')
        elif m == 'Charmander':
            self.player_life = self.charm_life
            self.poke_player = Fire(self.charm_img, 65, 39, {'Blaze Kick': {'type': 'Physical', 'strenght': 10, 'movement': 'kicking the opponent...'},
                'Fire Blast': {'type': 'Physical', 'strenght': 10, 'movement': 'Attacking opponent\nwith an intense blast...'},
                'Sunny Day': {'type': 'Status', 'strenght': 10, 'movement': 'Intensifying the sun...'}}, 'player')
        poke1, poke2, poke3 = self.bulb_img, self.charm_img, self.squir_img
        lista_pokes = [poke1, poke2, poke3]
        self.poke_img_bot = random.choice(lista_pokes)
        if self.poke_img_bot == poke1:
            self.poke_bot = Grass(self.bulb_img, 45, 45, {'Razor Leaf': {'type': 'Physical', 'strenght': 10,  'movement': 'throwing blades\nat you...'},
                'Stun Spore': {'type': 'Status', 'strenght': 10, 'movement': 'spreading\ncloud of numbing powder...'},
                'Absorb': {'type': 'Physical', 'strenght': 10, 'movement': 'draining you ...'}}, 'bot')
            self.bot_life = self.bulb_life
        elif self.poke_img_bot == poke2:
            self.bot_life = self.charm_life
            self.poke_bot = Fire(self.charm_img, 65, 39, {'Blaze Kick': {'type': 'Physical', 'strenght': 10, 'movement': 'kicking you...'},
                'Fire Blast': {'type': 'Physical', 'strenght': 10, 'movement': 'Attacking you with\nan intense blast...'},
                'Sunny Day': {'type': 'Status', 'strenght': 10, 'movement': 'Intensifying the sun...'}}, 'bot')
        else:
            self.bot_life = self.squir_life
            self.poke_bot = Water(self.squir_img, 43, 44, {'Rain Dance': {'type': 'Status', 'strenght': 10, 'movement': 'Summoning rain...'},
                'Bubble Beam': {'type': 'Status', 'strenght': 10, 'movement': 'Throwing bubble spray\nat you...'},
                'Razor Shell': {'type': 'Status', 'strenght': 10, 'movement': 'Slashing you\nwith shells...'}}, 'bot')
        self.imgfight = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\fight.png")
        self.imagem_fight = ImageTk.PhotoImage(self.imgfight)
        self.frame_0 = Label(self.janela, image=self.imagem_fight)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.label_bulb = Label(self.frame_0, image=self.poke_player.name)
        self.label_bulb.place(relx=0.13, rely=0.32, relwidth=0.25, relheight=0.25)
        self.label_bot = Label(self.frame_0, image=self.poke_img_bot)
        self.label_bot.place(relx=0.62, rely=0.32, relwidth=0.25, relheight=0.25)
        if self.poke_player.speed == self.poke_bot.speed:
            yn = ['p', 's']
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
        self.show_hp(self.poke_player.hp, self.poke_bot.hp)
        self.janela.after(3000, self.attack_bot)

    def show_hp(self, hp_player, hp_bot):
        if self.poke_player.hp < 0:
            hp_player = 0
        elif self.poke_bot.hp < 0:
            hp_bot = 0
        fonte = ('arial', 16, 'bold')
        label_life_bot = Label(self.frame_0, image=self.bot_life)
        label_life_bot.place(relx=0.90, rely=0.06, relwidth=0.06, relheight=0.06)
        label_life_player = Label(self.frame_0, image=self.player_life)
        label_life_player.place(relx=0.22, rely=0.06, relwidth=0.06, relheight=0.06)
        label_hp= Label(self.frame_0, text=hp_player, background='#000', fg='white', font= fonte)
        label_hp.place(relx=0.15, rely=0.12, relwidth=0.04, relheight=0.04)
        label_hp_bot = Label(self.frame_0, text=hp_bot, background='#000', fg='white', font= fonte)
        label_hp_bot.place(relx=0.84, rely=0.115, relwidth=0.04, relheight=0.04, )

    def you_start(self):
        self.imgfight = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\you_start.png")
        self.imagem_fight = ImageTk.PhotoImage(self.imgfight)
        self.frame_0 = Label(self.janela, image=self.imagem_fight)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.label_bulb = Label(self.frame_0, image=self.poke_player.name)
        self.label_bulb.place(relx=0.38, rely=0.30, relwidth=0.25, relheight=0.25)
        self.show_hp(self.poke_player.hp, self.poke_bot.hp)
        self.janela.after(3000, self.choose_attack_player)

    def attack_bot(self):
        self.put_attack_bot()
        self.show_hp(self.poke_player.hp, self.poke_bot.hp)
        self.fonte = ('arial', 16, 'bold')
        attack = []
        self.attacks = self.poke_bot.attack
        for i in self.attacks:
            attack.append(i)
        self.attaque_bot = random.choice(attack)
        self.next, self.dano = self.damage(self.attaque_bot, self.poke_bot, self.poke_player)
        if self.next == 'miss':
            self.show_missed('b')
        elif self.next == 'crit':
            self.att1 = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\critical.png")
            self.att1_img = ImageTk.PhotoImage(self.att1)
            self.frame_0 = Label(self.janela, image=self.att1_img)
            self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
            self.show_hp(self.poke_player.hp, self.poke_bot.hp)
            self.janela.after(3000, self.put_attack_bot)
            self.janela.after(3000, self.put_1st_label)
            self.janela.after(3000, self.put_poke_bot)
            self.janela.after(3000, self.show_damage_bot)
        else:
            self.put_1st_label()
            self.put_poke_bot()
            self.janela.after(3000, self.show_damage_bot)

    def put_attack_bot(self):
        self.att1 = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\op_attack.png")
        self.att1_img = ImageTk.PhotoImage(self.att1)
        self.frame_0 = Label(self.janela, image=self.att1_img)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)

    def put_attack_player(self):
        self.att1 = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\pl_attack.png")
        self.att1_img = ImageTk.PhotoImage(self.att1)
        self.frame_0 = Label(self.janela, image=self.att1_img)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
    def show_missed(self, next):
        self.miss = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\missed.png")
        self.missed = ImageTk.PhotoImage(self.miss)
        self.frame_0 = Label(self.janela, image=self.missed)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.show_hp(self.poke_player.hp, self.poke_bot.hp)
        if next == 'a':
            self.janela.after(3000, self.attack_bot)
        else:
            self.janela.after(3000, self.choose_attack_player)
    def put_1st_label(self):
        lab = Label(self.frame_0, text=self.attacks[f'{self.attaque_bot}']['movement'], font=self.fonte, fg='white', background='#727373')
        lab.place(relx=0.12, rely=0.29, relwidth=0.389, relheight=0.089)
    def put_poke_bot(self):
        self.put_1st_label()
        lab_op = Label(self.frame_0, image=self.poke_bot.name)
        lab_op.place(relx=0.75, rely=0.25, relwidth=0.24, relheight=0.24)

    def show_damage_bot(self):
        self.put_poke_bot()
        damage = f"Damage: {self.dano}"
        lab_damage = Label(self.frame_0, text=damage, font=self.fonte, background='#727373', fg='white')
        lab_damage.place(relx=0.34, rely=0.55, relwidth=0.20, relheight=0.05)
        if self.poke_player.hp < 0:
            self.show_hp(self.poke_player.hp, self.poke_bot.hp)
            self.janela.after(3000, self.show_lose)
        else:
            self.show_hp(self.poke_player.hp, self.poke_bot.hp)
            self.janela.after(3000, self.choose_attack_player)

    def choose_attack_player(self):
        attack = []
        attacks = self.poke_player.attack
        for attackk in attacks:
            attack.append(attackk)
        fonte = ('arial', 14, 'bold')
        chose = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\chose_attack.png")
        self.chose_attack = ImageTk.PhotoImage(chose)
        self.frame_0 = Label(self.janela, image=self.chose_attack)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.show_hp(self.poke_player.hp, self.poke_bot.hp)
        self.at1= Button(self.frame_0, text=attack[0], font=fonte, fg='black', background='#FEF339', relief='flat', command=lambda m=attack[0]: self.attack_player(m))
        self.at1.place(relx=0.14, rely=0.57, relwidth=0.16, relheight=0.07)
        self.at2 = Button(self.frame_0, text=attack[1], font=fonte, fg='black', background='#FEF339', relief='flat', command=lambda m=attack[1]: self.attack_player(m))
        self.at2.place(relx=0.43, rely=0.57, relwidth=0.18, relheight=0.07)
        self.at3 = Button(self.frame_0, text=attack[2], font=fonte, fg='black', background='#FEF339', relief='flat', command=lambda m=attack[2]: self.attack_player(m))
        self.at3.place(relx=0.73, rely=0.57, relwidth=0.16, relheight=0.07)

    def damage(self, attack_choice, player, next_player):
        self.attack_choice = attack_choice
        cri = [True, False, True, False]
        miss = [True, True, False, False, False]
        missed = random.choice(miss)
        crit = random.choice(cri)
        if missed:
            return 'miss', 0
        if crit and not missed:
            dic = (player.attacks)
            power = dic[f'{self.attack_choice}']['strenght']+10
            next_player.hp -= power
            return 'crit', power
        elif self.poke_player.advantages(self.poke_bot.type) == 'same' and not missed:
            dic = (player.attacks)
            power = dic[f'{self.attack_choice}']['strenght']
            next_player.hp -= power
            return next_player, power
        elif player.advantages(next_player.type) and not missed:
            dic = (player.attacks)
            power = dic[f'{self.attack_choice}']['strenght'] + 5
            next_player.hp -= power
            return next_player, power
        elif not player.advantages(next_player.type) and not missed:
            dic = (player.attacks)
            power = dic[f'{self.attack_choice}']['strenght'] - 3
            next_player.hp -= power
            return next_player, power

    def attack_player(self, attack):
        print(attack)
        self.put_attack_player()
        self.show_hp(self.poke_player.hp, self.poke_bot.hp)
        self.prox, self.dano_player = self.damage(attack, self.poke_player, self.poke_bot)
        if self.prox == 'miss':
            self.show_missed('a')
        elif self.prox == 'crit':
            self.att1 = Image.open(r"C:\Users\47829927855\Desktop\poke-game-main\img\critical.png")
            self.att1_img = ImageTk.PhotoImage(self.att1)
            self.frame_0 = Label(self.janela, image=self.att1_img)
            self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
            self.show_hp(self.poke_player.hp, self.poke_bot.hp)
            self.janela.after(3000, self.put_attack_player)
            self.janela.after(3000, self.put_1st_label_player)
            self.janela.after(3000, self.put_poke_player)
            self.janela.after(3000, self.show_damage_player)
        else:
            self.put_1st_label_player()
            self.put_poke_player()
            self.janela.after(3000, self.show_damage_player)

    def show_damage_player(self):
        fonte = ('arial', 16, 'bold')
        self.put_poke_player()
        damage = f"Damage: {self.dano_player}"
        lab_damage = Label(self.frame_0, text=damage, font=fonte, background='#727373', fg='white')
        lab_damage.place(relx=0.46, rely=0.86, relwidth=0.20, relheight=0.05)
        if self.poke_bot.hp < 0:
            self.show_hp(self.poke_player.hp, self.poke_bot.hp)
            self.janela.after(3000, self.show_won)
        else:
            self.show_hp(self.poke_player.hp, self.poke_bot.hp)
            self.janela.after(3000, self.attack_bot)
    def put_1st_label_player(self):
        fonte = ('arial', 16, 'bold')
        lab = Label(self.frame_0, text=self.poke_player.attacks[f'{self.attack_choice}']['movement'], font=fonte, fg='white', background='#727373')
        lab.place(relx=0.48, rely=0.60, relwidth=0.36, relheight=0.08)
    def put_poke_player(self):
        self.put_1st_label_player()
        lab_op = Label(self.frame_0, image=self.poke_player.name)
        lab_op.place(relx=0.02, rely=0.70, relwidth=0.24, relheight=0.24)
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

    def show_won(self):
        fonte = ('Arial', 12, 'bold')
        self.frame_0 = Label(self.janela, image=self.won_img)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.btpa = Button(self.frame_0, text="Play again", fg='black', font = fonte, background='#FEF339', relief='flat', command=self.home)
        self.btpa.place(relx=0.46, rely=0.71, relwidth=0.15, relheight=0.045)

    def show_lose(self):
        fonte = ('Arial', 12, 'bold')
        self.frame_0 = Label(self.janela, image=self.lose_img)
        self.frame_0.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        self.btpa = Button(self.frame_0, text="Play again", fg='black', font = fonte, background='#FEF339', relief='flat', command=self.home)
        self.btpa.place(relx=0.45, rely=0.75, relwidth=0.15, relheight=0.045)


jan = Aplicacao()
jan.tela()
