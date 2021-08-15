import pygame
import math
import os
from settings import guard_PATH_1,guard_PATH_2, en_BASE_1,en_BASE_2,IMAGE_PATH,SOUND_PATH
from color_settings import *
#import random

# pygame.init()
GUARD_IMAGE = [pygame.transform.scale(pygame.image.load(os.path.join("images", "guard_1.png")), (60, 90)),
                pygame.transform.scale(pygame.image.load(os.path.join("images", "guard_2.png")), (60, 90))]
                
                

class Guard:
    def __init__(self, herotype):
        self.hero_type = herotype
        self.path = guard_PATH_1
        self.path_index = 0
        self.move_count = 0
        self.stride = self.move_speed(self.hero_type)
        if self.hero_type == 'howhow':    
            self.image = self.hero_image(self.hero_type)[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.health = self.hero_hp_maxhp(self.hero_type)
        self.max_health = self.hero_hp_maxhp(self.hero_type)
        self.attack_count = 0
        self.attack_max_count = self.attack_max_cd(self.hero_type)
        self.power = self.hero_power(self.hero_type)
        self.range = self.attack_range(self.hero_type)
        self.attack_music = self.hero_attacksound(self.hero_type)

    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / self.stride)
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance
        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count
        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.rect.center = self.path[self.path_index]
            
        if self.hero_type == 'howhow':    
            self.image = self.hero_image(self.hero_type)[self.move_count//6 % 6]
        elif self.hero_type == 'godtone' :
            self.image = self.hero_image(self.hero_type)[self.move_count//8 % 5]
        elif self.hero_type == 'p' :
            self.image = self.hero_image(self.hero_type)[self.move_count//8 % 5]     
    
    def attack(self):
        if(self.attack_count < self.attack_max_count):
            self.attack_count += 1
            return False
        else:
            self.attack_count = 0
            self.attack_music.set_volume(0.8)
            pygame.mixer.Channel(1).play(self.attack_music)
            return True
        
    # 不同英雄的圖片
    def hero_image(self, herotype):
        if(herotype == 'howhow'):
            return HOWHOW_IMAGE
        elif(herotype == 'godtone'):
            return GODTONE_IMAGE
        elif(herotype == 'p'):
            return P_IMAGE
        
    # 攻擊聲音
    def hero_attacksound(self, herotype):
        if(herotype == 'howhow'):
            return pygame.mixer.Sound(os.path.join(SOUND_PATH,"punch2.wav"))
        elif(herotype == 'godtone'):
            return pygame.mixer.Sound(os.path.join(SOUND_PATH,"punch3.wav"))
        elif(herotype == 'p'):
            return pygame.mixer.Sound(os.path.join(SOUND_PATH,"longshot.mp3"))
        
    # 最大血量
    def hero_hp_maxhp(self, herotype):
        if(herotype == 'howhow'):
            return 15
        elif(herotype == 'godtone'):
            return 30
        elif(herotype == 'p'):
            return 10
        
        
    # 攻擊力    
    def hero_power(self, herotype):
        if(herotype == 'howhow'):
            return 3
        elif(herotype == 'godtone'):
            return 2
        elif(herotype == 'p'):
            return 7
        
        
    # 移動速度    
    def move_speed(self, herotype):
        if(herotype == 'howhow'):
            return 1.5
        elif(herotype == 'godtone'):
            return 1
        elif(herotype == 'p'):
            return 0.6
        
        
    # 攻擊最大冷卻    
    def attack_max_cd(self, herotype):
        if(herotype == 'howhow'):
            return 60
        elif(herotype == 'godtone'):
            return 60
        elif(herotype == 'p'):
            return 100
        
        
    # 要不要攻擊
    def attack(self):
        if(self.attack_count < self.attack_max_count):
            self.attack_count += 1
            return False
        else:
            self.attack_count = 0
            self.attack_music.set_volume(0.5)
            pygame.mixer.Channel(1).play(self.attack_music)
            return True
   
    # 攻擊距離
    def attack_range(self, herotype):
        return 60

class HeroGroup:
    def __init__(self):
        self.__reserved_members = []
        self.expedition = []

    def he_to_en_range(self, hero, enemy):
        x1, y1 = enemy.rect.center
        x2, y2 = hero.rect.center
        distance = math.sqrt((x2 - x1) ** 2)
        if distance <= hero.range:
            return True
        return False
    
    def he_to_base_range(self, hero):
        x1, y1 = hero.rect.center
        x2, y2 = en_BASE.center
        distance = math.sqrt((x2 - x1) ** 2 )
        if distance <= hero.range:
            return True
        return False
    
    def advance(self, model):
        self.sort_list()
        for hero in self.expedition:
            if hero.health <= 0:
                self.retreat(hero)
            if self.he_to_base_range(hero) :
                if(hero.attack()) and model.entower_hp > 0:
                    model.entower_hp -= hero.power
                elif model.entower_hp < 0:
                    model.entower_hp = 0
            elif model.en.expedition:
                for en in model.en.expedition:
                    if self.he_to_en_range(hero, en):
                        if(hero.attack()):
                            en.health -= hero.power
                            break
                        else:
                            break
                    else:
                        hero.move()
                        break
            else:
                hero.move()
                              
    def sort_list(self):
        for i in range(1, len(self.expedition)):
            if(self.expedition[i].rect.centerx < self.expedition[0].rect.centerx):
                temp = self.expedition[0]
                self.expedition[0] = self.expedition[i] 
                self.expedition[i] = temp

    def add(self, herotype):
        """Generate the enemies for next wave"""
        if herotype == 'howhow':
            self.expedition.append(Hero('howhow'))
        elif herotype == 'godtone':
            self.expedition.append(Hero('godtone'))
        elif herotype == 'p':
            self.expedition.append(Hero('p'))

    def get(self):
        """Get the enemy list"""
        return self.expedition

    def is_empty(self):
        """Return whether the enemy is empty (so that we can move on to next wave)"""
        return False if self.__reserved_members or self.expedition else True

    def retreat(self, guard):
        """Remove the enemy from the expedition"""
        self.expedition.remove(guard)
        
    
        