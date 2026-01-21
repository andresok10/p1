# rxconfig.py
import reflex as rx
import os

config = rx.Config(
    app_name="p1",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 3000)),
)

'''import reflex as rx
config = rx.Config(
    app_name="p1",
)'''