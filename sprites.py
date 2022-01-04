from settings import *


class Sprites:
    def __init__(self):
        self.sc = sc
        self.n = n
        self.score = score
        self.best = best
        self.game_over = game_over
        self.bird = pygame.image.load('img/bird.png')
        self.image = pygame.image.load('img/column1.png')
        self.image1 = pygame.image.load('img/column2.png')
        self.bg = pygame.image.load('img/bg.png')
        self.rect = self.bird.get_rect(centerx=width/4, bottom=height-225)
        self.rect1 = self.image.get_rect(centerx=width, bottom=height+40+self.n)
        self.rect2 = self.image1.get_rect(centerx=width, bottom=height-340+self.n)
        self.render_score = font_score.render(f'SCORE:{self.score}', 1, pygame.Color('blue'))
        self.render_best = font_score.render(f'BEST:{self.best}', 1, pygame.Color('blue'))
        self.render_end = font_game_over.render('GAME OVER!', 1, pygame.Color('orange'))

    def draw(self):
        self.sc.blit(self.bg, (0, 0))
        self.sc.blit(self.bird, self.rect)
        self.sc.blit(self.image1, self.rect1)
        self.sc.blit(self.image, self.rect2)
        self.sc.blit(self.render_score, (5, 3))
        self.sc.blit(self.render_best, (135, 3))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.KEYDOWN and not self.game_over:
                if i.key == pygame.K_SPACE and self.rect.y >= 0:
                    self.rect.y -= 60
            elif i.type == pygame.MOUSEBUTTONDOWN and not self.game_over and self.rect.y >= 0:
                self.rect.y -= 60
            elif i.type == pygame.KEYDOWN and self.game_over:
                if i.key == pygame.K_SPACE:
                    self.rect1.x = 260
                    self.rect2.x = 260
                    self.score = 0
                    self.render_score = font_score.render(f'SCORE:{self.score}', 1, pygame.Color('blue'))
                    self.sc.blit(self.render_score, (5, 5))
                    self.draw()
                    self.game_over = False
            elif i.type == pygame.MOUSEBUTTONDOWN and self.game_over:
                self.rect1.x = 270
                self.rect2.x = 270
                self.score = 0
                self.render_score = font_score.render(f'SCORE:{self.score}', 1, pygame.Color('blue'))
                self.sc.blit(self.render_score, (5, 5))
                self.draw()
                self.game_over = False
        if self.rect.y <= height - 50 and not self.game_over:
            self.rect.y += 2.5
        if not self.game_over:
            self.rect1.x -= 2
            self.rect2.x -= 2
        if pygame.Rect.colliderect(self.rect, self.rect1) or \
                pygame.Rect.colliderect(self.rect, self.rect2):
            self.game_over = True
        if self.rect1.x <= -63 and self.rect2.x <= -63:
            self.score += 1
            self.render_score = font_score.render(f'SCORE:{self.score}', 1, pygame.Color('blue'))
            self.sc.blit(self.render_score, (5, 3))
            self.n = randrange(-40, 140, 10)
            self.rect1.x = 270
            self.rect2.x = 270
            self.rect1 = self.image.get_rect(centerx=width, bottom=height+40+self.n)
            self.rect2 = self.image.get_rect(centerx=width, bottom=height-340+self.n)
            self.sc.blit(self.image, self.rect1)
            self.sc.blit(self.image, self.rect2)

        if self.game_over:
            self.sc.blit(self.render_end, (8, 160))
            if self.score > self.best:
                self.best = self.score
                self.render_best = font_score.render(f'BEST:{self.best}', 1, pygame.Color('blue'))
                self.sc.blit(self.render_best, (135, 3))
