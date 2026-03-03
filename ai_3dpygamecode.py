import streamlit as st
import re
import random
import math

st.set_page_config(page_title="PyGame Code Generator", layout="wide")

# Page styling
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        border-radius: 5px;
        height: 50px;
    }
    .success-message {
        padding: 20px;
        background-color: #d4edda;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "generated_code" not in st.session_state:
    st.session_state.generated_code = ""
if "last_query" not in st.session_state:
    st.session_state.last_query = ""

# Template-based code generator
def generate_pygame_code(query):
    """Generate PyGame code based on keywords in the query"""
    
    query_lower = query.lower()
    
    # Base code structure
    code = '''import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Visualization")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

'''
    
    # Detect what type of visualization the user wants
    has_particles = "particle" in query_lower
    has_mouse = "mouse" in query_lower
    has_bounce = "bounce" in query_lower
    has_snake = "snake" in query_lower
    has_pong = "pong" in query_lower
    has_flappy = "flappy" in query_lower
    has_shooter = "shooter" in query_lower or "bullet" in query_lower
    has_snow = "snow" in query_lower
    has_firework = "firework" in query_lower
    has_wave = "wave" in query_lower or "sine" in query_lower
    has_spiral = "spiral" in query_lower
    has_bubble = "bubble" in query_lower
    has_gravity = "gravity" in query_lower or "fall" in query_lower
    has_rain = "rain" in query_lower
    has_star = "star" in query_lower
    has_maze = "maze" in query_lower
    has_running = "running" in query_lower or "runner" in query_lower or "run" in query_lower
    has_fighting = "fighting" in query_lower or "fight" in query_lower or "fighter" in query_lower
    has_racing = "racing" in query_lower or "race" in query_lower or "car" in query_lower
    has_tetris = "tetris" in query_lower
    has_breakout = "breakout" in query_lower or "brick" in query_lower
    has_platformer = "platformer" in query_lower or "platform" in query_lower
    
    # Generate specific code based on keywords
    if has_particles:
        code += '''# Particle System
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-5, -1)
        self.life = 255
        self.color = random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN])
        self.size = random.randint(2, 6)
    
    def update(self, wind_x=0, wind_y=0):
        self.vx += wind_x * 0.1
        self.vy += wind_y * 0.1
        self.x += self.vx
        self.y += self.vy
        self.life -= 3
        self.size = max(1, self.size - 0.02)
    
    def draw(self, surface):
        if self.life > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))

particles = []
wind_x, wind_y = 0, 0

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                wind_x -= 1
            elif event.key == pygame.K_RIGHT:
                wind_x += 1
            elif event.key == pygame.K_UP:
                wind_y -= 1
            elif event.key == pygame.K_DOWN:
                wind_y += 1
    
    # Emit particles from mouse position
    if pygame.mouse.get_pressed()[0]:
        for _ in range(5):
            particles.append(Particle(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
    
    # Update and draw particles
    for particle in particles[:]:
        particle.update(wind_x, wind_y)
        particle.draw(screen)
        if particle.life <= 0 or particle.y > HEIGHT:
            particles.remove(particle)
    
    # Draw wind indicator
    font = pygame.font.Font(None, 36)
    wind_text = font.render(f"Wind: {wind_x}, {wind_y}", True, WHITE)
    screen.blit(wind_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_snow:
        code += '''# Snowfall Simulation
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.size = random.randint(1, 4)
        self.speed = random.uniform(1, 3)
        self.wind = random.uniform(-0.5, 0.5)
    
    def update(self):
        self.y += self.speed
        self.x += self.wind
        if self.y > HEIGHT:
            self.y = random.randint(-20, -5)
            self.x = random.randint(0, WIDTH)
        if self.x > WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = WIDTH
    
    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.size)

snowflakes = [Snowflake() for _ in range(200)]

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for snowflake in snowflakes:
        snowflake.update()
        snowflake.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_rain:
        code += '''# Rain Simulation
class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.length = random.randint(10, 20)
        self.speed = random.uniform(8, 15)
    
    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-20, -5)
            self.x = random.randint(0, WIDTH)
    
    def draw(self, surface):
        pygame.draw.line(surface, CYAN, (self.x, self.y), (self.x, self.y + self.length), 2)

raindrops = [Raindrop() for _ in range(300)]

running = True
while running:
    screen.fill((20, 20, 40))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for drop in raindrops:
        drop.update()
        drop.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_firework:
        code += '''# Firework Simulation
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vy = random.uniform(-10, -15)
        self.exploded = False
        self.particles = []
    
    def update(self):
        if not self.exploded:
            self.y += self.vy
            if self.vy >= 0:
                self.exploded = True
                for _ in range(50):
                    angle = random.uniform(0, 2 * math.pi)
                    speed = random.uniform(2, 6)
                    self.particles.append({
                        "x": self.x,
                        "y": self.y,
                        "vx": math.cos(angle) * speed,
                        "vy": math.sin(angle) * speed,
                        "color": random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE]),
                        "life": 255
                    })
        else:
            for p in self.particles:
                p["x"] += p["vx"]
                p["y"] += p["vy"]
                p["life"] -= 5
                p["vy"] += 0.1
            self.particles = [p for p in self.particles if p["life"] > 0]
    
    def draw(self, surface):
        if not self.exploded:
            pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), 3)
        else:
            for p in self.particles:
                pygame.draw.circle(surface, p["color"], (int(p["x"]), int(p["y"])), 2)

