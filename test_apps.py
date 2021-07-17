import pytest
from fastapi import Depends

from app.main import app
from config import Config
from data_init import APP
from models.models import AppModel
from test_base import client, get_test_db
from sqlalchemy.orm import Session

@pytest.fixture(scope="session", autouse=True)
def init(db: Session=Depends(get_test_db)):
    new_app = AppModel(**APP)    
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    AppModel.filter_or_404(db, id=APP["id"])

def test_get_apps(client, db: Session=Depends(get_test_db)):
    response = client.get("/applications")
    assert response.status_code == 200