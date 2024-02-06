import random 
import pygame 
import os 


from pygame.constants import QUIT,K_DOWN,K_UP,K_RIGHT,K_LEFT
pygame.init()

HEIGHT = 800
WEIDTH = 1200
FPS=pygame.time.Clock()


FONT = pygame.font.SysFont("Verdana", 20)#робимо шрифт 

bg = pygame.transform.scale(pygame.image.load('background.png'), (WEIDTH, HEIGHT)) #фотографія cтатичного фону 
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3 
#робимо барабан з картинок, щоб був ефект руху 


COLOR_WITHE = 255,255,255
COLOR_BLACK = 0,0,0
COLOR_BLUE = 0, 0, 255
COLOR_BLUE1 = 0,255,255



main_display=pygame.display.set_mode((WEIDTH,HEIGHT)) #робимо екран самої гри 

IMAGE_PATH = "goose"
PLAYER_IMAGEG = os.listdir(IMAGE_PATH)


player_size = 182,76 
player = pygame.image.load('player.png').convert_alpha() #фотографія 
#pygame.Surface((player_size))#вводимо ігрока в гру 
player_rect = player.get_rect(x=0,y=(HEIGHT/2)-76/2)#додаємо рух ігракові 
#player.fill((COLOR_BLACK))
player_move_down = [0,4]
player_move_up = [0,-4]
player_move_left = [-4,0]
player_move_right = [4,0]
#player_speed = [1,1]

def create_enemy():#функція, яка робить противників 
    enemy_size = (205,72)
    enemy = pygame.image.load('enemy.png').convert_alpha()
    #pygame.Surface(enemy_size)#вводимо противника в гру 
    #enemy.fill((COLOR_BLUE))
    enemy_rect = pygame.Rect(WEIDTH, random.randint(50,HEIGHT-50), *enemy_size) #додаємо рух ігракові, рух зправо на ліво
    enemy_move = [random.randint(-8,-4),0] #додаємо рух ігракові, рух зправо на ліво
    return [enemy, enemy_rect, enemy_move]#повертаємо список усіх противників,

def create_bonus():#функція, яка робить bonus 
    bonus_size = (179,298)
    bonus = pygame.image.load('bonus.png').convert_alpha()
    #pygame.Surface(bonus_size)#вводимо противника в гру 
    #bonus.fill((COLOR_BLUE1))
    bonus_rect = pygame.Rect(random.randint(30,WEIDTH-(50+298)), -298, *bonus_size) #додаємо рух ігракові, рух зправо на ліво
    bonus_move = [0, random.randint(4,8)] #додаємо рух ігракові, рух зправо на ліво
    return [bonus, bonus_rect, bonus_move]#повертаємо список усіх противників,

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY,1500)
CREATE_BONUS = CREATE_ENEMY + 1
pygame.time.set_timer(CREATE_BONUS,3000)
CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE,200)

enemies = []
bonuses = []

image_index = 0 #індекс списку фотографія, щоб зробити рух

score = 0 #к-сть бонусів

playing = True
while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False 
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGEG[image_index]))
            image_index += 1 
            if image_index >= len(PLAYER_IMAGEG):
                image_index = 0
                


    keys = pygame.key.get_pressed()

    bg_X1 -= bg_move #зміщаємо картинку
    bg_X2 -= bg_move 

    if bg_X1 < - bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < - bg.get_width():
        bg_X2 = bg.get_width()

    main_display.blit(bg,(bg_X1,0))
    main_display.blit(bg,(bg_X2,0))
    # main_display.fill((COLOR_BLACK)) в іграграх логіка слоїв така ж сама як й в фотошопі спочатку низ, потім на нього усе наслоюємо 

    if keys[K_DOWN] and player_rect.bottom < HEIGHT: #управління гравця
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WEIDTH: #управління гравця
        player_rect = player_rect.move(player_move_right)
    
    if keys[K_UP] and player_rect.top > 0: #управління гравця
        player_rect = player_rect.move(player_move_up)

    if keys[K_LEFT] and player_rect.left > 0: #управління гравця
        player_rect = player_rect.move(player_move_left)
    
    for enemy in enemies:
        enemy[1]= enemy[1].move(enemy[2])
        main_display.blit(enemy[0],enemy[1])#розташовуємо противника на полі, а через те що це рандом, проводити треба через список

        if player_rect.colliderect(enemy[1]):#зіткнення з предметом 
            playing = False

    for bonus in bonuses:
        bonus[1]= bonus[1].move(bonus[2])
        main_display.blit(bonus[0],bonus[1])#розташовуємо бонуси на полі, а через те що це рандом, проводити треба через список
        
        if player_rect.colliderect(bonus[1]):#зіткнення з предметом 
            score +=1
            bonuses.pop(bonuses.index(bonus))

    main_display.blit(player,player_rect) #розташовуємо гравця на полі 
    main_display.blit(FONT.render(str(score), True, COLOR_BLACK),(WEIDTH - 50,20)) #розташовуємо бали на полі 


    pygame.display.flip()

    
    for enemy in enemies:
        if enemy[1].left < -205: 
            enemies.pop(enemies.index(enemy))
    
    for bonus in bonuses:
        if bonus[1].top > HEIGHT+298: 
            bonuses.pop(bonuses.index(bonus))
