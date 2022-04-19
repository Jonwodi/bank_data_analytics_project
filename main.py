from BankFrequencyQuery import BankFrequencyQuery
from CardWithdrawQuery import CardWithdrawQuery
from DayFrequencyQuery import DayFrequencyQuery
from FestivalRelgionQuery import FestivalRelgionQuery


# if I have a CSV file without a header then reader.read(header=False)
def run_query(query):
    try:
        query.run()
    except FileNotFoundError:
        print("CSV file was not found")


run_query(BankFrequencyQuery("AggregatedData.csv"))
run_query(DayFrequencyQuery("AggregatedData.csv"))
run_query(CardWithdrawQuery("AggregatedData.csv"))
run_query(FestivalRelgionQuery("AggregatedData.csv"))
