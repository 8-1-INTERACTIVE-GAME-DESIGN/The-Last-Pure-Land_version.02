import pygame
from tower.towers import Tower, Vacancy
from settings import WIN_WIDTH, WIN_HEIGHT

"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""


class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        
        """add new enemy"""
        if  model.enemies_is_empty() and model.attack == 1:
            model.wave += 1
            if model.wave >= 2:
                model.wave = 2
            model.enemies.add(model.wave_to_enemies[model.wave])
            model.attack = 0


class TowerSeller:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """sell tower"""
        if user_request == "sell":
            x, y = model.selected_tower.rect.center
            model.money += int(model.selected_tower.get_cost()/2)
            model.plots.append(Vacancy(x, y))
            model.towers.remove(model.selected_tower)
            model.selected_tower = None


class TowerDeveloper:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """(Bonus.1) upgrade tower"""
        if user_request == "upgrade" and model.selected_tower.level < 5:
            # if the money > upgrade cost of the selected tower , level+1
            # use model.selected_tower to access the selected tower data
            # use model.money to access to money data
            if model.money > model.selected_tower.get_upgrade_cost():
                model.money -= model.selected_tower.get_upgrade_cost()
                model.selected_tower.level += 1
            pass



class TowerFactory:
    def __init__(self, subject):
        subject.register(self)
        self.tower_name = ["Disinfection", "rapid test", "alcohol"]

    def update(self, user_request: str, model):
        """add new tower"""
        for name in self.tower_name:
            if user_request == name:
                x, y = model.selected_plot.rect.center
                tower_dict = {"Disinfection": Tower.DISINFECTION(x, y), "rapid test": Tower.RapidTest(x, y), "alcohol": Tower.Alcohol(x, y)}
                new_tower = tower_dict[user_request]
                if model.money > new_tower.get_cost():
                    model.money -= new_tower.get_cost()
                    model.towers.append(new_tower)
                    model.plots.remove(model.selected_plot)
                    model.selected_plot = None


class Music:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.set_volume(0.01)
            pygame.mixer.music.unpause()
            model.sound.play()


class Muse:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """unpause the game"""
        if user_request == "mute":
            pygame.mixer.music.set_volume(0)
            pygame.mixer.music.pause()
            model.sound.stop()

class Pause:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """pause the game"""
        global pause
        pause = True
        if user_request == "pause":
            while pause: 
                pause = True
                screen = pygame.display.set_mode((1024,600))
                screen.fill((0,0,0))
                largeText = pygame.font.SysFont("comicsansms",115)
                smallText = pygame.font.SysFont("comicsansms",20)
                TextSurf = largeText.render('pause', True, (255,255,255))
                TextSurf2 = smallText.render('press u to unpause', True, (255,255,255))
                screen.blit(TextSurf, (WIN_WIDTH // 3  , WIN_HEIGHT // 3))
                screen.blit(TextSurf2, (WIN_WIDTH // 3  + 50 , WIN_HEIGHT // 3 + 150))


                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN or user_request == "continue":
                        if event.key == pygame.K_u:  # Unpausing
                            pause = False
                            break
class A_O_E:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "aoe":
            if model.money >= 500:
                for en in model.enemies.get():
                    if en.health <= 3:
                        en.health = 0
                    en.health = en.health//2
                model.money -= 500
                pass
class Heal:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "heal":
            if model.money >= 150 and model.hp < 10:
                model.hp += 1
                model.money -= 150
                pass