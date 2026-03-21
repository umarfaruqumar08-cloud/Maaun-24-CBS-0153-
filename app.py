from flask import Flask, render_template, request, redirect, flash

# Import our classes from models.py
from models import Patient, ClinicQueue

# Create the Flask application
app = Flask(__name__)
app.secret_key = 'my-secret-key-123'  # Needed for flash messages

# Create ONE queue that lasts while the app is running
clinic_queue = ClinicQueue()


@app.route('/')
def index():
    """
    Home page - shows the queue and current patient.
    """
    # Get data from our queue
    patients = clinic_queue.get_queue_positions()
    total_served = clinic_queue.get_total_served()
    current_patient = clinic_queue.peek()
    
    # Send data to the HTML template
    return render_template('index.html',
                         patients=patients,
                         total_served=total_served,
                         current_patient=current_patient,
                         queue_size=clinic_queue.size())


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Page to register new patients.
    GET: Show the form
    POST: Process the form data
    """
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        age = int(request.form['age'])
        symptoms = request.form['symptoms']
        
        # Create a Patient object (using our OOP class!)
        new_patient = Patient(name=name, age=age, symptoms=symptoms)
        
        # Add to queue (using our Queue data structure!)
        clinic_queue.enqueue(new_patient)
        
        # Show success message
        flash(f'Success! {name} added to queue. Position: {clinic_queue.size()}')
        
        # Go back to home page
        return redirect('/')
    
    # If GET request, just show the form
    return render_template('register.html')


@app.route('/serve_next')
def serve_next():
    """
    Serve the next patient (remove from front of queue).
    """
    patient = clinic_queue.dequeue()
    
    if patient:
        flash(f'Now serving: {patient.name} (ID: {patient.id})')
    else:
        flash('No patients in queue!')
    
    return redirect('/')


# This runs the app
if __name__ == '__main__':
    app.run(debug=True)