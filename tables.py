

from sqlalchemy import Boolean, Column, Integer, String

from db import Model


class Offices(Model):

    __tablename__ = "offices"

    office_code = Column("officeCode", Integer, primary_key=True)
    city = Column(String(255))
    country = Column(String(255))
    phone = Column(String(255))
