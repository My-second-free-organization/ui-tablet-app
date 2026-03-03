from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="FlowForge Admin", version="2.4.0")

@app.get("/api/admin/tenants")
def list_tenants(): return {"tenants": []}

@app.get("/api/admin/system/health")
def system_health(): return {"services": [{"name": "platform-core", "status": "healthy"}, {"name": "platform-api", "status": "healthy"}, {"name": "service-auth", "status": "healthy"}]}

@app.post("/api/admin/cache/clear")
def clear_cache(): return {"status": "cleared"}
