"""Preprocessing utilities for Vietnamese text.
Functions:
- preprocess_texts(texts): list of cleaned texts
- preprocess_df(df, text_col='text', label_col=None): returns X (list) and y (series or None)
"""
import re
import string
from typing import List, Tuple
from underthesea import word_tokenize
from .utils import normalize_unicode, standardize_vietnamese

# Vietnamese stop words - có thể cập nhật thêm
STOPWORDS = set([
    "và", "của", "các", "có", "được", "cho", "trong", "đã", "với",
    "những", "như", "này", "để", "theo", "về", "là", "nhưng", "từ",
    "khi", "đến", "tại", "vào", "còn", "sau", "trên", "phải", "bị",
    "được", "đang", "cũng", "khác", "tới", "chỉ", "sau", "nhất", "từng",
    "cả", "vẫn", "mà", "hay", "một", "rồi", "đều", "nếu", "thì",
    "đây", "ai", "sẽ", "vì", "lên", "xuống", "ngoài", "quá", "ở",
])


def clean_text(s: str, remove_tone: bool = False) -> str:
    """Clean Vietnamese text.
    
    Args:
        s: Input text
        remove_tone: Whether to remove tone marks
        
    Returns:
        Cleaned text
    """
    if not isinstance(s, str):
        return ""
        
    # Chuẩn hóa Unicode và lowercase
    s = normalize_unicode(s.lower().strip())
    
    # Xóa URLs và HTML
    s = re.sub(r"https?://\S+|www\.\S+", "", s)
    s = re.sub(r"<[^>]+>", "", s)
    
    # Xóa email
    s = re.sub(r"[\w\.-]+@[\w\.-]+", "", s)
    
    # Xóa số và ký tự đặc biệt nhưng giữ chữ tiếng Việt
    s = re.sub(r"[^\w\s\u00C0-\u1EF9]", " ", s)
    
    # Xóa khoảng trắng thừa
    s = re.sub(r"\s+", " ", s).strip()
    
    # Tùy chọn: xóa dấu
    if remove_tone:
        s = standardize_vietnamese(s)
    
    # Tokenize và loại stopwords
    tokens = word_tokenize(s)
    tokens = [t for t in tokens if t not in STOPWORDS]
    return " ".join(tokens)


def preprocess_texts(texts: List[str]) -> List[str]:
    return [clean_text(t) for t in texts]


def preprocess_df(df, text_col: str = "text", label_col: str = None):
    X = preprocess_texts(df[text_col].fillna("").astype(str).tolist())
    y = None
    if label_col and label_col in df.columns:
        y = df[label_col]
    return X, y
