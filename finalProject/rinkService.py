import pygame
from rinks.nhl_rink import NHLRink
from rinks.rink import Rink
from rinks.international_rink import InternationalRink
class RinkService:

    def __init__(self):
        pass


    def drawRink(self, ice_rink):
        pygame.draw.rect(ice_rink.display, [255,255,255], ice_rink.rink, border_radius=round(ice_rink.radius * ice_rink.SCALAR))
    
    def draw_dock(self, ice_rink, left, top):
        pygame.draw.rect(ice_rink.display, [125,125,125], pygame.Rect(left, top, round(4.7 * ice_rink.SCALAR), round(2.3*ice_rink.SCALAR)))
    
    def determine_rink(self, name):
        if name.upper() == "NHL":
            return NHLRink()
        elif name.lower() == "international":
            return InternationalRink()
        else:
            return Rink()