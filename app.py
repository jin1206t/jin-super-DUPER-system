import os
from flask import Flask, render_template, request, redirect, url_for
from google.cloud import firestore

# Set the environment variable to point to your service account key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'serviceAccountKey.json'

app = Flask(__name__)

# Initialize Firestore
db = firestore.Client(database="jin-note-page")

@app.route('/')
def home():
    # Fetch messages from Firestore
    messages_ref = db.collection('messages')
    messages = messages_ref.stream()
    return render_template('index.html', messages=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    message_content = request.form['message']
    # Add message to Firestore
    messages_ref = db.collection('messages')
    messages_ref.add({'content': message_content})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
