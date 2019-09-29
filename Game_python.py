# консольное приложение  
# компьютер вс игрок      
# рандомные ходы        
# одинаковое ХП (150)    

# рандомно        
# средний урон (18-25)   
# большой урон (10-35)   
# лечение (18-25)            

# сообщение после каждого действия    
# которое сообщает что произошло             
# и сколько здоровья у Игрока и Компьютера.   

# когда здоровье Компьютера достигает 35%, шанс на лечение больше 
# 0 хп - смерть
   
import random
import time
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
import os
# Подключили модули
os.system('cls')
 
# начало класса
class Player:
    health = 150 # очки здоровья игрока и бота ( ХП, health point )
    live = True # живой = правда
    cheat = True # переменная нужная для вывода сообщение о том, что у бота меньше 35% хп

    def use(self):
        return random.randint(0, 2) # метод для выбора шагов (умереный удар, рандомный удар, лечение)

    def hp_Bar(self):
        return  eval('print(Fore.CYAN +"{0}: {1} HP\t\t{2}: {3} HP \v".format(player1.name,player1.health,bot.name,bot.health))')
        # метод для вывода здоровья игрока и компьютера

    def step(self):
        self.s = random.randint(0, 4)
        phrase= {
            0: 'input(Fore.BLUE + Style.BRIGHT+"{}, давай нападай (Enter)".format(player1.name))',
            1: 'input(Fore.BLUE  +Style.BRIGHT+"{}, заходи, сбоку заходи! (Enter)".format(player1.name))',
            2: 'input(Fore.BLUE  +Style.BRIGHT+"Я МАСЛИНУ ПОЙМАЛ ААААА, КОРЕШ ПОМОГИ (Enter)")',
            3: 'input(Fore.BLUE  +Style.BRIGHT+"{}, да давай пиромантией убивай уже (Enter)".format(player1.name))',
            4: 'input(Fore.BLUE  +Style.BRIGHT+"{},あなたは最高です (Enter)".format(player1.name))'}
        return phrase[self.s] # метод для рандомного вывода фраз "нажать на Enter"

    def bot_Сheat (self):
        if self.cheat == True: # IF выдает фразу, что у бота меньше 35% хп и делает так, что бы она не появлялась на каждом действии бота при количестви хп меньше 35%
            print(Fore.RED + Style.NORMAL+"Liquid Snake: "+Fore.CYAN +Style.BRIGHT+Back.RED+'КРЕЕЕЕЕЕЕЕЕЕЕЕЙЗИИИИИ ДААААЙЙЙМОНТ')
            self.cheat=False  # срабатывает каждый раз, когда получает урон и переходит границу 35%, при том что было больше 35% хп 
        return random.randint(0, 3) # По сюжету игры, это заклинание которое увеличивает шанс вылечиться (50%), сам метод увеличавает шанс "полечиться"

    def __init__(self, name):
        self.name = name

    def midle_Hit(self):
        hit1 = random.randint(18, 25) 
        print(Fore.MAGENTA +"\v{0} нанес урон своим very rare оружием на {1} единиц".format(self.name, hit1))
        return hit1 # метод - удар с умереным уроном, принт вывод действие, что это "удар с умереным уроном"

    def random_Hit(self):
        hit2 = random.randint(10, 35)
        print(Fore.RED +Style.BRIGHT+'\v{0} использовал пиромантию архимагов "Взрыв Мегумин" на {1} единиц урона'.format(self.name, hit2))
        return hit2 # метод - пиромантия с большим диапазоном урона, принт вывод действие

    def heal(self):
        hp = random.randint(18, 25)
        print(Fore.GREEN +"\v{0} восполнил эстусом здоровье на {1} ХП".format(self.name, hp))
        self.health = self.health + hp  # метод - лечение, выводи действие
        if self.health > 150: 
            self.health = 150 # что бы Очки Здоровья не поднимались больше 150 единиц 
        
    def died(self):
        if self.health <= 0:
            print(Back.RED +"{} Died 死ぬ\n".format(self.name))
            self.live = False # метод - проверка на смерть, у кого хп будет меньше 0 - умирает, игра заканчиваеться, self.live = False (что бы остановить цыкл )
    # конец класса
            
time.sleep(1.5) # очень полезный текст
print(Fore.GREEN+Style.NORMAL+'От разработчиков "The Last of Us"', end=" ")
time.sleep(3)
print(Fore.GREEN+Style.NORMAL+'был интересный трейлер к "The Last of Us 2"\n')
time.sleep(3)
print(Fore.GREEN+Style.NORMAL+"В разработке принимали участие Hideo Kojima, Cory Barlog, Hidetaka Miyazaki", end="")
time.sleep(4)
print(Fore.GREEN+Style.NORMAL+"в таких играх как серия MGS, God Of War и Dark Souls\n\n")
time.sleep(3)
print(Fore.YELLOW+Style.BRIGHT+"\t\t\t\tThe Final SaperCraft",end=" ") # название игры
time.sleep(3)
print(Fore.MAGENTA +Style.NORMAL+"2077\n\n")
time.sleep(4)

