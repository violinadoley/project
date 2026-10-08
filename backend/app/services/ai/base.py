from abc import ABC, abstractmethod
from typing import Any, TypeVar

T = TypeVar("T")


class AIService(ABC):
    """Abstraction for Gemini and future model providers."""

    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        """Generate plain text from a user prompt."""

    def generate_structured_output(
        self, prompt: str, schema: type[T]
    ) -> T:
        """TODO: Structured JSON output via response_schema."""
        raise NotImplementedError(
            "Structured output is not implemented in the starter template."
        )

    def analyze_image(self, prompt: str, image_bytes: bytes, mime_type: str) -> str:
        """TODO: Multimodal image analysis."""
        raise NotImplementedError(
            "Image analysis is not implemented in the starter template."
        )

    def generate_with_context(
        self, messages: list[dict[str, Any]]
    ) -> str:
        """TODO: Multi-turn conversation / RAG context."""
        raise NotImplementedError(
            "Contextual generation is not implemented in the starter template."
        )

    def embed_text(self, text: str) -> list[float]:
        """TODO: Gemini embeddings for vector search."""
        raise NotImplementedError(
            "Embeddings are not implemented in the starter template."
        )
