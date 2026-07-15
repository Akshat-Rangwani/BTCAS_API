from collections import Counter


class Statistics:

    def __init__(self):

        self.counter = Counter()


    def update(self, detected):

        for obj in detected:

            self.counter[obj] += 1


    def json(self):

        return dict(self.counter)