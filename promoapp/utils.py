from uuid import uuid4
import os


class Utils():

    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)

        return wrapper