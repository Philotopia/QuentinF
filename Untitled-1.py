from flask import Flask, request, jsonify

app = Flask(__name__)

vpn_data = {}  # Dictionnaire pour stocker les données des utilisateurs et leurs VPN

@app.route('/update_vpn', methods=['POST'])
def update_vpn():
    username = request.form.get('username')
    vpn_name = request.form.get('vpn_name')
    vpn_data[username] = vpn_name
    return 'Updated', 200

@app.route('/get_vpn_names', methods=['GET'])
def get_vpn_names():
    return jsonify(vpn_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
