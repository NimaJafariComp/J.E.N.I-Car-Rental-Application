import datetime
from collections import defaultdict

class Revenue:
    def __init__(self):
        pass

    def revenue(self, reservations: list[tuple]) -> dict:
        """
        Calculates weekly, monthly, and yearly revenue from reservations. Partiotioned Based on starting day(pay day) 

        Parameters
        ----------
        reservations : list[tuple]
            A list of reservations where each tuple contains reservation information.
            Tuple format: (id, start_date, end_date, ..., total_price)

        Returns
        -------
        dict
            A dictionary with keys for weekly, monthly, and yearly revenue. 
        """
        # Initialize revenue containers
        weekly_revenue = defaultdict(float)
        monthly_revenue = defaultdict(float)
        yearly_revenue = defaultdict(float)

        for reservation in reservations:
            # Extract necessary fields from each reservation
            start_date = reservation[1]
            total_price = reservation[-1]  # Assuming total_price is the last field

            if not isinstance(start_date, datetime.date):
                continue  # Skip invalid data

            # Calculate year, month, and ISO week
            year = start_date.year
            month = start_date.month
            week = start_date.isocalendar()[1]

            # Accumulate revenues
            weekly_revenue[f"{year}-{week:02}"] += total_price
            monthly_revenue[f"{year}-{month:02}"] += total_price
            yearly_revenue[year] += total_price

        # Convert defaultdict to regular dict for cleaner output
        return {
            "weekly": dict(weekly_revenue),
            "monthly": dict(monthly_revenue),
            "yearly": dict(yearly_revenue),
        }
