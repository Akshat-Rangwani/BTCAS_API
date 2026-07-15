"""
Coach Counter Module
"""


class CoachCounter:

    def __init__(self):

        self.coach_count = 0

    def process(self, detected_objects):

        """
        detected_objects

        Example

        [

        "bio tank front",

        "connected pipe",

        "connecting_wire"

        ]

        """

        if "connecting_wire" in detected_objects:

            self.coach_count += 1

        elif "cbc_coupler" in detected_objects:

            self.coach_count += 1

        return self.coach_count