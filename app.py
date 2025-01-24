from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Appointment 
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    doctor = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f"Appointment('{self.name}', '{self.email}', '{self.doctor}', '{self.date}', '{self.time}')"

with app.app_context():
    db.create_all()

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

@app.route('/ourdoctor')
def our_doctor():
    return render_template('ourdoctor.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('login.html')
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        doctor = request.form['doctor']
        date = request.form['date']
        time = request.form['time']

#New Appointment

        new_appointment = Appointment(
            name=name,
            email=email,
            contact=contact,
            doctor=doctor,
            date=date,
            time=time
        )
        # Adding to database!!!!!!
        db.session.add(new_appointment)
        db.session.commit()

        return redirect(url_for('thank_you'))

    return render_template("appointment.html")

@app.route("/thank_you")
def thank_you():
    return "Thank you for booking an appointment!"

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('textarea')

        return redirect(url_for('thankyou'))
    return render_template('index.html') 

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
