from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from models import RequestDTO, ResponseDTO
from services import get_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/v1/chat",
          summary='Получение ответа от ChatGPT',
          status_code=200,
          response_model=ResponseDTO)
async def root(dto: RequestDTO):
    data = get_response(dto)
    if data is None:
        raise HTTPException(status_code=500, detail='Не удалось сформировать ответ!')
    return data
