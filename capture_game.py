# Importere pygame
import pygame
import sys
import random

# Konstanter
WIDTH = 400  # Bredden til vinduet
HEIGHT = 600 # Høyden til vinduet

SIZE = (WIDTH, HEIGHT) # Størrelsen til vinduet

# Frames Per Second (bilder per sekund)
FPS = 60

# Farger (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (100, 100, 255)
GREY = (142, 142, 142)


# Initiere pygame
pygame.init()

# Lager en overflate (surface) vi kan tegne på
surface = pygame.display.set_mode(SIZE)

# Lager en klokke
clock = pygame.time.Clock()


class Ball:
    def __init__(self):

        self.radius = 10
        self.color = WHITE
        self.x = random.randint(self.radius, WIDTH-self.radius)
        self.y = -self.radius
        self.center = (x, y)
        self.vy = 0
        
    def update(self):
        self.vy += ay
        self.y += self.vy #+ 0.5*ay
        
        self.center = (self.x, self.y)
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius)
        
lives = 3

# Variabel som styrer om spillet skal kjøres
run = True

# Verdier til spilleren
w = 60  # bredde
h = 80  # høyde

# Startposisjon
y = HEIGHT - h - 20
x = WIDTH//2 - w//2

# Hastighet
speed = 5

player_img = pygame.image.load("bucket.png")
background_img = pygame.image.load("background_snow_2-3.png")
background_img = pygame.transform.scale(background_img, SIZE)

# Ball
ay = 0.05
ball = Ball()

font = pygame.font.SysFont("Arial", 26)

# Poeng
poeng = 0

def display_points():
    text_img = font.render(f"Antall poeng: {poeng}", True, WHITE)
    surface.blit(text_img, (20, 10))

def display_lives():
    lives_img = font.render(f"Antall liv: {lives}", True, WHITE)
    surface.blit(lives_img, (WIDTH-120, 10))
    
# Spill-løkken
while run:
    # Sørger for at løkken kjører i korrekt hastighet
    clock.tick(FPS)

    
    # Går gjennom hendelser (events)
    for event in pygame.event.get():
        # Sjekker om vi ønsker å lukke vinduet
        if event.type == pygame.QUIT:
            run = False # Spillet skal avsluttes
            
    
    # Nullstiller farten
    vx = 0
            
    # Henter knappene fra tastaturet som trykkes på
    keys = pygame.key.get_pressed()
    
    # Sjekker om piltast til venstre er trykket på
    if keys[pygame.K_LEFT]:
        vx = -speed
        
    # Sjekker om piltast til høyre er trykket på
    if keys[pygame.K_RIGHT]:
        vx = speed
            
    
    # Fyller skjermen med en farge
    #surface.fill(LIGHTBLUE)
    
    # Endrer posisjonen til rektangelet
    x += vx
    
    # Sjekker kollisjon med høyre side av skjermen
    if x+w >= WIDTH:
        x = WIDTH - w # Sørger for at den ikke stikker av
        
    # Sjekker kollisjon med venstre side
    if x <= 0:
        x = 0
        
    surface.blit(background_img,(0,0))
    surface.blit(player_img, (x,y))
    
    
    # Ball
    ball.update()
    ball.draw(surface)
    
    
    # Spiller
    #pygame.draw.rect(surface, GREY, [x, y, w, h])
    
    if y < ball.y < y+h and x < ball.x < x+w:
        #print("Kollisjon!")
        poeng += 1
        
        # Lager ny ball
        ball = Ball()
        ay *= 1.1
        #print(ay)
    
    
    if ball.y + ball.radius > HEIGHT:
        lives-=1
        ball = Ball()
        if lives == 0:
            print("Du klarte ikke å fange ballen")
            print(f"Du fikk {poeng} poeng")
            run = False # Game over
    
    display_lives()
    display_points()   
    # "Flipper" displayet for å vise hva vi har tegnet
    pygame.display.flip()
    


# Avslutter pygame
pygame.quit()
#sys.exit() # Dersom det ikke er tilstrekkelig med pygame.quit()
