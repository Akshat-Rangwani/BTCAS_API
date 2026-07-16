"""
Coach Counter Module
"""

class CoachCounter:

    def __init__(self):

        self.coach_count = 0

        # Store processed connecting wire IDs
        self.processed_tracks = set()

    def process(self, result):

        """
        result = one YOLO Result object
        """

        if result.boxes is None:
            return self.coach_count

        if result.boxes.id is None:
            return self.coach_count

        names = result.names

        classes = result.boxes.cls.cpu().numpy().astype(int)

        track_ids = result.boxes.id.cpu().numpy().astype(int)

        for tid, cls in zip(track_ids, classes):

            classname = names[cls]

            if classname in ["connecting_wire", "cbc_coupler"]:

                if tid not in self.processed_tracks:

                    self.processed_tracks.add(tid)

                    self.coach_count += 1

        return self.coach_count