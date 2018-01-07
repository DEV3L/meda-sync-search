from flask import Flask, jsonify, request
from flask_script import Manager

from app.prescription_drug_search.services.prescription_loader import PrescriptionLoader
from app.prescription_drug_search.transformers.prescriptions_data_transformer import PrescriptionsDataTransformer
from app.prescription_drug_search.transformers.str_transformer import StrTransformer

prescription_data_file_path = './data/prescription_data.csv'
app = Flask(__name__)
manager = Manager(app)


@app.route('/prescriptions')
def prescriptions():
    search = request.args.get('search', '')

    prescription_loader = PrescriptionLoader(prescription_data_file_path)
    prescriptions_data_transformer = PrescriptionsDataTransformer(prescription_loader.prescriptions_data)
    prescriptions = prescriptions_data_transformer.transform()

    if not search:
        _prescriptions = prescriptions
    else:
        fuzzy_search = StrTransformer(search).fuzzy
        _prescriptions = [
            prescription for prescription in prescriptions
            if prescription.fuzzy.startswith(fuzzy_search) or
            (len(search) > 3 and search in prescription.description)
            ]

    return jsonify([prescription_data.__dict__ for prescription_data in _prescriptions])

if __name__ == '__main__':
    manager.run()
