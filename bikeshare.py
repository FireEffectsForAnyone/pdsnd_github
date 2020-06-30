import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify which city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalidinputs
    while True:
        city = input("Hello! What city would you like to learn more about? Chigaco, New York City, or Washington? ")
        if city not in ("Chigaco", "New York City", "Washington"):
            print("Sorry, that is not a valid city or you may have misspelled a city name. Please choose either Chigaco, New York City, or Washington")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Nice! Is there a specific month you wanna search by? If not, type 'all', if there is a month you do wanna search by, type in the number correspending to said month (e.g. 1 for January, 2 for February etc...). ")
        if month not in ("all", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"):
            print("Sorry, that is not a valid number/answer. Please type in 'all' if you do not wish to search by month. However, if you do wanna search by month, please type in a number correspending to said month (e.g. 1 for January, 2 for February etc...). ")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Nice! Is there a specific day of the week you wanna search by? If not, type 'all', if there is a day you do wanna search by, type in the number correspending to said day (e.g. 1 for Monday, 2 for Tuesday etc...). ")
        if day not in ("all", "1", "2", "3", "4", "5", "6", "7"):
            print("Sorry, that is not a valid number/answer. Please type in 'all' if you do not wish to search by a day of the week. However, if you do wanna search by a day of the week, please type in a number correspending to said day (e.g. 1 for Monday, 2 for Tuesday etc...). ")
            continue
        else:
            break

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print(common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print(total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("Sorry! There isn't any available gender data for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


"""Asking 5 lines of the raw data and more, if they want"""
def data(df):
raw_data = 0
while True:
answer = input("Do you want to see the raw data? Yes or No").lower()
if answer not in ['yes', 'no']:
answer = input("You wrote the wrong word. Please type Yes or No.").lower()
elif answer == 'yes':
raw_data += 5
print(df.iloc[raw_data : raw_data + 5])
again = input("Do you want to see more? Yes or No").lower()
if again == 'no':
break
elif answer == 'no':
return

def main():
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
    main()
