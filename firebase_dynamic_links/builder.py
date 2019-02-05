from urllib.parse import urlencode, unquote

from .client import FirebaseClient


def generate_short_link(client, app_code, query_params, unquoted=False):
    long_dynamic_link = generate_long_link(app_code=app_code, query_params=query_params, unquoted=unquoted)

    return client.shorten_link(long_link=long_dynamic_link)


def generate_long_link(app_code, query_params, unquoted=False):
    query_string = urlencode(query_params)
    if unquoted:
        query_string = unquote(query_string)

    link = 'https://{app_code}.page.link/?{query_string}'.format(app_code=app_code, query_string=query_string)

    return link


class DynamicLinkBuilder:
    def __init__(self, client, unquoted=False):
        self.client = client
        self.unquoted = unquoted

    def generate_long_link(self, app_code, **kwargs):
        return generate_long_link(app_code=app_code, query_params=kwargs)

    def generate_short_link(self, app_code, unquoted=False, **kwargs):
        return generate_short_link(client=self.client, app_code=app_code, query_params=kwargs, unquoted=unquoted)


def dynamic_link_builder(api_key):
    return DynamicLinkBuilder(client=FirebaseClient(api_key=api_key))
