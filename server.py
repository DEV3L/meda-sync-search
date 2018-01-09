from flask import Flask, jsonify, request
from flask import render_template
from flask_script import Manager

from app.prescription_drug_search.services.prescription_loader import PrescriptionLoader
from app.prescription_drug_search.services.search import Search

prescription_data_file_path = './data/prescription_data.csv'
app = Flask(__name__)
manager = Manager(app)


@app.route('/prescriptions')
def prescriptions():
    search_str = request.args.get('search', '')
    prescriptions_response = search_prescriptions(search_str, 'prescriptions')
    return jsonify(prescriptions_response)


@app.route('/search', methods=['GET', 'POST'])
def search():
    return _search('search')


@app.route('/search_description', methods=['GET', 'POST'])
def search_description():
    return _search('search_description', include_fuzzy=False)


def _search(route, *, include_fuzzy=True):
    args = request.get_json() or request.values
    search_str = args.get('search', '')
    prescriptions_response = search_prescriptions(search_str, route, include_fuzzy=include_fuzzy)
    return render_template('prescriptions.jinja', **prescriptions_response)


def search_prescriptions(search_str, form_name, *, include_fuzzy=True):
    prescription_loader = PrescriptionLoader(prescription_data_file_path)
    _prescriptions = prescription_loader.prescriptions
    search = Search(search_str, _prescriptions)

    if not include_fuzzy:
        search.value_fuzzy = None

    _prescriptions = search.results

    prescriptions_response = {
        'form_name': form_name,
        '_search': search_str,
        '_search_fuzzy': search.value_fuzzy,
        'data': [prescription_data.__dict__ for prescription_data in _prescriptions]
    }

    return prescriptions_response


if __name__ == '__main__':
    manager.run()
