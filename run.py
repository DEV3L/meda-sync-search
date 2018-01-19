from app.meda_sync_search.services.prescription_loader import PrescriptionLoader
from app.meda_sync_search.transformers.prescriptions_data_transformer import PrescriptionsDataTransformer

if __name__ == '__main__':
    prescription_data_file_path = './data/prescription_data.csv'
    prescription_loader = PrescriptionLoader(prescription_data_file_path)
    prescriptions_data = prescription_loader.prescriptions_data

    prescriptions_data_transformer = PrescriptionsDataTransformer(prescriptions_data)
    prescriptions = prescriptions_data_transformer.transform()

    print('Done')
