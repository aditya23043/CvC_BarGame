import sh1106
import ssd1306
from machine import Pin, I2C
import utime

# SETUP

WIDTH = 128
HEIGHT = 64

sda1 = Pin(18)
scl1 = Pin(19)
sda2 = Pin(16)
scl2 = Pin(17)

freq = 3000000

# I2C
i2c1 = I2C(1, scl=scl1, sda=sda1, freq=freq)
i2c2 = I2C(0, scl=scl2, sda=sda2, freq=freq)

# DISPLAY
display1 = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c1)
display2 = sh1106.SH1106_I2C(WIDTH, HEIGHT, i2c2, Pin(4), 0x3c)
display2.flip()

# BALL
radius = 4
ball_x = (WIDTH//2) - (radius//2)
ball_y = (HEIGHT//2) - (radius//2)
ball_vel_x = 1
ball_vel_y = 1

# BAR LEFT
bar_height_left = 14
bar_width_left = 3
bar_x_left = 2
bar_y_left = ball_y

# BAR RIGHT
bar_height_right = 14
bar_width_right = 3
bar_x_right = WIDTH - bar_width_right - 2
bar_y_right = ball_y

# MAIN LOOP
while True:

    # INIT
    ## ball
    display2.rect(ball_x, ball_y, radius, radius, 1)
    ## left bar
    if ball_x <= WIDTH // 2:
        bar_y_left = ball_y
        if bar_y_left <= ((bar_height_left//2)-(radius//2)):
            bar_y_left = ((bar_height_left//2)-(radius//2))
        if (bar_y_left-((bar_height_left//2)-(radius//2))) + bar_height_left >= HEIGHT:
            bar_y_left = HEIGHT + ((bar_height_left//2)-(radius//2)) - bar_height_left
    display2.fill_rect(bar_x_left, bar_y_left-((bar_height_left//2)-(radius//2)), bar_width_left, bar_height_left, 1)

    ## right bar
    if ball_x > WIDTH // 2:
        bar_y_right = ball_y
        if bar_y_right <= ((bar_height_right//2)-(radius//2)):
            bar_y_right = ((bar_height_right//2)-(radius//2))
        if (bar_y_right-((bar_height_right//2)-(radius//2))) + bar_height_right >= HEIGHT:
            bar_y_right = HEIGHT + ((bar_height_right//2)-(radius//2)) - bar_height_right
    display2.fill_rect(bar_x_right, bar_y_right-((bar_height_right//2)-(radius//2)), bar_width_right, bar_height_right, 1)

    display2.show()

    # UPDATE
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # CONDITION
    if ball_x >= WIDTH-radius or ball_x <= 0:
        ball_vel_x = -ball_vel_x
    if ball_y >= HEIGHT-radius or ball_y <= 0:
        ball_vel_y = -ball_vel_y

    ## collision with the bar
    if ball_x <= bar_x_left + bar_width_right:
        ball_vel_x = -ball_vel_x
    if ball_x >= bar_x_right - bar_width_right:
        ball_vel_x = -ball_vel_x

    # RESET
    display2.fill(0)
    utime.sleep(0.01)
