from flask import Flask
from handlers.routes import configure_routes
import webview

app = Flask(__name__)
window = webview.create_window('iMatch Tool', app, height=300, width=500)

configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=1002, host='0.0.0.0')
    # webview.start(http_server=True, http_port=5000)

# Build .exe file
# pyinstaller --noconfirm --onefile --windowed "/Users/mac/PycharmProjects/flask-imatch/app.py"
