
import pygame

class Renderer:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self.region_colors = {}  # Map player names to colors
        self.background = None
        self.load_assets()

    def load_assets(self):
        # Load the static background image
        try:
            self.background = pygame.image.load('assets/images/modern.png').convert()
        except pygame.error as e:
            print(f"Error loading background image: {e}")
            self.background = None  # Fallback if image fails to load

        # Define colors for ownership overlays
        self.region_colors = {
            "Player 1": (0, 0, 255, 100),      # Blue with alpha
            "Player 2": (255, 0, 0, 100),      # Red with alpha
            "AI 1": (0, 255, 0, 100),          # Green with alpha
            "AI 2": (255, 255, 0, 100),        # Yellow with alpha
            "Neutral": (200, 200, 200, 100)    # Grey with alpha
        }

        # Define unit colors
        self.unit_colors = {
            "Player 1": (0, 0, 255),    # Blue
            "Player 2": (255, 0, 0),    # Red
            "AI 1": (0, 255, 0),        # Green
            "AI 2": (255, 255, 0),      # Yellow
            "Neutral": (200, 200, 200)  # Grey
        }

        # Define unit sizes
        self.army_size = 10  # Half-length of square
        self.fleet_size = 12  # Radius of triangle

    def render_frame(self):
        # Draw the background
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill((0, 100, 0))  # Fallback: Fill with green if no background

        # Draw ownership overlays
        self.draw_ownership_overlays()

        # Draw units
        self.draw_units()

        # Update the display
        pygame.display.flip()

    def draw_ownership_overlays(self):
        """
        Draw semi-transparent overlays to indicate ownership.
        """
        for region in self.board.get_all_regions():
            if region.owner:
                color = self.region_colors.get(region.owner.name, (255, 255, 255, 100))
            else:
                color = self.region_colors["Neutral"]

            # Draw a semi-transparent circle or other shape over the region
            if region.coordinates:
                x, y = region.coordinates
                overlay_color = color  # Includes alpha
                pygame.draw.circle(self.screen, overlay_color, (x, y), 30)

    def draw_units(self):
        """
        Draw units as squares (armies) and triangles (fleets).
        """
        for region in self.board.get_all_regions():
            for unit in region.units:
                if region.coordinates:
                    x, y = region.coordinates
                    owner_color = self.unit_colors.get(unit.owner.name, (255, 255, 255))  # Default to white

                    if unit.type == 'army':
                        # Draw a square centered at (x, y)
                        square_size = self.army_size
                        top_left = (x - square_size, y - square_size)
                        square_rect = pygame.Rect(top_left, (square_size * 2, square_size * 2))
                        pygame.draw.rect(self.screen, owner_color, square_rect)
                        # Optional: Add a border for better visibility
                        pygame.draw.rect(self.screen, (0, 0, 0), square_rect, 2)

                    elif unit.type == 'fleet':
                        # Draw a triangle centered at (x, y)
                        triangle_size = self.fleet_size
                        point1 = (x, y - triangle_size)  # Top point
                        point2 = (x - triangle_size, y + triangle_size)  # Bottom-left
                        point3 = (x + triangle_size, y + triangle_size)  # Bottom-right
                        pygame.draw.polygon(self.screen, owner_color, [point1, point2, point3])
                        # Optional: Add a border for better visibility
                        pygame.draw.polygon(self.screen, (0, 0, 0), [point1, point2, point3], 2)

                    # Additional unit types can be handled here
