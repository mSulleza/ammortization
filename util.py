import pandas as pd
import numpy as np

def repayments_per_year(years, repayment_frequency):
    if repayment_frequency == "bi_weekly":
        return years * 24
    elif repayment_frequency == "monthly":
        return years * 12
    elif repayment_frequency == "quarterly":
        return years / 4
    elif repayment_frequency == "annually":
        return years
    elif repayment_frequency == "bi-yearly":
        return years / 2

