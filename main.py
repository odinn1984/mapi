from maze.Generator import Generator
from maze.Strategy_RecursiveBacktracker import Strategy_RecursiveBacktracker
from maze.Strategy_HuntAndKill import Strategy_HuntAndKill
from flask import Flask, render_template, abort, request
from time import gmtime, strftime

import optparse as op
import json

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/maze/generate/json/')
@app.route('/maze/generate/json/<width>/<height>')
@app.route('/maze/generate/json/<strategy>/<width>/<height>')
def mazeJson(width=10, height=10, strategy='RecursiveBacktracker'):
    maze_generator = mazeGeneratorFactory(width, height, strategy)
    maze_generator.generate()

    return maze_generator.getJSON()

@app.route('/maze/render')
@app.route('/maze/render/<width>/<height>')
@app.route('/maze/render/<strategy>/<width>/<height>')
def renderMaze(width=10, height=10, strategy='RecursiveBacktracker'):
    maze_generator = mazeGeneratorFactory(width, height, strategy)
    maze_generator.generate()
    maze_json = maze_generator.getJSON()

    return render_template('renderer.html', maze_json=maze_json)

@app.route('/maze/solve', methods=['POST'])
def solveMaze():
    if request.method != 'POST':
        abort(400)

    maze = json.loads(request.data)

    return json.dumps([{"x": 1, "y": 2}])

def mazeGeneratorFactory(width, height, algorith_type):
    maze_generator = None

    try:
        if int(width) <= 0 or int(height) <= 0:
            print '[%s - Error]: %s' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), "width and height have to be > 0")
            abort(400)

        if algorith_type == 'RecursiveBacktracker':
            maze_generator = Generator(Strategy_RecursiveBacktracker(int(width), int(height)))
        elif algorith_type == 'HuntAndKill':
            maze_generator = Generator(Strategy_HuntAndKill(int(width), int(height)))
        else:
            abort(404)

        return maze_generator
    except Exception as e:
        print '[%s - Error]: %s' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), e.message)
        abort(400)

if __name__ == '__main__':
    parser = op.OptionParser()
    parser.add_option('-p', '--port', dest='port', default=3666)
    parser.add_option('-b', '--bind', dest='host', default='0.0.0.0')
    parser.add_option('-d', '--debug', action='store_true', dest='debug', default=False)

    options, remainder = parser.parse_args()

    app.run(host=options.host, port=options.port, debug=options.debug)