print (Fore.GREEN+Style.NORMAL+"В эру древних, мир был бесформленным, его окутывал туман. Это была земля серых утесов, древних и присносущих драконов. но за тем был огонь и с приходом Огня все распалось на две части. Жар и Холод. Жизнь и Смерть. И, конечно, Свет и Тьма " + \
        Fore.GREEN+Style.NORMAL+"Через очень долгое время, на земле серых утесов и других земель тоже, другой вселенной и  в другое время, с другими людми и животными. " + \
        Fore.GREEN+Style.NORMAL+"Живут Hunters, которые должны нести свою службу оберегая обычных людей от драконов-химер и их стендов. " + \
        Fore.GREEN+Style.NORMAL+"Там же ходят слухи об одном не вероятно сильном герое, О Гатце из Берсерии. " + \
        Fore.GREEN+Style.NORMAL+"Возможно прям сейчас вы будете играть за него, не точно.\n")
input(Fore.BLUE+"Нажмите "+Fore.GREEN+ "Enter " +Fore.BLUE+"чтобы пропустить увлекательный лор игры") # очень полезный текст конец

player1 = Player(input(Fore.BLUE+Style.BRIGHT+"Боец, введи свой позывной: ")) # ввод имени игрока и компьютера
bot = Player("Liquid Snake")
print(Fore.GREEN+Style.NORMAL+"Нет времени объяснять, "+Fore.RED+Style.NORMAL+"Liquid Snake "+Fore.GREEN+Style.NORMAL+"Пришел не известно откуда и хочет захвать Зельдарию.")


while player1.live == True and bot.live == True: # начало цикла, работает если все живы
    if random.randint(0, 1) == 0: # определяет кто ходит
        time.sleep(1.5)
        exec(player1.step())    # выводит разные инпуты, что бы игрок нажимал "энтер", это главный геймплей игры
        time.sleep(1.5)
        if player1.use() == 0:  # проверка на удар с умереным уроном
            bot.health = bot.health - player1.midle_Hit()    # удар
            player1.hp_Bar()     # здоровье игрока и компьютера
            bot.died()  # проверяет состояние противника после удара
        elif player1.use() == 1:    # проверка на удар с большим диапазоном 
            bot.health = bot.health - player1.random_Hit() # удар
            player1.hp_Bar()
            bot.died()
        else: 
            player1.heal()  # лечиться
            player1.hp_Bar()
    else:
        if bot.health > (150 * 0.35): # проверяет больше ли 35% здоровья у компьютера
            time.sleep(2.5)  # тайм слипы должны показать что опонент игрока тоже "Энтеры" нажимает
            bot.cheat = True # для того, что бы бот говорил заклинание когда меньше 35% хп
            if bot.use() == 0: # проверка на удар с умереным уроном
                player1.health = player1.health - bot.midle_Hit()  # удар
                bot.hp_Bar()      # здоровье игрока и компьютера
                player1.died() # проверяет состояние игрока после удара         
            elif bot.use() == 1:   # проверка на удар с большим диапазоном 
                player1.health = player1.health - bot.random_Hit()  # удар 
                bot.hp_Bar()
                player1.died()
            else: 
                bot.heal()   # лечиться
                bot.hp_Bar()
        else:
            time.sleep(2.5)   # когда меньше 35% единиц здоровья
            if bot.bot_Сheat() == 0: # проверка на умереный удар
                player1.health = player1.health - bot.midle_Hit()    # удар
                bot.hp_Bar()
                player1.died()  # проверяет состояние игрока после удара
            elif bot.bot_Сheat() == 1:   # проверка на удар с большим диапазоном 
                player1.health = player1.health - bot.random_Hit()
                bot.hp_Bar()     # здоровье игрока и компьютера
                player1.died()   
            else: 
                bot.heal() # лечиться , если рандомное число 2 или 3 (увеличеный шанс излечиться)
                bot.hp_Bar()
time.sleep(1)
if player1.live == True and bot.live == False: # проверяет кто умер
    print(Fore.BLUE+Style.BRIGHT+"{0}".format(player1.name)+Fore.YELLOW+Style.BRIGHT+", ПОЗДРАВЛЯЮ, вы наш КОРОЛЬ. За победу над "+Fore.RED+Style.BRIGHT+"Liquid Snake"+\
        Fore.YELLOW+Style.BRIGHT+" вы получили здоровенный замок в Альтисии, городе на воде. Но через некоторое время, месяц, его разрушил большой морской дракон-змей, из-за чего погибло много людей."+\
        Fore.BLUE+Style.BRIGHT+" {0}".format(player1.name)+Fore.YELLOW+Style.BRIGHT+" выжил, потому что вызваный морской дракон-змей "+Fore.BLUE+Style.BRIGHT+"Левиафан"+Fore.YELLOW+Style.BRIGHT+" не может атаковать родствеников "+\
        Fore.BLUE+Style.BRIGHT+"Liquid Snake"+Fore.YELLOW+Style.BRIGHT+". Добравшись до ближайшей суши, от Альтисии, вас сьел дракон, красный, обычный")  
    print(Fore.RED+Style.BRIGHT+"the end")      # конец игры 1
else:
    print(Fore.GREEN+Style.BRIGHT+"{0} ".format(bot.name)+Fore.YELLOW+Style.BRIGHT+"захватил Зельдарию, на земле серых утесов и других земель тоже, стало невероятно хорошо жить. Hunters и "+\
        Fore.GREEN+Style.BRIGHT+"{0}".format(bot.name)+Fore.YELLOW+Style.BRIGHT+" одолели главных драконов-химер Мидира и Коломита. Жители Зельдари долгие века прославляли великого правителя "+\
        Fore.GREEN+Style.BRIGHT+"{0}".format(bot.name)+Fore.YELLOW+Style.BRIGHT+", в честь него своих детей называли 'Солидусами'. Снимали фильмы и цитировали мемы про него. ") 
    print(Fore.GREEN+Style.BRIGHT+"the end") # конец игры 2