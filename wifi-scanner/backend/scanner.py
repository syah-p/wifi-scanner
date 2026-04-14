import os
import subprocess
import re
from flask import Flask, jsonify

app = Flask(__name__)

def get_wifi_list():
    if os.name == 'posix':  # Linux/Android (Termux)
        result = subprocess.check_output(['nmcli', 'dev', 'wifi'])
        networks = re.findall(r'([^\s]+)\s+([^\s]+)\s+([^\s]+)', result.decode())
        return [{'SSID': n[0], 'Signal': n[1], 'Security': n[2]} for n in networks]
    elif os.name == 'nt':  # Windows
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
        networks = re.findall(r'([^\s]+)\s+([^\s]+)', result.decode())
        return [{'SSID': n[0], 'Signal': n[1]} for n in networks]
    return []

@app.route('/scan')
def scan():
    return jsonify(get_wifi_list())

@app.route('/get_password/<ssid>')
def get_password(ssid):
    if os.name == 'posix':
        result = subprocess.check_output(['sudo', 'nmcli', 'connection', 'show', ssid])
        password = re.search(r'security\.802-1x\.password=(\S+)', result.decode())
    elif os.name == 'nt':
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'])
        password = re.search(r'Key Content\s+:\s+(\S+)', result.decode())
    return jsonify({'password': password.group(1) if password else 'Tidak ditemukan'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)