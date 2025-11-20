import pygame
import os

from configuratieElectronica import configuratie_electronica_element, configuratie_electronica_ion
from afisare import elements, afisare, resource_path


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Ioni Chimie")

img = pygame.image.load(resource_path("assets\sistem_periodic.webp"))
tabel = pygame.transform.smoothscale_by(img, 2)
t_w, t_h = tabel.get_size()
width, height = screen.get_size()

elem_chimic = ""
font_size = 30
font = pygame.font.SysFont("Arial", font_size)
text_color = (0, 0, 0)
text_element = text_ion = ""


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            for symbol, rect in elements.items():
                if rect.collidepoint(mx, my):
                    print("Ai dat click pe:", symbol)
                    elem_chimic = symbol

    
    screen.fill((235, 225, 200))  # Fill the screen aka Backgroung color
    screen.blit(tabel, ((width - t_w) / 2 - 45, 0 + 20)) # Afisare Tabel
    
    afisare(font, elem_chimic, text_color, font_size, screen)
    
                    
    pygame.display.flip()  # Update the display
# Quit Pygame
pygame.quit()