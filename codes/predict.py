import argparse
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

parser = argparse.ArgumentParser()
parser.add_argument('--text', required=True)
parser.add_argument('--model_dir', default='models/distilbert')
args = parser.parse_args()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = AutoTokenizer.from_pretrained(args.model_dir)
model = AutoModelForSequenceClassification.from_pretrained(args.model_dir)
model.to(device).eval()
inputs = tokenizer(args.text, return_tensors='pt', truncation=True, max_length=192)
inputs = {k: v.to(device) for k, v in inputs.items()}
with torch.no_grad():
    probabilities = torch.softmax(model(**inputs).logits, dim=-1)[0]
idx = int(probabilities.argmax().item())
labels = model.config.id2label
label = labels.get(idx, labels.get(str(idx), str(idx)))
print('Predicted category:', label)
print('Confidence:', round(probabilities[idx].item(), 4))
