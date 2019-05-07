import random

class LaunchTechnic:
    
    def __init(self):
        pass

    def execute_launch(self, params_dict=None) -> bool:
        raise NotImplementedError


class PerfectTechnic(LaunchTechnic):

    def __init__(self):
        super()
        self.probability = 1

    def execute_launch(self, params_dict=None):
        return True


class FiftyPercentTechnic(LaunchTechnic):

    def __init__(self):
        super()
        self.probability = 2

    def execute_launch(self, params_dict=None):

        launch_result = random.randint(1, self.probability)

        return True if launch_result == 1 else False


class TwentyPercentTechnic(LaunchTechnic):

    def __init__(self):
        super()
        self.probability = 5

    def execute_launch(self, params_dict=None):

        launch_result = random.randint(1, self.probability)

        return True if launch_result == 1 else False


class DistanceTechnic(LaunchTechnic):

    def __init__(self):
        super()
        self.launch_distance = 0

    def execute_launch(self, params_dict=None) -> bool:

        max_range = params_dict["max_range"]
        launch_range = params_dict["launch_range"]
        percents = (max_range - launch_range)*100/max_range

        return random.randint(0,100) < percents
