"""Dino Game in Python

A game similar to the famous Chrome Dino Game, built using pygame-ce.
Made by intern: @bassemfarid, no one or nothing else. 🤖
"""

print("aaa")

import pygame
from random import randint
import random

print("meow")

def display_score():
    global score
    elapsed_time = (pygame.time.get_ticks() / 1000) - start_time # Keep float
    score = elapsed_time * (10 + elapsed_time * 0.05)
    score_surf = game_font.render(f'Score: {score:.1f}', True, "Black")
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    
def obstacle_movement(obstacle_list):
    if obstacle_list:  # If there are any obstacles
        for obstacle in obstacle_list:
            # Different speeds for different obstacles
            if obstacle['type'] == 'rocket':
                obstacle['rect'].x -= 12  # Much faster than other obstacles
            else:
                obstacle['rect'].x -= 5  # Normal speed for eggs and lasers
            
            # Draw the right image based on obstacle type
            if obstacle['type'] == 'egg':
                screen.blit(egg_surf, obstacle['rect'])  # Draw egg image
            elif obstacle['type'] == 'laser':
                screen.blit(obstacle['rotated_surf'], obstacle['rect'])  # Draw the specific rotated laser
            elif obstacle['type'] == 'rocket':
                screen.blit(rocket_surf, obstacle['rect'])
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle['rect'].right > -50]
        return obstacle_list
    else: 
        return []

def player_animation():
    global player_surf, player_index, player_rect

    if player_rect.bottom < GROUND_Y:
        player_surf = player_fly[int(player_index) % len(player_fly)]
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

    old_bottomleft = player_rect.bottomleft
    player_rect = player_surf.get_rect(bottomleft=old_bottomleft)

def background_animation():
    global current_level, sky_surf, layer_2_surf, layer_3_surf, layer_4_surf, layer_5_surf, layer_6_surf, layer_count
    
    new_level = (int(score) // 150) + 1

    available_levels = [4,3,5,7,8]
    level_index = (new_level - 1) % len(available_levels)
    new_level = available_levels[level_index]

    if new_level != current_level:
        current_level = new_level
    
        if current_level == 3:
            sky_surf = background_3_1
            layer_2_surf = background_3_2  # moon
            layer_3_surf = background_3_3  # cloud_1
            layer_4_surf = background_3_4  # cloud_2
            layer_count = 4
        elif current_level == 4:
            sky_surf = background_4_1
            layer_2_surf = background_4_2  # stars
            layer_3_surf = background_4_3  # cloud_1
            layer_4_surf = background_4_4  # cloud_2
            layer_count = 4
        elif current_level == 5:
            sky_surf = background_5_1
            layer_2_surf = background_5_2  # moon
            layer_3_surf = background_5_3  # cloud_1
            layer_4_surf = background_5_4  # cloud_2
            layer_count = 4
        elif current_level == 7:
            sky_surf = background_7_1
            layer_2_surf = background_7_2  # cloud_1
            layer_3_surf = background_7_3  # cloud_2
            layer_count = 3
        elif current_level == 8:
            sky_surf = background_8_1
            layer_2_surf = background_8_2  # stars
            layer_3_surf = background_8_3  # cloud_1
            layer_4_surf = background_8_4  # cloud_2
            layer_5_surf = background_8_5  # cloud_3
            layer_6_surf = background_8_6  # cloud_4
            layer_count = 6

def draw_function():
    global moon_x, cloud_1_x, cloud_2_x, stars_x, cloud_3_x, cloud_4_x, ground_x

    # Always draw the sky background first
    screen.blit(sky_surf, (0, 0), (0, 0, 800, 325))
    screen.blit(GROUND_SURF, (ground_x, 300))
    screen.blit(GROUND_SURF, (ground_x + 800, 300))
    ground_x -= 1
    if ground_x <= -800: ground_x = 0

    if current_level == 1:
        if layer_2_surf: screen.blit(layer_2_surf, (moon_x, 0))
        if layer_2_surf: screen.blit(layer_2_surf, (moon_x + 800, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x + 800, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x + 800, 0))
        moon_x -= 0.5
        cloud_1_x -= 2
        cloud_2_x -= 3
        
    elif current_level == 2:
        if layer_2_surf: screen.blit(layer_2_surf, (stars_x, 0))
        if layer_2_surf: screen.blit(layer_2_surf, (stars_x + 800, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x + 800, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x + 800, 0))
        stars_x -= 0.3
        cloud_1_x -= 2
        cloud_2_x -= 3
        
    elif current_level == 3:
        if layer_2_surf: screen.blit(layer_2_surf, (moon_x, 0))
        if layer_2_surf: screen.blit(layer_2_surf, (moon_x + 800, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x + 800, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x + 800, 0))
        moon_x -= 0.5
        cloud_1_x -= 2
        cloud_2_x -= 3
        
    elif current_level == 4:
        if layer_2_surf: screen.blit(layer_2_surf, (stars_x, 0))
        if layer_2_surf: screen.blit(layer_2_surf, (stars_x + 800, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x + 800, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x + 800, 0))
        stars_x -= 0.3
        cloud_1_x -= 2
        cloud_2_x -= 3
        
    elif current_level == 5:
        if layer_2_surf: screen.blit(layer_2_surf, (moon_x, 0))
        if layer_2_surf: screen.blit(layer_2_surf, (moon_x + 800, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x + 800, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x + 800, 0))
        moon_x -= 0.5
        cloud_1_x -= 2
        cloud_2_x -= 3
        
    elif current_level == 7:
        if layer_2_surf: screen.blit(layer_2_surf, (cloud_1_x, 0))
        if layer_2_surf: screen.blit(layer_2_surf, (cloud_1_x + 800, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_2_x, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_2_x + 800, 0))
        cloud_1_x -= 2
        cloud_2_x -= 3
        
    elif current_level == 8:
        if layer_2_surf: screen.blit(layer_2_surf, (stars_x, 0))
        if layer_2_surf: screen.blit(layer_2_surf, (stars_x + 800, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x, 0))
        if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x + 800, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x, 0))
        if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x + 800, 0))
        if layer_5_surf: screen.blit(layer_5_surf, (cloud_3_x, 0))
        if layer_5_surf: screen.blit(layer_5_surf, (cloud_3_x + 800, 0))
        if layer_6_surf: screen.blit(layer_6_surf, (cloud_4_x, 0))
        if layer_6_surf: screen.blit(layer_6_surf, (cloud_4_x + 800, 0))
        stars_x -= 0.3
        cloud_1_x -= 2
        cloud_2_x -= 3
        cloud_3_x -= 1.5
        cloud_4_x -= 1

    # Reset positions when they go off screen (loop the animation)
    if moon_x <= -800: moon_x = 0
    if cloud_1_x <= -800: cloud_1_x = 0
    if cloud_2_x <= -800: cloud_2_x = 0
    if stars_x <= -800: stars_x = 0
    if cloud_3_x <= -800: cloud_3_x = 0
    if cloud_4_x <= -800: cloud_4_x = 0

