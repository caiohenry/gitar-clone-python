import pygame

from config.config_game import HEIGHT, HIT_DISTANCE, NOTE_HEIGHT, NOTE_WIDTH, WIDTH
from config.keyboard_buttons import CONFIRM_BUTTON, KEY_OPEN, PRESSED_BUTTON
from game.notes import Note


class Events:
    
    @staticmethod
    def calculate_colusion(note: Note):
        distance_point = HEIGHT - HIT_DISTANCE + NOTE_HEIGHT // 4
        return (note.y >= distance_point - 28) and (note.y <= distance_point - 10)
    
    @staticmethod
    def note_point_event(note: Note, keys) -> bool:
        
        buttons_pressed_accept = [keys[KEY_OPEN[column]] for column in note.columns] + [keys[CONFIRM_BUTTON]]  
        print(PRESSED_BUTTON)
        
        for column in note.columns:
            
            time_pressed = pygame.time.get_ticks() - PRESSED_BUTTON[column]["start_time"]
            
            print(time_pressed)
            
            if (time_pressed >= 400 and PRESSED_BUTTON[column]["start_time"] != 0):
                return False
        
        return (all(buttons_pressed_accept) and Events.calculate_colusion(note))
    
    
    @staticmethod
    def key_pressed_event(keys):

        for i in range(5):
            
            if keys[KEY_OPEN[i]]:
        
                PRESSED_BUTTON[i]["pressed"] = True
                PRESSED_BUTTON[i]["start_time"] = pygame.time.get_ticks()
            
            else:
                
                PRESSED_BUTTON[i]["pressed"] = False
                PRESSED_BUTTON[i]["start_time"] = 0
        
                
                
                