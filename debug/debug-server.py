from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# テーマファイルのパス
THEME_FILE = '../themes/tsuki-theme.json'

def load_themes():
  with open(THEME_FILE, 'r') as file:
    return json.load(file)

def save_themes(themes):
  with open(THEME_FILE, 'w') as file:
    json.dump(themes, file, indent=2)

@app.route('/')
def index():
  themes = load_themes()
  return render_template('index.html', themes=themes)

@app.route('/update_theme', methods=['POST'])
def update_theme():
  themes = load_themes()
  updated_theme = request.json

  for i, theme in enumerate(themes):
    if theme['name'] == updated_theme['name']:
      themes[i] = updated_theme
      break

  save_themes(themes)
  return jsonify({"status": "success"})

if __name__ == '__main__':
  app.run(debug=True)