def draw_warning():
    global warning_timer,warning_active

    if warning_active:
        if warning_timer % 20 < 10:
            warning_rect = warning_surf.get_rect(center=(750, warning_y_position))
            screen.blit(warning_surf, warning_rect)

        warning_timer -= 1
        if warning_timer <= 0:
            warning_active = False

def powerup_movement(powerup_list):
    if powerup_list:
        for powerup in powerup_list:
            powerup['rect'].x -= 3

            if powerup['type'] == 'armour':
                screen.blit(armour_surf, powerup['rect'])
            elif powerup['type'] == 'life':
                screen.blit(life_surf, powerup['rect'])

        powerup_list = [powerup for powerup in powerup_list if powerup['rect'].x > -50]
        return powerup_list
    else:
        return []

def powerup_collision(player,powerups):
    global player_lives, armour_active, armour_timer

    if powerups:
        for powerup in powerups[:]:  # Use slice to avoid modification during iteration
            if player.colliderect(powerup['rect']):
                if powerup['type'] == 'armour':
                    armour_active = True
                    armour_timer = armour_time
                    print("Armour activated!")
                elif powerup['type'] == 'life' and player_lives < max_lives:
                    player_lives += 1
                    print(f"Extra life! Lives: {player_lives}")
                
                powerups.remove(powerup) 
    
    return powerups

def display_lives():
    """Display lives counter on screen"""
    lives_text = game_font.render(f'Lives: {player_lives}', True, "White")
    lives_rect = lives_text.get_rect(topright=(780, 10))  # Top right corner
    
    # Add black outline for better visibility
    outline_positions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
    for dx, dy in outline_positions:
        outline_rect = lives_rect.copy()
        outline_rect.x += dx
        outline_rect.y += dy
        outline_text = game_font.render(f'Lives: {player_lives}', True, "Black")
        screen.blit(outline_text, outline_rect)
    
    screen.blit(lives_text, lives_rect)

