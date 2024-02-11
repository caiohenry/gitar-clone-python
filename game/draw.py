import pygame
from config.colors import BLACK, WHITE, COLORS_NOTES
from config.config_game import BASE_REACT, NOTE_HEIGHT, NOTE_WIDTH, HIT_DISTANCE, HEIGHT, WIDTH
from game.notes import Note


class Drawing:
    
    def __init__(self, screen):
        self.screen = screen
    

    def draw_notes(self, notes: list[Note]):
        
        for note in notes:
        
            for index, column in enumerate(note.columns):
                pygame.draw.circle(self.screen, COLORS_NOTES[column], (note.x[index] + NOTE_WIDTH // 2, note.y + NOTE_HEIGHT // 2), NOTE_WIDTH // 2)
                pygame.draw.circle(self.screen, (0, 0, 0), (note.x[index] + NOTE_WIDTH // 2, note.y + NOTE_HEIGHT // 2), NOTE_WIDTH // 2, width=2)
            
                if not note.type:
                
                    pygame.draw.line(self.screen, COLORS_NOTES[column], (note.x[index] + NOTE_WIDTH // 2, note.y + NOTE_HEIGHT // 2 - 120) , (note.x[index] + NOTE_WIDTH // 2, note.y + NOTE_HEIGHT // 2), 20)
                
    
    def draw_hit_marker(self):
        circle_radius = NOTE_WIDTH // 2 + 5  
        circle_y = HEIGHT - HIT_DISTANCE + NOTE_HEIGHT // 4
        value = 45
        for i in range(5):
            pygame.draw.circle(self.screen, BLACK, (int((WIDTH /4)+(WIDTH/8) + value), circle_y), circle_radius, 2)
            value += 80
            
    def draw_base(self, base_rect):
        pygame.draw.rect(self.screen, WHITE, base_rect)
        pygame.draw.line(self.screen, BLACK, (base_rect.left, 0), (base_rect.left, HEIGHT), 2)
        pygame.draw.line(self.screen, BLACK, (base_rect.right, 0), (base_rect.right, HEIGHT), 2)
        
    def draw_circle_point_active(self, note: Note):
        for index, column in enumerate(note.columns):
            pygame.draw.circle(self.screen, COLORS_NOTES[column], (note.x[index] +int(NOTE_WIDTH / 2), note.y + int(NOTE_HEIGHT / 2)), (int(NOTE_WIDTH / 2)) + 10)


    def draw_bar(self, total):
        pygame.draw.line(self.screen, BLACK, (BASE_REACT.left + 20, 80), (BASE_REACT.right - 20, 80), 2)
        pygame.draw.line(self.screen, BLACK, (BASE_REACT.left + 20, 100), (BASE_REACT.right - 20, 100), 2)
        pygame.draw.line(self.screen, BLACK, (BASE_REACT.left + 20, 80), (BASE_REACT.left + 20, 100), 2)
        pygame.draw.line(self.screen, BLACK, (BASE_REACT.right - 20, 80), (BASE_REACT.right - 20, 100), 2)