from flask import Blueprint, jsonify, render_template, request, Response
from .generate import generate_bio

main = Blueprint('main', __name__)

@main.route('/api/generate/', methods=['POST'])
def generate_bio_api() -> Response:
    try:
        if request.is_json:
            description = request.json
            if 'description' not in description:
                return jsonify({'error': 'Missing description'}), 400
            response = generate_bio(description['description'])
            if response['status']:
                return jsonify(response)
            else:
                return jsonify(response), 400
        else:
            return jsonify({'error': 'Request must be JSON'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/')
def index() -> str:
    return render_template('index.html')

@main.route('/api/generate/', methods=['GET'])
def generate_bio_get() -> Response:
    return jsonify({"error": "Method Not Allowed"}), 405
