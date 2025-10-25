from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required


user_access_bp = Blueprint('user_access', __name__)

@user_access_bp.route('/retrieve', methods=['GET'])
@jwt_required()
def user_retrieve():
    current_user = get_jwt_identity()
    return {"message": "User Data Access Endpoint", "user": current_user}, 200

@user_access_bp.route('/truncate', methods=['DELETE'])
def user_truncate():
    # TODO: Implement posgres and mongodb truncate logic here
    return {"message": "User Truncate Endpoint"}, 200
