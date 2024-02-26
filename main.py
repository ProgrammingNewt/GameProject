import pygame
from pygame import mixer
import random
import math

#pygame.init() initializes all modules for pygame to work
#"sets up the underlying system and prepares Pygame to handle graphics, sound, events, and other functionalities.""

pygame.init()


#sets up the screen in pygame
#the 2 values will the Width and Height (W pixel x H pixel)

screen = pygame.display.set_mode((800, 600))
#when run, screen opens and closes immediately
#this is bc python runs the program line by lane and then ends the program: need to fix this

#Background
background = pygame.image.load("SpaceBG.png")

#Background sound

# Background sound
#background_sound = pygame.mixer.Sound('Tetris.wav')
#background_sound.play(-1)  # Start playing the sound, loop indefinitely



# pygame.display is a command to deal with anything regarding the display window
#Display Titale and Icon 
pygame.display.set_caption("Newt Invaders")
#Display icon must be .png and 32 x 32 pixels
icon = pygame.image.load("Newtt_Love.png")
pygame.display.set_icon(icon)


#Player image
playerimg = pygame.image.load("spaceship64.png")
playerX = 370
playerY = 480
playerX_change = 0

#Enemy image
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    #moves down a little
    enemyY_change.append(30)

#Bullet 
#Ready - you cant see bullet on screen
#Fire - the bullet is moving
bulletimg = pygame.image.load("laserbullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 24)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))
    
    
def player(x, y):
    #.blit() is to draw, draws image of player on screen
    #needs (image and coordinates)
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    #.blit() is to draw, draws image of player on screen
    #needs (image and coordinates)
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    #16 and 10 are so they are at the center of the ship
    screen.blit(bulletimg, (x + 28, y + 10))

""" def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27: 
        return True
    else:
        return False
        """
#game loop that runs the game
running = True

while running:
    
    #Screen color as R, G, B values
    screen.fill((0, 0, 0))
    #background and coordinates
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if close button is pressed, ends the program
            running = False
    
        #when keystroke pressed, check right or left
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
                
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Gets current x coordinate of spaceship for bullet
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                
        #When keystroke released    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                
    
                
    
    #player method must be after screen. 
    #screen drawn first and then player is drawn on top of screen
    playerX += playerX_change
    
    #player boundary
    if playerX <= 0:
        playerX = 0
        
    #We use 736 because the image is 64 pixels
    elif playerX >= 736:
        playerX = 736
    
    
    
    #enemy movement
    
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        
        #enemy boundary
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
            
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        
        # Create Rect objects for enemy and bullet
        enemy_rect = pygame.Rect(enemyX[i], enemyY[i], enemyimg[i].get_width()-30 , enemyimg[i].get_height()-30)
        bullet_rect = pygame.Rect(bulletX, bulletY, bulletimg.get_width(), bulletimg.get_height())
    
        # Collision
        if enemy_rect.colliderect(bullet_rect):
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)
    
        
    # Bullet movement
    if bulletY <= 0: 
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        
    # Collision
    
    
     
    
    
    
    
    
    
    
    """collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
        """
        
    
        
    
    player(playerX, playerY)
    show_score(textX, textY)

    #very important line, need to update screen things move and change
    pygame.display.update()