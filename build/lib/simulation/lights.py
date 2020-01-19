import turtle
import time


class Lights:
    """
    Class to switch on and off lights
    """
    def __init__(self):
        self.red_light = turtle.Turtle()
        self.red_light.setpos(2, 5)
        self.yellow_light = turtle.Turtle()
        self.yellow_light.setpos(2, -100)
        self.green_light = turtle.Turtle()
        self.green_light.setpos(2, -205)
        self.red_off()
        self.yellow_off()
        self.green_off()

    def red_on(self):
        """
        Switch on red light
        :return:
        """
        self.red_light.fillcolor('red')
        self.red_light.begin_fill()
        self.red_light.circle(50)
        self.red_light.end_fill()

    def red_off(self):
        """
        Switch off red light
        :return:
        """
        self.red_light.fillcolor('white')
        self.red_light.begin_fill()
        self.red_light.circle(50)
        self.red_light.end_fill()

    def yellow_on(self):
        """
        Switch on yellow
        :return:
        """
        self.yellow_light.fillcolor('yellow')
        self.yellow_light.begin_fill()
        self.yellow_light.circle(50)
        self.yellow_light.end_fill()

    def yellow_off(self):
        """
        Switch off yellow
        :return:
        """
        self.yellow_light.fillcolor('white')
        self.yellow_light.begin_fill()
        self.yellow_light.circle(50)
        self.yellow_light.end_fill()

    def green_on(self):
        """
        Switch on green
        :return:
        """
        self.green_light.fillcolor('green')
        self.green_light.begin_fill()
        self.green_light.circle(50)
        self.green_light.end_fill()

    def green_off(self):
        """
        Switch off green
        :return:
        """
        self.green_light.fillcolor('white')
        self.green_light.begin_fill()
        self.green_light.circle(50)
        self.green_light.end_fill()

    def close(self):
        """
        remove lights
        :return:
        """
        self.red_light.done()
        self.gree_light.done()
        self.yellow_light.done()




