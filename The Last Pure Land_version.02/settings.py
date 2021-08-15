import pygame
import os

# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 600
# frame rate
FPS = 60
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)
# enemy path
PATH = [(802, 16),  (801, 55), (802, 75), (802, 98), (802, 122), (800, 142), (792, 165), (777, 186), 
        (757, 193), (731, 195), (705, 190), (678, 188), (656, 185), (628, 183), (607, 188),(587, 197), 
        (571, 214), (562, 233), (558, 276), (557, 321), (537, 330),(515, 338), (494, 353), (480, 370), 
        (459, 412), (439, 414), (416, 416), (395, 418),(375, 414), (354, 410), (330, 401), (312, 382), 
        (289, 365), (262, 346), (230, 344), (198, 340),(172, 331), (149, 314), (128, 291), (105, 270), 
        (81, 256), (61, 258)]

PATH2 = [(1002, 267), (969, 266), (934, 268), (908, 284), (899, 315), (898, 348), (890, 382), (870, 404), 
         (835, 417), (799, 419), (769, 415), (744, 415), (712, 417), (684, 417), (653, 417), (643, 441), 
         (634, 462), (616, 482), (587, 493), (550, 495), (520, 489), (491, 473), (478, 456), (468, 431), 
         (447, 414), (416, 414), (385, 414), (361, 410), (337, 405), (315, 391), (296, 371), (271, 353), 
         (242, 345), (217, 344), (194, 343), (171, 336), (151, 323), (139, 304), (125, 288), (107, 274), 
         (86, 261), (61, 258)]

guard_PATH_1 = [(61, 258),  (81, 256), (105, 270), (128, 291), (149, 314), (172, 331), (198, 340), (230, 344), 
        (262, 346), (289, 365), (312, 382), (330, 401), (354, 410), (375, 414), (395, 418),(416, 416), 
        (439, 414), (459, 412), (480, 370), (494, 353), (515, 338),(537, 330), (557, 321), (558, 276), 
        (562, 233), (571, 214), (587, 197), (607, 188),(628, 183), (656, 185), (678, 188), (705, 190), 
        (731, 195), (757, 193), (777, 186), (792, 165),(800, 142), (802, 122), (802, 98), (802, 75), 
        (801, 55), (802, 16)]

guard_PATH_2 = [(61, 258), (86, 261), (107, 274), (125, 288), (139, 304), (151, 323), (171, 336), (194, 343), 
         (217, 344), (242, 345), (271, 353), (296, 371), (315, 391), (337, 405), (361, 410), (385, 414), 
         (416, 414), (447, 414), (468, 431), (478, 456), (491, 473), (520, 489), (550, 495), (587, 493), 
         (616, 482), (634, 462), (643, 441), (653, 417), (684, 417), (712, 417), (744, 415), (769, 415), 
         (799, 419), (835, 417), (870, 404), (890, 382), (898, 348), (899, 315), (908, 284), (934, 268), 
         (969, 266), (1002, 267)]
# base
BASE = pygame.Rect(0, 200, 70, 80)
en_BASE_1 = pygame.Rect(802, 16, 70, 80)
en_BASE_2 = pygame.Rect(1002, 267, 70, 80)
# image
BACKGROUND_IMAGE = pygame.image.load(os.path.join("images", "Map.png"))
HP_GRAY_IMAGE = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (40, 40))
HP_IMAGE = pygame.transform.scale(pygame.image.load("images/hp.png"), (40, 40))

