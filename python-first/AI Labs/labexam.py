class NaiveBayesClassifier:
    def __init__(self, data):
        self.data = data
        self.classes = list(set(row[-1] for row in data))
        self.class_probabilities = {}
        self.feature_probabilities = {}

    def calculate_prior_probabilities(self):
        total_instances = len(self.data)
        for class_label in self.classes:
            class_instances = [row for row in self.data if row[-1] == class_label]
            self.class_probabilities[class_label] = len(class_instances) / total_instances

    def calculate_conditional_probabilities(self):
        features_count = len(self.data[0]) - 1
        for class_label in self.classes:
            class_instances = [row for row in self.data if row[-1] == class_label]
            class_feature_probabilities = {}
            for i in range(features_count):
                feature_values = list(set(row[i] for row in class_instances))
                feature_prob = {}
                for value in feature_values:
                    count = sum(1 for row in class_instances if row[i] == value)
                    feature_prob[value] = count / len(class_instances)
                class_feature_probabilities[i] = feature_prob
            self.feature_probabilities[class_label] = class_feature_probabilities

    def predict(self, instance):
        probabilities = {}
        for class_label in self.classes:
            class_probability = self.class_probabilities[class_label]
            feature_probabilities = self.feature_probabilities[class_label]
            probability = class_probability
            for i, value in enumerate(instance):
                if i in feature_probabilities and value in feature_probabilities[i]:
                    probability *= feature_probabilities[i][value]
            probabilities[class_label] = probability
        return max(probabilities, key=probabilities.get)


 # according to this data the result will be produced 
    # as per the shortage of time I made the data small so the result will be given according to this data
training_data = [
    ['<=30', 'high', 'no', 'fair', 'no'],
    ['<=30', 'high', 'yes', 'excellent', 'no'],
    ['31...40', 'high', 'no', 'fair', 'yes'],
    ['>40', 'medium', 'yes', 'fair', 'yes'],
    ['>40', 'low', 'yes', 'excellent', 'yes']
    # ['age', 'income', 'student', 'credit_rating', 'buys_computer']

    ]


new_instance = ['<=30', 'excellent', 'yes', 'fair']

naive_bayes = NaiveBayesClassifier(training_data)
naive_bayes.calculate_prior_probabilities()
naive_bayes.calculate_conditional_probabilities()
prediction = naive_bayes.predict(new_instance)
print("Predicted class:", prediction)