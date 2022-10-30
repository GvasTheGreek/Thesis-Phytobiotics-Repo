import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import seaborn.timeseries


# matplotlib may not be a great choice. It's oriented towards publication-quality figures, not real-time display.


##################################################      BASIC EXAMPLES       #################################################
# Basic Line -- Not For Further Use


def f1():
    years = [2010, 2011, 2012, 2013, 2014, 2015]
    yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
    plt.plot(years, yield_apples)
    plt.xlabel('years')
    plt.ylabel('apples')
    plt.show()


# Stacked Bar --Not For Further Use
def f2():
    years = range(2000, 2006)
    apples = [0.35, 0.6, 0.9, 0.8, 0.7, 0.65]
    oranges = [0.4, 0.8, 0.7, 0.7, 0.6, 0.8]
    plt.bar(years, oranges)
    plt.bar(years, apples, bottom=oranges)
    plt.xlabel('Year')
    plt.ylabel('Yield (Tons Per Hectare)')
    plt.title("Crop Yields")
    plt.show()

##################################################      LINE PLOTS       #################################################


# Lineplot -- Showing news cases that occured every day
def fa():
    tips = pd.read_csv("WHO-COVID-19-global-data.csv")
    sns.lineplot(data=tips, x="Date_reported", y="New_cases")
    plt.xlabel('Date_reported')
    plt.ylabel('New_cases')
    plt.title("Πλήθος συμπτωμάτων ανά ημερομηνία")
    plt.show()


# fa()


# Lineplot -- Showing news cases that occured every day
def fb():
    tips = pd.read_json("WHO-COVID-19-global-data.json")
    sns.lineplot(data=tips, x="Date_reported", y="New_cases")
    plt.xlabel('Date_reported')
    plt.ylabel('New_cases')
    plt.title("Πλήθος συμπτωμάτων ανά ημερομηνία")
    plt.show()
# fb()


# Triple Lineplot -- Showing the progress of the temperature , humitidy and ambient_noise in time.
def fc():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.lineplot(data=tips, x="Timestamp", y="temperature", marker="o")
    sns.lineplot(data=tips, x="Timestamp", y="humidity", marker='*')
    sns.lineplot(data=tips, x="Timestamp", y="ambient_noise")
    plt.legend(['temperature', 'humidity', 'ambient_noise'])
    plt.xlabel('Timestamp')
    plt.ylabel('temp - humidity - ambient noise')
    plt.title("H αλλαγή θερμοκρασίας υγρασίας θορύβου στο χρόνο")
    plt.show()


# fc()


# Sum of Cases In a lineplot with margin error
# You can check if it works by the type of csv the file produces. Long form
def fd():
    tips = pd.read_json("WHO-COVID-19-global-data.json")
    sns.lineplot(data=tips, x="Date_reported", y="Cumulative_cases")
    plt.legend(['Sum Of Cases'])
    plt.xlabel('Date_reported')
    plt.ylabel('Sum Of Cases')
    plt.title("Η συνολική αύξηση κρουσμάτων στο χρόνο")
    plt.show()


# fd()


##################################################      BAR PLOTS       #################################################


# Side Bar -- Temperature per Timestamp Analoga ti tha valeis ws time allazei i thesi (To Bar plot den sinistatai gia time)
def fe():
    tips = pd.read_json("Sensor_Data_RTH1.json")
    #sns.barplot(x='NH3 (ppm)', y='temperature (\u00b0C)', data=tips)
    sns.barplot(y='NH3 (ppm)', x='ambient_light (lux)', data=tips)
    plt.xlabel('Time')
    plt.ylabel('temperature')
    plt.title("Η θερμοκρασία ανά χρόνο")
    plt.show()


# fe()


# Side Bar -- Temperature per Timestamp Grouped By humidity
def fh():
    tips = pd.read_json("Sensor_Data_RTH2.json")
    # data = sns.load_dataset(tips)
    sns.barplot(y='Timestamp', x='temperature (\u00b0C)', hue='humidity (%)', data=tips)
    plt.xlabel('temperature')
    plt.ylabel('Timestamp')
    plt.title("θερμοκρασία ανά Χρόνο δεδομένη την υγρασία")
    plt.show()


# fh()


##################################################      COUNT PLOTS       #################################################
# Voleuei to CountPlot an thelw na paiksw me Count Of Records