fireworks = []

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            fireworks.append(Firework(pygame.mouse.get_pos()[0], HEIGHT))
    
    for fw in fireworks[:]:
        fw.update()
        fw.draw(screen)
        if fw.exploded and len(fw.particles) == 0:
            fireworks.remove(fw)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_bounce or has_gravity:
        code += '''# Bouncing Balls with Gravity
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)
        self.radius = random.randint(15, 30)
        self.color = random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN])
        self.gravity = 0.5
        self.bounce = -0.8
    
    def update(self):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off walls
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= self.bounce
        if self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
            self.vx *= self.bounce
        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy *= self.bounce
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= self.bounce
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

balls = [Ball(random.randint(50, WIDTH-50), random.randint(50, HEIGHT//2)) for _ in range(10)]

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for ball in balls:
        ball.update()
        ball.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_wave or has_spiral:
        code += '''# Wave/Spiral Visualization
angle = 0

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw spiral pattern
    for i in range(500):
        r = i * 0.5
        theta = angle + i * 0.1
        x = WIDTH // 2 + r * math.cos(theta)
        y = HEIGHT // 2 + r * math.sin(theta)
        color_val = int(128 + 127 * math.sin(i * 0.1))
        color = (color_val, color_val, color_val)
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            pygame.draw.circle(screen, color, (int(x), int(y)), 2)
    
    angle += 0.02
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_bubble:
        code += '''# Bubble Sort Visualization
array = list(range(1, 51))
random.shuffle(array)
current_idx = 0
swapping = False

def draw_array(surface, arr, highlight=[], highlight_color=RED):
    for i, val in enumerate(arr):
        x = 50 + i * 14
        height = val * 5
        color = highlight_color if i in highlight else WHITE
        pygame.draw.rect(surface, color, (x, HEIGHT - height, 12, height))

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Bubble sort step
    if current_idx < len(array) - 1:
        if not swapping:
            if array[current_idx] > array[current_idx + 1]:
                array[current_idx], array[current_idx + 1] = array[current_idx + 1], array[current_idx]
                swapping = True
            else:
                current_idx += 1
        else:
            current_idx += 1
            swapping = False
    
    highlight = [current_idx, current_idx + 1] if current_idx < len(array) - 1 else []
    draw_array(screen, array, highlight)
    
    font = pygame.font.Font(None, 36)
    text = font.render("Bubble Sort: " + str(current_idx), True, WHITE)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
'''
    
    elif has_snake:
        code += '''# Snake Game
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_dir = (0, 0)
food = (random.randint(1, (WIDTH-20)//20) * 20, random.randint(1, (HEIGHT-20)//20) * 20)
score = 0
game_over = False

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and snake_dir != (0, 10):
                snake_dir = (0, -10)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -10):
                snake_dir = (0, 10)
            elif event.key == pygame.K_LEFT and snake_dir != (10, 0):
                snake_dir = (-10, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-10, 0):
                snake_dir = (10, 0)
            elif event.key == pygame.K_r:
                snake = [(WIDTH // 2, HEIGHT // 2)]
                snake_dir = (0, 0)
                score = 0
                game_over = False
    
    if not game_over and snake_dir != (0, 0):
        head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        
        if head in snake or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            game_over = True
        else:
            snake.insert(0, head)
            if head == food:
                score += 10
                food = (random.randint(1, (WIDTH-20)//20) * 20, random.randint(1, (HEIGHT-20)//20) * 20)
            else:
                snake.pop()
    
    # Draw snake
    for i, segment in enumerate(snake):
        color = GREEN if i == 0 else (0, 200, 0)
        pygame.draw.rect(screen, color, (segment[0], segment[1], 20, 20))
    
    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], 20, 20))
    
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    
    if game_over:
        game_over_text = font.render("Game Over! Press R to restart", True, RED)
        screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
'''
    
    elif has_pong:
        code += '''# Pong Game
paddle_width, paddle_height = 15, 80
player_y = HEIGHT // 2 - paddle_height // 2
ai_y = HEIGHT // 2 - paddle_height // 2
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_vx, ball_vy = 5, 5
player_score, ai_score = 0, 0

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= 8
    if keys[pygame.K_DOWN] and player_y < HEIGHT - paddle_height:
        player_y += 8
    
    # AI movement
    if ball_y < ai_y + paddle_height // 2:
        ai_y -= 5
    elif ball_y > ai_y + paddle_height // 2:
        ai_y += 5
    ai_y = max(0, min(HEIGHT - paddle_height, ai_y))
    
    # Ball movement
    ball_x += ball_vx
    ball_y += ball_vy
    
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_vy *= -1
    if ball_x <= paddle_width and player_y <= ball_y <= player_y + paddle_height:
        ball_vx *= -1
    if ball_x >= WIDTH - paddle_width - 15 and ai_y <= ball_y <= ai_y + paddle_height:
        ball_vx *= -1
    
    if ball_x < 0:
        ai_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_vx, ball_vy = 5, 5
    if ball_x > WIDTH:
        player_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_vx, ball_vy = -5, 5
    
    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (0, player_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (WIDTH - paddle_width, ai_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x - 10, ball_y - 10, 20, 20))
    
    # Draw score
    font = pygame.font.Font(None, 72)
    screen.blit(font.render(str(player_score), True, WHITE), (WIDTH // 4, 20))
    screen.blit(font.render(str(ai_score), True, WHITE), (3 * WIDTH // 4, 20))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_flappy:
        code += '''# Flappy Bird Clone
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.5
flap_strength = -10
pipes = []
pipe_width = 60
pipe_gap = 150
score = 0

