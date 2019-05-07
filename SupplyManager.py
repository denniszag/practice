from collections import defaultdict
from missiles import Missile


class Supply:
    def __init__(self):
        self.curr_missiles = []
        self.missile_mapping = defaultdict(list)


class SupplyManager:

    def __init__(self):
        self.supply = Supply()

    def add(self,missile: Missile):
        self.supply.curr_missiles.append(missile)
        index = len(self.supply.curr_missiles) -1
        if self.supply.missile_mapping.get(missile.missile_type, None):
            self.supply.missile_mapping[missile.missile_type].append(index)
        else:
            self.supply.missile_mapping[missile.missile_type] = [index]
        return True

    def remove(self, index: int) -> bool:
        if 0 <= index < len(self.supply.curr_missiles):
            curr = self.supply.curr_missiles.pop(index)
            self.supply.missile_mapping[curr.missile_type].remove(index)
            return True
        return False

    def clean_all(self):
        for i in range(len(self.supply.curr_missiles)):
            self.remove(i)