# Side Bar Countplot -- Can be used if i want to depict a bar with count of Records
def ff():
    tips = pd.read_json("Sensor_Data_RTH2.json")
    figure, axs = plt.subplots(ncols=2)
    sns.set_theme(style="darkgrid")
    sns.countplot(y='temperature (\u00b0C)', data=tips, ax=axs[0])
    axs[0].set_xlabel('Count Of Records')
    axs[0].set_ylabel('temperature')
    axs[0].set_title("θερμοκρασία ανά Δείγματα")

    sns.countplot(y='humidity (%)', data=tips, ax=axs[1])
    axs[1].set_xlabel('Count Of Records')
    axs[0].set_ylabel('humidity')
    axs[1].set_title("Υγρασία ανά Δείγματα")
    plt.subplots_adjust(bottom=0.15)
    plt.show()


# ff()


# Side Bar -- This example includes "hue function or break down by".
# Voleuei an exw string me 3-4 periptwseis giati alliws xalaei polu
def fg():
    tips = pd.read_json("Sensor_Data_RTH3.json")
    sns.set_theme(style="darkgrid")
    sns.countplot(y='ambient_noise', data=tips)
    plt.xlabel('Count Of Records')
    plt.ylabel('θόρυβος Περιβάλλοντος')
    plt.title("Αριθμός Δειγμάτων Ανά Θόρυβο Περιβάλλοντος")
    plt.show()


# fg()


##################################################      SCATTER PLOTS       #################################################


# Scatterplot -- Presenting how much ambient_noise is affected by temp and humidity
def fi():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    fig = plt.figure()
    sns.scatterplot(x=tips.temperature, y=tips.humidity, hue=tips.ambient_noise, s=70)
    plt.xlabel('temperature')
    plt.ylabel('humidity')
    plt.title("Heatmap θερμοκρασίας ανά Yγρασία χωρισμένο ανά θόρυβο")
    plt.show()


# fi()


# Scatterplot -- Presenting how much ambient_light is affected by temp and humidity
# To ambient_Light δεν παρεχει μεγάλη αποσαφήνιση στην συσχέτιση των 2 καθώς η τιμή του δεν μεταβάλλεται αρκετά.
def fj():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.scatterplot(x=tips.temperature, y=tips.humidity, hue=tips.ambient_light, s=70)
    plt.xlabel('temperature')
    plt.ylabel('humidity')
    plt.title("Heatmap θερμοκρασίας ανά Yγρασία χωρισμένο ανά λαμψη")
    plt.show()


# fj()


# Scatterplot -- Presenting how much CO2 is affected by temp and humidity
def fk():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.scatterplot(x=tips.temperature, y=tips.humidity, hue=tips.CO2, s=70)
    plt.xlabel('temperature')
    plt.ylabel('humidity')
    plt.title("Heatmap θερμοκρασίας ανά Yγρασία χωρισμένο ανά CO2")
    plt.show()


# fk()


# Scatterplot -- Presenting how much NH3 is affected by temp and humidity
def fl():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.scatterplot(x=tips.temperature, y=tips.humidity, hue=tips.NH3, s=70)
    plt.xlabel('temperature')
    plt.ylabel('humidity')
    plt.title("Heatmap θερμοκρασίας ανά Yγρασία χωρισμένο ανά NH3")
    plt.show()


# fl()


# Scatterplot -- Presenting how much CO2 is affected by temp and ambient_noise
def fm():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.scatterplot(x=tips.temperature, y=tips.ambient_noise, hue=tips.CO2, s=70)
    plt.xlabel('temperature')
    plt.ylabel('ambient_noise')
    plt.title("Heatmap θερμοκρασίας ανά θορύβου χωρισμένο ανά CO2")
    plt.show()
# fm()


# Scatterplot -- Presenting how much humidity is affected by temp and ambient_noise
def fn():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.scatterplot(x=tips.temperature, y=tips.ambient_noise, hue=tips.humidity, s=70)
    plt.xlabel('temperature')
    plt.ylabel('ambient_noise')
    plt.title("Heatmap θερμοκρασίας ανά θορύβου χωρισμένο ανά ποσοστό υγρασίας")
    plt.show()
# fn()


# Scatterplot -- Presenting how much ambient_noise is affected by temp and CO2
def fks():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.scatterplot(x=tips.temperature, y=tips.CO2, hue=tips.ambient_noise, s=70)
    plt.xlabel('temperature')
    plt.ylabel('CO2')
    plt.title("Heatmap θερμοκρασίας ανά CO2 χωρισμένο ανά ποσοστό θορύβου")
    plt.show()


# fks()


