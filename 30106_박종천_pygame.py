#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pygame


# In[2]:


import sys


# In[3]:


import pygame


# In[4]:


from pygame.locals import QUIT, Rect 


# In[5]:


r =Rect(30, 20, 60, 40)


# In[6]:


r.width


# In[7]:


r.bottomleft


# In[8]:


r.center


# In[9]:


r.bottomleft


# In[10]:


r.width


# In[11]:


r.move(100, 100)


# In[12]:


pygame.init()


# In[13]:


SURFACE = pygame.display.set_mode((800,600))
pygame.display.set_caption('Game Window')


# In[3]:


import sys
import pygame
from pygame.locals import QUIT, Rect 

pygame.init()

SURFACE = pygame.display.set_mode((800,600))
pygame.display.set_caption

def main() :
    
    while True:
        SURFACE.fill((255,255,255))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            pygame.draw.rect(SURFACE, (255,0,0), (100, 100, 200, 200))
            pygame.draw.rect(SURFACE, (0,255,0), (50, 50, 100, 100),3)
            pygame.draw.rect(SURFACE, (0,0,255), ((100, 80), (80, 50)))
                
            rect0 = Rect(200, 60, 140, 80)
            pygame.draw.rect(SURFACE, (255,255,0), rect0)
            
            pygame.draw.line(SURFACE, (255,0,0), (30, 300), (200, 80))
            pygame.draw.line(SURFACE, (0,0,255), (40, 400), (200, 150), 15)
            pygame.draw.line(SURFACE, (0,255,0), (50, 500),(250, 200), 30)
            
            pygame.draw.circle(SURFACE, (255,0,255), (450, 500), 10)
            pygame.draw.circle(SURFACE, (0,255,0), (550,500), 20)
            pygame.draw.circle(SURFACE, (255,255,0), (650, 500), 30)
                
            pygame.display.update()
                
if __name__=='__main__':
    main()


# In[6]:


import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT,K_RIGHT, K_UP, K_DOWN

pygame.init()
pygame.key.set_repeat(5,5)

SURFACE = pygame.display.set_mode((800,600))
pygame.display.set_caption('Game Window')

def main() :
    logo = pygame.image.load('pythonlogo.jpg')
    pos = [200, 150]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN :
                if event.key == K_LEFT :
                    pos[0] -= 5
                elif event.key == K_RIGHT :
                    pos[0] += 5
                elif event.key == K_UP :
                    pos[1] -= 5
                elif event.key == K_DOWN :
                    pos[1] += 5
                    
            pos[0] = pos[0] % 400
            pos[1] = pos[1] % 300
            
            SURFACE.fill((255,255,255))
        
            rect = logo.get_rect()
            rect.center = pos
        
            SURFACE.blit(logo, rect)
        
            pygame.display.update()
                    
if __name__=='__main__':
    main()               

