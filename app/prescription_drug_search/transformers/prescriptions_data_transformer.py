from app.prescription_drug_search.transformers.prescription_data_transformer import PrescriptionDataTransformer


class PrescriptionsDataTransformer:
    def __init__(self, prescriptions_data):
        self.prescriptions_data = prescriptions_data

    def transform(self):
        prescriptions = []

        for prescription_data in self.prescriptions_data:
            prescription = PrescriptionDataTransformer(prescription_data).transform()
            prescriptions.append(prescription)

        return prescriptions
