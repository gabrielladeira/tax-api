from . import create_app


app = create_app(additional_settings={"debug": True})
