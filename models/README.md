## Trained Models

The trained model weights are hosted on Hugging Face because of their large file sizes.

| Model | Description | Model Files |
|---|---|---|
| DistilBERT | Baseline AG News classifier | [View on Hugging Face](https://huggingface.co/GiJayByte/distilbert-news-classifier) |
| Augmented DistilBERT | Classifier trained with augmented data | [View on Hugging Face](https://huggingface.co/GiJayByte/augmenteddistilbert-news-classifier) |

Both repositories contain the trained model weights, configuration, and tokenizer files required to load the models.

### Model Loading

The models can be loaded using the Hugging Face Transformers library. Install the dependencies listed in the project requirements before running the inference code.
