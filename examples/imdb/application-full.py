#!/usr/bin/env python
from cloudmining import CloudMiningApp

# create a new CloudMining web application
app = CloudMiningApp.from_config_dir('config-full/', autoreload=False)

# pickup our custom templates, css etc ..
app.set_application_path('.', auto_load_public=True)

# set the preloading cache to the full data
app.set_preload_cache_file('data-full/redis-cache.dat')

# what sorting options are shown (key must match cl sort options)
app.set_ui_sort_by(
    dict(key='pop', description='popularity'),
    dict(key='dat', description='date'),
    dict(key='rat', description='user ratings'),
    dict(key='vot', description='number of votes')
)

# you can reorder the facets and change default look here
# name must match the sphinx client facet names
app.set_ui_facets(
    dict(name='year', color='purple', collapsed=True, visualization='rose'),
    dict(name='genre', color='green', visualization='counts'),
    dict(name='keyword', collapsed=True, color='black'),
    dict(name='director', color='blue'),
    dict(name='actor', color='red', visualization='counts'),
)

# some more options which can be set
app.set_debug(False)  # also web.config.debug
app.set_template_caching(True)  # also web.config.template_caching
app.set_flush_cache_on_startup(True)

# instance name and description which appears in the front page
app.set_ui_instance(
    instance_name='IMDb', 
    description='''
    <p>Search <strong>movies</strong> from <a href="http://www.imdb.com">IMDB</a>. 
    Note this interface was automatically built with <a href="https://github.com/alexksikes/cloudmining/">Cloud Mining</a>.</p>'''
)

# if called from the command line will start HTTP server
# otherwise it will honor cgi or fastcgi protocol
if __name__ == '__main__':
    app.run()