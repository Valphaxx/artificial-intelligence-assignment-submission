import pygame
import random
import math
from Person import Person

pygame.init()

# Window
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Problem – When does the first shared birthday appear?")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 40, 40)
GREEN = (40, 160, 40)
BLUE  = (50, 120, 220)
BG    = (245, 248, 255)
LIGHT_GRAY = (200, 200, 200)

# Fonts (more beautiful & consistent)
font_title = pygame.font.SysFont("segoeui", 48, bold=True)
font_big   = pygame.font.SysFont("segoeui", 32, bold=True)
font_med   = pygame.font.SysFont("segoeui", 24)
font_small = pygame.font.SysFont("segoeui", 18)

# State variables
people = []
seen = {}  # birthday → list of person indices
collision_found = False
collision_pair = None
current_step = 0
max_people = 60
running = True

# For probability curve
curve_points = []  # list of (x, y) for the curve line

def theoretical_prob(n):
    if n < 2: return 0.0
    p = 1.0
    for i in range(1, n):
        p *= (365 - i) / 365.0
    return 1.0 - p

def reset():
    global people, seen, collision_found, collision_pair, current_step, curve_points
    people.clear()
    seen.clear()
    collision_found = False
    collision_pair = None
    current_step = 0
    curve_points.clear()

reset()

# ────────────────────────────────────────────────
# Main loop
# ────────────────────────────────────────────────

while running:
    dt = clock.tick(30)
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_r:
                reset()

    # Add new person every ~800–1200 ms
    if not collision_found and current_step < max_people and current_step * 900 < pygame.time.get_ticks():
        birthday = random.randint(1, 365)
        # Grid positioned better to avoid overlaps
        x = 60 + (current_step % 12) * 95
        y = 220 + (current_step // 12) * 85

        person = Person(x, y, birthday, screen)
        people.append(person)

        if birthday in seen:
            collision_found = True
            collision_pair = (seen[birthday][0], current_step)
            seen[birthday].append(current_step)
        else:
            seen[birthday] = [current_step]

        current_step += 1

        # Add point to probability curve
        prob = theoretical_prob(current_step)
        curve_x = 900 + current_step * 6
        curve_y = 180 + (1 - prob) * 300
        curve_points.append((curve_x, curve_y))

    # ─── Draw semi-transparent info panel at top ───────────────────────────
    panel_rect = pygame.Rect(0, 0, WIDTH, 180)
    panel_surface = pygame.Surface((WIDTH, 180), pygame.SRCALPHA)
    panel_surface.fill((255, 255, 255, 220))  # Semi-transparent white
    screen.blit(panel_surface, (0, 0))
    
    # Draw subtle border
    pygame.draw.line(screen, LIGHT_GRAY, (0, 180), (WIDTH, 180), 2)

    # ─── Draw people ────────────────────────────────────────────────────────
    for i, p in enumerate(people):
        highlight = collision_found and i in (collision_pair or ())
        p.draw(highlight=highlight)

    # ─── UI texts (now with better spacing) ────────────────────────────────
    title = font_title.render("Birthday Problem Simulation", True, BLACK)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 25))

    # Left side info
    count_text = font_big.render(f"People: {current_step}", True, BLUE)
    screen.blit(count_text, (40, 95))

    # Right side probability
    if current_step >= 2:
        theo = theoretical_prob(current_step) * 100
        color = RED if theo > 50 else GREEN
        prob_text = font_med.render(f"Probability: {theo:.1f}%", True, color)
        screen.blit(prob_text, (40, 140))

    # ─── Collision message (centered overlay with background) ──────────────
    if collision_found:
        # Create semi-transparent overlay
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 100))  # Dark overlay
        screen.blit(overlay, (0, 0))
        
        # Message box
        box_width, box_height = 600, 250
        box_x = WIDTH//2 - box_width//2
        box_y = HEIGHT//2 - box_height//2
        
        # Draw white rounded box
        box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        pygame.draw.rect(box_surface, (255, 255, 255, 240), (0, 0, box_width, box_height), border_radius=15)
        screen.blit(box_surface, (box_x, box_y))
        
        # Border
        pygame.draw.rect(screen, RED, (box_x, box_y, box_width, box_height), 3, border_radius=15)
        
        # Message text
        msg = font_big.render("FIRST SHARED BIRTHDAY!", True, RED)
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, box_y + 50))

        pair_text = font_med.render(
            f"Person {collision_pair[1]+1} matches Person {collision_pair[0]+1}",
            True, BLACK)
        screen.blit(pair_text, (WIDTH//2 - pair_text.get_width()//2, box_y + 110))
        
        # Birthday info
        shared_birthday = people[collision_pair[0]].birthday
        birthday_text = font_small.render(f"Shared birthday: Day {shared_birthday}", True, (80, 80, 80))
        screen.blit(birthday_text, (WIDTH//2 - birthday_text.get_width()//2, box_y + 150))

        restart_text = font_med.render("Press SPACE or R to restart", True, BLUE)
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, box_y + 195))

    # Help text bottom
    if not collision_found:
        help_txt = font_small.render("Press SPACE or R to restart  |  Watch for the first birthday match!", True, (120, 120, 120))
        screen.blit(help_txt, (WIDTH//2 - help_txt.get_width()//2, HEIGHT - 35))

    pygame.display.flip()

pygame.quit()