import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import api_router

# REST API Settings
app = FastAPI(
    title="Modul.os API",
    description="API para el proyecto de Modul.os",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


#  TODO: if != "development":
#     app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")
# See https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
# and https://caddyserver.com/docs/caddyfile/directives/reverse_proxy#defaults

# Middleware Settings
# ! Esto está bien para la producción, pero no para el desarrollo.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router)


@app.get("/")
async def root():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
