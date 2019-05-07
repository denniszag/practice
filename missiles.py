from launchTechnics import *


class Missile:
    missile_type = None
    missile_range = 0
    failed = None
    #launched = None
    launch_technic = None
    launch_params = {}
    
    def __init__(self, launch_technic: LaunchTechnic, missile_range=-1, launch_params={}):

        self.missile_range = missile_range
        self.launch_technic = launch_technic
        self.failed = False
        self.launch_params = launch_params

    def set_params(self):
        raise NotImplementedError

    def launch(self):
        raise NotImplementedError


class Torpedo(Missile):

    def __init__(self):
        self.missile_type = "Torpedo"
        super().__init__(PerfectTechnic())

    def set_params(self) -> dict:
        return self.launch_params

    def launch(self):
        if self.failed:
            return False
        if self.launch_technic.execute_launch(self.set_params()):
            return True
        else:
            self.failed = True


class Ballistic(Missile):

    def __init__(self):
        self.missile_type = "Ballistic"
        super().__init__(FiftyPercentTechnic())

    def set_params(self) -> dict:
        return self.launch_params

    def launch(self):
        if self.failed:
            return False
        if self.launch_technic.execute_launch(self.launch_params):
            return True
        else:
            self.failed = True


class Cruise(Missile):

    def __init__(self):
        self.missile_type = "Cruise"
        super().__init__(TwentyPercentTechnic())

    def set_params(self) -> dict:
        return self.launch_params

    def launch(self):
        if self.failed:
            return False
        if self.launch_technic.execute_launch(self.launch_params):
            return True
        else:
            self.failed = True


class LongDistance(Missile):

    def __init__(self):
        super().__init__(DistanceTechnic())
        self.missile_type = "LongDistance"
        self.missile_range = 1500

    def set_params(self) -> dict:

        self.launch_params["max_range"] = self.missile_range
        print("to what distance do you want to launch")
        self.launch_params["launch_range"] = int(input())
        return self.launch_params

    def launch(self):

        if self.failed:
            return False
        if self.launch_technic.execute_launch(self.set_params()):
            return True
        else:
            self.failed = True




