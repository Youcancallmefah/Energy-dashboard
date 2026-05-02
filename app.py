from flask import Flask, jsonify
from generate_energy_data import generate_energy_data

app = Flask(__name__)

#--ROUTE---
@app.route("/api/energy", methods=["GET"])
def get_energy():
    data = generate_energy_data() #  ฟังก์ชันจาก Step 1
    return jsonify(data)            #แปลงเป็น JSON ส่งออก

#--- RUN SERVER ---
if __name__ == "__main__":
   app.run(debug=True)