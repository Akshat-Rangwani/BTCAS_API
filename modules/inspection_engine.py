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

        processed_tracks = set()

        for r in results:

            if r.boxes is None:
                continue

            if r.boxes.id is None:
                continue

            names = r.names

            classes = r.boxes.cls.cpu().numpy().astype(int)

            track_ids = r.boxes.id.cpu().numpy().astype(int)

            detected = [names[c] for c in classes]

        # ----------------------------
        # Update Statistics
        # ----------------------------

            self.statistics.update(r)

        # ----------------------------
        # Find New Bio Tank
        # ----------------------------

            bio_track = None

            for tid, cls in zip(track_ids, classes):

                classname = names[cls]

                if classname == "bio tank front":

                    if tid not in processed_tracks:

                        bio_track = tid

                        break

            if bio_track is None:
                continue

            processed_tracks.add(bio_track)

        # ----------------------------
        # Coach Counter
        # ----------------------------

            coach_no = self.counter.process(r)

        # ----------------------------
        # Tank Assignment
        # ----------------------------

            coach, tank = self.assigner.next_tank()

        # ----------------------------
        # Inspection
        # ----------------------------

            inspection = self.inspector.inspect(detected)

        # ----------------------------
        # Report
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

        self.report.save_csv("reports/report.csv")

        final_report = {

            "status": "success",

            "summary": summary,

            "inspection": df.to_dict(orient="records"),

            "statistics": self.statistics.json()

        }

        os.makedirs("reports", exist_ok=True)

        self.json_report.save(

            final_report,

            "reports/report.json"

        )

        return final_report