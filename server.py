from flask import Flask, request, jsonify
from blood_analysis import check_HDL
import database

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


@app.route("/add_patient", methods=["POST"])
def post_add_patient():
    # Call a function to validate input data
    in_data = request.get_json()
    expected_keys = ["first_name", "last_name", "mrn", "age"]
    expected_types = [str, str, int, int]
    message, status_code = validate_post_input(in_data,
                                               expected_keys,
                                               expected_types)
    if message is not True:
        return message, status_code
    # Call other functions to do the work
    database.add_single_patient(in_data)
    # Return result
    return "Successful addition", 200


def validate_post_input(in_data, expected_keys, expected_types):
    for key, expected_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} not found in input".format(key), 400
        if type(in_data[key]) is not expected_type:
            return "Key {} has a value type of {} " \
            "but should be {}".format(key,
                                      type(in_data[key]),
                                      expected_type), 400
    return True, 200


@app.route("/add_test_data/<mrn>", methods=["POST"])
def post_add_test_data():
    # Call a function to validate input data
    in_data = request.get_json()
    expected_keys = ["mrn", "test_name", "test_value"]
    expected_types = [int, str, float]
    message, status_code = validate_post_input(in_data,
                                               expected_keys,
                                               expected_types)
    if message is not True:
        return message, status_code
    # Call other functions to do the work
    database.add_test_data_to_db(in_data["mrn"],
                                 in_data["test_name"],
                                 in_data["test_value"])
    # Return result
    return "Successful addition", 200




if __name__ == "__main__":
    app.run()
