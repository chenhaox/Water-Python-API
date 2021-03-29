
if __name__ == '__main__':
    from water2driver import Water2Robot
    import time
    w = Water2Robot()
    def turn_lft(speed = 0.1):
        w.joy_control(angular_velocity=speed,linear_velocity=0)
    def turn_rgt(speed = 0.1):
        print(w.joy_control(angular_velocity=-speed,linear_velocity=0))
    def move_front(speed = 0.1):
        w.joy_control(angular_velocity=0,linear_velocity=speed)
    def move_back(speed = 0.1):
        w.joy_control(angular_velocity=0,linear_velocity=-speed)
    turn_rgt(speed=.5)
    time.sleep(.5)
    turn_rgt(speed=.5)
    time.sleep(.5)
    turn_rgt(speed=.5)
    time.sleep(.5)
    turn_rgt(speed=.5)
    time.sleep(.5)
    turn_rgt(speed=.5)

