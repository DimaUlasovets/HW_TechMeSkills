from app.main import create_app
from werkzeug.serving import run_simple

app = create_app()

if __name__ == "__main__":
    run_simple("127.0.0.1", 5000, app, use_reloader=True, use_debugger=True)
