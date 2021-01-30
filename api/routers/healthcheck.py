from fastapi import APIRouter
from mongoengine import get_db

router = APIRouter()


@router.get("/")
def healthcheck():
    db = get_db()
    result = {
        'mongodb': db.command('ping'),
        'example': {'ok': 1.0}
    }
    return result
