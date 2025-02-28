from flask import Flask, render_template, request, jsonify
import random
import os
from src import script
app = Flask(__name__)

@app.route('/')
def index():
    resume = script.generate_random_resume()
    script.save_resume(resume)
    return render_template('index.html', resume=resume)

@app.route('/update', methods=['POST'])
def update_resume():
    data = request.json
    script.save_resume(data)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)