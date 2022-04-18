from BankFrequencyQuery import BankFrequencyQuery
from CardWithdrawQuery import CardWithdrawQuery
from DayFrequencyQuery import DayFrequencyQuery
from FestivalRelgionQuery import FestivalRelgionQuery

# if I have a CSV file without a header then reader.read(header=False)
try:
    bank_frequency_query = BankFrequencyQuery("AggregatedData.csv")
    bank_frequency_query.run()
except TypeError:
    print("CSV file was not given as a arguement")
except FileNotFoundError:
    print("CSV file was not found")

try:
    day_frequency_query = DayFrequencyQuery("AggregatedData.csv")
    day_frequency_query.run()
except TypeError:
    print("CSV file was not given as a arguement")
except FileNotFoundError:
    print("CSV file was not found")

try:
    card_withdraw_query = CardWithdrawQuery("AggregatedData.csv")
    card_withdraw_query.run()
except TypeError:
    print("CSV file was not given as a arguement")
except FileNotFoundError:
    print("CSV file was not found")

try:
    festival_relgion_query = FestivalRelgionQuery("AggregatedData.csv")
    festival_relgion_query.run()
except TypeError:
    print("CSV file was not given as a arguement")
except FileNotFoundError:
    print("CSV file was not found")
