import pygame, sys,random
import neat
import os

pygame.init()
clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
images={}
images["bg1"] = pygame.image.load("bg1.png").convert_alpha()
images["base"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()

gen=0
birdcount=0

class Bird:
    r=pygame.Rect(100,250,30,30)
    speed=0
    g=0.5
    def flap(self):
        self.speed=0
        self.speed=-10
    def gravity(self):
        #self.r.x+=5
        self.speed+=self.g
        self.r.y += self.speed
    def display(self):
        screen.blit(images["bird"],self.r)
class Pipe:
    def __init__(self,x):
        self.gap=random.randint(150, 400)
        self.rtop=pygame.Rect(x,self.gap-400,40,320)
        self.rbot=pygame.Rect(x,self.gap+100,40,500)
    def move(self):
        self.rtop.x-=4
        self.rbot.x-=4
        if self.rtop.x<-40:
            self.reposition()
    def display(self):
        screen.blit(images["pipe"],self.rbot)
        screen.blit(images["pipe"],self.rtop)
    def reposition(self):
        self.rtop.x=460
        self.rbot.x=460
        self.gap=random.randint(150, 400)
        self.rtop.y=self.gap-400
        self.rbot.y=self.gap+100

def eval_fitness(generation, config):
    global gen
    birdcount=0
    gen = gen+1
    print(gen)
    for gid, genome in generation: 
        genome.fitness = 0  #initializing fitness of a genome to 0
        net = neat.nn.FeedForwardNetwork.create(genome, config) #creating a neural network for a genome
        pipe1 = Pipe(400)
        bird = Bird() 
        score=0
        score_font=pygame.font.Font('freesansbold.ttf', 20)       
        groundx=0
        state="play"
        bird.r.y=200 
        
        while True:
            screen.fill((50,150,255))
            screen.blit(images["bg1"],[0,0])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.flap()
                        
            genome.fitness += 0.1         
            pipe1.display()
            bird.gravity()
            bird.display()
            if bird.r.colliderect(pipe1.rbot) or bird.r.colliderect(pipe1.rtop):
                state="over"
            if pipe1.rtop.x == bird.r.x:
                score=score+1
                
            if groundx < -330:
                groundx=0
            if state=="play":
                groundx-=5
                pipe1.move()
                
            if bird.r.y > 600 or bird.r.y < 0:
                state="over"
       
            
            output = net.activate((bird.r.y, pipe1.gap))   #Giving bird's y location and  gap's locaion as input to artificial neural network
            if output[0] > 0.5: #Checking the output and making the bird flap()
                bird.flap() 
                
               
            if state=="over":
               state="play"
               birdcount+=1
               break
            
            screen.blit(images["base"],[groundx,550])
            
            score_text=score_font.render("Score:"+str(score)+"  Gen:"+str(gen)+" BirdNo."+str(birdcount), False, (255,255,0)) #####
            screen.blit(score_text,[10,10])
           
            pygame.display.update()
            clock.tick(30)

    


########################################  
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,'config-feedforward.txt')  
p = neat.Population(config)
p.run(eval_fitness,7) 


  

  
    