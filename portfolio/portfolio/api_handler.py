import os
from django.core.wsgi import get_wsgi_application
from mangum import Mangum  # For serverless

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio/portfolio.settings")

application = get_wsgi_application()
handler = Mangum(application)  # Vercel entry point
