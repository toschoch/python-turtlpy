try:
    import pkg_resources
    __version__ = pkg_resources.get_distribution('turtlpy').version
    import os
    os.environ['TURTL_CONFIG_FILE'] = pkg_resources.resource_filename('turtlpy','config.yaml')
except (pkg_resources.DistributionNotFound, ImportError):
    __version__ = 'dev'