"""Model evaluation utilities."""
from typing import Dict, List
import os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_recall_fscore_support,
    confusion_matrix, classification_report, f1_score
)
import joblib

def evaluate_model(model, X, y, labels: List[str] = None, save_dir: str = None):
    """Evaluate model and optionally save results.
    
    Args:
        model: Trained model with predict method
        X: Features
        y: True labels
        labels: List of label names
        save_dir: Directory to save evaluation results
        
    Returns:
        Dictionary with metrics
    """
    y_pred = model.predict(X)
    
    # Calculate metrics
    acc = accuracy_score(y, y_pred)
    f1 = f1_score(y, y_pred, average="weighted")
    metrics = {"accuracy": acc, "f1": f1}
    
    # Print report
    print("\nClassification Report:")
    print("-" * 60)
    print(classification_report(y, y_pred, target_names=labels))
    
    # Plot confusion matrix
    if labels:
        plot_confusion_matrix(y, y_pred, labels)
        plt.show()
    
    # Save results if directory specified
    if save_dir:
        save_evaluation_results(y, y_pred, labels, save_dir)
        
    return metrics

def plot_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray, 
                         labels: List[str] = None, figsize=(10, 8)):
    """Plot confusion matrix with seaborn.
    
    Args:
        y_true: Ground truth labels
        y_pred: Predicted labels
        labels: List of label names
        figsize: Figure size
    """
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=figsize)
    sns.heatmap(
        cm, 
        annot=True, 
        fmt='d',
        cmap='Blues',
        xticklabels=labels,
        yticklabels=labels
    )
    plt.title('Ma trận nhầm lẫn (Confusion Matrix)')
    plt.xlabel('Dự đoán (Predicted)')
    plt.ylabel('Thực tế (True)')
    plt.tight_layout()

def save_evaluation_results(y_true: np.ndarray, y_pred: np.ndarray,
                          labels: List[str], save_dir: str):
    """Save evaluation results to files.
    
    Args:
        y_true: Ground truth labels
        y_pred: Predicted labels
        labels: List of label names
        save_dir: Directory to save results
    """
    # Create directory if not exists
    os.makedirs(save_dir, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save confusion matrix plot
    plt.figure(figsize=(10, 8))
    plot_confusion_matrix(y_true, y_pred, labels)
    plt.savefig(os.path.join(save_dir, f'confusion_matrix_{timestamp}.png'))
    plt.close()
    
    # Save metrics to text file
    metrics_file = os.path.join(save_dir, f'metrics_{timestamp}.txt')
    with open(metrics_file, 'w', encoding='utf-8') as f:
        f.write("Báo cáo phân loại:\n")
        f.write("-" * 60 + "\n")
        f.write(classification_report(y_true, y_pred, target_names=labels))
        
        metrics = {
            'accuracy': accuracy_score(y_true, y_pred),
            'f1': f1_score(y_true, y_pred, average='weighted')
        }
        f.write("\nMetrics tổng quát:\n")
        f.write("-" * 60 + "\n")
        for metric, value in metrics.items():
            f.write(f"{metric.title()}: {value:.4f}\n")

def load_model(path: str):
    """Load model from file.
    
    Args:
        path: Path to saved model
        
    Returns:
        Loaded model
    """
    return joblib.load(path)
