import pygame

pygame.init()
pygame.mixer.init()
# для воспроизведения звуков.

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Player')
screen.fill('pink2')

def play_a_different_song():
    global currently_playing_song, songs, current_song_index
    next_song_index = (current_song_index + 1) % len(songs)
    #чтобы убедиться, что индекс остается в пределах диапазона плейлиста
    currently_playing_song = songs[next_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = next_song_index

def play_previous_song():
    global currently_playing_song, songs, current_song_index
    previous_song_index = (current_song_index - 1) % len(songs)
    currently_playing_song = songs[previous_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = previous_song_index

def stop_music():
    pygame.mixer.music.stop()

def play_pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

songs = ['C:/Users/aluas/Downloads/pp2_spring/lab77/musics/audio/Kazakhstan.mp3', 'C:/Users/aluas/Downloads/pp2_spring/lab77/musics/audio/Kel_kel.mp3','C:/Users/aluas/Downloads/pp2_spring/lab77/musics/audio/Yes, and.mp3', 'C:/Users/aluas/Downloads/pp2_spring/lab77/musics/audio/Unravel.mp3', 'C:/Users/aluas/Downloads/pp2_spring/lab77/musics/audio/Highway to hell.mp3']
#  Список путей к аудиофайлам треков.
current_song_index = 0

currently_playing_song = songs[current_song_index]

testFont = pygame.font.Font('C:/Users/aluas/Downloads/pp2_spring/lab77/musics/Pixeltype.ttf', 50)
# шрифт
player_surface = testFont.render("My player", False, 'pink4')
player_surface1 = testFont.render("Kazakhstan", False, 'firebrick4')
player_surface2 = testFont.render("Kel_kel", False, 'firebrick4')
player_surface3 = testFont.render("Yes, and?", False, 'firebrick4')
player_surface4 = testFont.render("Unravel", False, 'firebrick4')
player_surface5 = testFont.render("Highway to hell", False, 'firebrick4')
#  Создает поверхности для текстового отображения
player_rect = player_surface.get_rect(center = (400, 50))
player_rect1 = player_surface1.get_rect(topleft = (100, 100))
player_rect2 = player_surface2.get_rect(topleft = (100, 150))
player_rect3 = player_surface3.get_rect(topleft = (100, 200))
player_rect4 = player_surface4.get_rect(topleft = (100, 250))
player_rect5 = player_surface5.get_rect(topleft = (100, 300))
# Получает прямоугольники, охватывающие текстовые поверхности.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_pause_music()
            elif event.key == pygame.K_n:
                play_a_different_song()
            elif event.key == pygame.K_p:
                play_previous_song()
            elif event.key == pygame.K_s:
                stop_music()

    screen.blit(player_surface, player_rect)
    screen.blit(player_surface1, player_rect1)
    screen.blit(player_surface2, player_rect2)
    screen.blit(player_surface3, player_rect3)
    screen.blit(player_surface4, player_rect4)
    screen.blit(player_surface5, player_rect5)

    pygame.display.flip()

pygame.quit()