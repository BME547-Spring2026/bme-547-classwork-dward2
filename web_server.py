from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

db = []


def process_patient(fn, bt):
    print("First name: {}".format(fn))
    print("Blood type: {}".format(bt))
    db.append(fn)
    db.append(bt)
    return


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        blood_type = request.form["letter_choice"]
        process_patient(first_name, blood_type)
        status = "Accepted"
        return redirect(url_for("patient_info_display"))
    else:
        status = "Ready"
    return render_template("html_work.html",
                           status_string=status)


@app.route("/patient_info", methods=["GET"])
def patient_info_display():
    first_name = db[0]
    blood_type = db[1]
    return render_template("patient_display.html",
                           first_name = first_name,
                           blood_type = blood_type)


if __name__ == "__main__":
    app.run()
