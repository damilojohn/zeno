from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException, RequestValidationError


class AppException(Exception):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = "An unexpected error occurred"

    def __init__(self, message: str | None = None):
        if message:
            self.message = message
        super().__init__(self.message)


class NotFoundError(AppException):
    status_code = status.HTTP_404_NOT_FOUND
    message = "Resource not found"


class UnauthorizedError(AppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Authentication required"


class ForbiddenError(AppException):
    status_code = status.HTTP_403_FORBIDDEN
    message = "Permission denied"


class ConflictError(AppException):
    status_code = status.HTTP_409_CONFLICT
    message = "Resource already exists"


class BadRequestError(AppException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Invalid request"


class InternalServerError(AppException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "An unexpected error occurred"


async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"msg": exc.message, "data": None},
    )


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"msg": exc.detail or "An error occurred", "data": None},
    )


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    errors = exc.errors()
    detail = errors[0].get("msg", "Validation error") if errors else "Validation error"
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"msg": detail, "data": errors},
    )
