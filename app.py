from flask import Flask
from controllers.document_controller import document_blueprint
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

app.register_blueprint(document_blueprint)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)