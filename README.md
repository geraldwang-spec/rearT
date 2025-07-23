# rearT

Structure
  rearT/
  ├── app/
  │   ├── __init__.py          # 建立 app、連接資料庫
  │   ├── models.py            # SQLAlchemy 模型
  │   ├── auth.py              # 註冊/登入/JWT
  │   ├── schema.py            # GraphQL schema (使用 Ariadne)
  │   ├── resolvers.py         # GraphQL resolver
  │   ├── routes.py            # (選用) REST routes for health check
  ├── static/                  # 前端 HTML/CSS/JS
  │   └── index.html
  ├── tests/
  │   └── test_auth.py         # pytest 測試檔
  ├── migrations/              # Alembic migration
  ├── .env                     # MSSQL 帳號密碼等機密
  ├── .gitignore
  ├── config.py
  ├── requirements.txt
  ├── run.py                   # 啟動 Flask 伺服器
  ├── Dockerfile               # 容器化部署
  ├── docker-compose.yml       # MSSQL + Flask 整合
  └── .github/
      └── workflows/
          └── ci.yml           # GitHub Actions 自動測試流程

install library
  sudo apt install python-pip
  sudo apt install python3-venv

1. launch python venv
  python3 -m venv venv
  cd to execute folder
  source venv/bin/activate
2. install require library
  pip install -r requirements.txt