running = True
while running:
    screen.fill((135, 206, 235))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = flap_strength
    
    bird_velocity += gravity
    bird_y += bird_velocity
    
    # Spawn pipes
    if len(pipes) == 0 or pipes[-1][0] < WIDTH - 200:
        pipe_height = random.randint(50, HEIGHT - 150)
        pipes.append((WIDTH, pipe_height))
    
    # Update pipes
    for i, (pipe_x, pipe_height) in enumerate(pipes[:]):
        pipe_x -= 3
        pipes[i] = (pipe_x, pipe_height)
        
        # Draw pipes
        pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_height))
        pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT - pipe_height - pipe_gap))
        
        # Collision check
        if (pipe_x < 60 < pipe_x + pipe_width and (bird_y < pipe_height or bird_y > pipe_height + pipe_gap)) or bird_y > HEIGHT or bird_y < 0:
            score = 0
            pipes = []
            bird_y = HEIGHT // 2
            bird_velocity = 0
        
        if pipe_x < -pipe_width:
            pipes.remove((pipe_x, pipe_height))
            score += 1
    
    # Draw bird
    pygame.draw.circle(screen, YELLOW, (60, int(bird_y)), 20)
    pygame.draw.circle(screen, BLACK, (65, int(bird_y) - 5), 3)
    
    # Draw score
    font = pygame.font.Font(None, 48)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 50, 30))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_maze:
        code += '''# Maze Generator and Solver
cell_size = 40
cols, rows = WIDTH // cell_size, HEIGHT // cell_size
maze = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
player_pos = [0, 0]

def draw_maze():
    for y in range(rows):
        for x in range(cols):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, WHITE, (x * cell_size, y * cell_size, cell_size, cell_size))

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            new_x, new_y = player_pos[0], player_pos[1]
            if event.key == pygame.K_UP:
                new_y -= 1
            elif event.key == pygame.K_DOWN:
                new_y += 1
            elif event.key == pygame.K_LEFT:
                new_x -= 1
            elif event.key == pygame.K_RIGHT:
                new_x += 1
            
            if 0 <= new_x < cols and 0 <= new_y < rows and maze[new_y][new_x] == 0:
                player_pos = [new_x, new_y]

draw_maze()
pygame.draw.circle(screen, GREEN, (player_pos[0] * cell_size + cell_size // 2, player_pos[1] * cell_size + cell_size // 2), cell_size // 3)

pygame.display.flip()
clock.tick(FPS)

pygame.quit()
'''
    
    elif has_shooter:
        code += '''# Space Shooter
player_x = WIDTH // 2
player_y = HEIGHT - 50
bullets = []
enemies = []
score = 0

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x, player_y])
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 20:
        player_x -= 7
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 20:
        player_x += 7
    
    # Spawn enemies
    if random.randint(0, 50) == 0:
        enemies.append([random.randint(20, WIDTH - 20), -20])
    
    # Update bullets
    for bullet in bullets[:]:
        bullet[1] -= 10
        if bullet[1] < 0:
            bullets.remove(bullet)
    
    # Update enemies
    for enemy in enemies[:]:
        enemy[1] += 5
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
        
        for bullet in bullets[:]:
            if abs(enemy[0] - bullet[0]) < 20 and abs(enemy[1] - bullet[1]) < 20:
                if enemy in enemies:
                    enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)
                score += 10
                break
    
    # Draw player
    pygame.draw.polygon(screen, CYAN, [(player_x, player_y - 20), (player_x - 20, player_y + 20), (player_x + 20, player_y + 20)])
    
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, (bullet[0] - 3, bullet[1] - 10, 6, 15))
    
    # Draw enemies
    for enemy in enemies:
        pygame.draw.circle(screen, RED, (enemy[0], enemy[1]), 20)
    
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_star:
        code += '''# Star Field Simulation
