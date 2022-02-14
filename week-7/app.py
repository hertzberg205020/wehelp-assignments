from flask import Flask

import config
from blueprints import user_bp, api_bp

app = Flask(__name__,
            static_folder="static",
            static_url_path="/static")

app.config.from_object(config)
app.register_blueprint(user_bp)
app.register_blueprint(api_bp)


if __name__ == '__main__':
    app.run(port=3000)

