import json
def is_complex_num(objct):
    if '__complex__' in objct:
        return complex(objct['real'], objct['img'])
    return objct

complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = is_complex_num)
simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
print("Complex_object: ",complex_object)
print("Without complex object: ",simple_object)

# import json

# # create function to check instance is complex or not
# def complex_encode(object):
#     # check using isinstance method
#     if isinstance(object, complex):
#         return [object.real, object.imag]
#     # raised error using exception handling if object is not complex
#     raise TypeError(repr(object) + " is not JSON serialized")


# # perform json encoding by passing parameter
# complex_obj = json.dumps(4 + 5j, default=complex_encode)
# print(complex_obj)
