from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None 
    error_message = None
    if request.method == "POST":
        try:
            a = float(request.form.get("a", 0))  #Get with default 0 to handle missing fields
            b = float(request.form.get("b", 0))
            c = float(request.form.get("c", 0))

            if a == 0:
                error_message = "Error: 'a' cannot be zero."
            else:
                delta = (b**2) - 4*(a*c)
                if delta >= 0:
                    x1 = (-b - delta**0.5) / (2*a)
                    x2 = (-b + delta**0.5) / (2*a)
                    result = f"x1 = {x1:.2f}, x2 = {x2:.2f}"
                else:
                    result = "No real solutions"

        except ValueError:
            error_message = "Error: Invalid input. Please enter numbers only."
        except Exception as e:  #Catch any unexpected exception for debugging
            error_message = f"An unexpected error occurred: {e}"


    return render_template("index.html", result=result, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)