from sprites import *
sprite = Sprites()

while True:
    sprite.draw()
    pygame.display.flip()
    clock.tick(fps)
