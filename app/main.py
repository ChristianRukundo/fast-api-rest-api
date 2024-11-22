from fastapi import FastAPI


from research_management_system_fastapi.routes.user_apis import router
from research_management_system_fastapi.config.config import engine, create_tables

create_tables()

app = FastAPI()

app.include_router(router, prefix="/api/v1", tags=["user"])



