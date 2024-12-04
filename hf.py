from huggingface_hub import snapshot_download
import os

# Hugging Face 토큰 설정 (또는 huggingface-cli login 사용)
os.environ["HUGGING_FACE_HUB_TOKEN"] = "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"  # 여기에 실제 토큰 입력

# 다운로드 경로 지정
cache_dir = r"C:\Users\admin\.cache\huggingface\hub"

# 모델 다운로드
local_dir = snapshot_download(
    repo_id="google/gemma-2-2b-it",
    cache_dir=cache_dir,
    token=True  # 토큰 사용 명시
)

print(f"Model downloaded to: {local_dir}")
