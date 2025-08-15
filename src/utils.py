"""Utility functions for Vietnamese text processing."""
import re
import unicodedata
from typing import List

def remove_tone_marks(text: str) -> str:
    """Remove Vietnamese tone marks, keeping base characters.
    
    Args:
        text: Input text with tone marks
        
    Returns:
        Text with tone marks removed
    """
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    return text

def normalize_unicode(text: str) -> str:
    """Normalize Unicode text to canonical form NFKC.
    
    Args:
        text: Input text
        
    Returns:
        Normalized text
    """
    return unicodedata.normalize('NFKC', text)

def standardize_vietnamese(text: str) -> str:
    """Standardize common Vietnamese text variations.
    
    Args:
        text: Input text
        
    Returns:
        Standardized text
    """
    patterns = {
        '[áàảãạăắằẳẵặâấầẩẫậ]': 'a',
        '[éèẻẽẹêếềểễệ]': 'e',
        '[óòỏõọôốồổỗộơớờởỡợ]': 'o',
        '[íìỉĩị]': 'i',
        '[úùủũụưứừửữự]': 'u',
        '[ýỳỷỹỵ]': 'y',
        'đ': 'd',
    }
    
    text = normalize_unicode(text)
    for pattern, replacement in patterns.items():
        text = re.sub(pattern, replacement, text)
    return text
