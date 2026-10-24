# Project Report: News Category Classification

## Objective
Classify news articles into four categories using DistilBERT.

## Dataset
AG News contains World, Sports, Business, and Sci/Tech categories.

## Results
Recorded official test accuracy was 94.79%, with macro F1 of 94.80%.

## Innovation
Character-swap typo augmentation was evaluated on validation data.
Corrupted-text accuracy changed from 94.38% to 94.39%.
Clean validation accuracy changed from 94.69% to 94.52%.
The observed robustness gain was small.

## Limitations
Only one synthetic corruption method was evaluated.
More corruption types and external datasets would strengthen the evaluation.
