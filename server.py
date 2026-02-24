from flask import Flask, request, jsonify
from blood_analysis import check_HDL


app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_status():
    return "Server is running"


@app.route("/help", methods=["GET"])
def help_info():
    output_string = "For help with this website, "
    output_string += "contact david.a.ward@duke.edu"
    return output_string


@app.route("/hdl_analysis", methods=["POST"])
def hdl_analysis():
    in_json = request.get_json()
    print(in_json)
    analysis = check_HDL(in_json["test_value"])
    analysis = [10, 15]
    return jsonify(analysis)


@app.route("/hdl_analysis/<test_value>", methods=["GET"])
def hdl_analysis_2(test_value):
    analysis = check_HDL(int(test_value))
    return jsonify(analysis)



if __name__ == "__main__":
    app.run()
