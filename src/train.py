"""Training utilities.
Provides a simple baseline training pipeline using TF-IDF + LogisticRegression.
Keep notebooks thin: they call run_training() or train_and_save_model().
"""
import os
from pathlib import Path
from typing import Optional

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from src.preprocess import preprocess_df


def train_and_save_model(df, text_col: str = "text", label_col: str = "label", model_dir: str = "models") -> str:
    Path(model_dir).mkdir(parents=True, exist_ok=True)
    X, y = preprocess_df(df, text_col=text_col, label_col=label_col)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=20000)),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    pipe.fit(X_train, y_train)

    model_path = Path(model_dir) / "baseline_model.joblib"
    joblib.dump(pipe, model_path)
    print(f"Saved model to {model_path}")
    return str(model_path)


def run_training(data_path: Optional[str] = None, text_col: str = "text", label_col: str = "label"):
    import pandas as pd
    if data_path is None:
        data_path = "data/data.csv"
    df = pd.read_csv(data_path)
    return train_and_save_model(df, text_col=text_col, label_col=label_col)
