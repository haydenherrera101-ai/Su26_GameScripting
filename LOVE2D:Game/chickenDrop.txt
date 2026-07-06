--Hayden Herrera
--07/02/2026
--Rework Chicken Drop from In Class, Find your own sprites and substitute them for the chickens.
--Add in a powerup that should randomly spawn at a static position (not moving).
--You can either have the player click it OR have the chickens collide with it.
--The powerup can do anything. Some ideas are: speed up or down, size change, gravity change, color change, etc.


-- start debugger (special to VsCode) if the second argument is "debug"
if arg[2] == "debug" then
    require("lldebugger").start()
end

-- This function is called once at the beginning of the game. It is used to set up the game.
function love.load()
    chickenImage = love.graphics.newImage("chimpkin.png")
    eggImage = love.graphics.newImage("egg.png")

    chickenspeed = 200
    normalSpeed = 200
    slowSpeed = 100

    eggTimer = 10
    eggActive = false

    powerupTimer = 0

    chicken = {
        x = {},
        y = {},
        scale = 0.3
    }

    for i = 1, 5 do
        chicken.x[i] = math.random(
        0, love.graphics.getWidth() - chickenImage:getWidth() * chicken.scale)
        chicken.y[i] = math.random(
            chickenImage:getHeight(),
            chickenImage:getHeight() * 2)
            * -1
    end

    egg = {
        x = 0,
        y = 0,
        scale = 0.3
    }
end

-- This function is called when a mouse button is pressed.
-- x, y are the mouse coordinates.
-- button is the button pressed, istouch is true for touch events.
-- presses is the number of presses.
function love.mousepressed(x, y, button, istouch, presses)

    if button == 1 then

        print("Mouse pressed at: " .. x .. ", " .. y)


        if eggActive
        and x >= egg.x
        and x <= egg.x + eggImage:getWidth() * egg.scale
        and y >= egg.y
        and y <= egg.y + eggImage:getHeight() * egg.scale then

            print("Egg clicked!")

            chickenspeed = slowSpeed
            powerupTimer = 5

            eggActive = false
            eggTimer = 10

        end

        for i, value in ipairs(chicken.x) do

            if x >= chicken.x[i]
            and x <= chicken.x[i] + chickenImage:getWidth() * chicken.scale
            and y >= chicken.y[i]
            and y <= chicken.y[i] + chickenImage:getHeight() * chicken.scale then


                print("Chicken clicked!")

                chicken.y[i] = math.random(
                    chickenImage:getHeight(),
                    chickenImage:getHeight() * 2)
                    * -1

                break

            end
        end

    end

end

-- This function is called every frame and is used to update the game state. The dt parameter is the time in seconds since the last frame.
function love.update(dt)

    if powerupTimer > 0 then

    powerupTimer = powerupTimer - dt

    if powerupTimer <= 0 then
        chickenspeed = normalSpeed
    end

end

    -- Egg respawn timer
    if not eggActive then

        eggTimer = eggTimer - dt

        if eggTimer <= 0 then

            eggActive = true

            egg.x = math.random(
                0, love.graphics.getWidth() - eggImage:getWidth())

            egg.y = math.random(
                0, love.graphics.getHeight() - eggImage:getHeight())

        end
    end

    for i = 1, 5 do

        chicken.y[i] = chicken.y[i] + chickenspeed * dt

        if chicken.y[i] + chickenImage:getHeight() * chicken.scale 
            >= love.graphics.getHeight()
        then

            print("Chicken hit the ground!")
            love.event.quit()

            chicken.x[i] = math.random(
                0, love.graphics.getWidth() - chickenImage:getWidth() * chicken.scale)


            chicken.y[i] = math.random(
                chickenImage:getHeight(),
                chickenImage:getHeight() * 2)
                * -1

        end
    end
end

-- This function is called every frame and is used to draw the game. The dt parameter is the time in seconds since the last frame.
function love.draw()
    for i = 1, 5 do

        love.graphics.draw(
            chickenImage,
            chicken.x[i],
            chicken.y[i],
            0,
            chicken.scale,
            chicken.scale
        )

    end

    if eggActive then

        love.graphics.draw(
            eggImage,
            egg.x,
            egg.y,
            0,
            egg.scale,
            egg.scale
        )

    end
end

-- This is the default error handler that comes with Love2D. It is used to display errors in a nice way.
local love_errorhandler = love.errorhandler

function love.errorhandler(msg)
    if lldebugger then
        error(msg, 2)
    else
        return love_errorhandler(msg)
    end
end


