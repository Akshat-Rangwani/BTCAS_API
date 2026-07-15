import pandas as pd


class ReportGenerator:

    def __init__(self):

        self.rows=[]

    def add(

        self,

        coach,

        tank,

        pipe,

        surface,

        maintenance

    ):

        self.rows.append({

            "Coach":coach,

            "Tank":tank,

            "Pipe Status":pipe,

            "Surface":surface,

            "Maintenance":maintenance

        })

    def dataframe(self):

        return pd.DataFrame(

            self.rows

        ).drop_duplicates()

    def save_csv(

        self,

        filename

    ):

        self.dataframe().to_csv(

            filename,

            index=False

        )