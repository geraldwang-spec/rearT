from . import db

class Station(db.Model):
    __tablename__ = 'StationConfig'  # 大小寫與 MSSQL 保持一致

    pname = db.Column(db.String(50), nullable=True)
    station = db.Column(db.Integer, nullable=True)
    sname = db.Column(db.Unicode(50), nullable=True)     # 對應 NVARCHAR
    sversion = db.Column(db.String(50), nullable=True)
    config = db.Column(db.Integer, nullable=True)
    repair = db.Column(db.Integer, nullable=True)
    bindConf = db.Column(db.String(50), nullable=True)

