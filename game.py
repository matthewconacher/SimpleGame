# Pacman Styled Side Scrolling Game

import sys # For exit routine.
import random # Import to generate random numbers.
import pygame # Imports a game library that lets you use specific functions in your program.

# Initialize the pygame modules to get everything started.
pygame.init()

# The screen that will be created needs a width and a height.
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680

# This creates the screen and gives it the width and height specified as a 2 item sequence.
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create and assign player, enemies and prizes.
PLAYER = pygame.image.load("player.png")
PLAYER = pygame.transform.scale(PLAYER, (49, 58)) #resize.

ENEMY1 = pygame.image.load("monster.png")
ENEMY1 = pygame.transform.scale(ENEMY1, (79, 70)) #resize.

ENEMY2 = pygame.image.load("monster.png")
ENEMY2 = pygame.transform.scale(ENEMY2, (79, 70)) #resize.

ENEMY3 = pygame.image.load("monster.png")
ENEMY3 = pygame.transform.scale(ENEMY3, (79, 70)) #resize.

PRIZE1 = pygame.image.load("prize.png")
PRIZE1 = pygame.transform.scale(PRIZE1, (49, 37)) #resize.

PRIZE2 = pygame.image.load("prize.png")
PRIZE2 = pygame.transform.scale(PRIZE2, (49, 37)) #resize.

# Get the width and height of the images in order to do
# boundary detection (i.e. make sure the image stays within screen boundaries or know when the image
# is off the screen).
IMAGE_HEIGHT = PLAYER.get_height()
IMAGE_WIDTH = PLAYER.get_width()

ENEMY1_HEIGHT = ENEMY1.get_height()
ENEMY1_WIDTH = ENEMY1.get_width()

ENEMY2_HEIGHT = ENEMY2.get_height()
ENEMY2_WIDTH = ENEMY2.get_width()

ENEMY3_HEIGHT = ENEMY3.get_height()
ENEMY3_WIDTH = ENEMY3.get_width()

PRIZE1_HEIGHT = PRIZE1.get_height()
PRIZE1_WIDTH = PRIZE1.get_width()

PRIZE2_HEIGHT = PRIZE2.get_height()
PRIZE2_WIDTH = PRIZE2.get_width()

print("This is the height of the player image: " +str(IMAGE_HEIGHT))
print("This is the width of the player image: " +str(IMAGE_WIDTH))

# Store the positions of the player and enemy as variables so that you can change them later.
PLAYER_XPOSITION = 50
PLAYER_YPOSITION = 50

# Make the enemy start off screen and at a random y position.
# enemy1
ENEMY1_XPOSITION = SCREEN_WIDTH
ENEMY1_YPOSITION = random.randint(0, SCREEN_HEIGHT - ENEMY1_HEIGHT)

# enemy2 - staggered by 100
ENEMY2_XPOSITION = SCREEN_WIDTH + 100
ENEMY2_YPOSITION = random.randint(0, SCREEN_HEIGHT - ENEMY2_HEIGHT)

# enemy3 - staggered by 200
ENEMY3_XPOSITION = SCREEN_WIDTH + 200
ENEMY3_YPOSITION = random.randint(0, SCREEN_HEIGHT - ENEMY3_HEIGHT)

# prize1 - random position
PRIZE1_XPOSITION = random.randint(0, SCREEN_WIDTH - PRIZE1_WIDTH)
PRIZE1_YPOSITION = random.randint(0, SCREEN_HEIGHT - PRIZE1_HEIGHT)

# prize2 - random position
PRIZE2_XPOSITION = random.randint(0, SCREEN_WIDTH - PRIZE2_WIDTH)
PRIZE2_YPOSITION = random.randint(0, SCREEN_HEIGHT - PRIZE2_HEIGHT)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False.
# Boolean values are True or False values that can be used to test conditions and test states that
# are binary, i.e. either one way or the other.

KEY_UP = False
KEY_DOWN = False
KEY_LEFT = False
KEY_RIGHT = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to
# represent real time game play.

# This is a looping structure that will loop the indented code until you tell it to stop(in the
# event where you exit the program by quitting). In Python the int 1 has the boolean value of
# 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false.
# You can test this out with the bool(...) function to see what boolean value types have. You will
# learn more about while loop structers later.

