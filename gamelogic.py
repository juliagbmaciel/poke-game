from pokeclass import Grass, Fire, Water
from time import sleep
import random
import inquirer
import os


class Play:
    def __init__(self):
        types = ['bot', 'player']
        self.pokemons_bot = []
        for type in types:
            self.pokemons = [Grass('Bulbasaur', 45, 45, {'Razor Leaf': {'type': 'Physical', 'strenght': 10,  'movement': 'throwing blades at the opponent...'},
                'Stun Spore': {'type': 'Status', 'strenght': 10, 'movement': 'spreading cloud of numbing powder...'},
                'Absorb': {'type': 'Physical', 'strenght': 10, 'movement': 'draining the opponents ...'}}, type),
                             Fire('Charmander', 65, 39, {'Blaze Kick': {'type': 'Physical', 'strenght': 10, 'movement': 'kicking the opponent...'},
                'Fire Blast': {'type': 'Physical', 'strenght': 10, 'movement': 'Attacking opponent with an intense blast...'},
                'Sunny Day': {'type': 'Status', 'strenght': 10, 'movement': 'Intensifying the sun...'}}, type),
                             Water('Squirtle', 43, 44, {'Rain Dance': {'type': 'Status', 'strenght': 10, 'movement': 'Summoning rain...'},
                'Bubble Beam': {'type': 'Status', 'strenght': 10, 'movement': 'Throwing bubble spray at the opponent...'},
                'Razor Shell': {'type': 'Status', 'strenght': 10, 'movement': 'Slashing opponent with shells...'}}, type)]
            if type == 'bot':
                self.pokemons_bot.append(self.pokemons)
        self.battle()

    def define_player(self):
        """
        Player escolhe o pokemon que irá batalhar no jogo
        :return: classe do pokemon escolhido
        """
        questions = [
            inquirer.List(
                "character",
                message="Choose your character",
                choices=[self.pokemons[0].name, self.pokemons[1].name, self.pokemons[2].name],
            ),
        ]
        answers = inquirer.prompt(questions)
        player_choice = answers['character']
        for i in range(3):
            if player_choice == self.pokemons[i].name:
                player_choice = self.pokemons[i]
                return player_choice

    def return_bot_player(self):
        """
        Escolhe um pokemon e armazena na variável do bot
        :return: classe de pokemon escolhida pelo bot
        """
        random.shuffle(self.pokemons_bot[0])
        poke_bot = self.pokemons_bot[0][0]
        return poke_bot

    def choice_player(self):
        """
        Escolhe quem começa o jogo de acordo com a velocidade
        :return: str com o valor da variável pra fazer comparação, e a própria classe do jogador que começará
        """
        if self.poke_bot.speed > self.poke_player.speed:
            print("THE OPPONENT START!!")
            print(f"The opponent chose: {self.poke_bot.name}, with speed {self.poke_bot.speed}!!")
            return 'self.poke_bot', self.poke_bot, 'self.poke_player'
        elif self.poke_bot.speed < self.poke_player.speed:
            print("YOU WILL START!!!")
            print(f"Your speed is {self.poke_player.speed}")
            return 'self.poke_player', self.poke_player, 'self.poke_bot'
        else:
            players = ['player', 'opponent']
            choice = random.choice(players)
            print(f"You are similar, so the computer choose the {choice} to start!")
            if choice == 'player':
                return 'self.poke_player', self.poke_player, 'self.poke_bot'
            else:
                return 'self.poke_bot', self.poke_bot, 'self.poke_player'

    def choice_attack(self):
        """
        :return: chave com valores do ataque escolhido
        """
        if self.player_str == 'self.poke_player':
            self.attacks = []
            attack = self.poke_player.attack
            for key in attack:
                self.attacks.append(key)
            questions = [
                inquirer.List(
                    "attack",
                    message="Choose your attack",
                    choices=[attack for attack in self.attacks],
                ),
            ]
            answers = inquirer.prompt(questions)
            values = self.poke_player.attack.get(answers['attack'])
            return values
        elif self.player_str == 'self.poke_bot':
            sleep(3)
            self.attacks = []
            attack = self.poke_bot.attack
            for key in attack:
                self.attacks.append(key)
            choice = random.choice(self.attacks)
            print(f'The opponent choose the {choice} attack!!!!')
            return self.poke_bot.attack.get(choice)

    def damage(self, value, text='self.poke_player', operator='less'):
        """
        Calcula o dano de acordo com a vantagem sob o adversario
        :param value: dicionario referente ao ataque
        :param text: próximo jogador
        :param operator: se irá somar ou diminuir de acorodo com a vantagem
        :return: próximo jogador
        """
        special = random.choice([False, True, False, False, True])
        wrong = random.choice([False, True])
        power = value['strenght']
        if wrong:
            print("Oh damn, missed this one!!")
            sleep(2)
            return text
        elif special:
            power = value['strenght'] + 10
            print(f'Oh! It was critical')
        elif operator == 'plus' and not special:
            power = value['strenght'] + 5
        elif operator == 'less' and not special:
            power = value['strenght'] - 3
        print(value['movement'])
        sleep(2)
        print(f"Damage: {power}")
        sleep(2)
        if text == 'self.poke_player':
            self.poke_player.hp -= power
        else:
            self.poke_bot.hp -= power
        return text

    def default_damage(self, value, text='self.poke_player'):
        """
        calcula o dano caso sejam o mesmo pokemon
        :param value: dicionário de valores referente ao ataque
        :param text: prox jogador
        :return: prox jogador
        """
        print(f"Damage: {value['strenght']}")
        sleep(1)
        print(value['movement'])
        if text == 'self.poke_player':
            self.poke_player.hp -= value['strenght']
        else:
            self.poke_bot.hp -= value['strenght']
        return text

    def battle(self):
        """
        faz a lógica da batalha e configura os pokemons, chama todas as funções de configuração
        """
        self.poke_player = self.define_player()
        self.poke_bot = self.return_bot_player()
        self.player_str, self.player_one, self.player_two = self.choice_player()
        sleep(3)

        while self.poke_bot.hp > 0  and self.poke_player.hp > 0:
            os.system('cls')
            print(f"PLAYER HP: {self.poke_player.hp}")
            print(f"OPPONENT HP: {self.poke_bot.hp}")
            if self.player_str == 'self.poke_player':
                value = self.choice_attack()
                if self.poke_player.advantages(self.poke_bot.type):
                    self.player_str = self.damage(value, 'self.poke_bot', 'plus')
                elif not self.poke_player.advantages(self.poke_bot.type):
                    self.player_str = self.damage(value, 'self.poke_bot')
                else:
                    self.player_str = self.default_damage(value, 'self.poke_bot')
            elif self.player_str == 'self.poke_bot':
                value = self.choice_attack()
                if self.poke_bot.advantages(self.poke_player.type):
                    self.player_str = self.damage(value, 'self.poke_player', 'plus')
                elif not self.poke_bot.advantages(self.poke_player.type):
                    self.player_str = self.damage(value, 'self.poke_player')
                else:
                    self.player_str = self.default_damage(value, 'self.poke_player')

        if self.poke_bot.hp > 0:
            print("YOU LOSE!!")
        else:
            print("YOU WON")


j = Play()
