"""
Inspection Module
"""


class BTCASInspection:

    def inspect(self, detected):

        # ------------------------

        # Pipe

        # ------------------------

        if "connected pipe" in detected:

            pipe = "Connected"

        #else:

            #pipe = "Not Connected"

        # ------------------------

        # Surface

        # ------------------------

        if "cleaned bio tank top surface" in detected:

            surface = "Clean"

        else:

            surface = "Dirty"

        # ------------------------

        # Maintenance

        # ------------------------

        if pipe == "Connected" or surface == "Clean":
            maintenance = "NO"
        else:
            maintenance = "YES"

        return {

            "Pipe Status": pipe,

            "Surface": surface,

            "Maintenance": maintenance

        }