from fastapi import Depends, APIRouter

from app.api.dependencies import verify_user
from app.schemas.email import Email
from app.services import notify_services

router = APIRouter()


@router.post("/send-notification", dependencies=[Depends(verify_user)])
def send_notification(email: Email):
    return notify_services.send_notification(email=email)
