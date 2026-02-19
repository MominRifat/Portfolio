from portfolio.wsgi import application  # normal Django WSGI
from mangum import Mangum

handler = Mangum(application)  # serverless handler
