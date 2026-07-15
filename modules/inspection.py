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

        else:

            pipe = "Not Connected"

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

        maintenance = "NO"

        if pipe == "Not Connected":

            maintenance = "YES"

        if surface == "Dirty":

            maintenance = "YES"

        return {

            "Pipe Status": pipe,

            "Surface": surface,

            "Maintenance": maintenance

        }