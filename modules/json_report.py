import json


class JSONReport:

    def save(self, data, filename):

        with open(filename, "w") as f:

            json.dump(

                data,

                f,

                indent=4

            )