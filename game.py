import pygame
import asyncio
import websockets
from player import Actor
import json
import random



# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# New players should join this list
SESSION = []


# Connection button
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 200
BUTTON_TEXT = pygame.font.Font(None, 30).render("Connect", True, pygame.Color("white"))
BUTTON_COLOR = pygame.Color('Red')
CONNECT_BUTTON = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, (HEIGHT- BUTTON_HEIGHT) // 2, BUTTON_WIDTH, BUTTON_HEIGHT )
CONNECT_BUTTON_RECT = CONNECT_BUTTON


# Initialize pygame


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Multiplayer Game')

# Game loop
RUNNING = True

player = Actor()

async def send_info(websocket):
    data = {
        'player_id': player.player_id,
        'color': player.color,
        'x': player.x,
        'y': player.y,
    }
    message = json.dumps(data)
    print(f'Your user information: player_id - {player.player_id}, color - {player.color}, x - {player.x}, y - {player.y} ')
    await websocket.send(message)


async def connect():
    print('running')
    async with websockets.connect(f'ws://localhost:7889') as websocket:
        await send_info(websocket)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if CONNECT_BUTTON_RECT.collidepoint(event.pos):
                print("Connection to the server...")
                asyncio.run(connect())


def game_loop():
    while RUNNING:
        clock.tick(60)
        handle_events()
        WINDOW.fill(pygame.Color("black"))
        pygame.draw.rect(WINDOW, BUTTON_COLOR, CONNECT_BUTTON_RECT )
        WINDOW.blit(BUTTON_TEXT, CONNECT_BUTTON_RECT.center) # displaying button and text
        pygame.display.flip() # need to flip display to display object correctly

game_loop()



