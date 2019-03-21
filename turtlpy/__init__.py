try:
    import pkg_resources
    __version__ = pkg_resources.get_distribution('turtlpy').version
except (pkg_resources.DistributionNotFound, ImportError):
    __version__ = 'dev'