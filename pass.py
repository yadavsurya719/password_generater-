from flask import Flask, render_template, request
from termcolor import colored

app = Flask(__name__)

# Route for the main page
@app.route('/')


# Route for handling form submission
@app.route('/generate_password', methods=['GET', 'POST'])
def generate_password():
    try:
        if request.method == 'POST':
            # Get form data
            choice = int(request.form['choice'])

            if choice == 1:
                name = request.form['name']
                if not name:
                    raise ValueError("Name should not be empty.")
                password = generate_random_password(len(name) + 8)
                colored_output = colored(f"Generated Password: {password}", "green")
            elif choice == 2:
                password_length = int(request.form['passwordLength'])
                password = generate_random_password(password_length)
                colored_output = colored(f"Generated Password: {password}", "blue")
            elif choice == 3:
                password = generate_single_code()
                colored_output = colored(f"Generated Code: {password}", "yellow")
            else:
                raise ValueError("Invalid choice. Please enter 1, 2, or 3.")

            return render_template('ssss.html', colored_output=colored_output)

    except ValueError as e:
        return render_template('index.html', colored_output=colored(f"Error: {e}", "red2"))
    def index():
     return render_template('ssss.html')
    return generate_password
    
if __name__ == "__main__":
    app.run(debug=True)
