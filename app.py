from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    python_executable = 'C://Users//nJoy//AppData//Local//Programs//Python//Python312//python.exe'
    script_path = 'C://Users//nJoy//OneDrive//Desktop//Mini Project VI SEM//main//emoji_detection.py'
    try:
        result = subprocess.run([python_executable, script_path], capture_output=True, text=True)
        return jsonify({
            'stdout': result.stdout if result.stdout else 'No output captured.',
            'stderr': result.stderr if result.stderr else 'No error captured.'
        })
    except FileNotFoundError as e:
        return jsonify({
            'error': str(e),
            'python_executable': python_executable,
            'script_path': script_path
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
