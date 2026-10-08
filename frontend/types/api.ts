export type ApiErrorBody = {
  success: false;
  error: {
    code: string;
    message: string;
    details?: Record<string, unknown>;
  };
};

export type GenerateAIResponse = {
  success: true;
  response: string;
};

export type FileUploadResponse = {
  success: true;
  filename: string;
  content_type: string;
  size_bytes: number;
  storage_key: string | null;
};
