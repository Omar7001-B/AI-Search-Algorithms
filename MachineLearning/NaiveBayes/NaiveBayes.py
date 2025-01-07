import csv
import numpy as np

# Load data from CSV file
def load_data(file_name):
    texts = []
    sentiments = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        table_header = next(reader)
        text_idx = table_header.index('text')
        sentiment_idx = table_header.index('sentiment')
        next(reader)  # skip header
        for row in reader:
            texts.append(row[text_idx])
            sentiments.append(row[sentiment_idx])
    return texts, sentiments

# Preprocess text data
def preprocess(texts):
    preprocessed_texts = []
    for text in texts:
        # Convert text to lowercase and split into words
        words = text.lower().split()
        preprocessed_texts.append(words)
    return preprocessed_texts

# Extract features
def extract_features(texts):
    word_set = set()
    for text in texts:
        for word in text:
            word_set.add(word)
    features = list(word_set)
    return features

# Calculate probabilities for Naive Bayes
def calculate_probabilities(texts, sentiments, features):
    num_texts = len(texts)
    num_features = len(features)
    num_classes = len(set(sentiments))
    # Initialize counts
    class_counts = {c: 0 for c in set(sentiments)}
    feature_counts = {c: {feature: 0 for feature in features} for c in set(sentiments)}
    # Count occurrences
    for i in range(num_texts):
        text = texts[i]
        sentiment = sentiments[i]
        class_counts[sentiment] += 1
        for word in text:
            feature_counts[sentiment][word] += 1
    # Calculate probabilities
    class_probs = {c: class_counts[c] / num_texts for c in class_counts}
    feature_probs = {c: {feature: (feature_counts[c][feature] + 1) / (class_counts[c] + num_features) for feature in features} for c in class_counts}
    return class_probs, feature_probs

# Train Naive Bayes classifier
def train_naive_bayes(texts, sentiments):
    preprocessed_texts = preprocess(texts)
    features = extract_features(preprocessed_texts)
    class_probs, feature_probs = calculate_probabilities(preprocessed_texts, sentiments, features)
    return class_probs, feature_probs, features

# Predict sentiment for a given text
def predict_sentiment(text, class_probs, feature_probs, features):
    text = text.lower().split()
    scores = {c: np.log(class_probs[c]) for c in class_probs}
    for c in class_probs:
        for word in text:
            if word in features:
                scores[c] += np.log(feature_probs[c][word])
    return max(scores, key=scores.get)

# Load data
texts, sentiments = load_data('data.csv')

# Train Naive Bayes classifier
class_probs, feature_probs, features = train_naive_bayes(texts, sentiments)

# Make predictions
text = "This is a great movie"
predicted_sentiment = predict_sentiment(text, class_probs, feature_probs, features)
print("Predicted sentiment:", predicted_sentiment)
