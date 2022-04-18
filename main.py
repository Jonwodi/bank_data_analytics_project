from BankFrequencyQuery import BankFrequencyQuery
from DayFrequencyQuery import DayFrequencyQuery

# if I have a CSV file without a header then reader.read(header=False)
bank_frequency_query = BankFrequencyQuery("AggregatedData.csv")
bank_frequency_query.run()

day_frequency_query = DayFrequencyQuery("AggregatedData.csv")
day_frequency_query.run()
