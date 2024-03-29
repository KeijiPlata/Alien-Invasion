# Alien Invasion

# importing the packages needed
import sys
import pygame
from save_read_highscore import ReadWriteHs

from time import sleep

# import the settings
from settings import Settings

# import ship
from ship import Ship
from bullet import Bullet
from game_stats import GameStats    
from alien import Alien
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """manage game assets and behavior"""

    def __init__(self):
        """Initializing the screen/form"""
        pygame.init()

        # creating instance for the class Settings
        self.settings = Settings()

        # Full screen for the game
        # get the size of the screen
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_height=self.screen.get_rect().height
        self.settings.screen_width=self.screen.get_rect().width

        # create an instance to store game
        self.stats = GameStats(self)

        # create an instance for reading and writing text files
        self.rwhs = ReadWriteHs(self)

        # create instance for game scoreboard
        self.sb = Scoreboard(self)

        # make the play button
        self.play_button = Button(self, "Play")

        # make the difficulty buttons
        self._difficulty_buttons()

        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Alien Invasion")

        # creating instance for for class Ship
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # create alien
        self._create_fleet()

    def _difficulty_buttons(self):
        """create difficulty buttons"""
        self.easy_button = Button(self, "Easy")
        self.medium_button = Button(self, "Medium")
        self.hard_button = Button(self, "Hard")

        self.easy_button.rect.top = (
            self.play_button.rect.top + 1.5*self.play_button.rect.height)
        self.easy_button._update_msg_position()

        self.medium_button.rect.top = (
            self.easy_button.rect.top + 1.5*self.easy_button.rect.height)
        self.medium_button._update_msg_position()

        self.hard_button.rect.top = (
            self.medium_button.rect.top + 1.5*self.medium_button.rect.height)
        self.hard_button._update_msg_position()

    def _check_difficulty_button(self, mouse_pos):
        """when the user click the button, change difficulty"""
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)

        if easy_button_clicked:
            self.settings.difficulty_level = "easy"
        elif medium_button_clicked:
            self.settings.difficulty_level = "medium"
        elif hard_button_clicked:
            self.settings.difficulty_level = "hard"



    def _ship_hit(self):
        """respond to the ship being hit"""

        if self.stats.ship_left > 0:
            # decrement ship left
            self.stats.ship_left -= 1
            self.sb.prep_ships()

            # get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)



    def _create_fleet(self):
        """Create the fleet of aliens"""
        # get the alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        # to know the available space, we need to get the width of the 
        # screen and the rect of the alien
        # since we need a margin in both side of screen, we have to minus it
        # to the screen size. the margin size is one alien width
        
        available_space_x = self.settings.screen_width - (2 * alien_width)

        # to determine the number of aliens we can fit in the screen
        # we havve to get the available space divide (// floor division)
        # 2 * alien width because we need space between the alien ships
        # so we need the twice of the width
        number_aliens_x = available_space_x // (2 * alien_width)

        # get the ship height
        ship_height = self.ship.rect.height

        # to know the row, we need to know first the available height
        # to calculate it, first we need to get the screen height. we place
        # margin to the top and bottom of the screen according to the height 
        # of the alien. 1 alien height to the top and 2 alien height from the
        # bottom which makes it 3, then we need also to get the height of our 
        # ship and minus it to the screen height
        available_space_y = (self.settings.screen_height - (3 * alien_height)
                             - ship_height)
        
        # to get the number of rows, we need to divide the available space
        # to the actual alien height and another alien height for the margin
        # below it which makes it 2.
        number_rows = available_space_y // (2*alien_height)

        # we will create new alien base on how many number of alien is
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
           

    def _create_alien(self, alien_number, row_number):
        """create an alien and place it in a row"""
         # create an alien and place it in row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # alien_width is the size of the alien. (2 * alien_width) is the  
        # margin left and right for the ship and we need to 
        # multiply by the alien_number to know where he can be placed(position).
        alien.x = alien_width + 2 * alien_width * alien_number

        # place to the rect
        alien.rect.x = alien.x

        # starts with the actual height of alien. We put two
        # margin so we multiply by 2 alien height, to define the position
        # we multipy it by the which number of row
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

        # add to the group
        self.aliens.add(alien)

    def _check_aliens_bottom(self):
        """check if the alien reach the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # the ship is hit
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """respond if the alien reach the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

        
    def run_game(self):
        """Loop for the game"""
        while True:
            self._checks_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
   
    def _update_aliens(self):
        """
        update the position of aliens fleet and checks if 
        the alien is in the edge of the screen
        """
        self._check_fleet_edges()
        self.aliens.update()

        # look for alien and ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()
        

    def _update_bullets(self):
        """updating position of bullets and delete the old ones """
        # updates the bullet position
        self.bullets.update()
        
        # we need to delete the bullets so it will not consume ram
        # length of the bullets in copy() method
        # if the bullets is outside the rect, it will delete that bullet
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
         """Respond to bullet alien collisions"""
         # refactor the code 
         collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
         
         # if bullet collide with the alien, it will store the score
         
         if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

            # start new level
            self.start_new_level()
        
        
        
    def start_new_level(self):
        """Start a new level"""
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
        
    def _checks_events(self):
        """Respond to kepresses adn mouse events"""
        # monitor in the player wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rwhs.write_highscore()
                sys.exit()
            # checks for keypress
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_difficulty_button(mouse_pos)

    def _start_game(self):
         """reset the game and start it again"""
         self.stats.game_active = True

         #reset game stats
         self.stats.reset_stats()

         # delete remaining aliens and bullets
         self.aliens.empty()
         self.bullets.empty()

         # create new alient and center the ship
         self._create_fleet()
         self.ship.center_ship()

         # hide the mouse cursor
         pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Start an new game when player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self._start_game()

            # restart the score
            self.stats.reset_stats()

            # prepare the level, ship and score when button clicked
            self.sb.prep_image()

               

    def _check_keydown_events(self, event):
        """ Respond to keypress """
        if event.key ==  pygame.K_RIGHT:
            # move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move the shipt to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.rwhs.write_highscore()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            # start the game and if the game is started,
            # it cannot be pushed again unless false
            if not self.stats.game_active:
                self._start_game()
    
    def _fire_bullet(self):
        """Create a new bullet and add it to bullet group """
        # the if statement limits the bullets to 3
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _check_keyup_events(self, event):
        """ Respond to key release """
        if event.key ==  pygame.K_RIGHT:
            # if the user release his finger from the key
            # stop moving left
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # if the user release his finger from the key
            # stop moving left
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images, flip to the new screen"""
        # bgcolor
        self.screen.fill(self.settings.bg_color)

        # position for the ship
        self.ship.blitme()

        # draw the group bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # draw the aliens to the screen
        self.aliens.draw(self.screen)

        # draw the score information on top right
        self.sb.show_score()

        # draw the button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
            
        # screen
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, run the game
    ai = AlienInvasion()
    ai.run_game()