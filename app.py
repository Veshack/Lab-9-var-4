from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'project.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class StepEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    steps = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(10), nullable=False)

@app.route('/')
def index():
    entries = StepEntry.query.all()
    total_steps = sum(entry.steps for entry in entries)
    return render_template('index.html', entries=entries, total_steps=total_steps)

@app.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json()
    new_entry = StepEntry(steps=data['steps'], date=data['date'])
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_entries():
    StepEntry.query.delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
