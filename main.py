# main.py

import pygame
import sys
from game_logic.board import Board
from game_logic.player import Player, AIPlayer
from game_logic.unit import Unit
from gui.renderer import Renderer
from utils.helpers import load_map

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 30

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Diplomacy Game")
    clock = pygame.time.Clock()

    # Load Map Data
    map_data = load_map('data/map.json')  # Ensure map.json is correctly formatted and contains coordinates
    board = Board(map_data)

    # Initialize Players
    players = [
        Player(name="Player 1", player_type='human'),
        AIPlayer(name="AI 1"),
        AIPlayer(name="AI 2"),
        Player(name="Player 2", player_type='human')
    ]

    # Assign Initial Ownership and Place Units
    initial_ownership = {
        "London": "Player 1",
        "Paris": "Player 1",
        "Berlin": "AI 1",
        "Rome": "AI 1",
        "Madrid": "AI 2",
        "Vienna": "AI 2",
        "Warsaw": "Player 2",
        "Sevastopol": "Player 2"
        # Add all necessary regions
    }

    for region_name, player_name in initial_ownership.items():
        region = board.get_region(region_name)
        player = next((p for p in players if p.name == player_name), None)
        if player and region:
            region.owner = player
            # Place a unit; determine unit type based on region type or predefined setup
            unit_type = 'fleet' if region.type == 'sea' else 'army'
            unit = Unit(unit_type=unit_type, location=region, owner=player)
            player.units.append(unit)
            region.units.append(unit)

    # Initialize Renderer
    renderer = Renderer(screen=screen, board=board)

    # Main Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle other events (e.g., mouse clicks) here
            # This is where you'd integrate the UserInterface class for interactions

        # Rendering
        renderer.render_frame()

        # Control the frame rate
        clock.tick(FPS)

    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
