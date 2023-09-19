import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

def start_carrera():

    # Configuración de la pantalla
    screen_width = 450
    screen_height = 800
    PANTALLA = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Juego de Carreras')

    # Colores
    BLANCO = (255, 255, 255)

    #Música de fondo
    pygame.mixer.music.load('sonido/carreras.mp3')
    pygame.mixer.music.play(-1) # con -1 reproduce la musica infinitamente
    pygame.mixer.music.set_volume(0.2) # Volumen

    # Cargar la imagen de fondo
    fondo = pygame.image.load("images/pista.jpg")
    fondo = pygame.transform.scale(fondo, (screen_width, screen_height))

    # Cargar imágenes
    player_image = pygame.image.load('images/carroP.png')  # Ajusta la ruta según tu imagen
    player_image = pygame.transform.scale(player_image, (50, 100))

    obstacle_image = pygame.image.load('images/carroE.png')  # Ajusta la ruta según tu imagen
    obstacle_image = pygame.transform.scale(obstacle_image, (50, 100))

    # Jugador
    player_width = 50
    player_height = 50
    player_x = (screen_width - player_width) // 2
    player_y = screen_height - player_height -50
    player_velocity = 5

    # Obstáculos
    obstacle_width = 50
    obstacle_height = 50
    obstacle_velocity = 5
    obstacles = []

    # Fuente para mostrar el puntaje
    font = pygame.font.Font(None, 36)

    # Reloj para controlar la velocidad de actualización
    clock = pygame.time.Clock()

    # Tiempo inicial (en milisegundos)
    start_time = pygame.time.get_ticks()

    # Función para dibujar al jugador en la pantalla
    def draw_carro(x, y):
        PANTALLA.blit(player_image, (x, y))

    # Función para dibujar los obstáculos en la pantalla
    def draw_obstacles(obstacles):
        for obstacle in obstacles:
            PANTALLA.blit(obstacle_image, obstacle)

    # Ciclo principal del juego
    running = True
    clock = pygame.time.Clock()

    # Función para mostrar el puntaje en la pantalla
    def display_score(score):
        score_text = font.render("Puntaje: " + str(score), True, BLANCO)
        PANTALLA.blit(score_text, (10, 10))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Actualizar el tiempo y el puntaje
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000
        score = int(elapsed_time)

        # Movimiento del jugador
        if keys[pygame.K_LEFT] and player_x - player_velocity > 0:
            player_x -= player_velocity
        if keys[pygame.K_RIGHT] and player_x + player_velocity < screen_width - player_width:
            player_x += player_velocity

        # Generar obstáculos
        if random.randint(1, 600) < 10:  # Probabilidad de generar un obstáculo
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        # Mover obstáculos
        for obstacle in obstacles:
            obstacle.y += obstacle_velocity
            if obstacle.y > screen_height:
                obstacles.remove(obstacle)

        # Colisión con obstáculos
        for obstacle in obstacles:
            if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(obstacle):
                print("Game Over")
                running = False

        # Limpiar la pantalla
        PANTALLA.blit(fondo, (0, 0))

        # Dibujar al jugador y los obstáculos
        draw_carro(player_x, player_y)
        draw_obstacles(obstacles)

        # Mostrar el puntaje
        display_score(score)

        # Actualizar la pantalla
        pygame.display.update()
        clock.tick(60)

    # Salir del juego
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_carrera()
