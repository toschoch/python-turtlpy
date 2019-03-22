import turtlpy.core as core
import yaml


class TurtlClient(object):

    def __init__(self, server, server_v2=None):
        config = """---
# set to `true` if you want errors to be wrapped in an object that includes the
# file/line number. nice for testing, probably annoying when actually using the
# core
wrap_errors: false

messaging:
  # the channel our request/response dialog happens on
  reqres: "inproc://turtl-req"
  # the channel used to send events from the core to the UI
  events: "inproc://turtl-events"
  # if true, the reqres channel responses will vary by the message id. so if you
  # set a message id of 53 and this is `true`, and messaging.reqres is
  # "turtl-req" then the response will come back on the channel "turtl-req:53"
  #
  # if this is false, the responses will come back on "turtl-req" and each
  # response message will have a message id you can use to match.
  reqres_append_mid: false

# override w/ runtime config! on desktop this should be a subfolder in the user
# folder. in android it should be the location of the app's data folder.
data_folder: '/tmp/turtl'

# logging configuration
logging:
  # the log level (ignore all messages with a log level lower than this)
  level: 'info'
  # the file to log to. if missing, logging will just be stdout
  file: 'core.log'
  # log rotation, only applies if `logging.file` is set
  rotation:
    keep: 3
    size: 1048576

api:
  endpoint: "https://apiv3.turtlapp.com"
  # this should be set by the client loading the core. standard format is
  # <platform>/<version>, like "android/0.7.0"
  client_version_string: 'core'
  # defines the proxy server we use for all outgoing connections. format is
  # <ip/host>:<port>: eg "10.67.23.144:6777"
  proxy: null
  # accept invalid certs
  allow_invalid_ssl: false
  # point this at a v0.6 api (the old lisp server) if you want to enable
  # migration from the old system to the new.
  v6:
    endpoint: "https://api.turtlapp.com/v2"

sync:
  enable_incoming: true
  enable_outgoing: true
  enable_files_incoming: true
  enable_files_outgoing: true
  poll_timeout: 25

# configuration integration tests
integration_tests:
  data_folder: /tmp/turtl/integration
  login:
    username: testdata@turtlapp.com
    password: omgitsatest
  v6_login:
    username: 'duck duck'
    password: 'juice'
"""
        config = yaml.load(config, yaml.CLoader)
        core.start(config)
