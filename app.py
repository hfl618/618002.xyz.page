from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 工具列表配置
TOOLS = [
    {
        "category": "常用工具",
        "items": [
            {"name": "Google", "url": "https://www.google.com", "desc": "全球最大的搜索引擎", "icon": "🔍"},
            {"name": "ChatGPT", "url": "https://chat.openai.com", "desc": "AI 智能助手", "icon": "🤖"},
            {"name": "GitHub", "url": "https://github.com", "desc": "代码托管平台", "icon": "🐙"},
            {"name": "Cloudflare", "url": "https://dash.cloudflare.com", "desc": "网络安全与CDN服务", "icon": "☁️"},
        ]
    },
    {
        "category": "开发/设计",
        "items": [
            {"name": "Canva", "url": "https://www.canva.com", "desc": "在线平面设计工具", "icon": "🎨"},
            {"name": "Vercel", "url": "https://vercel.com", "desc": "前端部署平台", "icon": "▲"},
            {"name": "TinyPNG", "url": "https://tinypng.com", "desc": "图片压缩工具", "icon": "🐼"},
            {"name": "JSON Editor", "url": "https://jsoneditoronline.org", "desc": "在线 JSON 编辑器", "icon": "🔧"},
        ]
    },
    {
        "category": "娱乐/生活",
        "items": [
            {"name": "YouTube", "url": "https://www.youtube.com", "desc": "视频分享平台", "icon": "📺"},
            {"name": "Bilibili", "url": "https://www.bilibili.com", "desc": "国内弹幕视频网站", "icon": "📺"},
            {"name": "Spotify", "url": "https://open.spotify.com", "desc": "音乐流媒体", "icon": "🎵"},
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html', tool_groups=TOOLS)

@app.route('/api/tools')
def get_tools():
    return jsonify(TOOLS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=True)