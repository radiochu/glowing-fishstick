from flask import Flask, render_template, jsonify, request, url_for


def create_app():
    app = Flask(__name__)

    parts = {
        'lowpressure': {
            'name': 'Low Tire Pressure Warning',
            'image': '../static/lowpressure.jpg',
            'description': 'This illuminates when your tire pressure is low. If the lamp remains on with the engine '
                           'running or when driving, check your tire pressure as soon as possible. It will also '
                           'illuminate momentarily when you switch the ignition on to confirm the lamp is functional. '
                           
        },
        'autolamps': {
            'name': 'Autolamps',
            'image': '../static/lighting.jpg',
            'description': 'When the lighting control is in the autolamps position, the headlamps turn on in low '
                           'light situations, or when the wipers turn on. The headlamps remain on for a period of '
                           'time after you switch the ignition off. Use the information display controls to adjust '
                           'the period of time that the headlamps remain on.'
        },
        'meme': {
            'name': 'Meme',
            'image': '../static/meme.jpg',
            'description': 'The world\'s greatest meme, guaranteed.'
                            '                                      '
        }
    }

    @app.route('/')
    def main_page():
        return render_template("index.html")

    @app.route('/qr')
    def qr():
        return render_template("qr.html")

    @app.route('/details')
    def details():
        return render_template("details.html")

    @app.route('/details2')
    def details2():
        return render_template("details2.html")

    @app.route('/details3')
    def details3():
        return render_template("details3.html")

    @app.route('/scans')
    def scans():
        return render_template("scans.html")

    @app.route('/parts/<part>', methods=['GET'])
    def disp(part):
        data = {
            'name': parts[part]["name"],
            'image': parts[part]["image"],
            'description': parts[part]["description"]
        }

        return jsonify(data)

    return app
