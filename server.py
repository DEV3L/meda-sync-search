from flask import Flask, jsonify, request
from flask import render_template
from flask_script import Manager

from app.meda_sync_search.services.equipment_loader import EquipmentLoader
from app.meda_sync_search.services.prescription_loader import PrescriptionLoader
from app.meda_sync_search.services.search import Search

prescription_data_file_path = './data/prescription_data.csv'
equipment_data_file_path = './data/equipment_data.csv'

app = Flask(__name__)

manager = Manager(app)


@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/prescriptions')
def prescriptions():
    search_response = _search('prescriptions')
    return jsonify(search_response)


@app.route('/equipment')
def equipment():
    search_response = _search('equipment', is_equipment=True)
    return jsonify(search_response)


@app.route('/search', methods=['GET', 'POST'])
def search():
    search_response = _search('search_prescription')
    return _render_template('prescriptions.jinja', search_response)


@app.route('/search_prescriptions', methods=['GET', 'POST'])
def search_prescription():
    search_response = _search('search_prescription')
    return _render_template('prescriptions.jinja', search_response)

@app.route('/search_equipment', methods=['GET', 'POST'])
def search_equipment():
    search_response = _search('search_equipment', is_equipment=True)
    return _render_template('equipment.jinja', search_response)


def _search(form_name, *, include_fuzzy=True, is_equipment=False):
    args = request.get_json() or request.values

    search_str = args.get('search', '')
    quantity_str = args.get('quantity', '')

    prescriptions_response = search_items(search_str, quantity_str, form_name,
                                          include_fuzzy=include_fuzzy, is_equipment=is_equipment)
    return prescriptions_response


def search_items(search_str, quantity_str, form_name, *, include_fuzzy=True, is_equipment=False):
    loader = _loader_factory(is_equipment)

    _items = loader.list
    search = Search(search_str, _items)

    if not include_fuzzy:
        search.value_fuzzy = None

    _items = search.results

    if quantity_str:
        quantity = int(quantity_str)

        for item in _items:
            if hasattr(item, 'cost_per_unit'):
                quantity_cost = quantity * item.cost_per_unit
                item.quantity_cost = f'{quantity_cost:.2f}'

    items_response = {
        'form_name': form_name,
        '_search': search_str,
        '_search_fuzzy': search.value_fuzzy,
        '_quantity': quantity_str,
        'data': [item.__dict__ for item in _items]
    }

    return items_response


def _render_template(template_name, _response):
    return render_template(template_name, **_response)


def _loader_factory(is_equipment):
    return EquipmentLoader(equipment_data_file_path) if is_equipment \
        else PrescriptionLoader(prescription_data_file_path)


if __name__ == '__main__':
    manager.run()
