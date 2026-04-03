from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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


