from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")


class GoMetrics(BaseModel):
    go_id: str
    time: int
    cpu_percent: float
    memory_used: float
    mem_total: float
    disk_used: float

@app.post("/metrics")
async def receive_metrics(metric: GoMetrics):
    print(f"Пришли данные от {metric.go_id}: CPU {metric.cpu_percent}%")
    return {"status": "ok"}



@app.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    metrics_list = [{"agent": "Home-PC", "cpu": 45}, {"agent": "Work-Srv", "cpu": 12}]
    return templates.TemplateResponse("index.html", {"request": request, "metrics": metrics_list})



@app.get("/status")
async def get_status():
    return {
        "agents": [
            {
                "agent_id": "laptop",
                "online": True,
                "cpu_percent": 43,
                "mem_used_mb": 1600000,
                "last_seen": 0000000
            },
            {
                "agent_id": "server",
                "online": False,
                "cpu_percent": 0.0,
                "mem_used_mb": 0,
                "last_seen": 0000000
            }
        ]
    }


