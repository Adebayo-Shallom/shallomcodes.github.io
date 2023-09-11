from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.now().strftime('%A')

    # Get current UTC time with +/-2 minute validation
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct response JSON
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time,
        "track": track,
        "github_file_url": "https://github.com/Adebayo-Shallom/shallomcodes.github.io/blob/main/endpoint/endpoint/app.py",
        "github_repo_url": "https://github.com/Adebayo-Shallom/shallomcodes.github.io",
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
