import pygame
import math
import screen # type: ignore




#initializing pygame
pygame.init()



clock = pygame.time.Clock()


#constants initilization
screen_width = 900
screen_height = 550
grnd_speed = 8
bird_speed = 9
num_cactus = 2
game_state = False


DeadScreen = screen.deadscreen(screen_width, screen_height)


#cactus width collectin
flag = False
height = 0

#defining games
screen = pygame.display.set_mode((screen_width,screen_height))


#defining classes

class dragon(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.var = 0
        self.down_var = 0
        self.jumpCount = 0
        self.jumping = False
        self.down = False
        self.gravity = 1
        self.y_velocity = 0
        self.jump_speed = -17
        self.collection = []
        self.down_collection = []
        for i in range(1,3):
            image = pygame.image.load(f"./Assets/Dino/DinoRun{i}.png").convert_alpha()
            image = pygame.transform.scale(image,(55,55))
            self.collection.append(image)
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (self.x,self.y))

    
    def animation(self):
        if not self.jumping and not self.down:
            self.var += 0.2
            if self.var > len(self.collection):
                self.var = 0
            self.image = self.collection[math.floor(self.var)]
        elif self.down:
            self.down_move()
        

    def jump(self):

        self.jumpCount = 1
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity

        # Stop the dragon at ground level
        if self.rect.bottom >= screen_height - 98:
            self.rect.bottom = screen_height - 98
            self.y_velocity = 0
            self.jumpCount = 0
            self.jumping = False


    def jum_animation(Self):
            if  Self.jumping:
                image = pygame.image.load('./Assets/Dino/DinoJump.png')
                image = pygame.transform.scale(image,(55,55))
                Self.image = image

    def down_animation(self):
        if self.down:
            for i in range(1,3):
                image = pygame.image.load(f"./Assets/Dino/DinoDuck{i}.png").convert_alpha()
                image = pygame.transform.scale(image,(75,45))
                self.down_collection.append(image)
            self.image = self.down_collection[0]

    def down_move(self):
        if self.down:    
            self.down_var += 0.2
            if self.down_var > len(self.down_collection):
                self.down_var = 0
            self.image = self.down_collection[math.floor(self.down_var)]
    






class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x =  x
        self.y = y
        self.var = 0
        self.collection = []
        for i in range(1,3):
            image = pygame.image.load(f"./Assets/Bird/Bird{i}.png").convert_alpha()
            image = pygame.transform.scale(image,(55,55))
            self.collection.append(image)
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (self.x,self.y));  

    def animation(self):
        self.var += 0.1
        if self.var > len(self.collection):
            self.var = 0
        self.image = self.collection[math.floor(self.var)]


    def move(self,speed):
        self.rect.x -= speed
        if self.rect.x < -self.rect.width:
            self.rect.x = screen_width
        
        


class ground(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.count = 0
        self.image =  pygame.image.load("./Assets/Other/Track.png")
        self.rect = self.image.get_rect(topleft = (self.x , self.y))
        self.width = self.image.get_width()

    def animation(self,x):
        self.rect.x -=x
        if self.rect.x < -self.width:
            self.rect.x = screen_width


class cloud(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("./Assets/Other/Cloud.png")
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        self.width = self.image.get_width()

    def animation(self,speed):
        self.rect.x -= speed
        if self.rect.x <  -self.width:
            self.rect.x = screen_width


class catcus(pygame.sprite.Sprite):
    def __init__(self, x,y,n):
        super().__init__() 
        self.x = x
        self.y = y
        self.i = n
        self.image = pygame.image.load(f"./Assets/Cactus/Cactus{self.i}.png")
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        self.height = self.image.get_height()


        
    
    def animation(self,speed):
        self.rect.x -= speed
        if(self.rect.x <= -self.rect.width):
            self.rect.x = self.rect.x + screen_width * 3
            





#class in constants
Ground1 = ground(0,screen_height-115)
Ground2 = ground(Ground1.width,screen_height-115)
Dragon = dragon((screen_width//2)-225,screen_height-147)
Cloud = cloud(screen_width//3,screen_height//4)
Bird = bird(screen_width, screen_height - 193)


cactus_group_list = pygame.sprite.Group()
dx = screen_width

for i in range(1,7):
    Catcus = catcus(dx,screen_height-173,i)
    dx += screen_width//2
    cactus_group_list.add(Catcus)








#adding class in groups
group = pygame.sprite.Group()
group.add(Dragon)
group.add(Ground1,Ground2)
group.add(Cloud)
group.add(Bird)





run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            

    # Check if a key is pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Dragon.jumpCount == 0 :
               Dragon.jumping = True
               Dragon.y_velocity = Dragon.jump_speed
               Dragon.jum_animation()
               game_state = True


            if event.key == pygame.K_DOWN:
                Dragon.down = True
                Dragon.down_animation()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                Dragon.down = False
    
               
               
                


    screen.fill((255,255,255))
    


    print(game_state)   

    #drawing
    if game_state:
        group.draw(screen)
        
        Ground1.animation(grnd_speed)
        Ground2.animation(grnd_speed)
        Dragon.animation()
        Bird.move(bird_speed)
        Bird.animation()
        Cloud.animation(grnd_speed)
        cactus_group_list.draw(screen)


        for i in cactus_group_list:
            i.animation(grnd_speed)


        for i in cactus_group_list:
            if pygame.sprite.collide_rect(i,Dragon):
                print("Game Over")
                game_state = False




        if Dragon.jumping:
            Dragon.jump()
    

    clock.tick(60)
    pygame.display.update()


pygame.quit()