from flask import Flask, send_file
import os
from werkzeug.serving import run_simple
from flask import send_from_directory


class FileServer:
    def __init__(self, root_dir):
        self.app = Flask(__name__)
        self.root_dir = root_dir

        @self.app.route('/<path:filename>')
        def download_file(filename):
            file_path = os.path.join(self.root_dir, filename)
            return send_from_directory(self.root_dir, filename, as_attachment=False, mimetype='audio/mpeg')
        @self.app.route('/xml/<path:filename>')
        def display_xml(filename):
            xml_path = os.path.join(self.root_dir, filename)
            return send_from_directory(self.root_dir, filename, as_attachment=False, mimetype='application/xml')
        @self.app.route('/favicon.ico')
        def ignore_favicon():
            return "", 204  # 返回空响应，状态码204表示请求成功，但没有内容

    def start(self, host, port):
        run_simple(host, port, self.app, use_reloader=False, threaded=True)



