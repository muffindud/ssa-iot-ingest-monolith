from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from repository.iot_data import publish_data


iot_ingest_bp = Blueprint('iot_ingest', __name__)


@iot_ingest_bp.route('/publish', methods=['POST'])
@jwt_required()
def iot_publish():
    identity = get_jwt_identity()

    if identity['role'] != 'device':
        return {
            "message": "Unauthorized"
        }, 403

    device_id = identity['device_id']
    body = request.get_json()

    publish_data(device_id, body)

    return {
        "message": "Data published successfully"
    }, 200
