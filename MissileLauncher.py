from missiles import *
from LauncherReporter import  LauncherReporter
from SupplyManager import SupplyManager


class MissileLauncher:

    def __init__(self):

        self.supply_manager = SupplyManager()

    def launch(self, position: int) -> int:
        if position == -1:
            results = [missile.launch() for missile in self.supply_manager.supply.curr_missiles]
            self.supply_manager.clean_all()
            return results.count(True)

        elif 0 <= position < len(self.supply_manager.supply.curr_missiles):
            results = self.supply_manager.supply.curr_missiles[position].launch()
            if results:
                self.supply_manager.remove(position)
            return 1 if results else 0

        return -1

    def add_to_supply(self,missile: Missile) -> bool:
        return self.supply_manager.add(missile)

    def remove_from_supply(self, index: int) -> bool:
        return self.supply_manager.remove(index)

    def full_report(self) -> str:
        report_str = LauncherReporter.full_report(self.supply_manager.supply)
        return report_str



