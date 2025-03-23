from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/armstrong/<int:n>")
def armstrong(n):
    if n < 0:
        return jsonify({"error": "Input must be a non-negative integer"}), 400
    
    sum_of_digits = 0
    order = len(str(n))
    original_n = n

    while n > 0:
        digit = n % 10
        sum_of_digits += digit ** order
        n //= 10

    if sum_of_digits == original_n:
        result = {
            "Number": original_n,
            "Armstrong": True
        }
    else:
        result = {
            "Number": original_n,
            "Armstrong": False
        }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
