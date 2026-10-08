import logging
from typing import Annotated

from app.core.deps import get_gemini_service, require_user
from app.core.exceptions import AIGenerationError
from app.schemas.ai import GenerateRequest, GenerateResponse
from app.services.ai.base import AIService
from fastapi import APIRouter, Depends

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/generate", response_model=GenerateResponse)
async def generate_text(
    body: GenerateRequest,
    ai: Annotated[AIService, Depends(get_gemini_service)],
    _user: Annotated[dict | None, Depends(require_user)],
) -> GenerateResponse:
    try:
        text = ai.generate_text(body.message)
    except AIGenerationError:
        raise
    except Exception as exc:
        logger.exception("AI generation failed")
        raise AIGenerationError() from exc
    return GenerateResponse(success=True, response=text)
