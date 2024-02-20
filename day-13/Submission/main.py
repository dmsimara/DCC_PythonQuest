import csv
from flask import Flask, jsonify  

app = Flask(__name__)

csv_file = 'programming_languages.csv'

def read_csv(csv_file):
    
    content = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            content.append(row)

    return (content)

@app.route('/', methods=['GET'])
def get_langs():

    content = read_csv(csv_file)
    return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)