import pygame
import sys

from config.colors import *
from game.draw import Drawing
from game.notes import Note
from config.config_game import *
from config.keyboard_buttons import *
from game.events import Events

from moviepy.editor import VideoFileClip
import numpy as np

from music.tuca_donka.partiture import PartitureTucaDonka



# Get Partiture Music

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guitar Hero Clone - By Caio H.")
clock = pygame.time.Clock()
drawing = Drawing(screen)

music_path = ""
video_frames = []
current_frame = 0
frame_delay = int(1000 / FPS)
video_clip = VideoFileClip("music/tuca_donka/video_1.mp4")
frames = video_clip.iter_frames(fps=FPS)

pygame.init()

def main():
    
    global frames
    notes: list[Note] = []
    score = 0
    total_notes = 0

    current_note = 0
    current_time = 0

   
    MUSIC_NOTES = PartitureTucaDonka() .get_partiture()
    music_path = r"C:\Users\vidal\Desktop\gh\music\tuca_donka\music.mp3"
        
        

    start_time = pygame.time.get_ticks()
    pygame.mixer.init()
    
    countdown_start = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get the keys pressed of user
        keys = pygame.key.get_pressed()

        elapsed_time = pygame.time.get_ticks() - start_time

        countdown_elapsed = (pygame.time.get_ticks() - countdown_start) / 1000
        countdown_remaining = max(0, COUTING_REGRESSIVE - countdown_elapsed)

        # Se o contador regressivo ainda não terminou, exiba o texto
        if countdown_remaining > 0:
            screen.fill(WHITE)
            font = pygame.font.Font(None, 100)
            countdown_text = font.render(str(int(countdown_remaining) + 1), True, (0, 0, 0))
            screen.blit(countdown_text, (WIDTH // 2 - 20, HEIGHT // 2 - 50))
            pygame.display.flip()
            continue


        screen.fill(WHITE)
        drawing.draw_base(BASE_REACT)
        drawing.draw_bar(3)

        if elapsed_time >= (2300 + (COUTING_REGRESSIVE*1000)):
            try:
                frame = next(frames)
            except StopIteration:
                video_clip = VideoFileClip("music/tuca_donka/video_1.mp4")
                frames = video_clip.iter_frames(fps = FPS)
                frame = next(frames)

            frame = np.rot90(frame)
            frame = pygame.transform.scale(pygame.surfarray.make_surface(frame), (WIDTH, HEIGHT))
            screen.blit(frame, (0, 0))
            drawing.draw_base(BASE_REACT)
            drawing.draw_bar(3)

            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play()

        if current_note < len(MUSIC_NOTES) and MUSIC_NOTES[current_note].time <= current_time:
            note: Note = MUSIC_NOTES[current_note]
            notes.append(note)
            current_note += 1

        for note in notes:
            if not note.animation_state != 0:
                note.y += NOTE_SPEED
                
        
        # Drawing the notes
        drawing.draw_notes(notes)
        
        
        drawing.draw_hit_marker()
        

        for note in notes:
            
            if note.y - 20 >= (BASE_REACT.bottom - NOTE_HEIGHT):
                notes.remove(note)
                total_notes += 1 
                
            Events.key_pressed_event(keys)
                
            
            if (
                Events.note_point_event(note, keys)
            ):
                
                if note.animation_state == 0:
                    note.animation_state = 1
                    score += 1
                    
                if note.animation_state == 0 and pygame.time.get_ticks() - note.start_hold_time >= 400:
                    note.animation_state = 1
                    score += 1
                    
                if note.animation_state == 1:
                    drawing.draw_circle_point_active(note)
                    notes.remove(note)
                    total_notes += 1
            
        
        font = pygame.font.Font(None, 36)
        try:
            text = font.render(f"Taxa de acertos: {score/total_notes * 100 // 1}%", True, (0, 0, 0))
        except ZeroDivisionError:
            text = font.render(f"Taxa de acertos: 100%", True, (0, 0, 0))
        text_time = font.render(f"tempo: {current_time // 1000}", True, (0, 0, 0))
        screen.blit(text, ((WIDTH /4)+(WIDTH/8) + 40, 10))
        screen.blit(text_time, ((WIDTH /4)+(WIDTH/8) + 40, 30))

        pygame.display.flip()
        clock.tick(FPS)
        current_time += 1000 // FPS

if __name__ == "__main__":
    
    main()