# Scatterplot -- Presenting how much humidity is affected by temp and CO2
def fο():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.scatterplot(x=tips.temperature, y=tips.CO2, hue=tips.humidity, s=70)
    plt.xlabel('temperature')
    plt.ylabel('CO2')
    plt.title("Heatmap θερμοκρασίας ανά CO2 χωρισμένο ανά ποσοστό υγρασίας")
    plt.show()
# fο()


# Scatterplot -- Presenting how much NH3 is affected by temp and CO2
def fp():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.scatterplot(x=tips.temperature, y=tips.CO2, hue=tips.NH3, s=60)
    plt.xlabel('temperature')
    plt.ylabel('CO2')
    plt.title("Heatmap θερμοκρασίας ανά CO2 χωρισμένο ανά ποσοστό αμμωνίας")
    plt.show()
# fp()


# Scatterplot -- Presenting how much Temperature is affected by Ambient_noise and CO2
def fr():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.scatterplot(x=tips.CO2, y=tips.humidity, hue=tips.temperature, size=tips.temperature, s=60)
    plt.xlabel('Διοξείδιο του Άνθρακα')
    plt.ylabel('θερμοκρασία')
    plt.title("Heatmap Διοξείδιου ανά υγρασία με βάση τη θερμοκρασία")
    plt.show()


# fr()


# Double Scatterplot on the same Figure -- Showing how much ambient_noise is affected by temp and humidity
# The dots are affected by the value as well.
def fs():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    figure, axs = plt.subplots(ncols=2)
    # plt.title('Figure1')
    sns.scatterplot(x=tips.temperature, y=tips.humidity, hue=tips.ambient_noise, size=tips.ambient_noise, s=70, ax=axs[0])
    # plt.title('Figure2')
    sns.scatterplot(x=tips.temperature, y=tips.humidity, hue=tips.ambient_noise, s=70, ax=axs[1])

    plt.show()


# fs()

# Scatterplot -- Presenting how much Temperature is affected by Ambient_noise and CO2
def ffs():
    tips = pd.read_json("Sensor_Data_RTH4.json")

    #sns.scatterplot(x="CO2", y="humidity", hue="temperature", size="temperature", style="Entity-Name", data=tips)
    sns.jointplot(data=tips, x="CO2", y="humidity", hue="ambient_noise")
    #plt.title("Heatmap Διοξείδιου ανά υγρασία με βάση τη θερμοκρασία")
    #plt.xlabel('Διοξείδιο του Άνθρακα')
    # plt.ylabel('θερμοκρασία')
    #plt.title("Heatmap Διοξείδιου ανά υγρασία με βάση τη θερμοκρασία")
    plt.show()


# ffs()

# Scatterplot -- Presenting how much Temperature is affected by Ambient_noise and CO2


def ffx():
    import matplotlib.style as mplstyle
    import matplotlib as mpl
    #from IPython.display import Image

    #mplstyle.use({'mplstyle': 'fast'})
    tips = pd.read_json("Sensor_Data_RTH4.json")
    tips = pd.DataFrame(tips)

    #sns.scatterplot(x="CO2", y="humidity", hue="temperature", size="temperature", style="Entity-Name", data=tips)
    # sns.set_theme('fast')
    #sns.pairplot(data=tips, hue="Entity-Name")
    #plt.title("Heatmap Διοξείδιου ανά υγρασία με βάση τη θερμοκρασία")
    #plt.xlabel('Διοξείδιο του Άνθρακα')
    # plt.ylabel('θερμοκρασία')
    #plt.title("Heatmap Διοξείδιου ανά υγρασία με βάση τη θερμοκρασία")
    # mplstyle.use('fast')
    # plt.show(block=True)

    sns_plot = sns.pairplot(tips, size=2.0)
    sns_plot.savefig("pairplot.png")

    plt.clf()  # Clean parirplot figure from sns
    Image(filename='pairplot.png')  # Show pairplot as image

# ffx()

# Scatterplot -- Presenting how much Temperature is affected by Ambient_noise and CO2


def ffy():
    tips = pd.read_json("Sensor_Data_RTH4.json")

    #sns.scatterplot(x="CO2", y="humidity", hue="temperature", size="temperature", style="Entity-Name", data=tips)
    sns.jointplot(data=tips, x="CO2", y="temperature", hue="ambient_light", kind="hist")
    #plt.title("Heatmap Διοξείδιου ανά υγρασία με βάση τη θερμοκρασία")
    #plt.xlabel('Διοξείδιο του Άνθρακα')
    # plt.ylabel('θερμοκρασία')
    #plt.title("Heatmap Διοξείδιου ανά υγρασία με βάση τη θερμοκρασία")
    plt.show()


