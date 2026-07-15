"""
BTCAS Inspection Engine
"""

import os

from modules.detector import BTCASDetector
from modules.coach_counter import CoachCounter
from modules.tank_assignment import TankAssignment
from modules.inspection import BTCASInspection
from modules.report import ReportGenerator
from modules.utils import Statistics
from modules.json_report import JSONReport


class InspectionEngine:

    def __init__(self):

        self.detector = BTCASDetector()

        self.counter = CoachCounter()

        self.assigner = TankAssignment()

        self.inspector = BTCASInspection()

        self.report = ReportGenerator()

        self.statistics = Statistics()

        self.json_report = JSONReport()

    def inspect_video(self, video_path):

        results = self.detector.detect(video_path)

        processed_tanks = set()

        for r in results:

            if r.boxes is None:
                continue

            names = r.names

            classes = r.boxes.cls.cpu().numpy().astype(int)

            detected = [names[c] for c in classes]

            # ----------------------------
            # Update Statistics
            # ----------------------------

            self.statistics.update(detected)

            # ----------------------------
            # Skip frame if no Bio Tank
            # ----------------------------

            if "bio tank front" not in detected:
                continue

            # ----------------------------
            # Coach Counter
            # ----------------------------

            coach_no = self.counter.process(detected)

            # ----------------------------
            # Tank Assignment
            # ----------------------------

            coach, tank = self.assigner.next_tank()

            # Avoid duplicate tank IDs

            if tank in processed_tanks:
                continue

            processed_tanks.add(tank)

            # ----------------------------
            # Inspection
            # ----------------------------

            inspection = self.inspector.inspect(detected)

            # ----------------------------
            # Save Report
            # ----------------------------

            self.report.add(

                coach=coach,

                tank=tank,

                pipe=inspection["Pipe Status"],

                surface=inspection["Surface"],

                maintenance=inspection["Maintenance"]

            )

        # ------------------------------------
        # DataFrame
        # ------------------------------------

        df = self.report.dataframe()

        # ------------------------------------
        # Summary
        # ------------------------------------

        maintenance_count = 0

        if len(df):

            maintenance_count = len(

                df[df["Maintenance"] == "YES"]

            )

        summary = {

            "total_coaches": self.assigner.current_coach - 1,

            "total_tanks": len(df),

            "maintenance_required": maintenance_count

        }

        # ------------------------------------
        # Final JSON
        # ------------------------------------

        final_report = {

            "status": "success",

            "summary": summary,

            "inspection":

                df.to_dict(

                    orient="records"

                ),

            "statistics":

                self.statistics.json()

        }

        # ------------------------------------
        # Save JSON
        # ------------------------------------

        os.makedirs("reports", exist_ok=True)

        self.json_report.save(

            final_report,

            "reports/report.json"

        )

        return final_report