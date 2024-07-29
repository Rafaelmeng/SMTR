from flask import jsonify, current_app as app
from scripts.prtg_fetcher import Request

def fetch_prtg_data(fetch_method):
    try:
        # Obtenção dos dados do PRTG
        request = Request()
        prtg_data = getattr(request, fetch_method)()

        return jsonify(prtg_data)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/<data_type>', methods=['GET'])
def get_prtg_data(data_type):
    valid_methods = {
        'backbone': 'get_backbone',
        'ops': 'get_ops',
        'anel': 'get_anel',
        'pps': 'get_pps'
    }
    
    if data_type not in valid_methods:
        return jsonify({"error": "Invalid data type"}), 400

    fetch_method = valid_methods[data_type]
    return fetch_prtg_data(fetch_method)
