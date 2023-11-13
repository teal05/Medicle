from flask import Flask, render_template, request

app = Flask(__name__)

patients = {
    "patient1": {"name": "Sanhawit", "medication": ["Aspirin", "Antibiotic"], "status": "Healthy"},
    "patient2": {"name": "Tle", "medication": ["Painkiller"], "status": "Sick"},
    "patient3": {"name": "John", "medication": ["Cough Syrup", "Antihistamine"], "status": "Sick"},
    "patient4": {"name": "Jane", "medication": ["Vitamin C", "Painkiller"], "status": "Healthy"},
    "patient5": {"name": "Bob", "medication": ["Antibiotic", "Painkiller"], "status": "Sick"},
    "patient6": {"name": "Alice", "medication": ["Aspirin", "Cough Syrup"], "status": "Healthy"},
    "patient7": {"name": "Eve", "medication": ["Paracetamol", "Antihistamine"], "status": "Healthy"},
    "patient8": {"name": "Charlie", "medication": ["Antibiotic", "Painkiller"], "status": "Sick"},
    "patient9": {"name": "Grace", "medication": ["Vitamin D", "Cough Syrup"], "status": "Sick"},
    "patient10": {"name": "David", "medication": ["Aspirin", "Painkiller"], "status": "Healthy"},
    "patient11": {"name": "Emma", "medication": ["Paracetamol", "Antibiotic"], "status": "Healthy"},
    "patient12": {"name": "Frank", "medication": ["Vitamin C", "Painkiller"], "status": "Sick"},
}

@app.route('/')
def home():
    return render_template('home.html', patients=patients)

@app.route('/dispense_medication', methods=['POST'])
def dispense_medication():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        medication = request.form['medication']

        if patient_id in patients and medication in patients[patient_id]['medication']:
            status = patients[patient_id]['status']
            return f"Dispensing {medication} to {patients[patient_id]['name']} ({status}) completed."
        else:
            return "Invalid patient or medication."

if __name__ == '__main__':
    app.run(debug=True)
