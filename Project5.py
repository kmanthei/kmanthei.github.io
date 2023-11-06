from flask import Flask, jsonify, request
import hashlib
import math
import requests

app = Flask(__name__)

@app.route('/md5/<string:text>', methods=['GET'])
def md5(text):
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return jsonify(input=text, output=md5_hash)

@app.route('/factorial/<int:n>', methods=['GET'])
def factorial(n):
    if n < 0:
        return jsonify(input=n, output="Error: Input must be a non-negative integer")
    result = math.factorial(n)
    return jsonify(input=n, output=result)

@app.route('/fibonacci/<int:n>', methods=['GET'])
def fibonacci(n):
    if n < 0:
        return jsonify(input=n, output="Error: Input must be a non-negative integer")
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return jsonify(input=n, output=fib_sequence)

@app.route('/is-prime/<int:n>', methods=['GET'])
def is_prime(n):
    if n <= 1:
        return jsonify(input=n, output=False)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return jsonify(input=n, output=False)
    return jsonify(input=n, output=True)

@app.route("/slack-alert/<string>")
import requests 
import sys
import getopt

#Send Slack Message using Slack APUI 

def send_slack_message(message):
	payload = '{"text":"%s"}' % message
	response = requests.post('https://hooks.slack.com/services/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',
							 data=payload)
	print(response.text)
def main(argv):

	message = ''
	
	try: opts, args = getopt.getopt(argv, "hm:" , ["message="])
	
	except getopt.GetoptError:
		print('Slackmessage.py -m <message>')
		sys.exit(2)
	if len(opts) == 0:
		message = "HELLO, WORLD!"
	for opt, arg in opts:
		if opt == '-h' :
			print('SlackMessage.py -m <message>')
			sys.exit()
		elif opt in ("-m", "--message"):
			message = arg
			
	send_slack_message(message)
	
if __name__ == "__main__":
	main(sys.argv[1:])