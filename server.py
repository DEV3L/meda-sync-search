from flask import Flask, jsonify
from flask_script import Manager

from app.prescription_drug_search.services.prescription_loader import PrescriptionLoader
from app.prescription_drug_search.transformers.prescriptions_data_transformer import PrescriptionsDataTransformer

prescription_data_file_path = './data/prescription_data.csv'
app = Flask(__name__)
manager = Manager(app)


@app.route('/prescriptions')
def prescriptions():
    prescription_loader = PrescriptionLoader(prescription_data_file_path)
    prescriptions_data_transformer = PrescriptionsDataTransformer(prescription_loader.prescriptions_data)
    return jsonify([prescription_data.__dict__ for prescription_data in prescriptions_data_transformer.transform()])

if __name__ == '__main__':
    manager.run()
