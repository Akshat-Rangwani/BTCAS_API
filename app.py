from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil

from config import UPLOAD_DIR
from modules.inspection_engine import InspectionEngine

app = FastAPI(

    title="BTCAS API",

    version="1.0"

)

print("Loading BTCAS Inspection Engine...")

engine = InspectionEngine()

print("Inspection Engine Ready")


@app.get("/")
def home():

    return {

        "status": "success",

        "message": "BTCAS API Running"

    }


@app.get("/health")
def health():

    return {

        "status": "healthy"

    }


@app.post("/inspect")
async def inspect(

    file: UploadFile = File(...)

):

    try:

        upload_path = UPLOAD_DIR / file.filename

        with open(upload_path, "wb") as buffer:

            shutil.copyfileobj(file.file, buffer)

        report = engine.inspect_video(

            str(upload_path)

        )

        return JSONResponse(report)

    except Exception as e:

        return JSONResponse(

            status_code=500,

            content={

                "status": "failed",

                "error": str(e)

            }

        )