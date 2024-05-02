import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data from the CSV file
data = pd.read_csv('data.csv')

# Drop rows with missing values
data.dropna(inplace=True)

# Split the data into features (text) and labels (sentiment)
X = data['text']        # Accuracy with 'text  is 0.64 and with 'selected_text' is 0.77
y = data['sentiment']

# Convert the text data into a matrix of token counts
vectorizer = CountVectorizer()
X_counts = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_counts, y, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = nb_classifier.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)