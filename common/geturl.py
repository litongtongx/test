# 需要url拼接时使用，未实现
import os


def get_url(url):
    urls = url.split(os.path.sep)
    url = urls[0] + "//"+ urls[1]
    return url


if __name__ == '__main__':
    get_url("http://127.0.0.1/index.php?m=user&c=public&a=login")