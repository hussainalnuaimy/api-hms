from fastapi.encoders import jsonable_encoder


def ok(data=None, message: str = "Request completed successfully") -> dict:
    return {"success": True, "data": jsonable_encoder(data), "message": message}