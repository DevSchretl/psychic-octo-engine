import pygame
import random
import math

if __name__ == '__main__':
    width = 800
    height = 800
    run = True
    gridCount = 0
    x = width / 2 - 400
    y = height / 2 - 400
    X = 0
    Y = 0
    on = False
    spawned = False
    noise = 0
    xPos = 0
    yPos = 0
    xSpeed = 0
    ySpeed = 0
    Night: int = 0
    time = 0
    health = 100
    spawnTimer = 0

    # INVENTORY
    wood = 0
    sticks = 0
    fish = 0
    stone = 0
    iron = 0
    diamonds = 0
    dirt = 0
    woodenSword = 0
    woodenPic = 0
    stoneSword = 0
    stonePic = 0
    ironSword = 0
    ironPic = 0
    diamondSword = 0
    diamondPic = 0
    ironArmour = 0
    diamondArmour = 0






    screen = pygame.display.set_mode((width, height))
    class Square:
        def __init__(self, xPos, yPos, height, near, heightNear, colour, type):
            self.xPos = xPos
            self.yPos = yPos
            self.height = height
            self.near = near
            self.heightNear = heightNear
            self.colour = colour
            self.type = type


    class Enemies:
        def __init__(self, xPos, yPos, xSpeed, ySpeed, colour, health, speed, cooldown):
            self.xPos = xPos
            self.yPos = yPos
            self.xSpeed = xSpeed
            self.ySpeed = ySpeed
            self.colour = colour
            self.health = health
            self.speed = speed
            self.cooldown = cooldown

squareList: list = []
enemyList: list = []

