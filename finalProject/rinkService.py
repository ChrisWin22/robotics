import pygame
from rinks.nhl_rink import NHLRink
from rinks.rink import Rink
from rinks.international_rink import InternationalRink
class RinkService:

    def __init__(self):
        pass


    def drawRink(self, surface, ice_rink):
        pygame.draw.rect(ice_rink.display, [255,255,255], ice_rink.rink, border_radius=round(ice_rink.radius * ice_rink.SCALAR))
    
    def determine_rink(self, name):
        if name.upper() == "NHL":
            return NHLRink()
        elif name.lower() == "international":
            return InternationalRink()
        else:
            return Rink()