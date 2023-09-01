import pygame, sys
from bullet import Bullet
from alien import Alien
import time

def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():  # окно во время всех событий
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            if event.key == pygame.K_LEFT:
                gun.mleft = False

def update(bg_color, screen, stats, sc, gun, aliens, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, aliens, bullets):
    """обновить пизицию пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collision:
        stats.score += 10
        sc.image_score()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)

def gun_kill(stats, screen, gun, aliens, bullets):
    """столкновение пушки и пришельца"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_aliens(stats, screen, gun, aliens, bullets):
    """обновляет позицию пришельца"""
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, gun, aliens, bullets)
    aliens_check(stats, screen, gun, aliens, bullets)

def aliens_check(stats, screen, gun, aliens, bullets):
    """проверка на край экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, aliens, bullets)
            break

def create_army(screen, aliens):
    """создание армии пришельцев"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for row_number in range (number_alien_y):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number

            aliens.add(alien)