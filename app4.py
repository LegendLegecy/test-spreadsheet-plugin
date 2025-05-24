# app.py
from flask import Flask, request, jsonify
import main4  # your existing Google Sheets Python code

app = Flask(__name__)

@app.route('/run-script', methods=['POST'])
def run_script():
    result = main4.run()  # or whatever function your code uses
    return jsonify({"status": "success", "result": result})

if __name__ == '__main__':
    app.run(debug=True)
