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
    """ Implement POST route to analyze HDL

    This function implements the /hdl_analysis route of the server.  This
    POST route receives JSON input in the form of a dictionary:

    {"test_value": <int>}

    It then sends the value of the "test_value" key to the
    blood_analysis.check_HDL function and receives a string in return.  This
    string is then returned to the requestor.

    Returns:
        str:  the result of the HDL analysis

    """
    in_json = request.get_json()
    analysis = check_HDL(in_json["test_value"])
    return jsonify(analysis)


@app.route("/hdl_analysis/<test_value>", methods=["GET"])
def hdl_analysis_2(test_value):
    """ Implement GET route to analyze HDL

    This function implements the /hdl_analysis/<test_value> route of the
    server.  Rather than receiving the HDL value to analyze via JSON in a POST
    request, this route uses a variable URL in which to receive the integer
    value of the HDL value.  The variable URL component is changed into an
    integer and then sent to the blood_analysis.check_HDL function and receives
    a string in return.  This string is then returned to the requestor.

    Args:
        test_value (str): the HDL test value to analyze

    Returns:
        str:  the result of the HDL analysis

    """
    analysis = check_HDL(int(test_value))
    return jsonify(analysis)


@app.route("/add_patient", methods=["POST"])
def post_add_patient():
    """ Implement POST route for adding a new patient

    This function implements the /add_patient route of the server.  This POST
    route receives JSON input in the form of a dictionary:

        {
            "first_name": <str>,
            "last_name": <str>,
            "mrn": <int>,
            "age": <int>
        }

    After validating that the input has the expected keys and data types, the
    data is sent to the database.add_single_patient function to add the
    patient information to the database.

    Returns:
        str:  message indicating either the success or failure of the request
        int:  status code:  200 for successful request, 400 otherwise

    """
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
    """ Validates keywords and data types of dictionary inputs

    This function is called by a flask handler function to validate that
    the keywords and data types sent to the server are those that were
    expected.  If an expected keyword is missing, or a value data type does not
    match the expected, an error message is returned along with a 400 status
    code.  If the keys and data types do match, True is return with a 200
    status code.

    Args:
        in_data (dict): data received by the server to be validated
        expected_keys (list of str): the keywords that should exist in the
                                       input data
        expected_types (list of types):  the expected data types for the
                                           expected keys.  Should be in the
                                           same order as the expected keys.

    Returns:
        bool or str:  True if expected keys and data types are found, else an
                        error message if not
        int:  status code of 200 if validation successful, 400 if not
    """
    if type(in_data) is not dict:
        return "Input to route must be a dictionary", 400
    for key, expected_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} not found in input".format(key), 400
        if type(in_data[key]) is not expected_type:
            return "Key {} has a value type of {} " \
                   "but should be {}".format(key,
                                             type(in_data[key]),
                                             expected_type), 400
    return True, 200


@app.route("/add_test_data", methods=["POST"])
def post_add_test_data():
    """ Implement POST route for adding test data to a patient record

    This function implements the /add_test_data route of the server.  This POST
    route receives JSON input in the form of a dictionary:

        {
            "mrn": <int>,
            "test_name": <str>,
            "test_value": <float>
        }

    It contains the medical record number of the patient for whom the test
    belongs, the name of the test, and the test result.  This function
    validates the received data and returns an error message if the input
    data does not meet expectations.   If the input data is valid, the
    database.add_test_data_to_db function is called and sent the information.

    Returns:
        str:  message indicating either the success or failure of the request
        int:  status code:  200 for successful request, 400 otherwise
    """
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


@app.route("/get_patient_info/<mrn>", methods=["GET"])
def get_get_patient_info(mrn):
    """ Implement GET route for getting patient information

    This function implements the /get_patient_info/<mrn> route of the server.
    This route uses a variable URL in which to receive the medical record
    number of the patient.  The function takes that mrn from the variable URL
    and uses its integer value as the parameter to the
    database.get_patient_output function.  The result of this function call is
    returned to the requestor.

    Args:
        mrn (str): portion of the variable URL containing the patient medical
                    record number

    Returns:
        str:  patient information
        int:  status code

    """
    try:
        mrn = int(mrn)
    except ValueError:
        return "/get_patient_info/<mrn> expects an integer" \
        "for the mrn value", 400
    answer = database.get_patient_output(int(mrn))
    if answer is None:
        return "MRN {} not found".format(mrn), 400
    return answer, 200


if __name__ == "__main__":
    app.run()
