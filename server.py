from flask import Flask, jsonify, request
from flask_script import Manager

from app.prescription_drug_search.services.prescription_loader import PrescriptionLoader
from app.prescription_drug_search.services.search import Search

prescription_data_file_path = './data/prescription_data.csv'
app = Flask(__name__)
manager = Manager(app)


@app.route('/prescriptions')
def prescriptions():
    search_str = request.args.get('search', '')

    prescription_loader = PrescriptionLoader(prescription_data_file_path)
    _prescriptions = prescription_loader.prescriptions

    search = Search(search_str, _prescriptions)
    _prescriptions = search.results

    prescriptions_response = {
        '_search': search_str,
        '_search_fuzzy': search.fuzzy_value,
        'data': [prescription_data.__dict__ for prescription_data in _prescriptions]
    }

    return jsonify(prescriptions_response)


if __name__ == '__main__':
    manager.run()
