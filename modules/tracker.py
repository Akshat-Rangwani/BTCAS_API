"""
BTCAS Tracker Module
"""


class TankTracker:

    def __init__(self):

        self.tracked = {}

    def process(self, result):

        tanks = []

        if result.boxes is None:

            return tanks

        if result.boxes.id is None:

            return tanks

        ids = result.boxes.id.cpu().numpy().astype(int)

        classes = result.boxes.cls.cpu().numpy().astype(int)

        names = result.names

        for track_id, cls in zip(ids, classes):

            tanks.append({

                "track_id": int(track_id),

                "class": names[cls]

            })

        return tanks