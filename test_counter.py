from modules.coach_counter import CoachCounter

counter = CoachCounter()

frames = [

["bio tank front"],

["connecting_wire"],

["connected pipe"],

["connecting_wire"],

["cbc_coupler"],

["bio tank front"]

]

for frame in frames:

    print(counter.process(frame))