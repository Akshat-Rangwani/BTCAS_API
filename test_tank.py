from modules.tank_assignment import TankAssignment

assigner = TankAssignment()

for i in range(12):

    coach, tank = assigner.next_tank()

    print(coach, tank)