import os

from pecutil.run import copy_folder_minify

__author__ = 'jbui'

if __name__ == '__main__':
    package_name = 'boadoc'

    LOCAL_FOLDER = os.path.dirname(os.path.abspath(__file__))
    SOURCE_LOCATION = os.path.join(os.path.split(LOCAL_FOLDER)[0], package_name)
    MINIFIED_LOCATION = os.path.join(LOCAL_FOLDER, package_name)

    print('Local Folder "%s"' % LOCAL_FOLDER)
    print('Source Location "%s"' % SOURCE_LOCATION)
    print('Minified Location "%s"' % MINIFIED_LOCATION)

    # Copy folder and minify
    copy_folder_minify(SOURCE_LOCATION, MINIFIED_LOCATION)
