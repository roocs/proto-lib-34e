import os


REQ_BASE_DIR = 'outputs/requests'
if not os.path.isdir(REQ_BASE_DIR):
    os.makedirs(REQ_BASE_DIR)


class WPSResponse(object):

    def __init__(self, msg='', result=None):
        self.msg = msg or 'SUCCESS'
        self.result = result
        self._setup()

    def _setup(self):
        self.urls = ['http://download?path=' + _ for _ in self.result.file_paths]
        self.metadata = self.result.metadata

    def repr(self):
        return f'{self.msg}: {self.result}, {self.urls}'


class WPSRequest(object):

    _counter = 0

    def __init__(self, **kwargs):
        self._content = dict(**kwargs)
        self._setup()

    def _setup(self):
        self._set_id()
        self.directory = os.path.join(REQ_BASE_DIR, f'{self._get_id()}')

        if not os.path.isdir(self.directory):
            os.makedirs(self.directory)

    def _set_id(self):
        self._id = WPSRequest._counter
        WPSRequest._counter += 1

    def _get_id(self):
        return self._id


def translate_args(**kwargs):
    """
    Returns a dictionary of arguments converted from WPS input types
    to python types

    :param kwargs: Dictionary of arguments
    :return: Dictionary of converted arguments
    """
    translated = {}

    for key, value in kwargs.items():

        if value in (None, ''):
            continue 
        elif key == 'time':
            value = value.split('/')
        elif key in ('space', 'level'):
            value = [float(_) for _ in value.split(',')]

        print(key, '-->', value)
        translated[key] = value

    return translated

