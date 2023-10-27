import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }

listMonth = {'January':1, 'Feburary':2, 'March':3, 'April':4, 'May':5, 'June':6}
listDayOfWeek = {"Monday": 0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print("")
        print("Please select a city:")
        print(" c  => Chicago")
        print(" ny => New York")
        print(" w  => Washington")
        city = input("\n")
        city = city.lower()
        if city == "chicago" or city == "c":
            city = "chicago"
            break
        elif city == "new york" or city == "ny" or city == "new_york_city":
            city = "new_york_city"
            break
        elif city == "washington" or city ==  "w":
            city = "washington"
            break
        else:
            print("\n\"{}\" is wrong input, please select again!\n".format(city))
    print("You have select city: {}".format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print("")
        print("Please select a month:")
        print(" 0 => All")
        print(" 1 => January")
        print(" 2 => Feburary")
        print(" 3 => March")
        print(" 4 => April")
        print(" 5 => May")
        print(" 6 => June")
        month = input("\n")
        month = month.capitalize()
        if month == "0" or month == "All".capitalize():
            month = "All".capitalize()
            break
        elif month == "1" or month == "January".capitalize():
            month = "January".capitalize()
            break
        elif month == "2" or month == "Feburary".capitalize():
            month = "Feburary".capitalize()
            break
        elif month == "3" or month == "March".capitalize():
            month = "March".capitalize()
            break
        elif month == "4" or month == "April".capitalize():
            month = "April".capitalize()
            break
        elif month == "5" or month == "May".capitalize():
            month = "May".capitalize()
            break
        elif month == "6" or month == "June".capitalize():
            month = "June".capitalize()
            break
        else:
            print("\n\"{}\" is wrong input, please select again!\n".format(month))
    print("You have select month: {}".format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print("")
        print("Please select a day:")
        print(" all => All")
        print(" mon => Monday")
        print(" tue => Tuesday")
        print(" wed => Wednesday")
        print(" thu => Thursday")
        print(" fri => Friday")
        print(" sat => Saturday")
        print(" sun => Sunday")
        day = input("\n")
        day = day.capitalize()
        if day == "All" or day == "All".capitalize():
            day = "All".capitalize()
            break
        elif day == "Mon" or day == "Monday".capitalize():
            day = "Monday".capitalize()
            break
        elif day == "Tue" or day == "Tuesday".capitalize():
            day = "Tuesday".capitalize()
            break
        elif day == "Wed" or day == "Wednesday".capitalize():
            day = "Wednesday".capitalize()
            break
        elif day == "Thu" or day == "Thursday".capitalize():
            day = "Thursday".capitalize()
            break
        elif day == "Fri" or day == "Friday".capitalize():
            day = "Friday".capitalize()
            break
        elif day == "Sat" or day == "Saturday".capitalize():
            day = "Saturday".capitalize()
            break
        elif day == "Sun" or day == "Sunday".capitalize():
            day = "Sunday".capitalize()
            break
        else:
            print("\n\"{}\" is wrong input, please select again!\n".format(day))
    print("You have select day: {}".format(day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nLoad data for: Citiy = {}, Month = {}, Day = {}".format(city, month, day))
    data = pd.read_csv('./' + CITY_DATA[city])
    print(data)
    """Convert Start Time to Datetime """
    data["Start Time"] = pd.to_datetime(data["Start Time"])

    """Fitler data by month and day"""
    if month != "none":
        print("Filter data by month\n")
        #data = data[data["Start Time"].dt.month ==  listMonth.get(month)]
        data = data[data["Start Time"].dt.month ==  listMonth.get(month)]

    if day != "none":
        print("Filter data by Day of week\n")
        data = data[data["Start Time"].dt.dayofweek == listDayOfWeek.get(day)]

    df = pd.DataFrame(data)
    print(df)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_stats = df["Start Time"].dt.month.value_counts()
    most_common_month = month_stats.idxmax()
    print("The most common month:", most_common_month)

    # TO DO: display the most common day of week
    day_stats = df["Start Time"].dt.dayofweek.value_counts()
    most_common_day = day_stats.idxmax()

    for key, value in listDayOfWeek.items():
        if value == most_common_day:
            print("The most common day of week:", key)
            break

    # TO DO: display the most common start hour
    hour_stats = df["Start Time"].dt.hour.value_counts()
    most_common_hour = hour_stats.idxmax()
    print("The most common hour: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_stats = df["Start Station"].value_counts()
    common_start = start_stats.idxmax()
    print("Most commonly used start station: ", common_start)

    # TO DO: display most commonly used end station
    end_stats = df["End Station"].value_counts()
    common_end = end_stats.idxmax()
    print("Most commonly used end station: ", common_end)

    # TO DO: display most frequent combination of start station and end station trip
    group_combination = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count')
    most_frequent = group_combination.loc[group_combination['count'].idxmax()]
    print("Most frequent combination:")
    print("Start station: ", most_frequent['Start Station'])
    print("End station: ", most_frequent['End Station'])
    print("Count: ", most_frequent['count'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration'] = df['Trip Duration'].astype('int')
    sum_duration = df['Trip Duration'].sum()
    print("Total duration: {} (seconds)".format(sum_duration))

    # TO DO: display mean travel time
    travel_time = df.groupby(["Start Station", "End Station"])["Trip Duration"].mean()
    print("Mean travel time")
    print(travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    genders = df["Gender"].value_counts()
    print(genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = int(df["Birth Year"].min())
    print("The Earliest Year of birth: ", earliest_year)

    most_recent = int(df["Birth Year"].max())
    print("Most recent: ", most_recent)
    
    year_stats = df["Birth Year"].value_counts()
    most_common_year_of_birth = year_stats.idxmax()
    print("Most common year of birth:", int(most_common_year_of_birth))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Display raw data """
    i = 0
    raw = input("Do you want to view raw data? (yes/no)\n").lower()
    # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)
    
    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:(i+5)])
            raw = input("Do you want to view raw data? (yes/no)\n").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except BaseException:
            print("The data is invalid!")

if __name__ == "__main__":
	main()
