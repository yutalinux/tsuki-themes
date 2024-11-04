#!/bin/python3

import json

themes = []

with open("themes/tsuki-theme.json", "r") as f:
  themes = json.load(f)

# HTMLテンプレート
html_template = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>テーマエディタ</title>
  <style>
    body {{
      font-family: 'Helvetica Neue', Arial, sans-serif;
      background-color: #2A2A2A;
      color: #FFFFFF;
      line-height: 1.6;
      margin: 0;
      padding: 20px;
    }}
    .theme-container {{
      max-width: 800px;
      margin: 20px auto;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.3);
    }}
    h1, h2, h3 {{
      color: #FFFFFF;
    }}
    ul {{
      list-style-type: none;
      padding: 0;
    }}
    .button {{
      display: inline-block;
      padding: 10px 20px;
      border-radius: 5px;
      text-decoration: none;
      transition: background-color 0.3s ease;
    }}
    #theme-buttons {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-bottom: 20px;
    }}
    .theme-button {{
      padding: 10px 20px;
      font-size: 16px;
      background-color: #3A3A3A;
      color: #FFFFFF;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }}
    .theme-button:hover {{
      background-color: #4A4A4A;
    }}
    #editor-form {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-top: 20px;
    }}
    #editor-form label {{
      display: flex;
      align-items: center;
    }}
    #editor-form input {{
      margin-left: 10px;
    }}
  </style>
</head>
<body>
  <h1>テーマエディタ</h1>
  <div id="theme-buttons">
    {theme_buttons}
  </div>
  <div id="theme-display"></div>
  <div id="theme-editor"></div>

  <script>
    let themes = {themes_json};
    let currentThemeIndex = 0;

    function changeTheme(index) {{
      currentThemeIndex = index;
      const selectedTheme = themes[index];
      const themeDisplay = document.getElementById('theme-display');
      const themeEditor = document.getElementById('theme-editor');

      themeDisplay.innerHTML = `
        <div class="theme-container" style="background-color: #1e1e1e;">
          <h2 style="color: ${{selectedTheme.accent_color}};">${{selectedTheme.name}}テーマ</h2>
          <p>このセクションは${{selectedTheme.name}}テーマの色設定を使用しています。</p>
          <h3 style="color: ${{selectedTheme.accent_color}};">テーマの特徴</h3>
          <ul>
            <li>アクセントカラー: <span style="color: ${{selectedTheme.accent_color}};">${{selectedTheme.accent_color}}</span></li>
            <li>リンクカラー: <span style="color: ${{selectedTheme.link_color}};">${{selectedTheme.link_color}}</span></li>
            <li>テキストカラー: <span style="color: ${{selectedTheme.text_color}};">${{selectedTheme.text_color}}</span></li>
            <li>セカンダリカラー: <span style="color: ${{selectedTheme.secondary_color}};">${{selectedTheme.secondary_color}}</span></li>
            <li>背景色: <span style="color: ${{selectedTheme.back_color}};">${{selectedTheme.back_color}}</span></li>
          </ul>
          <p>詳細については<a href="#" style="color: ${{selectedTheme.link_color}};">こちらのリンク</a>をご覧ください。</p>
          <a href="#" class="button" style="background-color: ${{selectedTheme.secondary_color}}; color: #1e1e1e;">詳細を見る</a>
        </div>
      `;

      themeEditor.innerHTML = `
        <h3>テーマ編集</h3>
        <form id="editor-form">
          <label>アクセントカラー: <input type="color" name="accent_color" value="${{selectedTheme.accent_color}}"></label>
          <label>リンクカラー: <input type="color" name="link_color" value="${{selectedTheme.link_color}}"></label>
          <label>テキストカラー: <input type="color" name="text_color" value="${{selectedTheme.text_color}}"></label>
          <label>セカンダリカラー: <input type="color" name="secondary_color" value="${{selectedTheme.secondary_color}}"></label>
          <label>背景色: <input type="color" name="back_color" value="${{selectedTheme.back_color}}"></label>
        </form>
      `;

      document.getElementById('editor-form').addEventListener('input', updateTheme);
    }}

    function updateTheme(event) {{
      const color = event.target.value;
      const property = event.target.name;
      themes[currentThemeIndex][property] = color;
      changeTheme(currentThemeIndex);
    }}

    // 初期テーマを表示
    changeTheme(0);
  </script>
</body>
</html>
"""

# テーマボタンを生成
theme_buttons = "".join([f'<button class="theme-button" onclick="changeTheme({i})">{theme["name"]}テーマ</button>' for i, theme in enumerate(themes)])

# テーマデータをJSON形式で埋め込む
themes_json = json.dumps(themes, ensure_ascii=False)

# 最終的なHTMLコンテンツを生成
html_content = html_template.format(theme_buttons=theme_buttons, themes_json=themes_json)

# HTMLファイルを生成
with open('dist/index.html', 'w') as file:
  file.write(html_content)

print("テーマエディタページを生成しました: dist/index.html")
