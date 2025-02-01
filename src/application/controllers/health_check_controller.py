from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/health-check",
    tags=["Health Check Services"],
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
)
async def health_check() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"success": True, "message": "Service is running successfully"}
    )
