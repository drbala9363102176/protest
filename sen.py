from transformers import pipeline

# Specify the model name explicitly
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline("text-classification", model=model_name)

# Use the classifier on your text
result = classifier("Meeting at 6 pm .")
print(result)