# ffy()


##################################################     Stacked Areas       #################################################


# Area chart
def ft():
    tips = pd.read_json("Sensor_Data_RTH4.json")

    # set the seaborn style
    sns.set_style("whitegrid")

    # Color palette
    blue, = sns.color_palette("muted", 1)

    x = tips["Timestamp"]
    y = tips["temperature"]
    z = tips["humidity"]

    # Make the plot
    fig, ax = plt.subplots()
    ax.plot(x, y, color=blue, lw=1)
    ax.plot(x, z, color="red", lw=1)
    plt.legend(['temperature', 'humidity'])

    ax.fill_between(x, 0, y, alpha=.3)
    ax.fill_between(x, 0, z, alpha=.3)

    plt.xlabel('Time')
    plt.ylabel('temperature & humidity')

    # Show the graph
    plt.show()


#ft()


# Stacked Area chart, needs fixing
def fy():
    tips = pd.read_json("Sensor_Data_RTH4.json")

    # set the seaborn style
    sns.set_style("whitegrid")

    # Color palette
    blue, = sns.color_palette("muted", 1)

    x = tips["Timestamp"]
    y = tips["temperature"]
    z = tips["humidity"]
    w = tips["NH3"]

    plt.stackplot(x, y, z, w, labels=['A', 'B', 'C'])
    plt.legend(loc='upper left')

    # Show the graph
    plt.show()


# fy()


##################################################     Pie Charts Maybe       #################################################


# Timeline -- Showing the temperature variation during the time.
def f8():

    tips = pd.read_json("Sensor_Data_RTH4.json")
    sns.set_style("darkgrid")
    plt.style.use('fivethirtyeight')
    plt.plot(tips.Timestamp, tips.temperature)
    plt.show()


# f8()


#########################################################     SECOND FILE COVID       ###################################################################################
#########################################################         LINE PLOTS          #################################################


# Line Plot New Cases Per Day
def ex1():
    tips = pd.read_json("WHO-COVID-19-global-data.json")
    sns.lineplot(data=tips, x="Date_reported", y="New_cases")
    plt.xlabel('Date_reported')
    plt.ylabel('New_cases')
    plt.title("Συνολικό πλήθος κρουσμάτων ανά μέρα")
    plt.style.use('fivethirtyeight')
    plt.show()


# ex1()


# Line Plot New Deaths Per Day
def ex2():
    tips = pd.read_json("WHO-COVID-19-global-data.json")
    sns.lineplot(data=tips, x="Date_reported", y="New_deaths")
    plt.xlabel('Date_reported')
    plt.ylabel('New_deaths')
    plt.title("Συνολικό πλήθος θανάτων ανά μέρα")
    plt.style.use('fivethirtyeight')
    plt.show()


# ex2()


##################################################      BAR PLOTS       #################################################


# Doesn't work
# LIne Plot New Deaths per Day
def ex3():
    tips = pd.read_json("WHO-COVID-19-global-data.json")
    # sns.lineplot(data=tips.sort_values('Country').tail(5), x="Date_reported", y="New_deaths", hue="Country")
    # plt.xlabel('Date_reported')
    # plt.ylabel('New_deaths')
    # plt.title("Συνολικό πλήθος θανάτων ανά μέρα")
    # plt.style.use('fivethirtyeight')
    # plt.show()

    sns.barplot(x='Country', y='New_cases', data=tips.sort_values('New_cases', ascending=False).head(5))
    plt.xlabel('Time')
    plt.ylabel('temperature')
    plt.title("Η θερμοκρασία ανά χρόνο")
    # plt.style.use('fivethirtyeight')
    plt.show()


# ex3()


##################################################      STACKED AREAS       #################################################


# Area chart --- Not the ideal result
def ex4():
    tips = pd.read_json("WHO-COVID-19-global-data.json")

    # set the seaborn style
    sns.set_style("whitegrid")

    # Color palette
    blue, = sns.color_palette("muted", 1)

    x = tips["Date_reported"]
    y = tips["New_deaths"]

    # Make the plot
    fig, ax = plt.subplots()
    ax.plot(x, y, color=blue, lw=3)
    ax.fill_between(x, 0, y, alpha=.3)

    plt.xlabel('Date')
    plt.ylabel('New_deaths')
    # plt.legend(['New_cases'])

    # Show the graph
    plt.show()


# ex4()


##################################################      PIE       #################################################

