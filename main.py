import pygame
pygame.init()

# screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

# paddle
paddle1 = pygame.Rect(680, 250, 10, 100)
paddle2 = pygame.Rect(10, 250, 10, 100)
ypos = 150
ypos2 = 150
direction = "STOP"
direction2 = "STOP"

# ball
ball = pygame.Rect(350, 250, 20, 20)

# ball speed
xspeed = .5
yspeed = -.5

# ball position
bx = 350
by = 200

# scores
s1 = 0
s2 = 0
winning_score = 10

# define the score board function
def display_scores():
 font = pygame.font.SysFont('comic sans', 28)
 text = font.render(f"Player A: {s1} | Player B: {s2}", True, (255, 255, 255))
 text_rect = text.get_rect(center=(screen_width / 2, 50))
 screen.blit(text, text_rect)

# sounds
pong_sound = pygame.mixer.Sound("sound.wav")
score_sound = pygame.mixer.Sound("other sound.wav")
winner_music = pygame.mixer.Sound("winner.wav")

# winner
def game_over():
    if s1 == winning_score:
        pygame.mixer.Sound.play(winner_music)
        font = pygame.font.SysFont('comic sans', 50)
        text3 = font.render(f"GAME OVER, Player A Wins!!", True, (255, 255, 255), None)
        text3_rect = text3.get_rect(center=(screen_width / 2, 200))
        screen.blit(text3, text3_rect)

    elif s2 == winning_score:
        pygame.mixer.Sound.play(winner_music)
        font = pygame.font.SysFont('comic sans', 50)
        text3 = font.render(f"GAME OVER, Player B Wins!!", True, (255, 255, 255), None)
        text3_rect = text3.get_rect(center=(screen_width / 2, 200))
        screen.blit(text3, text3_rect)

while True:
 # events
 for events in pygame.event.get():
     if events.type == pygame.QUIT:
         pygame.quit()
     if events.type == pygame.KEYDOWN:
         if events.key == pygame.K_UP:
             direction = "UP"
         if events.key == pygame.K_DOWN:
             direction = "DOWN"
     if events.type == pygame.KEYUP:
         if events.key == pygame.K_UP:
             direction = "STOP"
         if events.key == pygame.K_DOWN:
             direction = "STOP"
     if events.type == pygame.KEYDOWN:
         if events.key == pygame.K_w:
             direction2 = "UP"
         if events.key == pygame.K_s:
             direction2 = "DOWN"
     if events.type == pygame.KEYUP:
         if events.key == pygame.K_w:
             direction2 = "STOP"
         if events.key == pygame.K_s:
             direction2 = "STOP"

 # logic
 # moving ball
 bx += xspeed
 by += yspeed

 # top
 if by < 0:
     yspeed *= -1
     pygame.mixer.Sound.play(pong_sound)
 # bottom
 if by > 390:
     yspeed *= -1
     pygame.mixer.Sound.play(pong_sound)

 # if ball misses paddle
 if bx > 700:
     bx = 1
     by = 350
     s1 += 1
     pygame.mixer.Sound.play(score_sound)

 if bx < 0:
     bx = 700
     by = 350
     s2 += 1
     pygame.mixer.Sound.play(score_sound)

 # moving paddles smoothly
 if direction == "UP" and ypos > 0:
     ypos -= 2
 if direction == "DOWN" and ypos < 300:
     ypos += 2
 if direction2 == "UP" and ypos2 > 0:
     ypos2 -= 2
 if direction2 == "DOWN" and ypos2 < 300:
     ypos2 += 2

     # ball hitting paddle
 collide = pygame.Rect.colliderect(paddle1, ball)
 if collide:
     pygame.mixer.Sound.play(pong_sound)
     xspeed *= -1
     bx -= 10
 collide = pygame.Rect.colliderect(paddle2, ball)
 if collide:
     pygame.mixer.Sound.play(pong_sound)
     xspeed *= -1
     bx -= -10

 # display
 paddle1 = pygame.Rect(680, ypos, 15, 100)
 paddle2 = pygame.Rect(5, ypos2, 15, 100)
 ball = pygame.Rect(bx, by, 20, 20)
 screen.fill((121, 205, 205))
 display_scores()
 pygame.draw.rect(screen, (32, 178, 170), paddle1)
 pygame.draw.rect(screen, (32, 178, 170), paddle2)
 pygame.draw.rect(screen, (0, 139, 139), ball)
 game_over()
 pygame.display.update()