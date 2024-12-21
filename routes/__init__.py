# from .user import user_bp
# from .order import order_bp
from .home import home_bp


# Blueprintをリストとしてまとめる
#routesにファイルを追加してBlueprintを作成するたびに追加して欲しい
blueprints = [
  home_bp,
]
