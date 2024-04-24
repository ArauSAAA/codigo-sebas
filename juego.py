import pygame

pygame.init()

ventana= pygame.display.set_mode((1280,500))

person= pygame.Vector2(ventana.get_width() /2, ventana.get_height() /2)

dt= 0

reloj= pygame.time.Clock()
correr= False

while not correr:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr = True


    ventana.fill('red')
    pygame.draw.circle(ventana, 'blue', person,40)

    key= pygame.key.get_pressed()
    if key[pygame.K_w]:
        person.y -= 300 * dt
    if key[pygame.K_s]:
        person.y += 300 * dt 
    if key[pygame.K_a]:
        person.x -= 300 * dt
    if key[pygame.K_d]:
        person.x += 300 * dt


    

    dt= reloj.tick(60) // 1000

    print(person[0])


    pygame.display.flip()