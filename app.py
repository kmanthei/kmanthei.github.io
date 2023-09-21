from flask import Flask, request, jsonify
import hashlib
import math

app = Flask(__name__)

@app.route('/md5/<string:text>', methods=['GET'])
def calculate_md5(text):
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return jsonify({"md5_hash": md5_hash})

@app.route('/factorial/<int:num>', methods=['GET'])
def calculate_factorial(num):
    if num < 0:
        return jsonify({"error": "Factorial is not defined for negative numbers"}), 400

    try:
        factorial_result = math.factorial(num)
        return jsonify({"factorial": factorial_result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide a valid non-negative integer."}), 400

@app.route('/fibonacci/<int:num>', methods=['GET'])
def calculate_fibonacci(num):
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    fibonacci_sequence = [fibonacci(i) for i in range(num+1)]
    return jsonify({"fibonacci_sequence": fibonacci_sequence})

@app.route('/is-prime/<int:num>', methods=['GET'])
def check_prime(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    is_prime_result = is_prime(num)
    return jsonify({"is_prime": is_prime_result})

@app.route('/slack-alert/<string:message>', methods=['POST'])
def send_slack_alert(message):
   
    return jsonify({"message": f"Slack alert sent: {message}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
