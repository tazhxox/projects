# backend.py

from FlaskDemo import Flask, request, jsonify 

app = Flask(__name__)

class PhishingClassifier:
    def __init__(self):
        pass

    def train(self):
        # Dummy training function
        pass

    def predict(self, url):
        # Dummy prediction function
        # Simple classification based on URL length and presence of certain characteristics
        if len(url) > 50:
            return True # Phishing
        elif '@' in url or '-'in url:
            return True # Phishing
        else:
            return False # Legit
        
classifier = PhishingClassifier()
classifier.train()

@app.route('/classify', methods=['POST'])
def classify_url():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL not provided'}), 400
    

    is_phishing = classifier.predict(url)
    return jsonify({'url': url,  'is_phishing': is_phishing})

if __name__ == '__main__':
    app.run(debug=True)
