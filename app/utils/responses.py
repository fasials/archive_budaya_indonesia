from flask import jsonify


def error(message, status):
    """Format error standar: {"error": "..."}"""
    return jsonify({"error": message}), status