stars = []
for _ in range(500):
    stars.append({
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "z": random.randint(1, WIDTH)
    })

center_x, center_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for star in stars:
        star["z"] -= 2
        if star["z"] <= 0:
            star["x"] = random.randint(0, WIDTH)
            star["y"] = random.randint(0, HEIGHT)
            star["z"] = WIDTH
        
        screen_x = (star["x"] - center_x) / star["z"] * WIDTH + center_x
        screen_y = (star["y"] - center_y) / star["z"] * WIDTH + center_y
        size = max(1, int(3 - star["z"] / WIDTH * 3))
        
        if 0 <= screen_x < WIDTH and 0 <= screen_y < HEIGHT:
            brightness = int(255 * (1 - star["z"] / WIDTH))
            pygame.draw.circle(screen, (brightness, brightness, brightness), (int(screen_x), int(screen_y)), size)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_mouse:
        code += '''# Interactive Mouse Visualization
mouse_trail = []

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    mouse_pos = pygame.mouse.get_pos()
    mouse_trail.append(mouse_pos)
    if len(mouse_trail) > 50:
        mouse_trail.pop(0)
    
    # Draw trail
    for i, pos in enumerate(mouse_trail):
        alpha = int(255 * (i / len(mouse_trail)))
        color = (alpha, 255 - alpha, 128)
        pygame.draw.circle(screen, color, pos, 5)
    
    # Draw current mouse position
    pygame.draw.circle(screen, WHITE, mouse_pos, 10)
    
    # Show mouse position
    font = pygame.font.Font(None, 36)
    pos_text = font.render("X: " + str(mouse_pos[0]) + ", Y: " + str(mouse_pos[1]), True, WHITE)
    screen.blit(pos_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_running:
        code += '''# Running Game
player_x = 100
player_y = HEIGHT - 150
player_velocity_y = 0
is_jumping = False
gravity = 0.8
jump_strength = -15
ground_y = HEIGHT - 100
obstacles = []
score = 0
game_speed = 6

