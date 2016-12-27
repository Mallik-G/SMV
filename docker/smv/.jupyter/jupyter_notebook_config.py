import os

## The IP address the notebook server will listen on.
c.NotebookApp.ip = os.environ.get('JUPYTER_HOST', '*')

## The port the notebook server will listen on.
c.NotebookApp.port = int(os.environ.get('JUPYTER_PORT', '8888'))

## The work directory
c.FileContentsManager.root_dir = u'notebooks'

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (NotebookApp.browser)
#  configuration option.
c.NotebookApp.open_browser = False

## Supply overrides for the tornado.web.Application that the Jupyter notebook
#  uses.
c.NotebookApp.tornado_settings = {
    'headers': {
    }
}