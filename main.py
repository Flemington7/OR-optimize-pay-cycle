# We assume that one month has 30 days.
# We assume that we have the same amount of money to spend every day.

from docplex.mp.model import Model


class CreditCard:
    def __init__(self, billing_date, repayment_date, max_cycle_time):
        self.billing_date = billing_date
        self.repayment_date = repayment_date
        self.max_cycle_time = max_cycle_time


def input_credit_card_info():
    cards = {}
    num_cards = int(input("Please enter the number of credit cards: "))
    for _ in range(num_cards):
        name = input("Please enter the name of the credit card: ")
        current_billing_date = int(input("Please enter the current billing date (1-30): "))
        current_repayment_date = int(input("Please enter the current repayment date (1-30): "))
        max_cycle_time = current_repayment_date + 30 + 30 - current_billing_date
        card = CreditCard(current_billing_date, current_repayment_date, max_cycle_time)
        cards[name] = card
    return cards


# input credit card info
credit_cards = input_credit_card_info()


def calculate_optimal_payment_cycle(credit_cards):
    # Calculate the optimal payment cycle
    credit_cards_rearranged = {}
    # Sort the credit cards by cycle time in descending order
    credit_cards_sorted_items = sorted(credit_cards.items(), key = lambda card: card[1].max_cycle_time, reverse = True)
    credit_cards_sorted = dict(credit_cards_sorted_items)

    # Create a model
    model = Model(name = "Optimal Payment Cycle")

    # Create decision variables for each credit card's billing date
    billing_dates = {card[0]: model.integer_var(1, 30, name = f"billing_date_{card[0]}") for card in credit_cards_sorted}

    # Create decision variables for each date's max cycle time
    max_cycle_times = {date: model.continuous_var(name = f"max_cycle_time_{date}") for date in range(1, 31)}

    # Add constraints to ensure that max_cycle_times[date] is equal to the max cycle time for that date
    for date in range(1, 31):
        for card in credit_cards_sorted:
            date_cycle_time = billing_dates[card[0]] + 30 - date + card[1].max_cycle_time - 30 \
                if billing_dates[card[0]] < date \
                else card[1].max_cycle_time - 30 + billing_dates[card[0]] - date
            model.add_constraint(max_cycle_times[date] >= date_cycle_time)
    # Every date has its own repayment cycle which based on the billing date of the credit cards and corresponding cycle time,
    # we need to sum them up to get the total cycle time

    # Create the objective function
    total_max_cycle_time = model.sum(max_cycle_times.values())
    model.maximize(total_max_cycle_time)

    # Solve the model
    solution = model.solve()

    # return the optimal repayment cycle
    if solution:
        for card in credit_cards_sorted:
            credit_cards_rearranged[card[0]] = billing_dates[card[0]].solution_value
        print("Solution found!")
        print(credit_cards_rearranged)
        return credit_cards_rearranged
    else:
        print("No solution found!")
        return None


calculate_optimal_payment_cycle(credit_cards)
