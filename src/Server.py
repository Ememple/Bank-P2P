from flask import Flask, render_template, request, jsonify
import os

from ReadConfig import ReadConfig
from MySQLStorage import MysqlStorage
from JsonStorage import JsonStorage
from Bank import Bank

app = Flask(__name__, static_folder='static')

tcp_server_instance = None
bank = None

if bank is None:
    try:
        try:
            config = ReadConfig.read_database_config()
            storage = MysqlStorage(config)
        except:
            storage = JsonStorage()
        bank = Bank(storage)
    except Exception:
        print("Couldn't connect to bank")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/accounts')
def api_get_accounts():
    accounts = bank.repo.get_all()
    data = [{"id": acc.id, "balance": acc.balance} for acc in accounts]
    return jsonify(data)

@app.route('/create_account', methods=['POST'])
def api_create_account():
    try:
        new_id = bank.create_account()
        return jsonify({"success": True, "id": new_id})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/transaction', methods=['POST'])
def api_transaction():
    data = request.json
    acc_id = int(data.get('id'))
    amount = int(data.get('amount'))
    action = data.get('action')

    try:
        if action == 'deposit':
            bank.deposit(acc_id, amount)
        elif action == 'withdraw':
            bank.withdraw(acc_id, amount)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/shutdown', methods=['POST'])
def shutdown():
    if tcp_server_instance:
        try:
            tcp_server_instance.stop()
        except Exception as e:
            print(f"Error stopping TCP server: {e}")

    os._exit(0)

if __name__ == '__main__':
    app.run(debug=True, port=8080)