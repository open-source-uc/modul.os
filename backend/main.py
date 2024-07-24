import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import user_router
from models import schedule, user, group, meeting
from models.database import engine
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError

def create_enum_type(engine):
    with engine.connect() as conn:
        try:
            conn.execute(text("""
                DO $$ BEGIN
                    CREATE TYPE day_enum AS ENUM ('monday', 'tuesday', 'wednesday', 'thursday', 'friday');
                EXCEPTION
                    WHEN duplicate_object THEN null;
                END $$;
            """))
            conn.commit()
        except ProgrammingError:
            conn.rollback()

# Crear el tipo Enum antes de crear las tablas
create_enum_type(engine)

#Database models
schedule.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
group.Base.metadata.create_all(bind=engine)
meeting.Base.metadata.create_all(bind=engine)

# REST API Settings
app = FastAPI(
    title="Modul.os API",
    description="API para el proyecto de Modul.os",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Middleware Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)

@app.get("/")
async def root():
    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
