from flask import Flask, render_template, request, jsonify
import os
from src import resume_generator

app = Flask(__name__)

@app.route('/')
def index():
    # При первом запуске отображаем информацию о профиле xyzfbi
    username = "xyzfbi"
    resume_data = resume_generator.generate_resume(username)
    return render_template('index.html', data=resume_data)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    username = request.json.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        resume_data = resume_generator.generate_resume(username)
        return jsonify(resume_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)