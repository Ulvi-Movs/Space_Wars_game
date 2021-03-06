# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 10:41:58 20

@author: ULVI PC
"""

class Settings():
    '''Save all setings of game'''
    def __init__(self):
        '''init static settings'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135,206,250)
        
        # ship settings
        self.ship_limit = 3
        
        
        # aliens settings
        self.fleet_drop_speed = 5
        
        
        #bullets setings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        
        #scaling settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        '''init dinamic settings'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
    
