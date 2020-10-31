import pygame
import pygame.gfxdraw
import random
import time
import math

def draw_shape(screen, shape, color, line_width):
    if (shape is not None):
        pygame.draw.polygon(screen, color, shape, line_width)

def play(get_shape, ship_move, get_cone, ship_detected):
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res = (1280, 720)

    # Create a window and a display surface
    screen = pygame.display.set_mode(res)

    # Timer
    delta_time = 0
    prev_time = time.time()

    # Show mouse cursor
    pygame.mouse.set_visible(True)
    # Don't lock the mouse cursor to the game window
    pygame.event.set_grab(False)

    random.seed(1234)

    stars = [(int(random.uniform(0,res[0])), 
              int(random.uniform(0,res[1])),
              int(random.uniform(20,255))) for i in range(0, 300)]

    ship_position = (res[0] / 2, res[1] / 2)
    ship_speed = 100
    ship_rotation = 0 
    ship_rotation_speed = 90

    enemies = []
    for i in range(0, 10):
        px = random.uniform(0, res[0])
        py = random.uniform(0, res[1])
        vision_angle = random.uniform(25, 60)
        vision_dist = random.uniform(80, 200)
        rotation = random.uniform(0, 360)
        enemies.append([(px, py), rotation, vision_angle, vision_dist])

    # Game loop, runs forever
    while True:
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if event.type == pygame.QUIT:
                # Exits the application immediately
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # If ESC is pressed exit the application
                    return

        #################################### ANIMATION ###################################
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT]):
            ship_rotation -= ship_rotation_speed * delta_time
        if (keys[pygame.K_RIGHT]):
            ship_rotation += ship_rotation_speed * delta_time

        if (keys[pygame.K_UP]):
            new_position = ship_move(ship_position, ship_rotation, ship_speed * delta_time)
            if (new_position is not None):
                ship_position = new_position
        if (keys[pygame.K_DOWN]):
            new_position = ship_move(ship_position, ship_rotation, -ship_speed * delta_time * 0.5)
            if (new_position is not None):
                ship_position = new_position
        
        ##################################### RENDER #####################################
        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0, 0, 0))

        # Draw some stars as background
        for star in stars:
            screen.fill((star[2], star[2], star[2]), ((star[0],star[1]), (2,2)))

        # Draw the player ship
        ship_model = get_shape(ship_position, 20, 3, ship_rotation)
        draw_shape(screen, ship_model, (255, 255, 0), 2)
        cone_pos = (ship_position[0] + 10 * math.cos(math.radians(ship_rotation)), ship_position[1] + 10 * math.sin(math.radians(ship_rotation)))
        ship_model = get_shape(cone_pos, 10, 3, ship_rotation)
        draw_shape(screen, ship_model, (255, 200, 0), 0)

        # Draw the enemies
        for enemy in enemies:
            color_main = (0, 255, 0)

            detected = ship_detected(ship_position, enemy[0], enemy[1], enemy[2], enemy[3])
            if (detected is not None) and (detected):
                color_main = (255, 0, 0)

            color_range = (color_main[0], color_main[1], color_main[2], 15)
            color_cone = (color_main[0], color_main[1], color_main[2], 25)

            # Draw enemy
            enemy_model = get_shape(enemy[0], 15, 5, enemy[1])
            draw_shape(screen, enemy_model, color_main, 3)
            
            cone_pos = (enemy[0][0] + 10 * math.cos(math.radians(enemy[1])), enemy[0][1] + 10 * math.sin(math.radians(enemy[1])))
            enemy_model = get_shape(cone_pos, 10, 5, enemy[1])
            draw_shape(screen, enemy_model, color_main, 0)

            # Draw radius
            pygame.gfxdraw.filled_circle(screen, int(enemy[0][0]), int(enemy[0][1]), int(enemy[3]), color_cone)
            # Draw cone
            cone = get_cone(enemy[0], enemy[1], enemy[2], enemy[3])
            if (cone is not None):
                pygame.gfxdraw.filled_polygon(screen, cone, color_cone)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()

