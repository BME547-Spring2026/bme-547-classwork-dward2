def get_tach_limit(a):
    return 150


def tachycardia_analysis(hr, age):
    tach_limit = 100
    if age < 15:
        tach_limit = get_tach_limit(age)
    if hr > tach_limit:
        result = "tachycardic"
    else:
        result = "normal"
    return result
