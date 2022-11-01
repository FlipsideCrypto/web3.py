#import requests

from ...pylru import pylru

from ...utils.caching import generate_cache_key


_session_cache = pylru.lrucache(8)


def _get_session(*args, **kwargs):
    cache_key = generate_cache_key((args, kwargs))
    if cache_key not in _session_cache:
        _session_cache[cache_key] = urlfetch.Session()
    return _session_cache[cache_key]


def make_post_request(endpoint_uri, data, *args, **kwargs):
    kwargs.setdefault('timeout', 10)
    # session = _get_session(endpoint_uri)
    # response = urlfetch.post(endpoint_uri, data=data, *args, **kwargs)
    response = urlfetch.fetch(endpoint_uri, deadline = 30, payload=data, method=urlfetch.POST)

    #TODO: make this better!

    #response.raise_for_status()

    return response.content