def collision(player, obstacles):
    global player_lives, armour_active, armour_timer
    
    if obstacles and not armour_active:  # Only check collision if armor is not active
        for obstacle in obstacles[:]:  # Use slice to avoid modification during iteration
            # Only check collision if obstacle is actually on screen and near the player
            if (obstacle['rect'].right > 0 and obstacle['rect'].left < 800 and 
                obstacle['rect'].x < player.right + 50):
                
                if player.colliderect(obstacle['rect']):
                    print(f"Collision detected with: {obstacle['type']}")
                    player_lives -= 1
                    print(f"Lives remaining: {player_lives}")
                    
                    # Remove the obstacle after collision so you don't hit it again
                    obstacles.remove(obstacle)
                    
                    if player_lives <= 0:
                        print("Game Over - No lives left!")
                        return False  # Game over only when no lives left
                    else:
                        print("Continue playing - Lives remaining!")
                        # Don't return True here - continue checking other obstacles
                        # but only lose one life per frame
                        break  # Exit the loop after first collision
    
    return True

def display_armour():
    global armour_active, armour_timer
    if armour_active:
        armour_timer -= 1
        if armour_timer == 0:
            armour_active = False

def game_over():
    screen.blit(sky_surf, (0, 0), (0, 0, 800, 325))

    if layer_2_surf: screen.blit(layer_2_surf, (moon_x, 0))
    if layer_2_surf: screen.blit(layer_2_surf, (moon_x + 800, 0))
    if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x, 0))
    if layer_3_surf: screen.blit(layer_3_surf, (cloud_1_x + 800, 0))
    if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x, 0))
    if layer_4_surf: screen.blit(layer_4_surf, (cloud_2_x + 800, 0))

    

    small_font = pygame.font.Font(pygame.font.get_default_font(), 30)

    # center the game over image
    game_over_rect = game_surf.get_rect(center = (400,120))
    screen.blit(game_surf, game_over_rect)

    #displaying final score
    final_score_surf = small_font.render(f'Final Score: {score:.1f}', True, "Black")
    final_score_rect = final_score_surf.get_rect(center=(400, 200))
    screen.blit(final_score_surf, final_score_rect)

    # Instructions to restart
    restart_surf = small_font.render('Press SPACE to Play Again', True, "Black")
    restart_rect = restart_surf.get_rect(center=(400, 240))
    screen.blit(restart_surf, restart_rect)

    menu_surf = small_font.render('Press M for Menu', True, "Black")
    menu_rect = menu_surf.get_rect(center=(400, 280))
    screen.blit(menu_surf, menu_rect)

# Initialize Pygame and create a window 
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True  # Pygame main loop, kills pygame when False
test_font = pygame.font.Font(None, 50)
start_time = 0
score = 0

print("ello")


#resizing the image to make it right
player_walk = []
scale = 0.1
for i in range(1,16):
    img = pygame.image.load(f"graphics/player/player_running/player_run_{i}.png").convert_alpha()
    original_size = img.get_size()
    scaled_img = pygame.transform.scale(img, (int(original_size[0] * scale), int(original_size[1] * scale)))
    player_walk.append(scaled_img)


player_fly = []
for i in range(1, 6):
    img = pygame.image.load(f"graphics/player/player_flying/flying_{i}.png").convert_alpha()
    original_size = img.get_size()
    scaled_img = pygame.transform.scale(img, (int(original_size[0] * scale), int(original_size[1] * scale)))
    player_fly.append(scaled_img)


# Add laser timer after your obstacle_timer (around line 295)
laser_timer = pygame.USEREVENT + 2
pygame.time.set_timer(laser_timer, 3000)  # Spawn laser every 3 seconds
# rocket timers and etc
rocker_timer= pygame.USEREVENT + 3
pygame.time.set_timer(rocker_timer, 4000)
#powerup timers  every 8 second
powerup_timer = pygame.USEREVENT + 5
pygame.time.set_timer(powerup_timer, 8000)


# Game state variables
is_playing = "menu"  # Whether in game or in menu
GROUND_Y = 330  # The Y-coordinate of the ground level
JUMP_GRAVITY_START_SPEED = -1  # The speed at which the player jumps
players_gravity_speed = 0  # The current speed at which the player falls

