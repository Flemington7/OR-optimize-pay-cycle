from CardsInfo import *


def max_date_cycle_time(credit_cards, date):
    max_cycle_time = 0
    card_name = None
    for name, card in credit_cards.items():
        cycle_time = (card.billing_date - date + 30) % 30 + card.max_cycle_time - 30 + 1
        if cycle_time > max_cycle_time:
            max_cycle_time = cycle_time
            card_name = name
    return card_name, max_cycle_time


credit_cards_rearranged = credit_cards
max_total_cycle_time = 0
billing_dates_rearranged = []
# We assume that we have already known the basic information of the credit cards
for i in range(1, 31):
    credit_cards_rearranged["BOD"].billing_date = i
    for j in range(1, 31):
        credit_cards_rearranged["PAB"].billing_date = j
        for k in range(1, 31):
            credit_cards_rearranged["ICBC"].billing_date = k

            # Calculate the total cycle time in this satiation
            total_cycle_time = 0
            for date in range(1, 31):
                card_name, max_cycle_time = max_date_cycle_time(
                    credit_cards_rearranged, date
                )
                total_cycle_time += max_cycle_time

            if total_cycle_time >= max_total_cycle_time:
                max_total_cycle_time = total_cycle_time
                billing_dates_rearranged = [i, j, k]
                print("sol", billing_dates_rearranged, "fval", max_total_cycle_time)
