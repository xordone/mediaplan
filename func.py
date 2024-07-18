import datetime
from dateutil.relativedelta import relativedelta



month1 = datetime.datetime.now()
month2 = month1 + relativedelta(months=+1)
# month3 = month1 + relativedelta(months=+2)

list = [
    month1.strftime("%m"),
    month2.strftime("%m"),
    # month3.strftime("%m"),
    ]
