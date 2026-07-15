"""
Tank Assignment Module
"""


class TankAssignment:

    def __init__(self):

        self.current_coach = 1
        self.tank_index = 0

        self.tank_order = [
            "L1A",
            "L1B",
            "R1A",
            "R1B"
        ]

    def next_tank(self):

        coach = self.current_coach

        tank = self.tank_order[self.tank_index]

        tank = tank.replace("1", str(coach))

        self.tank_index += 1

        if self.tank_index == 4:

            self.tank_index = 0
            self.current_coach += 1

        return coach, tank