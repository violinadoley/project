from typing import Annotated, Any

from app.ai.base import AIService
from app.ai.services.gemini_service import GeminiService
from app.core.config import Settings, get_settings
from app.core.exceptions import AuthenticationError
from app.services.firebase.firestore_service import FirestoreService
from app.services.storage.storage_service import StorageService
from fastapi import Depends, Header

_gemini_override: AIService | None = None


def set_gemini_service_override(service: AIService | None) -> None:
    global _gemini_override
    _gemini_override = service


def get_gemini_service(
    settings: Annotated[Settings, Depends(get_settings)],
) -> AIService:
    if _gemini_override is not None:
        return _gemini_override
    return GeminiService(settings)


def get_firestore_service(
    settings: Annotated[Settings, Depends(get_settings)],
) -> FirestoreService:
    return FirestoreService(settings)


def get_storage_service(
    settings: Annotated[Settings, Depends(get_settings)],
) -> StorageService:
    return StorageService(settings)


async def get_current_user_optional(
    settings: Annotated[Settings, Depends(get_settings)],
    authorization: Annotated[str | None, Header()] = None,
) -> dict[str, Any] | None:
    if not settings.auth_required:
        return None
    if not authorization or not authorization.startswith("Bearer "):
        raise AuthenticationError()
    token = authorization.removeprefix("Bearer ").strip()
    if not token:
        raise AuthenticationError()
    try:
        from firebase_admin import auth

        decoded: dict[str, Any] = auth.verify_id_token(token)
        return decoded
    except Exception as exc:
        raise AuthenticationError("Invalid or expired token.") from exc


async def require_user(
    user: Annotated[dict[str, Any] | None, Depends(get_current_user_optional)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> dict[str, Any] | None:
    if settings.auth_required and user is None:
        raise AuthenticationError()
    return user