def ex5():

    tips = pd.read_json("WHO-COVID-19-global-data.json")

    new = pd.DataFrame(tips, columns=['Country', 'New_cases'])
    tp = new.groupby('Country').sum()
    tp = tp.to_dict()

    countries = []
    cases_per_countries = []

    for i in tp.keys():
        for j in tp[i].keys():
            countries.append(j)
        for k in tp[i].values():
            cases_per_countries.append(k)

    cases_per_countries, countries = zip(*sorted(zip(cases_per_countries, countries), reverse=True))

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    sizes = [cases_per_countries[0], cases_per_countries[1], cases_per_countries[2], cases_per_countries[3], cases_per_countries[4]]
    labels = [countries[0], countries[1], countries[2], countries[3], countries[4]]
    explode = (0, 0.1, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, explode=explode)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Οι 5 χώρες με τα περισσότερα κρούσματα Covid")

    plt.show()


def ex6():

    tips = pd.read_json("WHO-COVID-19-global-data.json")

    new = pd.DataFrame(tips, columns=['Country', 'New_cases'])
    tp = new.groupby('Country').sum()
    tp = tp.to_dict()

    countries = []
    cases_per_countries = []

    for i in tp.keys():
        for j in tp[i].keys():
            countries.append(j)
        for k in tp[i].values():
            cases_per_countries.append(k)

    cases_per_countries, countries = zip(*sorted(zip(cases_per_countries, countries), reverse=True))

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    sizes = [cases_per_countries[0], cases_per_countries[1], cases_per_countries[2], cases_per_countries[3], cases_per_countries[4]]
    labels = [countries[0], countries[1], countries[2], countries[3], countries[4]]
    explode = (0, 0.1, 0, 0, 0)

    sizes_min = [cases_per_countries[-6], cases_per_countries[-7], cases_per_countries[-8], cases_per_countries[-9], cases_per_countries[-10]]
    labels_min = [countries[-6], countries[-7], countries[-8], countries[-9], countries[-10]]

    print(sizes_min)
    print(labels_min)

    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)
        return my_autopct

    fig1, axs = plt.subplots(ncols=2)
    axs[0].pie(sizes, labels=labels, autopct=make_autopct(sizes),
               shadow=True, startangle=90, explode=explode)
    axs[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    axs[0].set_title("Οι 5 χώρες με τα περισσότερα κρούσματα Covid")

    axs[1].pie(sizes_min, labels=labels_min, autopct=make_autopct(sizes_min),
               shadow=True, startangle=90, explode=explode)
    axs[1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    axs[1].set_title("Οι 5 χώρες με τα περισσότερα κρούσματα Covid")

    plt.show()


# ex5()


def ffz():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    tips = pd.DataFrame(tips)

    sns.displot(data=tips, x="CO2", hue="NH3", multiple="stack", kind="kde")
    #plt.title("Heatmap Διοξείδιου ανά υγρασία με βάση τη θερμοκρασία")
    #plt.xlabel('Διοξείδιο του Άνθρακα')
    # plt.ylabel('θερμοκρασία')
    #plt.title("Heatmap Διοξείδιου ανά υγρασία με βάση τη θερμοκρασία")
    plt.show(block=True)


# ffz()

# regression
def final():
    tips = pd.read_json("Sensor_Data_RTH4.json")
    tips = pd.DataFrame(tips)

    #sns.regplot(x="temperature", y="CO2", data=tips)
    sns.lmplot(x="temperature", y="CO2", data=tips)
    plt.show(block=True)


# final()
# Ypo sizitisi fy,ft, ffx ,ffs ,ffy ,ffz , final
# mpikan ffx
# ffz()

def countplot_CO2():
    import random
    import json
    #tips = pd.read_json("Sensor_Data_RTH4.json")

    #tips = pd.DataFrame(tips)
    with open("Sensor_Data_RTH4.json", 'r') as f:
        data = json.load(f)

        dat = random.sample(data, k=75)
        dat = pd.DataFrame(dat)

        sns.set_theme(style="darkgrid")
        sns.countplot(y='CO2', data=dat)
        plt.xlabel('Count Of Records')
        plt.ylabel('Διοξείδιο Του Ανθρακα')
        plt.title("Αριθμός Δειγμάτων Ανά CO2")
        plt.show()


# countplot_CO2()


def temp():
    import random
    import json
    tips = pd.read_json("Sensor_Data_RTH3.json")
    print(type(tips))

    with open("Sensor_Data_RTH4.json", 'rb') as f:
        data = json.load(f)

        dat = random.sample(data, k=100)
        print(type(dat))
        print(len(data))
