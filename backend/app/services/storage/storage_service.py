import logging
import uuid
from dataclasses import dataclass

from app.core.config import Settings

logger = logging.getLogger(__name__)

ALLOWED_CONTENT_TYPES = {
    "application/pdf",
    "image/png",
    "image/jpeg",
    "text/plain",
}


@dataclass
class UploadResult:
    storage_key: str | None
    filename: str
    content_type: str
    size_bytes: int


class StorageService:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @property
    def storage_configured(self) -> bool:
        return bool(
            self._settings.firebase_storage_bucket
            and (
                self._settings.google_application_credentials
                or self._settings.environment == "production"
            )
        )

    def upload(self, data: bytes, filename: str, content_type: str) -> UploadResult:
        size = len(data)
        storage_key: str | None = None

        if self.storage_configured:
            try:
                from google.cloud import storage

                client = storage.Client(project=self._settings.firebase_project_id)
                bucket = client.bucket(self._settings.firebase_storage_bucket)
                storage_key = f"uploads/{uuid.uuid4().hex}/{filename}"
                blob = bucket.blob(storage_key)
                blob.upload_from_string(data, content_type=content_type)
                logger.info("Uploaded file to storage", extra={"storage_key": storage_key})
            except Exception:
                logger.exception("Storage upload failed; returning metadata only")
                storage_key = None
        else:
            logger.debug("Storage not configured; metadata-only upload (TODO: enable GCS).")

        return UploadResult(
            storage_key=storage_key,
            filename=filename,
            content_type=content_type,
            size_bytes=size,
        )
