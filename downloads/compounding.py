def main(year_start, value_type, value_start, monthly_add, cagr, period, tax, inflation, unit, plot, log):
    import matplotlib.pyplot as plt

    def create_plot(mode):
        plt.ticklabel_format(style = "plain")
        
        plt.title(f"Value ({unit}) as a function of Time (years), f(Time) = Value");  plt.xlabel("Time (years)");  plt.ylabel(f"Value ({unit})")
        
        mode(years, values);  plt.show()

    years, values = [], [];  years.append(year_start);  values.append(value_start)

    print(f"""\n\nParameters: year_start = {year_start}, value_start = {value_start:,.2f} ({unit}), monthly_add = {monthly_add} ({unit}), cagr = {cagr}, period = {period} (years), tax = {tax * 100}%, inflation = {inflation * 100}%
\n\nYear {year_start}: {unit}{value_start:,.0f}\n""")
    
    if cagr >= 1:
        sign = "+";  result = "gain"
    else:
        sign = "";  result = "loss"

    for i in range(0, period):
        year_start += 1;  years.append(year_start);  value_start = (value_start + monthly_add * 12) * cagr;  values.append(value_start)
        
        change = values[i + 1] - values[i]

        print(f"Year {year_start}: {unit}{value_start:,.0f} ({sign}{unit}{change:,.0f} {result})\n")
    
    print(f"\nAverage yearly {result}\n\n= {sign}{unit}{(values[period] - values[0]) / period:,.0f}\n")

    if value_type == "investment":
        print(f"""\nMinimum after-tax inflation-adjusted value at the end of period ({year_start}): {1 - tax:,.2f} * {unit}{values[period]:,.0f} * {1 - inflation} ** {period}
\n= {unit}{(1 - tax) * values[period] * (1 - inflation) ** period:,.0f}\n\n""")
    else:
        pass
    
    if plot == 0:
        pass
    if plot == 1:
        if log == 1:
            create_plot(plt.semilogy)
        else:
            create_plot(plt.plot)

main(2026, "instrument", 66000, 0, 1.3, 20, 0.25, 0.04, "€", 1, 0)