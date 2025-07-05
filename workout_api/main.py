from fastapi import FastAPI
from workout_api.router import api_router

app = FastAPI(title='WorkoutApi')

@app.get('/')
def read_root():
    return {'message': 'Hello World - WorkoutApi'}

@app.get('/health')
def health_check():
    return {'status': 'OK'}

app.include_router(api_router)

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)