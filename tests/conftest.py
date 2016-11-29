from os import path

from hypothesis import settings

settings.register_profile('ci', settings(max_examples=1000))
settings.register_profile('dev', settings(database_file=path.join(path.dirname(__file__), '.hypothesis')))

settings.load_profile('dev')
