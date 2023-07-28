from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#sample task list
tasks = [
         {'description': 'Buy groceries', 'status': 'Incomplete'},
         {'description': 'Do the laundry', 'status': 'Incomplete'},
         {'description': 'Walk the doggo', 'status': 'Incomplete'},
         {'description': 'Take out the trash', 'status': 'Incomplete'},
         {'description': 'Go to the gym', 'status': 'Incomplete'},
         {'description': 'Call yo Mama', 'status': 'Incomplete'},
         {'description': 'Homework', 'status': 'Incomplete'}, 
         {'description': 'Meditate', 'status': 'Incomplete'},
         {'description': 'Play the guitar', 'status': 'Incomplete'},
         {'description': 'Do the dishes', 'status': 'Incomplete'},
         {'description': 'Check the mail', 'status': 'Incomplete'},
         {'description': 'Pay yo dang bills', 'status': 'Incomplete'},
         {'description': 'Clean the crib', 'status': 'Incomplete'},
         {'description': 'Get that paper', 'status': 'Incomplete'},
         {'description': 'Breathe', 'status': 'Incomplete'},
         {'description': 'Eat some foods', 'status': 'Incomplete'},
         {'description': 'Read a book', 'status': 'Incomplete'},
         {'description': 'Get some beauty sleep', 'status': 'Incomplete'}]

# Route for to-do list
@app.route('/todo', methods=['GET', 'POST'])
def todo():
    global tasks   # makes it possible to edit/change the tasks var

    if request.method == 'POST':
        # Get new task description 
        new_task_description = request.form['task']
        # Create a new task w/ description and status
        new_task = {'description': new_task_description, 'status': 'Incomplete'}
        # Add new task to list of tasks
        tasks.append(new_task)


    return render_template('todo.html', tasks=tasks)

#Route to mark a task as completed 
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    global tasks
   
    # Check to see if task_id is valid
    if task_id < len(tasks): 
        # If it is, remove from the list 
        del tasks[task_id]

    #Redirect user back to main to-do list 
    return redirect(url_for('todo'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)
