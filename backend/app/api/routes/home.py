from app.core.logging import get_logger
from fastapi import APIRouter

logger = get_logger()

router = APIRouter(prefix="/home")


@router.get("/")
def home():
    logger.info("Home page acccessed")
    logger.debug("Home page acccessed")
    logger.error("Home page acccessed")
    logger.warning("Home page acccessed")
    logger.critical("Home page acccessed")
    return {"message": "Welcome to the NextGen Bank API"}
