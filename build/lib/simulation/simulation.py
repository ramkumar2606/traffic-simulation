import time
if __package__ is None or __package__ == '':
    import lights
else:
    from . import lights
import turtle

class Simulation:
    def __init__(self):
        self.red_seconds = None
        self.green_seconds = None
        self.yellow_seconds = None
        self.simulation_stop = False

    def validate_seconds(self, seconds):
        """
        Validates seconds
        :param seconds: int
        :return: Boolean
        """
        if seconds <= 0:
            print("No of seconds should be greater than 0")
            return False
        return True

    def hold(self, seconds):
        """
        Holds for given seconds.For every one second checks for a stop signal
        :param seconds:
        :return:
        """
        while not self.simulation_stop and seconds:
            time.sleep(1)
            seconds -= 1

    def run(self):
        """
        This method prints the signals to the console
        :return:
        """

        try:
            traffic_lights = lights.Lights()

            color_indicator = 1
            while not self.simulation_stop:
                if color_indicator == 4:
                    color_indicator = 1 # Resetting to 1
                if color_indicator == 1:  # That means red color
                    traffic_lights.red_on()
                    self.hold(self.red_seconds)
                    traffic_lights.red_off()
                elif color_indicator == 2:  # That means yellow color
                    traffic_lights.yellow_on()
                    self.hold(self.yellow_seconds)
                    traffic_lights.yellow_off()
                else:  # That means green color
                    traffic_lights.green_on()
                    self.hold(self.green_seconds)
                    traffic_lights.green_off()
                color_indicator += 1

            traffic_lights.close()
        except Exception:  # Mostly turtle exceptions here
            self.stop()

    def stop(self):
        """
        This method stops the simulation
        :return:
        """
        self.simulation_stop = True
        print("Thank you for using simulation, Good Bye!")

    def request_input(self, input_type, message, validator):
        """
        This method is to handle the user input
        :param input_type: String
        :param message: String
        :param validator: Function
        :return: User Value
        """
        while True:
            try:
                user_input = input_type(input(message))
            except ValueError:
                print("Please enter a {0} value".format(str(input_type)))
                continue
            else:
                if not validator(user_input):
                    continue
                else:
                    return user_input

    def start(self):
        """
        Starts the simulation
        :return: None
        """
        print("################")
        print("Welcome to the Traffic Light Simulator!")
        print("If at any time you'd like to stop please press CTRL+C")
        print("################")
        self.red_seconds = self.request_input(input_type=int,
                                              message="Enter No of seconds for red signal to lit:",
                                              validator=self.validate_seconds)
        self.yellow_seconds = self.request_input(input_type=int,
                                                 message="Enter No of seconds for yellow signal to lit:",
                                                 validator= self.validate_seconds)
        self.green_seconds = self.request_input(input_type=int,
                                                message="Enter No of seconds for green signal to lit:",
                                                validator=self.validate_seconds)
        print("################")
        print("Enjoy the simulation in other window which just opened(see in your task bar)")
        print("################")
        self.run()


