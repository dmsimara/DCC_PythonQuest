from flask import Flask, jsonify  

app = Flask(__name__)

my_info = {
    "name": "Daniella",
    "course_and_section": "BSIT 1-5",
    "favorite_programming language": "Python",
    "aws_service": "AWS DynamoDB"
}

@app.route('/', methods=['GET'])
def get_info():
    return (my_info)

if __name__ == '__main__':
    app.run(debug=True)