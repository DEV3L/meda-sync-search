from app.services.prescription_loader import PrescriptionLoader

def test_init_prescription_loader_service():
    expected_data_file_path = '/'
    prescription_loader = PrescriptionLoader(expected_data_file_path)

    assert prescription_loader
    assert expected_data_file_path == prescription_loader.data_file_path

