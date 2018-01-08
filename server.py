from flask import Flask, jsonify, request
from flask_script import Manager

from app.prescription_drug_search.services.prescription_loader import PrescriptionLoader
from app.prescription_drug_search.transformers.str_transformer import StrTransformer

prescription_data_file_path = './data/prescription_data.csv'
app = Flask(__name__)
manager = Manager(app)


@app.route('/prescriptions')
def prescriptions():
    search = request.args.get('search', '')

    prescription_loader = PrescriptionLoader(prescription_data_file_path)
    _prescriptions = prescription_loader.prescriptions

    if search:
        search_prescriptions = [prescription for prescription in _prescriptions
                                if search.lower() in prescription.description.lower()]

        fuzzy_search = StrTransformer(search).fuzzy
        fuzzy_prescriptions = [prescription for prescription in _prescriptions
                               if prescription.fuzzy.startswith(fuzzy_search)]

        fuzzy_prescriptions.extend(search_prescriptions)

        _prescriptions = list(set(fuzzy_prescriptions))

    return jsonify([prescription_data.__dict__ for prescription_data in _prescriptions])


if __name__ == '__main__':
    manager.run()
