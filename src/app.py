import os
from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health_check():
    # The app expects an environment variable named 'APP_ENV'
    env_status = os.environ.get('APP_ENV', 'MISSING_ENV_VARIABLE')
    return f"Status: OK | Environment: {env_status}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)