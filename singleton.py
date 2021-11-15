import urllib.parse
import urllib.request


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# class URLFetcher:
class URLFetcher(metaclass=SingletonMeta):
    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)
                urls = self.urls
                urls.append(url)
                self.urls = urls


fetcher = URLFetcher()
other_fetcher = URLFetcher()

fetcher.fetch('https://google.com')
fetcher.fetch('https://epam.com')

other_fetcher.fetch('https://python.org')

print(fetcher is other_fetcher)
print(fetcher.urls)
print(other_fetcher.urls)

# test 1

