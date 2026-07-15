from modules.inspection_engine import InspectionEngine

engine = InspectionEngine()

result = engine.inspect_video("uploads/train1.mp4")

print(result)