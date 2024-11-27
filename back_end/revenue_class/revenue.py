import datetime
from collections import defaultdict

class Revenue:
    def __init__(self):
        # Initialize any necessary attributes
        pass

    def revenue(self, reservations: list[tuple]) -> dict:
        """
        Calculates the weekly, monthly, and yearly revenue from the reservations.

        Parameters
        ----------
        reservations : list[tuple]
            A list of reservations where each tuple contains reservation information.
        
        Returns
        -------
        dict
            A dictionary with keys for weekly, monthly, and yearly revenue.
        """
        weekly_revenue = defaultdict(float)
        monthly_revenue = defaultdict(float)
        yearly_revenue = defaultdict(float)

        # Loop through the reservations and calculate revenue
        for reservation in reservations:
            start_date = reservation[1]  # Assuming the start date is in the second column
            amount = reservation[2]  # Assuming the revenue amount is in the third column
            
            # Get the week, month, and year from the start_date
            week = start_date.strftime("%Y-%U")  # Format as Year-Week
            month = start_date.strftime("%Y-%m")  # Format as Year-Month
            year = start_date.year  # Get the year

            # Add the amount to each of the categories
            weekly_revenue[week] += amount
            monthly_revenue[month] += amount
            yearly_revenue[year] += amount

        # Return the revenue data as a dictionary
        return {
            'weekly': dict(weekly_revenue),
            'monthly': dict(monthly_revenue),
            'yearly': dict(yearly_revenue)
        }
