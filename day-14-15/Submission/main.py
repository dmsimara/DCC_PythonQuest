from flask import Flask, jsonify, request  

app = Flask(__name__)

aws_services = [
    {
        "id": 1,
        "service": "Lambda"
    },
    {
        "id": 2,
        "service": "Simple Storage Service(S3)"
    },
    {
        "id": 3,
        "service": "DynamoDB"
    },
    {
        'id': 4,
        "service": "IAM"
    }
]

# base url
@app.route('/', methods=['GET'])
def hello():
    return 'Hello. Welcome!'


# /aws_services/get_all
@app.route('/aws_services/get_all', methods=['GET'])
def get_all():
    return jsonify({"aws_services": aws_services})


# /aws_services/<int:service_id>
@app.route('/aws_services/<int:service_id>', methods=['GET'])
def get_service(service_id):

    service = next((a for a in aws_services if a['id'] == service_id), None)
    if service:
        return jsonify({"aws_service" : [service]})
    else:
        return jsonify({"Error" : "Service not found"}), 404


# /aws_services/add_service
@app.route('/aws_services/add_service', methods=['POST'])
def add_service():
    new_service = request.get_json()
    aws_services.append(new_service)
    return jsonify ({"Note" : "Service added successfully"})


# /aws_services/delete_service/<int:service_id>
@app.route('/aws_services/delete_service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    global aws_services
    aws_services = [a for a in aws_services if a['id'] != service_id]
    return jsonify({"Note" : "Service deleted successfully"})


# /aws_services/update_service/<int:service_id>
@app.route('/aws_services/update_service/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    service = next((a for a in aws_services if a['id'] == service_id), None)
    if service:
        updated_service = request.get_json()
        service.update(updated_service)
        return jsonify ({"Note" : "Service updated successfully"})
    else:
        return jsonify ({"Error" : "Service not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)