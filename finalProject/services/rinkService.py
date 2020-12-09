import pygame
from models.rinks.nhl_rink import NHLRink
from models.rinks.rink import Rink
from models.rinks.international_rink import InternationalRink
class RinkService:

    def __init__(self):
        pass


    def drawRink(self, ice_rink):
        # Rink
        pygame.draw.rect(ice_rink.display, [0,0,255], ice_rink.rinkBorder, border_radius=round(ice_rink.radius * ice_rink.SCALAR))
        pygame.draw.rect(ice_rink.display, [255,255,255], ice_rink.rink, border_radius=round(ice_rink.radius * ice_rink.SCALAR))
        
        # Lines
        pygame.draw.line(ice_rink.display, [255,0,0], (ice_rink.rink.center[0], ice_rink.rink.center[1] - ice_rink.rink_y * ice_rink.SCALAR/2), (ice_rink.rink.center[0], ice_rink.rink.center[1] + ice_rink.rink_y * ice_rink.SCALAR/2))
        
        pygame.draw.line(ice_rink.display, [255,0,0], (ice_rink.rink.center[0] - (ice_rink.rink_x) * 4, ice_rink.rink.center[1] - ice_rink.rink_y * ice_rink.SCALAR/2), (ice_rink.rink.center[0] - (ice_rink.rink_x) * 4, ice_rink.rink.center[1] + ice_rink.rink_y * ice_rink.SCALAR/2))
        
        pygame.draw.line(ice_rink.display, [255,0,0], (ice_rink.rink.center[0] + (ice_rink.rink_x) * 4, ice_rink.rink.center[1] - ice_rink.rink_y * ice_rink.SCALAR/2), (ice_rink.rink.center[0] + (ice_rink.rink_x) * 4, ice_rink.rink.center[1] + ice_rink.rink_y * ice_rink.SCALAR/2))
        
        pygame.draw.line(ice_rink.display, [0,0,255], (ice_rink.rink.center[0] - (ice_rink.rink_x) * 1, ice_rink.rink.center[1] - ice_rink.rink_y * ice_rink.SCALAR/2), (ice_rink.rink.center[0] - (ice_rink.rink_x) * 1, ice_rink.rink.center[1] + ice_rink.rink_y * ice_rink.SCALAR/2))
        
        pygame.draw.line(ice_rink.display, [0,0,255], (ice_rink.rink.center[0] + (ice_rink.rink_x) * 1, ice_rink.rink.center[1] - ice_rink.rink_y * ice_rink.SCALAR/2), (ice_rink.rink.center[0] + (ice_rink.rink_x) * 1, ice_rink.rink.center[1] + ice_rink.rink_y * ice_rink.SCALAR/2))
        
        circleRadius = 40
        circuleInnerRadius = 38
        dotRadius = 5
        
        # Center Circle
        pygame.draw.circle(ice_rink.display, [0, 0, 255], ice_rink.rink.center, circleRadius)
        pygame.draw.circle(ice_rink.display, [255, 255, 255], ice_rink.rink.center, circuleInnerRadius)
        pygame.draw.circle(ice_rink.display, [0, 0, 255], ice_rink.rink.center, dotRadius)
        
        # Top Left Circle
        pygame.draw.circle(ice_rink.display, [255, 0, 0], (ice_rink.rink.center[0] - 160, ice_rink.rink.center[1] - 70), circleRadius)
        pygame.draw.circle(ice_rink.display, [255, 255, 255], (ice_rink.rink.center[0] - 160, ice_rink.rink.center[1] - 70), circuleInnerRadius)
        pygame.draw.circle(ice_rink.display, [255, 0, 0], (ice_rink.rink.center[0] - 160, ice_rink.rink.center[1] - 70), dotRadius)
        
        # Bottom Left Circle
        pygame.draw.circle(ice_rink.display, [255, 0, 0], (ice_rink.rink.center[0] - 160, ice_rink.rink.center[1] + 70), circleRadius)
        pygame.draw.circle(ice_rink.display, [255, 255, 255], (ice_rink.rink.center[0] - 160, ice_rink.rink.center[1] + 70), circuleInnerRadius)
        pygame.draw.circle(ice_rink.display, [255, 0, 0], (ice_rink.rink.center[0] - 160, ice_rink.rink.center[1] + 70), dotRadius)
        
        # Top Right Circle
        pygame.draw.circle(ice_rink.display, [255, 0, 0], (ice_rink.rink.center[0] + 160, ice_rink.rink.center[1] - 70), circleRadius)
        pygame.draw.circle(ice_rink.display, [255, 255, 255], (ice_rink.rink.center[0] + 160, ice_rink.rink.center[1] - 70), circuleInnerRadius)
        pygame.draw.circle(ice_rink.display, [255, 0, 0], (ice_rink.rink.center[0] + 160, ice_rink.rink.center[1] - 70), dotRadius)
        
        # Bottom Right Circle
        pygame.draw.circle(ice_rink.display, [255, 0, 0], (ice_rink.rink.center[0] + 160, ice_rink.rink.center[1] + 70), circleRadius)
        pygame.draw.circle(ice_rink.display, [255, 255, 255], (ice_rink.rink.center[0] + 160, ice_rink.rink.center[1] + 70), circuleInnerRadius)
        pygame.draw.circle(ice_rink.display, [255, 0, 0], (ice_rink.rink.center[0] + 160, ice_rink.rink.center[1] + 70), dotRadius)
    
        
        
        
    def draw_dock(self, ice_rink, left, top):
        pygame.draw.rect(ice_rink.display, [125,125,125], pygame.Rect(left, top, round(4.7 * ice_rink.SCALAR), round(2.3*ice_rink.SCALAR)))
    
    def determine_rink(self, name):
        if name.upper() == "NHL":
            return NHLRink()
        elif name.lower() == "international":
            return InternationalRink()
        else:
            return Rink()