running = True
while running:
    screen.fill((135, 206, 235))
    
    # Draw ground
    pygame.draw.rect(screen, GREEN, (0, ground_y, WIDTH, HEIGHT - ground_y))
    pygame.draw.line(screen, WHITE, (0, ground_y), (WIDTH, ground_y), 3)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                player_velocity_y = jump_strength
                is_jumping = True
    
    # Player physics
    player_velocity_y += gravity
    player_y += player_velocity_y
    
    if player_y >= ground_y:
        player_y = ground_y
        is_jumping = False
        player_velocity_y = 0
    
    # Spawn obstacles
    if random.randint(0, 60) == 0:
        obstacles.append({"x": WIDTH, "y": ground_y - 40, "width": 30, "height": 40})
    
    # Update obstacles
    for obstacle in obstacles[:]:
        obstacle["x"] -= game_speed
        if obstacle["x"] < -50:
            obstacles.remove(obstacle)
            score += 1
    
    # Collision check
    player_rect = pygame.Rect(player_x - 20, player_y - 40, 40, 40)
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"])
        if player_rect.colliderect(obstacle_rect):
            game_over = True
            score = 0
            obstacles = []
    
    # Draw player
    pygame.draw.rect(screen, RED, (player_x - 20, player_y - 40, 40, 40))
    pygame.draw.circle(screen, (255, 200, 150), (player_x, player_y - 50), 15)
    
    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, (100, 50, 0), (obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"]))
    
    # Draw score
    font = pygame.font.Font(None, 48)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 50, 30))
    
    # Instructions
    instructions = font.render("Press SPACE to jump!", True, WHITE)
    screen.blit(instructions, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_fighting:
        code += '''# Fighting Game
class Fighter:
    def __init__(self, x, y, color, controls):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 80
        self.color = color
        self.velocity_y = 0
        self.is_jumping = False
        self.health = 100
        self.is_attacking = False
        self.attack_cooldown = 0
        self.controls = controls
        self.facing_right = True
    
    def move(self, keys, ground_y):
        if keys[self.controls["left"]] and self.x > 0:
            self.x -= 5
            self.facing_right = False
        if keys[self.controls["right"]] and self.x < WIDTH - self.width:
            self.x += 5
            self.facing_right = True
        if keys[self.controls["jump"]] and not self.is_jumping:
            self.velocity_y = -15
            self.is_jumping = True
        
        # Gravity
        self.velocity_y += 0.8
        self.y += self.velocity_y
        
        if self.y >= ground_y - self.height:
            self.y = ground_y - self.height
            self.is_jumping = False
            self.velocity_y = 0
        
        # Attack
        if keys[self.controls["attack"]] and self.attack_cooldown == 0:
            self.is_attacking = True
            self.attack_cooldown = 30
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.attack_cooldown < 20:
            self.is_attacking = False
    
    def draw(self, surface):
        # Body
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        # Head
        pygame.draw.circle(surface, (255, 200, 150), (self.x + self.width // 2, self.y - 10), 20)
        # Direction indicator
        eye_x = self.x + self.width - 10 if self.facing_right else self.x + 10
        pygame.draw.circle(surface, BLACK, (eye_x, self.y - 10), 3)
        # Attack effect
        if self.is_attacking:
            attack_x = self.x + self.width if self.facing_right else self.x - 40
            pygame.draw.rect(surface, YELLOW, (attack_x, self.y + 20, 40, 20))
    
    def get_attack_rect(self):
        if self.is_attacking:
            if self.facing_right:
                return pygame.Rect(self.x + self.width, self.y + 20, 40, 20)
            else:
                return pygame.Rect(self.x - 40, self.y + 20, 40, 20)
        return None

ground_y = HEIGHT - 100

player1 = Fighter(100, ground_y - 80, RED, {
    "left": pygame.K_a, "right": pygame.K_d, 
    "jump": pygame.K_w, "attack": pygame.K_f
})

player2 = Fighter(WIDTH - 150, ground_y - 80, BLUE, {
    "left": pygame.K_LEFT, "right": pygame.K_RIGHT, 
    "jump": pygame.K_UP, "attack": pygame.K_KP0
})

running = True
while running:
    screen.fill((50, 50, 50))
    
    # Draw ground
    pygame.draw.rect(screen, GREEN, (0, ground_y, WIDTH, HEIGHT - ground_y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    player1.move(keys, ground_y)
    player2.move(keys, ground_y)
    
    # Check attacks
    p1_attack = player1.get_attack_rect()
    p2_attack = player2.get_attack_rect()
    
    if p1_attack and p2_attack:
        p2_rect = pygame.Rect(player2.x, player2.y, player2.width, player2.height)
        if p1_attack.colliderect(p2_rect):
            player2.health -= 10
    
    if p2_attack:
        p1_rect = pygame.Rect(player1.x, player1.y, player1.width, player1.height)
        if p2_attack.colliderect(p1_rect):
            player1.health -= 10
    
    player1.draw(screen)
    player2.draw(screen)
    
    # Draw health bars
    pygame.draw.rect(screen, RED, (20, 20, 200, 20))
    pygame.draw.rect(screen, GREEN, (20, 20, player1.health * 2, 20))
    pygame.draw.rect(screen, RED, (WIDTH - 220, 20, 200, 20))
    pygame.draw.rect(screen, GREEN, (WIDTH - 220, 20, player2.health * 2, 20))
    
    # Draw score
    font = pygame.font.Font(None, 36)
    p1_text = font.render("Player 1 (WASD+F)", True, WHITE)
    p2_text = font.render("Player 2 (Arrows+0)", True, WHITE)
    screen.blit(p1_text, (20, 50))
    screen.blit(p2_text, (WIDTH - 220, 50))
    
    if player1.health <= 0 or player2.health <= 0:
        winner = "Player 2" if player1.health <= 0 else "Player 1"
        win_text = font.render(winner + " Wins!", True, YELLOW)
        screen.blit(win_text, (WIDTH // 2 - 50, HEIGHT // 2))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_racing:
        code += '''# Racing Game
car_x = WIDTH // 2
car_y = HEIGHT - 150
car_width = 40
car_height = 70
road_left = 100
road_right = WIDTH - 100
road_markings = []
obstacles = []
score = 0
game_speed = 5

# Initialize road markings
for i in range(6):
    road_markings.append({"y": i * 120})

running = True
while running:
    screen.fill((34, 139, 34))
    
    # Draw road
    pygame.draw.rect(screen, (80, 80, 80), (road_left, 0, road_right - road_left, HEIGHT))
    pygame.draw.rect(screen, WHITE, (road_left, 0, 5, HEIGHT))
    pygame.draw.rect(screen, WHITE, (road_right - 5, 0, 5, HEIGHT))
    
    # Draw road markings
    for marking in road_markings:
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, marking["y"], 10, 60))
        marking["y"] += game_speed
        if marking["y"] > HEIGHT:
            marking["y"] = -60
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > road_left:
        car_x -= 7
    if keys[pygame.K_RIGHT] and car_x < road_right - car_width:
        car_x += 7
    if keys[pygame.K_UP]:
        game_speed = min(15, game_speed + 0.2)
    if keys[pygame.K_DOWN]:
        game_speed = max(3, game_speed - 0.2)
    
    # Spawn obstacles
    if random.randint(0, 40) == 0:
        obs_x = random.randint(road_left + 10, road_right - 50)
        obstacles.append({"x": obs_x, "y": -50})
    
    # Update obstacles
    for obs in obstacles[:]:
        obs["y"] += game_speed
        if obs["y"] > HEIGHT:
            obstacles.remove(obs)
            score += 1
        
        # Collision check
        car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
        obs_rect = pygame.Rect(obs["x"], obs["y"], 40, 40)
        if car_rect.colliderect(obs_rect):
            game_speed = 0
            game_over_text = "Game Over! Score: " + str(score)
    
    # Draw car
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))
    pygame.draw.rect(screen, (200, 0, 0), (car_x + 5, car_y + 10, car_width - 10, 15))
    pygame.draw.circle(screen, BLACK, (car_x + 10, car_y + car_height - 10), 8)
    pygame.draw.circle(screen, BLACK, (car_x + car_width - 10, car_y + car_height - 10), 8)
    
    # Draw obstacles
    for obs in obstacles:
        pygame.draw.rect(screen, BLUE, (obs["x"], obs["y"], 40, 40))
    
    # Draw score and speed
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    speed_text = font.render("Speed: " + str(int(game_speed * 10)), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(speed_text, (10, 50))
    
    instructions = font.render("Arrow Keys to move, UP/DOWN for speed", True, WHITE)
    screen.blit(instructions, (WIDTH // 2 - 180, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_tetris:
        code += '''# Tetris Game
import copy

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN]

grid = [[BLACK for _ in range(10)] for _ in range(20)]
current_piece = None
piece_pos = [0, 0]
score = 0
game_over = False

def new_piece():
    global current_piece, piece_pos
    shape_idx = random.randint(0, len(SHAPES) - 1)
    current_piece = {"shape": copy.deepcopy(SHAPES[shape_idx]), "color": COLORS[shape_idx]}
    piece_pos = [3, 0]

def draw_grid():
    for y in range(20):
        for x in range(10):
            pygame.draw.rect(screen, grid[y][x], (x * 30 + 50, y * 30 + 50, 28, 28))
            pygame.draw.rect(screen, WHITE, (x * 30 + 50, y * 30 + 50, 28, 28), 1)

def check_collision(offset_x=0, offset_y=0):
    for y, row in enumerate(current_piece["shape"]):
        for x, cell in enumerate(row):
            if cell:
                new_x = piece_pos[0] + x + offset_x
                new_y = piece_pos[1] + y + offset_y
                if new_x < 0 or new_x >= 10 or new_y >= 20:
                    return True
                if new_y >= 0 and grid[new_y][new_x] != BLACK:
                    return True
    return False

def lock_piece():
    global score
    for y, row in enumerate(current_piece["shape"]):
        for x, cell in enumerate(row):
            if cell:
                grid[piece_pos[1] + y][piece_pos[0] + x] = current_piece["color"]
    
    # Clear full rows
    for y in range(19, -1, -1):
        if all(cell != BLACK for cell in grid[y]):
            score += 100
            for y2 in range(y, 0, -1):
                grid[y2] = grid[y2 - 1][:]
            grid[0] = [BLACK for _ in range(10)]
    
    new_piece()
    if check_collision():
        global game_over
        game_over = True

new_piece()
fall_time = 0

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_LEFT and not check_collision(-1, 0):
                piece_pos[0] -= 1
            elif event.key == pygame.K_RIGHT and not check_collision(1, 0):
                piece_pos[0] += 1
            elif event.key == pygame.K_DOWN:
                if not check_collision(0, 1):
                    piece_pos[1] += 1
                else:
                    lock_piece()
            elif event.key == pygame.K_UP:
                # Rotate piece
                rotated = list(zip(*current_piece["shape"][::-1]))
                old_shape = current_piece["shape"]
                current_piece["shape"] = rotated
                if check_collision():
                    current_piece["shape"] = old_shape
    
    if not game_over:
        fall_time += 1
        if fall_time >= 30:
            fall_time = 0
            if not check_collision(0, 1):
                piece_pos[1] += 1
            else:
                lock_piece()
    
    draw_grid()
    
    # Draw current piece
    for y, row in enumerate(current_piece["shape"]):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, current_piece["color"], 
                    ((piece_pos[0] + x) * 30 + 50, (piece_pos[1] + y) * 30 + 50, 28, 28))
    
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    
    if game_over:
        game_over_text = font.render("Game Over! Press R to restart", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            grid = [[BLACK for _ in range(10)] for _ in range(20)]
            score = 0
            game_over = False
            new_piece()
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_breakout:
        code += '''# Breakout Game
paddle_x = WIDTH // 2 - 50
paddle_y = HEIGHT - 40
paddle_width = 100
paddle_height = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_radius = 10
ball_dx = 4
ball_dy = -4
bricks = []
score = 0

# Create bricks
brick_width = 75
brick_height = 25
brick_padding = 5
brick_offset_x = 50
brick_offset_y = 60

colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

for row in range(6):
    for col in range(9):
        bricks.append({
            "x": brick_offset_x + col * (brick_width + brick_padding),
            "y": brick_offset_y + row * (brick_height + brick_padding),
            "width": brick_width,
            "height": brick_height,
            "color": colors[row]
        })

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 8
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += 8
    
    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy
    
    # Ball collision with walls
    if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
        ball_dx *= -1
    if ball_y <= ball_radius:
        ball_dy *= -1
    if ball_y >= HEIGHT:
        # Game over - reset ball
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = 4
        ball_dy = -4
    
    # Ball collision with paddle
    if (paddle_x <= ball_x <= paddle_x + paddle_width and 
        paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height):
        ball_dy *= -1
        ball_dy += 0.5
    
    # Ball collision with bricks
    for brick in bricks[:]:
        if (brick["x"] <= ball_x <= brick["x"] + brick["width"] and
            brick["y"] <= ball_y <= brick["y"] + brick["height"]):
            bricks.remove(brick)
            ball_dy *= -1
            score += 10
    
    # Draw paddle
    pygame.draw.rect(screen, CYAN, (paddle_x, paddle_y, paddle_width, paddle_height))
    
    # Draw ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)
    
    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, brick["color"], 
            (brick["x"], brick["y"], brick["width"], brick["height"]))
    
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Win condition
    if len(bricks) == 0:
        win_text = font.render("You Win! Score: " + str(score), True, YELLOW)
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    elif has_platformer:
        code += '''# Platformer Game
player_x = 100
player_y = HEIGHT - 150
player_width = 30
player_height = 40
velocity_x = 0
velocity_y = 0
gravity = 0.8
jump_strength = -15
is_jumping = False

# Platforms
platforms = [
    {"x": 0, "y": HEIGHT - 50, "width": WIDTH, "height": 50},
    {"x": 200, "y": HEIGHT - 150, "width": 200, "height": 20},
    {"x": 500, "y": HEIGHT - 250, "width": 150, "height": 20},
    {"x": 100, "y": HEIGHT - 350, "width": 200, "height": 20},
    {"x": 400, "y": HEIGHT - 450, "width": 150, "height": 20},
]

collectibles = [
    {"x": 250, "y": HEIGHT - 180, "collected": False},
    {"x": 550, "y": HEIGHT - 280, "collected": False},
    {"x": 150, "y": HEIGHT - 380, "collected": False},
    {"x": 450, "y": HEIGHT - 480, "collected": False},
]

score = 0
exit_rect = pygame.Rect(WIDTH - 80, HEIGHT - 550, 50, 50)

running = True
while running:
    screen.fill((100, 150, 200))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                velocity_y = jump_strength
                is_jumping = True
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        velocity_x = -5
    elif keys[pygame.K_RIGHT]:
        velocity_x = 5
    else:
        velocity_x = 0
    
    # Apply gravity
    velocity_y += gravity
    
    # Move player
    player_x += velocity_x
    player_y += velocity_y
    
    # Platform collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    on_ground = False
    
    for platform in platforms:
        plat_rect = pygame.Rect(platform["x"], platform["y"], platform["width"], platform["height"])
        if player_rect.colliderect(plat_rect):
            if velocity_y > 0 and player_y + player_height - velocity_y <= platform["y"]:
                player_y = platform["y"] - player_height
                velocity_y = 0
                is_jumping = False
                on_ground = True
            elif velocity_y < 0 and player_y - velocity_y >= platform["y"] + platform["height"]:
                player_y = platform["y"] + platform["height"]
                velocity_y = 0
    
    # Screen boundaries
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_width:
        player_x = WIDTH - player_width
    if player_y > HEIGHT:
        player_y = HEIGHT - player_height
        is_jumping = False
    
    # Collectible collision
    for item in collectibles:
        if not item["collected"]:
            item_rect = pygame.Rect(item["x"], item["y"], 20, 20)
            if player_rect.colliderect(item_rect):
                item["collected"] = True
                score += 100
    
    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, (100, 70, 50), 
            (platform["x"], platform["y"], platform["width"], platform["height"]))
    
    # Draw collectibles
    for item in collectibles:
        if not item["collected"]:
            pygame.draw.circle(screen, YELLOW, (item["x"] + 10, item["y"] + 10), 10)
    
    # Draw exit
    pygame.draw.rect(screen, GREEN, exit_rect)
    
    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))
    pygame.draw.circle(screen, (255, 200, 150), (player_x + 15, player_y - 5), 10)
    
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Check win
    if player_rect.colliderect(exit_rect):
        win_text = font.render("You Win! Final Score: " + str(score), True, GREEN)
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    else:
        # Default interactive visualization
        code += '''# Interactive PyGame Visualization
shapes = []

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shapes.append({
                "pos": pygame.mouse.get_pos(),
                "size": random.randint(20, 60),
                "color": random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN]),
                "vx": random.uniform(-3, 3),
                "vy": random.uniform(-3, 3)
            })
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                shapes = []
    
    # Update and draw shapes
    for shape in shapes[:]:
        shape["pos"] = (shape["pos"][0] + shape["vx"], shape["pos"][1] + shape["vy"])
        
        if shape["pos"][0] < 0 or shape["pos"][0] > WIDTH:
            shape["vx"] *= -1
        if shape["pos"][1] < 0 or shape["pos"][1] > HEIGHT:
            shape["vy"] *= -1
        
        pygame.draw.circle(screen, shape["color"], (int(shape["pos"][0]), int(shape["pos"][1])), shape["size"])
    
    # Instructions
    font = pygame.font.Font(None, 36)
    text = font.render("Click to add shapes, Press C to clear", True, WHITE)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
