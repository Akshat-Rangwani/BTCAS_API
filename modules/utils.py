from collections import defaultdict

class Statistics:

    def __init__(self):

        self.objects = defaultdict(list)

    def update(self, result):

        if result.boxes is None:
            return

        boxes = result.boxes.xyxy.cpu().numpy()
        classes = result.boxes.cls.cpu().numpy().astype(int)
        names = result.names

        for box, cls in zip(boxes, classes):

            name = names[cls]

            x1, y1, x2, y2 = box

            cx = (x1 + x2) / 2

            found = False

            for old in self.objects[name]:

                if abs(old - cx) < 100:
                    found = True
                    break

            if not found:
                self.objects[name].append(cx)

    def json(self):

        return {

            k: len(v)

            for k, v in self.objects.items()

        }