from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Micky Valentino / 18222093"}

@app.get("/status")
async def get_status():
    return {"status": "Application is running"}

@app.get("/info")
async def get_info():
    return {
        "app_name": "Chili Grinding Machine Hybrid System",
        "description": "A project on chili grinding machine using wind and solar energy",
        "version": "1.0.0"
    }

@app.get("/author")
async def get_author():
    return {
        "author": "Education Office of Lebak Regency",
        "contact": "contact@lebak-education.gov"
    }

@app.get("/machine/status")
async def machine_status():
    return {"machine_status": "Idle", "energy_source": "Solar"}

@app.get("/machine/energy")
async def machine_energy():
    return {"current_energy_source": "Hybrid (Wind & Solar)"}

@app.get("/usage/history")
async def usage_history():
    return {
        "usage": [
            {"date": "2024-11-01", "duration": "2 hours", "energy_used": "Solar"},
            {"date": "2024-11-02", "duration": "3 hours", "energy_used": "Wind"},
        ]
    }
