import os
import uuid
from datetime import datetime
from typing import Optional

# 确保目录存在
def ensure_directories(dir_path: str = None):
    if dir_path is None:
        # 默认创建两个目录
        dirs = ["static/uploads", "static/results"]
        for d in dirs:
            if not os.path.exists(d):
                os.makedirs(d, exist_ok=True)
    else:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

# 保存上传的文件
def save_upload_file(file, upload_dir: str = "static/uploads") -> str:
    ensure_directories(upload_dir)
    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    file_path = os.path.join(upload_dir, filename)
    
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    return file_path

# 生成唯一文件名
def generate_unique_filename(ext: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    return f"{timestamp}_{unique_id}.{ext}"

# 获取文件的可访问URL
def get_file_url(file_path: str, base_dir: str = None) -> str:
    if base_dir and "static/" in base_dir:
        return "/" + base_dir.replace("static/", "") + "/" + file_path
    if "static/" in file_path:
        return "/" + file_path.split("static/", 1)[1]
    return file_path