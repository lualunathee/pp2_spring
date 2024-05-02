import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((829, 836))
done = False
bg_image = pygame.image.load('C:/Users/aluas/Downloads/pp2_spring/lab77/clock/images/main.png')
sec_img = pygame.image.load('C:/Users/aluas/Downloads/pp2_spring/lab77/clock/images/left-hand.png')
min_img = pygame.image.load('C:/Users/aluas/Downloads/pp2_spring/lab77/clock/images/right-hand.png')
rect = bg_image.get_rect(center=(415, 418)) 
# центрирует его по указанным координатам (415, 418)

while not done:
    screen.blit(bg_image, (0, 0))
    #  Рисует фоновое изображение на поверхности отображения по координатам (0, 0).
    for event in pygame.event.get(): 
        #  Итерирует по списку событий, 
        if event.type == pygame.QUIT: 
            # Проверяет, пытается ли пользователь закрыть окно.
            done = True

    time = datetime.now().time()

    sec_angle = -(time.second * 6) 
    # Рассчитывает угол поворота
    nsec_img = pygame.transform.rotate(sec_img, sec_angle)
    # Поворачивает изображение секундной стрелки до рассчитанного угла.
    sec_rect = nsec_img.get_rect(center=rect.center)
    screen.blit(nsec_img, sec_rect.topleft)
    # Рисует повернутое изображение секундной стрелки

    min_angle = -(time.minute * 6)
    nmin_img = pygame.transform.rotate(min_img, min_angle)
    min_rect = nmin_img.get_rect(center=rect.center)
    screen.blit(nmin_img, min_rect.topleft)

    pygame.display.flip()
