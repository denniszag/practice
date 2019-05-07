from SupplyManager import Supply


class LauncherReporter:

    def __init__(self):
        pass

    @staticmethod
    def full_report(supply:Supply):

        if not supply.curr_missiles:
            return "supply is empty"

        report_str = ""
        for key in supply.missile_mapping.keys():
            if supply.missile_mapping[key]:
                report_str += "launcher have {} {}s \n ".format(len(supply.missile_mapping[key]), key)

        return report_str





