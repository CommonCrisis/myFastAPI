from fastapi import FastAPI
import uvicorn
from api.api_v1.api import router as api_router
from core.logging import init_logger
from db.database import close_db
from db.database import start_db

logger = init_logger('BackendLogger')

app = FastAPI()


@app.on_event('startup')
async def startup_event():
    logger.info('Starting application')
    load_envs()
    logger.info('Loaded environment variables')
    logger.info('Initializing SQL databases connection')
    start_db()
    logger.info('Initializing scheduler and adding jobs')
    init_scheduler()
    logger.info('All done - application up and running')
    
    
app.add_event_handler('shutdown', close_db)
app.add_event_handler('shutdown', kill_scheduler)


app.include_router(api_router, prefix='/api')
app.include_router(server_routers)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=54322, log_level='info')