# Load level assets
game_font = pygame.font.Font(pygame.font.get_default_font(), 50)

# title on the game menu
title_surf = game_font.render('Pirate game', True, "Black")
title_rect = title_surf.get_rect(center=(400, 50))

obstacle_rect_list = []

# Load sprite assets for player
player_walk_1 = pygame.image.load("graphics/player/player_running/player_run_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/player/player_running/player_run_2.png").convert_alpha()
player_walk_3 = pygame.image.load("graphics/player/player_running/player_run_3.png").convert_alpha()
player_walk_4 = pygame.image.load("graphics/player/player_running/player_run_4.png").convert_alpha()
player_walk_5 = pygame.image.load("graphics/player/player_running/player_run_5.png").convert_alpha()
player_walk_6 = pygame.image.load("graphics/player/player_running/player_run_6.png").convert_alpha()
player_walk_7 = pygame.image.load("graphics/player/player_running/player_run_7.png").convert_alpha()
player_walk_8 = pygame.image.load("graphics/player/player_running/player_run_8.png").convert_alpha()
player_walk_9 = pygame.image.load("graphics/player/player_running/player_run_9.png").convert_alpha()
player_walk_10= pygame.image.load("graphics/player/player_running/player_run_10.png").convert_alpha()
player_walk_11= pygame.image.load("graphics/player/player_running/player_run_11.png").convert_alpha()
player_walk_12= pygame.image.load("graphics/player/player_running/player_run_12.png").convert_alpha()
player_walk_13= pygame.image.load("graphics/player/player_running/player_run_13.png").convert_alpha()
player_walk_14= pygame.image.load("graphics/player/player_running/player_run_14.png").convert_alpha()
player_walk_15= pygame.image.load("graphics/player/player_running/player_run_15.png").convert_alpha()

player_index = 0.1
player_fly_1 = pygame.image.load("graphics/player/player_flying/flying_1.png").convert_alpha()
player_fly_2 = pygame.image.load("graphics/player/player_flying/flying_2.png").convert_alpha()
player_fly_3 = pygame.image.load("graphics/player/player_flying/flying_3.png").convert_alpha()
player_fly_4 = pygame.image.load("graphics/player/player_flying/flying_4.png").convert_alpha()
player_fly_5 = pygame.image.load("graphics/player/player_flying/flying_5.png").convert_alpha()

#loading sprite asset for background
background_3_1 = pygame.image.load("graphics/level/clouds_3/3_background.png").convert_alpha()
background_3_3 = pygame.image.load("graphics/level/clouds_3/3_cloud_1.png").convert_alpha()
background_3_4 = pygame.image.load("graphics/level/clouds_3/3_cloud_2.png").convert_alpha()
background_3_2 = pygame.image.load("graphics/level/clouds_3/3_moon.png").convert_alpha()

background_4_1 = pygame.image.load("graphics/level/clouds_4/4_background.png").convert_alpha()
background_4_3 = pygame.image.load("graphics/level/clouds_4/4_cloud_1.png").convert_alpha()
background_4_4 = pygame.image.load("graphics/level/clouds_4/4_cloud_2.png").convert_alpha()
background_4_2 = pygame.image.load("graphics/level/clouds_4/4_stars.png").convert_alpha()

background_5_1 = pygame.image.load("graphics/level/clouds_5/5_background.png").convert_alpha()
background_5_3 = pygame.image.load("graphics/level/clouds_5/5_cloud_1.png").convert_alpha()
background_5_4 = pygame.image.load("graphics/level/clouds_5/5_cloud_2.png").convert_alpha()
background_5_2 = pygame.image.load("graphics/level/clouds_5/5_moon.png").convert_alpha()

background_7_1 = pygame.image.load("graphics/level/clouds_7/7_background.png").convert_alpha()
background_7_2 = pygame.image.load("graphics/level/clouds_7/7_cloud_1.png").convert_alpha()
background_7_3 = pygame.image.load("graphics/level/clouds_7/7_cloud_2.png").convert_alpha()

background_8_1 = pygame.image.load("graphics/level/clouds_8/8_background.png").convert_alpha()
background_8_3 = pygame.image.load("graphics/level/clouds_8/8_cloud_1.png").convert_alpha()
background_8_4 = pygame.image.load("graphics/level/clouds_8/8_cloud_2.png").convert_alpha()
background_8_2 = pygame.image.load("graphics/level/clouds_8/8_stars.png").convert_alpha()
background_8_6 = pygame.image.load("graphics/level/clouds_8/8_cloud_4.png").convert_alpha()
background_8_5 = pygame.image.load("graphics/level/clouds_8/8_cloud_3.png").convert_alpha()

