
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify({
        "status": "ok",
        "time": datetime.datetime.utcnow().isoformat() + "Z"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
