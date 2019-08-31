import configparser
import os


# read the source under [browser] item
def get_browser(name):
    global base_path, cf_path
    base_path = os.path.dirname(os.getcwd())
    cf_path = os.path.join(base_path, "config", "config.ini")
    cf = configparser.ConfigParser()
    cf.read(cf_path)
    return cf.get('browser', name)


def get_url():
    cp = configparser.ConfigParser()
    cp.read(cf_path)
    return cp.get('browser', 'Url')