'''
    
    return code

# Streamlit sidebar
with st.sidebar:
    st.title("Configuration")
    st.markdown("---")
    
    st.info("""
    How to use:
    1. Write your PyGame query
    2. Click Generate Code
    3. Copy the code and run locally or on Trinket
    """)
    
    st.markdown("---")
    st.markdown("[Run on Trinket](https://trinket.io/features/pygame)")

# Main UI
st.title("AI PyGame Visualizer")
st.markdown("*Generate PyGame code instantly*")

example_query = "Create a particle system simulation where particles emit from the mouse position"
query = st.text_area(
    "Enter your PyGame query:",
    height=70,
    placeholder="e.g.: " + example_query
)

# Split the buttons into columns
col1, col2 = st.columns(2)
generate_code_btn = col1.button("Generate Code")
clear_btn = col2.button("Clear")

if clear_btn:
    st.session_state.generated_code = ""
    st.session_state.last_query = ""
    st.rerun()

if generate_code_btn and query:
    # Show loading spinner
    with st.spinner("Generating PyGame code..."):
        try:
            # Generate the code using template system
            generated_code = generate_pygame_code(query)
            
            # Store the generated code
            st.session_state.generated_code = generated_code
            st.session_state.last_query = query
            
            st.success("Code generated successfully!")
            
        except Exception as e:
            st.error("Error generating code: " + str(e))

# Display generated code
if st.session_state.generated_code:
    st.markdown("### Generated PyGame Code")
    st.code(st.session_state.generated_code, language="python")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("Select all code above (Ctrl+A) and copy (Ctrl+C)")
    
    with col2:
        st.markdown("[Run on Trinket](https://trinket.io/features/pygame)")
        st.markdown("**To run:** Go to https://trinket.io/features/pygame, paste the code, and click Run!")

# Show last query if exists
if st.session_state.last_query:
    st.markdown("---")
    st.markdown("**Last Query:** " + st.session_state.last_query)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>PyGame Code Generator</p>
    
</div>
""", unsafe_allow_html=True)
