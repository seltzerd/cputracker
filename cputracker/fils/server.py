# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi import Request

# app = FastAPI()

# templates = Jinja2Templates(directory="templates")


# class GoMetrics(BaseModel):
#     go_id: str
#     time: int
#     cpu_percent: float
#     memory_used: float
#     mem_total: float
#     disk_used: float

# @app.post("/metrics")
# async def receive_metrics(metric: GoMetrics):
#     print(f"Пришли данные от {metric.go_id}: CPU {metric.cpu_percent}%")
#     return {"status": "ok"}

# @app.get("/dashboard", response_class=HTMLResponse)
# async def read_dashboard(request: Request):
#     metrics_list = [{"agent": "Home-PC", "cpu": 45}, {"agent": "Work-Srv", "cpu": 12}]
#     return templates.TemplateResponse("index.html", {"request": request, "metrics": metrics_list})


# @app.get("/status")
# async def get_status():
#     return {
#         "agents": [
#             {
#                 "agent_id": "laptop",
#                 "online": True,
#                 "cpu_percent": 43,
#                 "mem_used_mb": 1600000,
#                 "last_seen": 0000000
#             },
#             {
#                 "agent_id": "server",
#                 "online": False,
#                 "cpu_percent": 0.0,
#                 "mem_used_mb": 0,
#                 "last_seen": 0000000
#             }
#         ]
#     }

from fastapi import FastAPI, Depends, Request
from pydantic import BaseModel
from sqlalchemy import create_all_engines, Column, String, Float, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import time

SQLALCHEMY_DATABASE_URL = "нужен ссылка от девопса"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class MetricEntry(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(String)
    timestamp = Column(Integer)
    cpu_percent = Column(Float)
    mem_used_mb = Column(Float)

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class GoMetrics(BaseModel):
    agent_id: str
    timestamp: int
    cpu_percent: float
    mem_used_mb: float
    mem_total_mb: float
    disk_used_percent: float

@app.post("/metrics")
async def receive_metrics(metric: GoMetrics, db: Session = Depends(get_db)):
    db_metric = MetricEntry(
        agent_id=metric.agent_id,
        timestamp=metric.timestamp,
        cpu_percent=metric.cpu_percent,
        mem_used_mb=metric.mem_used_mb
    )
    db.add(db_metric)
    db.commit()
    print(f"Данные от {metric.agent_id} сохранены в БД")
    return {"status": "ok"}

@app.get("/status")
async def get_status(db: Session = Depends(get_db)):
    all_metrics = db.query(MetricEntry).all()
    agents_data = []
    for m in all_metrics:
        agents_data.append({
            "agent_id": m.agent_id,
            "online": (time.time() - m.timestamp) < 60,
            "cpu_percent": m.cpu_percent,
            "mem_used_mb": m.mem_used_mb,
            "last_seen": m.timestamp
        })
    return {"agents": agents_data}
# Короче какая-то хуета попробывал сделать дешборд
# @app.get("/dashboard", response_class=HTMLResponse)
# async def read_dashboard(request: Request, db: Session = Depends(get_db)):
#     metrics_list = db.query(MetricEntry).order_by(MetricEntry.id.desc()).limit(10).all()
#     return templates.TemplateResponse("index.html", {"request": request, "metrics": metrics_list})

