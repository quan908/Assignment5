import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Agents")

# Agent settings
AGENT_COUNT = 5
AGENT_SIZE = 10
AGENT_SPEED = 2

# Target settings
TARGET_SIZE = 15
target_pos = [WIDTH // 2, HEIGHT // 2]

# Define different colors for each agent
AGENT_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]  # Red, Green, Blue, Yellow, Magenta

# Agent class
class Agent:
    def __init__(self, x, y, color):
        self.pos = pygame.Vector2(x, y)
        self.speed = AGENT_SPEED
        self.color = color

    def move_towards(self, target):
        direction = pygame.Vector2(target) - self.pos
        if direction.length() != 0:
            direction = direction.normalize()
            self.pos += direction * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), AGENT_SIZE)

# Create exactly 5 agents at random positions with different colors
agents = [Agent(random.randint(0, WIDTH), random.randint(0, HEIGHT), AGENT_COLORS[i]) for i in range(AGENT_COUNT)]

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Mouse click to set target position
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target_pos = list(event.pos)

    # Keyboard control for target movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        target_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        target_pos[0] += 5
    if keys[pygame.K_UP]:
        target_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        target_pos[1] += 5

    # Mouse movement to set target position
    if pygame.mouse.get_focused():
        mouse_pos = pygame.mouse.get_pos()
        target_pos = list(mouse_pos)

    # Update agent positions
    for agent in agents:
        agent.move_towards(target_pos)

    # Draw everything
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), target_pos, TARGET_SIZE)
    for agent in agents:
        agent.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
