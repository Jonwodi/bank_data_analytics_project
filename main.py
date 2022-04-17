from BankFrequencyQuery import BankFrequencyQuery

# if I have a CSV file without a header then reader.read(header=False)
frequency_query = BankFrequencyQuery("AggregatedData.csv")
frequency_query.run()