while 1:
    SCREEN.fill(0) # Clears the screen.
    # This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    SCREEN.blit(PLAYER, (PLAYER_XPOSITION, PLAYER_YPOSITION))

    # 3 enemies.
    SCREEN.blit(ENEMY1, (ENEMY1_XPOSITION, ENEMY1_YPOSITION))
    SCREEN.blit(ENEMY2, (ENEMY2_XPOSITION, ENEMY2_YPOSITION))
    SCREEN.blit(ENEMY3, (ENEMY3_XPOSITION, ENEMY3_YPOSITION))

    # 2 prizes.
    SCREEN.blit(PRIZE1, (PRIZE1_XPOSITION, PRIZE1_YPOSITION))
    SCREEN.blit(PRIZE2, (PRIZE2_XPOSITION, PRIZE2_YPOSITION))

    pygame.display.flip()# This updates the screen.

    # This loops through events in the game.
    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # This event checks if the user press a key down.
        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant.
                KEY_UP = True
            if event.key == pygame.K_DOWN:
                KEY_DOWN = True
            if event.key == pygame.K_LEFT:
                KEY_LEFT = True
            if event.key == pygame.K_RIGHT:
                KEY_RIGHT = True

        # This event checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                KEY_UP = False
            if event.key == pygame.K_DOWN:
                KEY_DOWN = False
            if event.key == pygame.K_LEFT:
                KEY_LEFT = False
            if event.key == pygame.K_RIGHT:
                KEY_RIGHT = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    if KEY_UP:
        # This makes sure that the user does not move the player above the window.
        if PLAYER_YPOSITION > 0:
            PLAYER_YPOSITION -= 3
    if KEY_DOWN:
        # This makes sure that the user does not move the player below the window.
        if PLAYER_YPOSITION < SCREEN_HEIGHT - IMAGE_HEIGHT:
            PLAYER_YPOSITION += 3
    if KEY_LEFT:
        # This makes sure that the user does not move the player off the left side of the screen
        if PLAYER_XPOSITION > 0:
            PLAYER_XPOSITION -= 3
    if KEY_RIGHT:
        # This makes sure that the user does not move the player below the window.
        if PLAYER_XPOSITION < SCREEN_WIDTH - IMAGE_WIDTH:
            PLAYER_XPOSITION += 3

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:
    PLAYER_BOX = pygame.Rect(PLAYER.get_rect())

    # The following updates the PLAYER_BOX position to the player's position,
    # in effect making the box stay around the player image.
    PLAYER_BOX.top = PLAYER_YPOSITION
    PLAYER_BOX.left = PLAYER_XPOSITION

    # Bounding box for the enemy:
    ENEMY_BOX1 = pygame.Rect(ENEMY1.get_rect())
    ENEMY_BOX1.top = ENEMY1_YPOSITION
    ENEMY_BOX1.left = ENEMY1_XPOSITION

    ENEMY_BOX2 = pygame.Rect(ENEMY2.get_rect())
    ENEMY_BOX2.top = ENEMY2_YPOSITION
    ENEMY_BOX2.left = ENEMY2_XPOSITION

    ENEMY_BOX3 = pygame.Rect(ENEMY3.get_rect())
    ENEMY_BOX3.top = ENEMY3_YPOSITION
    ENEMY_BOX3.left = ENEMY3_XPOSITION

    # Bounding box for the prizes:
    PRIZE_BOX1 = pygame.Rect(PRIZE1.get_rect())
    PRIZE_BOX1.top = PRIZE1_YPOSITION
    PRIZE_BOX1.left = PRIZE1_XPOSITION

    PRIZE_BOX2 = pygame.Rect(PRIZE2.get_rect())
    PRIZE_BOX2.top = PRIZE2_YPOSITION
    PRIZE_BOX2.left = PRIZE2_XPOSITION

    # Test collision of the boxes:
    if ((PLAYER_BOX.colliderect(ENEMY_BOX1))
            or (PLAYER_BOX.colliderect(ENEMY_BOX2))
            or (PLAYER_BOX.colliderect(ENEMY_BOX3))):

        # Display losing status to the user:
        print("You lose!")

        # Quit game and exit window:
        pygame.quit()
        sys.exit()

    # If the enemy is off the screen the user wins the game:
    if ((ENEMY1_XPOSITION < 0 - ENEMY1_WIDTH)
            or (ENEMY2_XPOSITION < 0 - ENEMY2_WIDTH)
            or (ENEMY3_XPOSITION < 0 - ENEMY3_WIDTH)):

        # Display wining status to the user:
        print("You win!")

        # Quite game and exit window:
        pygame.quit()
        sys.exit()

    # If the user get a prize, they win the game:
    if (PLAYER_BOX.colliderect(PRIZE_BOX1)) or (PLAYER_BOX.colliderect(PRIZE_BOX2)):

        # Display wining status to the user:
        print("You win!")

        # Quite game and exit window:
        pygame.quit()
        sys.exit()

    # Make enemies approach the player.
    ENEMY1_XPOSITION -= 1
    ENEMY2_XPOSITION -= 1
    ENEMY3_XPOSITION -= 1

    # ================The game loop logic ends here. =============
