from celery import Celery

import cv2
import numpy as np
import json

c = Celery(main='romanesco', backend='amqp', broker='amqp://guest:guest@localhost:5672//')

class NumPyArangeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist() # or map(int, obj)
        return json.JSONEncoder.default(self, obj)

@c.task(name='app.add')
def add(x, y):
    print 'hello task'
    return x + y


@c.task(name='app.excarb')
def excarb(**kwargs):

    # import json
    # import pprint
    # import sys

    cell_contents = kwargs['payload']['cell']

    return_result = {}

    if cell_contents:
        try:
            exec(cell_contents)
            return_result['status'] = 'success'
        except Exception as e:
            return_result['status'] = 'failed'
            return_result['exception'] = e.message


    # pprint.pprint(sys.path)
    # pprint.pprint(kwargs)

    # return_result['kwargs'] = dict(kwargs)
    # return_result['syspath'] = sys.path

    return return_result