background_3_1 = pygame.transform.scale(background_3_1, (800, 325))
background_3_2 = pygame.transform.scale(background_3_2, (800, 325))
background_3_3 = pygame.transform.scale(background_3_3, (800, 325))
background_3_4 = pygame.transform.scale(background_3_4, (800, 325))

background_4_1 = pygame.transform.scale(background_4_1, (800, 325))
background_4_2 = pygame.transform.scale(background_4_2, (800, 325))
background_4_3 = pygame.transform.scale(background_4_3, (800, 325))
background_4_4 = pygame.transform.scale(background_4_4, (800, 325))

background_5_1 = pygame.transform.scale(background_5_1, (800, 325))
background_5_2 = pygame.transform.scale(background_5_2, (800, 325))  
background_5_3 = pygame.transform.scale(background_5_3, (800, 325))  
background_5_4 = pygame.transform.scale(background_5_4, (800, 325))

background_7_1 = pygame.transform.scale(background_7_1, (800, 325))
background_7_2 = pygame.transform.scale(background_7_2, (800, 325))
background_7_3 = pygame.transform.scale(background_7_3, (800, 325))

background_8_1 = pygame.transform.scale(background_8_1, (800, 325))
background_8_2 = pygame.transform.scale(background_8_2, (800, 325))  
background_8_3 = pygame.transform.scale(background_8_3, (800, 325))  
background_8_4 = pygame.transform.scale(background_8_4, (800, 325)) 
background_8_5 = pygame.transform.scale(background_8_5, (800, 325))  
background_8_6 = pygame.transform.scale(background_8_6, (800, 325))  

ground_5 = pygame.image.load("graphics/level/ground_5.png").convert_alpha()
ground_5 = pygame.transform.scale(ground_5, (800, 100))

rocket_surf = pygame.image.load('graphics/obstacle/rocket.png').convert_alpha()
rocket_surf = pygame.transform.scale(rocket_surf, (40, 75))
rocket_surf = pygame.transform.rotate(rocket_surf, 90)


warning_surf = pygame.image.load('graphics/obstacle/exclamation.png').convert_alpha()
warning_surf = pygame.transform.scale(warning_surf, (40, 60))

armour_surf = pygame.image.load('graphics/obstacle/armour.png').convert_alpha()
armour_surf = pygame.transform.scale(armour_surf, (30, 30))

life_surf = pygame.image.load('graphics/obstacle/life.png').convert_alpha()
life_surf = pygame.transform.scale(life_surf, (30, 30))

game_surf = pygame.image.load('graphics/game_over.png')
game_surf = pygame.transform.scale(game_surf, (350,200))

GROUND_SURF = ground_5

current_level = 4
sky_surf = background_4_1
layer_2_surf = background_4_2  # moon
layer_3_surf = background_4_3  # cloud_1
layer_4_surf = background_4_4  # cloud_2
layer_5_surf = None  # Initialize these too
layer_6_surf = None
layer_count = 4

ground_x = 0
moon_x = 0
cloud_1_x = 0
cloud_2_x = 0
stars_x = 0
cloud_3_x = 0
cloud_4_x = 0

warning_active = False
warning_timer = 0
warning_y_position = 0
warning_time = 120

player_lives = 3
max_lives  = 5
armour_active = False
armour_time = 180
powerup_list = []



player_surf = player_walk[int(player_index)]
player_rect = player_surf.get_rect(bottomleft=(25, GROUND_Y))
egg_surf = pygame.image.load("graphics/obstacle/egg_1.png").convert_alpha()
egg_rect = egg_surf.get_rect(bottomleft=(800, GROUND_Y))

laser_Surf = pygame.image.load("graphics/obstacle/laser.png").convert_alpha()
laser_Surf = pygame.transform.scale(laser_Surf, (100, 8))


#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

print("wsg")

