from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    print("✅ 静态网站已生成到 'build' 文件夹。")
    print("👉 将 'build' 文件夹上传到 Cloudflare Pages 即可托管。")