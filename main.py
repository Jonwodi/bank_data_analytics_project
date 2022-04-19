from queries.BankFrequencyQuery import BankFrequencyQuery
from queries.CardWithdrawQuery import CardWithdrawQuery
from queries.DayFrequencyQuery import DayFrequencyQuery
from queries.FestivalRelgionQuery import FestivalRelgionQuery


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
