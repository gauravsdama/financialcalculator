
import matplotlib.pyplot as plt
plt.ylabel('Account value')
plt.xlabel('Year')

years = int(input("How long is your investment term in years? "))
initial_investment = int(input("What is your initial investment? Keep in mind that it may be zero."))
yearly = int(input("How much will your investment be in year 1?"))
yearlyy = yearly
increment = float(input("By how much will you increment your yearly investments?(%)?"))
increment *= 0.01
increment += 1
print('The S&P500 index fund has returned a yearly average of approximately 10% over the last 50 years and 14% for the last 10 years. A conservative assumed return would be 9%.')
ror = float(input("What is your expected rate of return (%)?"))
ror *= 0.01
ror += 1
account = initial_investment
principle = initial_investment
yearlist = [0]
accountlist = [0]
yearss = years
yearcountfrombottom = 0


while years > 0:
    yearcountfrombottom +=1
    years = years - 1
    yearlyy = yearlyy * increment
    account += yearlyy
    account = account * ror
    print("At year",yearcountfrombottom,", your account is worth ", account,".")
    yearly = yearly * increment
    principle += yearly
    print("Your principle is ", principle,".")
    returns = account - principle
    print("your returns reaped are", returns,".")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    yearcount = yearss - years
    yearlist.append(yearcount)
    accountlist.append(account)

def plotin():

    plt.title('Account value over the years')
    plt.plot(yearlist, accountlist, color = 'blue', linewidth = 3, marker = 'o', markerfacecolor='red', markersize=12)
    maximu = (account*1.5)
    plt.ylim(0, maximu)
    plt.axis([0, yearss, 0, account])
    plt.show()
plotin()




