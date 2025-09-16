from flask import Blueprint, request, jsonify

workflow_bp = Blueprint('workflow', __name__)

# Minimal example: create a leave request
WORKFLOW_STORE = []


@workflow_bp.route('/requests', methods=['POST'])
def create_request():
    data = request.get_json() or {}
    # expected: requester_id, type, start_date, end_date, reason
    WORKFLOW_STORE.append(data)
    return jsonify({'status': 'created', 'data': data}), 201


@workflow_bp.route('/requests', methods=['GET'])
def list_requests():
    return jsonify(WORKFLOW_STORE)