while run:
    spawnTimer += 1
    if Night > 0:
        if spawnTimer >= 400/Night:
            spawnSide = random.randint(1, 4)
            if spawnSide == 1:
                spawnX = 0 - xPos
                spawnY = random.randint(1 - yPos, 800 - yPos)
            elif spawnSide == 2:
                spawnX = 1200  - xPos
                spawnY = random.randint(1 - yPos, 800 - yPos)
            elif spawnSide == 3:
                spawnY = 0 - yPos
                spawnX = random.randint(1 - xPos, 800 - xPos)
            elif spawnSide == 4:
                spawnY = 900 - yPos
                spawnX = random.randint(1 - xPos, 800 - xPos)

            enemyList.append(Enemies(spawnX, spawnY, 0, 0, (0, 255, 0), 50, 2, 50))
            spawnTimer = 0





    if x >= (width / 2 + 400):
        y += 25
        x = width / 2 - 400
    if y <= (height / 2 + 400):
        x += 25
        o = random.randint(1, 10)
        squareList.append(Square(x, y, o, 0, 0, (0, 0, 0), "None"))
    else:
        spawned = True

    if spawned:
        if noise <= 2:
            for obj in squareList:
                for i in squareList:
                    delX = obj.xPos - i.xPos
                    delY = obj.yPos - i.yPos
                    hypo = math.sqrt(delX ** 2 + delY ** 2)
                    if hypo < 100:
                        obj.near += 1
                        obj.heightNear += i.height
            for obj in squareList:
                obj.height = obj.heightNear / obj.near
                if obj.height > 5.55 and obj.height <= 5.9:
                    tree = random.randint(1, 6)
                    if tree == 1:
                        obj.type = "Tree"
                else:
                    obj.type = False
                if obj.height <= 5.25:
                    obj.colour = (0, 0, 130)
                    obj.type = "Water"
                elif obj.height <= 5.45:
                    obj.type = "Sand"
                    obj.colour = (255, 255, 0)
                elif obj.height <= 6:
                    if obj.type != "Tree":
                        obj.type = "Grass"
                    obj.colour = (0, 160, 0)
                else:
                    obj.colour = (100, 100, 100)
                    obj.type = "Rock"
            noise += 1

        pygame.time.delay(10)
        time += 1
        if time >= 3000:
            Night += 1
            print("Wave", Night - 1, "has started!")
            time = 0
        screen.fill((0, 0, 0))
        for obj in squareList:
            if obj.height <= 5.25 and (obj.type == "Sand" or obj.type == "Water"):
                obj.colour = (0, 0, 130)
                obj.type = "Water"
            elif obj.height <= 5.25:
                obj.colour = (211, 211, 211)
                obj.type = "Stone"
            if obj.height <= 0:
                obj.type = "Bedrock"
                obj.colour = (25, 25, 25)
            if obj.type == "Grass":
                obj.colour = (0, 160, 0)
                if random.randint(1, 100000) == 1:
                    obj.type = "Tree"
            if obj.type == "Dirt":
                obj.colour = (139, 69, 19)
            (R, G, B) = obj.colour
            pygame.draw.rect(screen, (R / (Night/2 + 1), G / (Night/2 + 1), B / (Night/2 + 1)), pygame.Rect(obj.xPos - xPos, obj.yPos - yPos, 25, 25))
            if obj.type == "Tree":
                pygame.draw.rect(screen, (0, 75 / (Night/2 + 1), 0), pygame.Rect(obj.xPos + 5 - xPos, obj.yPos + 5 - yPos, 15, 15))

        player = pygame.draw.circle(screen, (255, 0, 0), (width / 2, height / 2), 10)
        hitBox = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width / 2, height / 2, 1, 1))
        #attack = pygame.draw.circle(screen, (255, 255, 255), (X + 400, Y + 400), 35, 0)
        for obj in enemyList:
            obj.colour = (4.8 * (-obj.cooldown + 50), 255/(1 + Night/4), 4.8 * (-obj.cooldown + 50))
            pygame.draw.circle(screen, obj.colour, (obj.xPos, obj.yPos), 15, 30)
            enemyXDiff = obj.xPos - 400
            enemyYDiff = obj.yPos - 400
            enHypo = math.sqrt(enemyXDiff ** 2 + enemyYDiff ** 2)
            if obj.speed != 0:
                Div = enHypo / obj.speed
                obj.xSpeed = enemyXDiff / -Div
                obj.ySpeed = enemyYDiff / -Div
            else:
                obj.xSpeed = 0
                obj.ySpeed = 0
            obj.xPos += obj.xSpeed - xSpeed
            obj.yPos += obj.ySpeed - ySpeed
            if obj.speed < 0:
                obj.cooldown -= 1
                if obj.cooldown <= 0:
                    obj.speed = 2 + (Night/10)
                    obj.cooldown = 50/(1 + Night/5)
            elif math.sqrt((obj.xPos - 400) ** 2 + (obj.yPos - 400) ** 2) <= 20:
                obj.speed = 0
                obj.cooldown -= 1
                if obj.cooldown <= 0:
                    if diamondArmour == 1:
                        health -= 2.5
                    elif ironArmour == 1:
                        health -= 5
                    else:
                        health -= 10
                    print("You got hit!")
                    print("Health:", health)
                    obj.cooldown = 50/(1 + Night/5)
            else:
                obj.cooldown = 50/(1 + Night/5)
                obj.speed = 2 + (Night/10)

        if health <= 0:
            print("You died!")
            pygame.time.delay(1000)
            run = False
                # take damage


        pygame.display.update()

        #craft with keys
        # 1 - 3 = wood, iron, diamond sword
        # 4 - 5 = iron + diamond armor
        # 6 = bow
        # 7 = wall
        # 8 = door
        # pickaxes to mine ores

        xPos += xSpeed
        yPos += ySpeed


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print("Pressed")
                xDiff = mouseX - 400
                yDiff = mouseY - 400
                if xDiff == 0 and yDiff == 0:
                    xDiff = random.randint(1, 100)
                    yDiff = random.randint(1, 100)
                else:
                    mouseHypo = math.sqrt(xDiff ** 2 + yDiff ** 2)
                    Div = mouseHypo / 30
                    X = xDiff / Div
                    Y = yDiff / Div

                for obj in enemyList:
                    enemyXDiff = X + 400 - obj.xPos
                    enemyYDiff = Y + 400 - obj.yPos
                    enHypo = math.sqrt(enemyXDiff ** 2 + enemyYDiff ** 2)
                    if enHypo <= 50:
                        obj.speed = -4
                        obj.cooldown = 20
                        if diamondSword >= 1:
                            obj.health -= 30
                        elif ironSword >= 1:
                            obj.health -= 25
                        elif stoneSword >= 1:
                            obj.health -= 20
                        elif woodenSword >= 1:
                            obj.health -= 15
                        else:
                            obj.health -= 5
                        if obj.health <= 0:
                            enemyList.remove(obj)
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    ySpeed += 2
                if event.key == pygame.K_s:
                    ySpeed -= 2
                if event.key == pygame.K_a:
                    xSpeed += 2
                if event.key == pygame.K_d:
                    xSpeed -= 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ySpeed -= 2
                if event.key == pygame.K_s:
                    ySpeed += 2
                if event.key == pygame.K_a:
                    xSpeed -= 2
                if event.key == pygame.K_d:
                    xSpeed += 2
                if event.key == pygame.K_SPACE:
                    for obj in squareList:
                        block = pygame.draw.rect(screen, obj.colour,
                                                 pygame.Rect(obj.xPos - xPos, obj.yPos - yPos, 25, 25))
                        if obj.type == "Tree":
                            pygame.draw.rect(screen, (0, 75, 0),
                                             pygame.Rect(obj.xPos + 5 - xPos, obj.yPos + 5 - yPos, 15, 15))
                        if hitBox.colliderect(block):
                            if obj.type == "Tree":
                                obj.type = "Grass"
                                print("Tree harvested")
                                print("+4 wood")
                                print("+2 sticks")
                                wood += 4
                                sticks += 2

                            elif obj.type == "Grass" or obj.type == "Dirt":
                                print("Dirt dug")
                                print("+1 dirt")
                                obj.type = "Dirt"
                                dirt += 1
                                obj.height -= 0.15

                            elif obj.type == "Rock" or obj.type == "Stone":
                                if woodenPic == 1:
                                    if ironPic == 1:
                                        i = random.randint(1, 8 / (diamondPic + 1))
                                        if i == 1:
                                            print("Diamond found!")
                                            diamonds += 1
                                    if stonePic == 1:
                                        i = random.randint(1, 4 / (diamondPic + 1))
                                        if i == 1:
                                            print("Iron found!")
                                            iron += 1
                                    print("Stone mined")
                                    print("+1 stone")
                                    obj.type = "Stone"
                                    stone += 1
                                    obj.height -= 0.15
                                else:
                                    print("You need a wooden pickaxe to mine this")

                            elif obj.type == "Sand":
                                obj.height -= 0.15
                                print("Sand dug")
                            elif obj.type == "Water":
                                fish = random.randint(1, 4)
                                if fish == 1:
                                    print("You caught a fish!")
                                    fish += 1
                                else:
                                    print("You caught nothing")

                            elif obj.type == "Bedrock":
                                print("You reached the bottom of the world!")

                if event.key == pygame.K_1:
                    if woodenSword < 1:
                        if wood >= 2 and sticks >= 1:
                            print("You crafted a wooden sword! (Damage: 15)")
                            wood -= 2
                            sticks -= 1
                            woodenSword += 1
                            print("Wood remaining", wood)
                            print("Sticks remaining", sticks)
                        else:
                            print("You need 2 wood and a stick to craft a wooden sword")
                    else:
                        print("You already have a wooden sword")

                if event.key == pygame.K_2:
                    if woodenPic < 1:
                        if wood >= 3 and sticks >= 2:
                            print("You crafted a wooden pickaxe (Mines stone)")
                            wood -= 3
                            sticks -= 2
                            woodenPic += 1
                            print("Wood remaining", wood)
                            print("Sticks remaining", sticks)
                        else:
                            print("You need 3 wood and two sticks to craft a wooden pickaxe")
                    else:
                        print("You already have a wooden pickaxe")

                if event.key == pygame.K_3:
                    if stoneSword < 1:
                        if stone >= 2 and sticks >= 1:
                            print("You crafted a stone sword (Damage: 20)")
                            stone -= 2
                            sticks -= 1
                            stoneSword += 1
                            print("Stone remaining", stone)
                            print("Sticks remaining", sticks)
                        else:
                            print("You need 2 stone and one stick to craft a stone sword")
                    else:
                        print("You already have a stone pickaxe")

                if event.key == pygame.K_4:
                    if stonePic < 1:
                        if stone >= 3 and sticks >= 2:
                            print("You crafted a stone pickaxe (Chance of mining iron)")
                            stone -= 3
                            sticks -= 2
                            stonePic += 1
                            print("Stone remaining", stone)
                            print("Sticks remaining", sticks)
                        else:
                            print("You need 3 stone and two sticks to craft a stone pickaxe")
                    else:
                        print("You already have a stone pickaxe")

                if event.key == pygame.K_5:
                    if ironSword < 1:
                        if iron >= 2 and sticks >= 1:
                            print("You crafted a iron sword (Damage: 25)")
                            iron -= 2
                            sticks -= 1
                            ironSword += 1
                            print("Iron remaining", iron)
                            print("Sticks remaining", sticks)
                        else:
                            print("You need 2 iron and one stick to craft a iron sword")
                    else:
                        print("You already have a iron pickaxe")

                if event.key == pygame.K_6:
                    if ironPic < 1:
                        if iron >= 3 and sticks >= 2:
                            print("You crafted a iron pickaxe (Chance of mining diamonds)")
                            iron -= 3
                            sticks -= 2
                            ironPic += 1
                            print("Iron remaining", iron)
                            print("Sticks remaining", sticks)
                        else:
                            print("You need 3 iron and two sticks to craft a iron pickaxe")
                    else:
                        print("You already have a iron pickaxe")

                if event.key == pygame.K_7:
                    if diamondSword < 1:
                        if diamonds >= 2 and sticks >= 1:
                            print("You crafted a diamond sword (Damage: 30)")
                            diamonds -= 2
                            sticks -= 1
                            diamondSword += 1
                            print("Diamonds remaining", diamonds)
                            print("Sticks remaining", sticks)
                        else:
                            print("You need 2 diamonds and one stick to craft a diamond sword")
                    else:
                        print("You already have a diamond pickaxe")

                if event.key == pygame.K_8:
                    if diamondPic < 1:
                        if diamonds >= 3 and sticks >= 2:
                            print("You crafted a diamond pickaxe (Higher chance of finding ores)")
                            diamonds -= 3
                            sticks -= 2
                            diamondPic += 1
                            print("Diamonds remaining", diamonds)
                            print("Sticks remaining", sticks)
                        else:
                            print("You need 3 diamonds and two sticks to craft a diamond pickaxe")
                    else:
                        print("You already have a diamond pickaxe")

                if event.key == pygame.K_9:
                    if ironArmour < 1:
                        if iron >= 15:
                            print("You crafted a iron armour (Blocks 50% of damage)")
                            iron -= 15
                            ironArmour += 1
                            print("Iron remaining:", iron)
                        else:
                            print("You need 15 iron to craft iron armour")
                    else:
                        print("You already have iron armour")

                if event.key == pygame.K_0:
                    if diamondArmour < 1:
                        if diamonds >= 15:
                            print("You crafted diamond armour (Blocks 75% of damage)")
                            diamonds -= 15
                            diamondArmour += 1
                            print("Diamonds remaining", diamonds)
                        else:
                            print("You need 15 diamonds  to craft diamond armour")
                    else:
                        print("You already have diamond armour")


        pygame.display.update()