from flask import Flask, render_template, request, jsonify

from ReadConfig import ReadConfig
from MySQLStorage import MysqlStorage
from JsonStorage import JsonStorage
from Bank import Bank

app = Flask(__name__, static_folder='static')

def get_bank_service():
    try:
        config = ReadConfig.read_config()
        storage = MysqlStorage(config)
    except Exception:
        storage = JsonStorage()
    return Bank(storage)

bank = get_bank_service()

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)