# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:02:27 2021

@author: ULVI PC
"""

import pygame
from pygame.sprite import Sprite



class Ship(Sprite):
    '''Initialazie of sheeps'''
    def __init__(self,ai_settings, screen):
        '''Download images for sip'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/13.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)

        
        # movement flags
        self.moving_right = False
        self.moving_left = False
        
        
    
    
    def update(self):
        '''update ship position'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
    
        self.rect.centerx = self.center
    
    def blitme(self):
        '''draw ship in posiction'''
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        self.center = self.screen_rect.centerx