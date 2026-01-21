# rxconfig.py
import reflex as rx
import os

config = rx.Config(
    app_name="p1",
    pwa=False,
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
#port=int(os.environ.get("PORT", 3000)),
'''import reflex as rx
config = rx.Config(
    app_name="p1",
)'''

#host="0.0.0.0",
# disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
# api_url="https://TU-BACKEND.onrender.com",
# pip install -r requirements.txt && reflex export
# reflex run --env prod --backend-host 0.0.0.0 --backend-port $PORT
# reflex run --env prod --backend-host 0.0.0.0 --backend-port $PORT