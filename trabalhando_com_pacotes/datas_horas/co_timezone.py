from datetime import datetime, timezone, timedelta

data_sp = datetime.now(timezone(timedelta(hours=2))) # hours 2 representa gmt+2 horario de sao paulo
data_oslo = datetime.now(timezone(timedelta(hours=3))) # hours 2 representa gmt+3 horario de oslo

print(data_sp)
print(data_oslo)
