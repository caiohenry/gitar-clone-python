

# Class Note
import pygame

from config.colors import COLORS_NOTES
from config.config_game import BASE_REACT


class Note:
    
    def __init__(self, time: int, columns: list, type: bool = True):
            
        self.time = time
        self.columns = columns
        self.type = type
        self.y = 0
        self.x = []
        self.animation_state = 0
        self.start_hold_time = 0
        
        for column in columns:
            self.x.append(column * BASE_REACT.width // 5 + BASE_REACT.left + 20)
        
    def __str__(self) -> str:
        return f"{self.columns}"