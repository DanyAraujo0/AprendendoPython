from datetime import datetime

import pytz  # $ pip install pytz - para usar a biblioteca

data = datetime.now(
    pytz.timezone("Europe/Oslo")
)  # passa a zona para pegar a hora de lá

print(data)

# -m verrv .env
# source .env/bin/activate
