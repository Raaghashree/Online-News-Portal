from flask import Flask, request, jsonify, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'supersecretkey'  
CORS(app)

users = {'admin': 'password123', 'user': 'userpass'}

news_articles = {
    'sports': [{'title': 'Sports News 1', 'content': 'Content of sports news 1'}],
    'technology': [{'title': 'Tech News 1', 'content': 'Content of tech news 1'}],
    'politics': [{'title': 'Politics News 1', 'content': 'Content of politics news 1'}]
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username, password = data.get('username'), data.get('password')
    if username in users and users[username] == password:
        session['user'] = username
        return jsonify({'message': 'Login successful', 'status': 'success'})
    return jsonify({'message': 'Invalid credentials', 'status': 'fail'})

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    return jsonify({'message': 'Logged out successfully'})

@app.route('/news/<category>', methods=['GET'])
def get_news(category):
    if 'user' not in session:
        return jsonify({'message': 'Unauthorized', 'status': 'fail'}), 401
    return jsonify({'articles': news_articles.get(category, [])})

if __name__ == '__main__':
    app.run(debug=True)
