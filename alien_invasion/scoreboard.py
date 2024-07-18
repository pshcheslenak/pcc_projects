import pygame.font


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                self.tect_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.reght = self.screen_rect.reght - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw scores to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
