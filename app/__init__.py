from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return (
            "<h1>GCP CI/CD Flask Pipeline</h1>"
            "<p>This app is deployed by an automated DevOps pipeline.</p>"
        )

    @app.route("/health")
    def health():
        return jsonify(status="healthy"), 200

    return app