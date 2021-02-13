import io

from flask import send_file

from . import app, local_storage_manager


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/api/documentation', methods=['GET'])
def get_documentation():
    return send_file(io.BytesIO(local_storage_manager.get_api_documentation()),
                     mimetype='text/yaml', attachment_filename='api_documentation.yaml', as_attachment=True)
