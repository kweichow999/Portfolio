def calculate(start_value, period, end_value):
    cagr = ((end_value / start_value) ** (1 / period) - 1) * 100

    if start_value > 0 and period > 0 and end_value > 0:
        print(f"\n\n\n\nCAGR (Compound Annual Growth Rate) of {cagr:,.2f}% is required to compound {start_value:,.0f}€ into {end_value:,.0f}€ in {period} years.\n\n\n\n")
    else:
        print(f"\n\n\n\nNo negative values allowed, please input positive values.\n\n\n\n")

calculate(10000, 10, 1000000)