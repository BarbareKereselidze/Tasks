import pandas as pd


class ProcessingTaxiData:
    def __init__(self, file_path, start_index=1000, num_of_records=1000):
        self.df = pd.read_csv(file_path)
        self.filtered_df = None

        self.start_index = start_index
        self.num_of_records = num_of_records

    def read_specified_records(self):
        """Reads a specified number of records. """
        stop_index = self.start_index + self.num_of_records
        self.filtered_df = self.df.iloc[self.start_index:stop_index].copy()

        return self.filtered_df

    def convert_to_datetime(self):
        """Converts pickup and dropoff datetime strings to datetime objects."""
        self.filtered_df.loc[:, 'pickup_datetime'] = pd.to_datetime(self.filtered_df['pickup_datetime'])
        self.filtered_df.loc[:, 'dropoff_datetime'] = pd.to_datetime(self.filtered_df['dropoff_datetime'])

        return self.filtered_df

    def delete_fields(self):
        """Deletes all fields except pickup_datetime and dropoff_datetime."""
        self.filtered_df = self.filtered_df.loc[:, ['pickup_datetime', 'dropoff_datetime']]

        return self.filtered_df

    def add_two_days_ride(self):
        """Adds a new field for is_two_days_ride."""
        self.filtered_df['is_two_days_ride'] = self.filtered_df.apply(ProcessingTaxiData.calculate_two_days_ride, axis=1)

        return self.filtered_df

    @staticmethod
    def calculate_two_days_ride(row):
        """Calculates the value for the new field is_two_days_ride."""
        if row['pickup_datetime'].date() == row['dropoff_datetime'].date():
            return 0
        else:
            return 1

    def replace_strings(self):
        """Replaces '_' with ' ' in column names."""
        self.filtered_df.columns = self.filtered_df.columns.str.replace('_', ' ')

        return self.filtered_df

    def process_data(self):
        """ Processes data. """
        self.read_specified_records()
        self.convert_to_datetime()
        self.delete_fields()
        self.add_two_days_ride()
        self.replace_strings()

        return self.filtered_df


# To display all 1000 rows
pd.set_option('display.max_rows', None)

path = 'nyc_tlc_yellow_trips_2018_subset_1.csv'
processor = ProcessingTaxiData(path)
result_df = processor.process_data()

print(result_df)



