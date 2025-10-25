from flask import Blueprint


user_access_bp = Blueprint('user_access', __name__)

@user_access_bp.route('/retrieve', methods=['GET'])
def user_retrieve():
    # TODO: Implement user data access logic here
    return "User Data Access Endpoint"

@user_access_bp.route('/truncate', methods=['DELETE'])
def user_truncate():
    # TODO: Implement posgres and mongodb truncate logic here
    return "User Truncate Endpoint"
