def main(credit, paydown, interest, account_fee, paydown_min):
    import matplotlib.pyplot as plt

    values, months, interests, total, month, interest_total, total_paid = [], [], [], [], 0, 0, 0

    months.append(month);  values.append(credit);  interests.append(interest_total);  total.append(0);  print(f"\nMonth {month}: {credit:,.2f}€\n")

    def create_plot():
        plt.ticklabel_format(style = "plain")
        
        plt.title(f"Credit (€) as a function of Time (months), f(Time) = Value");  plt.xlabel("Time (months)");  plt.ylabel(f"Credit (€)")
        
        plt.plot(months, values, label="Credit");  plt.plot(months, interests, label="Interest");  plt.plot(months, total, label="Total paid"),  plt.legend();  plt.show()

    while credit > 30:
        month += 1;  months.append(month)
        
        paydown_current = paydown * credit
        
        if paydown_current >= paydown_min:
            pass
        else:
            paydown_current = paydown_min
    
        interest_current = credit * interest;  interest_total += interest_current;  interests.append(interest_total)
        credit = credit - paydown_current;  values.append(credit)

        total_paid_current = interest_current + paydown_current + account_fee
        total_paid += total_paid_current;  total.append(total_paid)

        print(f"""Month {month}: {credit:,.2f}€ (Total paid last month = {total_paid_current:,.2f}€, Interest = {interest_current:,.2f}€, Paydown = {paydown_current:,.2f}€, Account fee = {account_fee}€, Total paid = {total_paid:,.2f}€)\n""")
    
    create_plot()
        
main(1000, 0.2, 0.11, 3.5, 30)