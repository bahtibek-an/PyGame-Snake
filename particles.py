import random
import pygame 


window_height = 800
window_width = 1000
screen = pygame.display.set_mode((window_width, window_height))
pygame.init()

x = window_width / 4
y = window_height / 4
vy = -10
vx = 10
gravity = 1.5

    







while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.time.delay(100)
    screen.fill((0, 0, 0))

    
    

#     Particle.prototype.draw = function() {
#   this.x += this.vx;
#   this.y += this.vy;

#   // Adjust for gravity
#   this.vy += settings.gravity;

#   // Age the particle
#   this.life++;

#   // If Particle is old, remove it
#   if (this.life >= settings.maxLife) {
#     delete particles[this.id];
#   }

#   // Create the shapes
#   context.clearRect(settings.leftWall, settings.groundLevel, canvas.width, canvas.height);
#   context.beginPath();
#   context.fillStyle="#ffffff";
#   context.arc(this.x, this.y, settings.particleSize, 0, Math.PI*2, true); 
#   context.closePath();
#   context.fill();
# }

    pygame.display.update() 