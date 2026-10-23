# News Category Classification Using DistilBERT

Registration Number: 2430010355

## Objective
Classify news articles into World, Sports, Business, and Sci/Tech.

## Dataset
- Dataset: AG News
- Hugging Face ID: fancyzhx/ag_news
- Training samples: 108,000
- Validation samples: 12,000
- Official test samples: 7,600
- Random seed: 42

## Models
- TF-IDF + Logistic Regression
- TF-IDF + Linear SVM
- Fine-tuned DistilBERT
- DistilBERT with typo augmentation

## Recorded official test results
- Accuracy: 94.79%
- Macro precision: 94.81%
- Macro recall: 94.79%
- Macro F1: 94.80%
- Multiclass ROC-AUC: 99.33%

## Robustness experiment
- Standard model, clean validation accuracy: 94.69%
- Standard model, typo-corrupted accuracy: 94.38%
- Augmented model, clean validation accuracy: 94.52%
- Augmented model, typo-corrupted accuracy: 94.39%
- The measured improvement on corrupted text was small.

## Folder structure
- notebooks/: experiment notebook
- code/: prediction script
- models/: saved model checkpoints
- results/: evaluation metrics and tables
- figures/: plots
- reports/: report draft
- resources/: dataset and experiment information

## Reproducibility
See requirements.txt for installed package versions.
Run the notebook in Google Colab with a GPU runtime.

## References
- DistilBERT: https://arxiv.org/abs/1910.01108
- AG News: https://huggingface.co/datasets/fancyzhx/ag_news
