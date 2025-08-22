from flask import Blueprint, jsonify, request
from src.services.printerService import PrinterService

printer_bp = Blueprint('printer', __name__)

@printer_bp.route('/', methods=['GET'])
def list_printers():
    try:
        return jsonify(PrinterService.get_printer_list()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@printer_bp.route('/<string:printer_name>/jobs', methods=['GET'])
def get_printer_jobs(printer_name):
    try:
        jobs = PrinterService.get_printer_list(printer_name)
        return jsonify(jobs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500