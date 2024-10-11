from db import session_
import tables

result = session_.query(tables.Offices.city, tables.Offices.country).filter(
    tables.Offices.city == "London").one_or_none()
print(result)