while running:
    # Poll for events
    for event in pygame.event.get():
        # pygame.QUIT --> user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False

        elif is_playing == "playing":
            # When player wants to jump by pressing SPACE
            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
                or event.type == pygame.MOUSEBUTTONDOWN
            ) and player_rect.bottom >= GROUND_Y:
                players_gravity_speed = JUMP_GRAVITY_START_SPEED
        else:
            # When player wants to play again by pressing SPACE
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_playing = "playing"
                egg_rect.left = 800
                start_time = pygame.time.get_ticks() / 1000
        if event.type == obstacle_timer and is_playing:
            new_egg_rect = egg_surf.get_rect(midbottom=(randint(900, 1100), GROUND_Y))
            egg_obstacle = {
                'type': 'egg', 
                'rect': new_egg_rect
            }
            obstacle_rect_list.append(egg_obstacle)

        if event.type == laser_timer and is_playing == "playing":
            # Create random laser properties
            laser_length = randint(40, 80)    # Much shorter - only 40-80 pixels long
            laser_width = randint(2, 5)       # Very thin - only 2-5 pixels wide
            laser_angle = randint(-45, 45)    # Limited angle range so it's not vertical
            laser_x = randint(900, 1100)
            laser_y = randint(80, 200) 

            # Scale and rotate the laser
            laser_scaled = pygame.transform.scale(laser_Surf, (laser_length, laser_Surf.get_height()))
            laser_rotated = pygame.transform.rotate(laser_scaled, laser_angle)

            laser_rect = laser_rotated.get_rect()
            laser_rect.center = (laser_x, laser_y)  # Now this works correctly

            laser_obstacle = {
                'type': 'laser',
                'rect': laser_rect,
                'rotated_surf': laser_rotated
            }
            obstacle_rect_list.append(laser_obstacle)
        
        if event.type == rocker_timer and is_playing == "playing":
            warning_active = True
            warning_timer = warning_time
            warning_y_position = player_rect.centery 

            pygame.time.set_timer(pygame.USEREVENT + 4, int(warning_time * 1000/60))
    
        if event.type == pygame.USEREVENT + 4 and is_playing == "playing":
            rocket_rect = rocket_surf.get_rect(midleft=(850, warning_y_position))
            rocket_obstacle = {
                'type': 'rocket',
                'rect': rocket_rect,
                'target_y': warning_y_position
            }

            obstacle_rect_list.append(rocket_obstacle)
            pygame.time.set_timer(pygame.USEREVENT + 4, 0)

        if event.type == powerup_timer and is_playing == "playing":
            x = random.randint(1,2)
            if player_lives >= max_lives:
                powerup_type = 'armour'
            else:
                if x == 1:
                    powerup_type = 'armour'
                else:
                    powerup_type = 'life'

            powerup_rect = armour_surf.get_rect(center=(randint(850, 1000), randint(50, 250)))
            
            new_powerup = {
                'type': powerup_type,
                'rect': powerup_rect
            }
            powerup_list.append(new_powerup)
    print("tests")

    if is_playing == "menu":
        screen.fill("black")
        print("hello")
        screen.blit(background_4_1)




    elif is_playing == "playing":
        screen.fill("purple")  # Wipe the screen
        screen.blit(player_surf, player_rect)
        background_animation()
        draw_function()
        display_score()
        draw_warning()
        display_lives()
        display_armour()

        # Adjust player's vertical location then blit it
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            players_gravity_speed += -2.5
        else:
            players_gravity_speed += 1
        
        players_gravity_speed = max(min(players_gravity_speed, 10), -8)
        
        player_rect.y += players_gravity_speed
        if player_rect.top < 0:
            player_rect.top = 0
        if player_rect.bottom > GROUND_Y:
            player_rect.bottom = GROUND_Y
        player_animation()
        screen.blit(player_surf, player_rect)
        

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        powerup_list = powerup_movement(powerup_list)
        powerup_list = powerup_collision(player_rect, powerup_list)

        collision_result = collision(player_rect, obstacle_rect_list)
        if not collision_result:
            is_playing = False

    # When game is over, display game over message
    elif is_playing == 'game over':
        game_over()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Reset everything for new game
                    is_playing = True
                    start_time = pygame.time.get_ticks() / 1000
                    player_lives = 3  # Reset lives to 3
                    armour_active = False
                    armour_timer = 0
                    powerup_list.clear()
                    obstacle_rect_list.clear()
                    players_gravity_speed = 0
                    player_rect.bottom = GROUND_Y
                    score = 0  # Reset score
                elif event.key == pygame.K_m:
                    # We'll implement menu later
                    pass
        


   
    # flip the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # Limits game loop to 60 FPS

pygame.quit()