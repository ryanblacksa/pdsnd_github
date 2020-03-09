## Udacity Nano degree | Bikeshare opython project | Ryan Black
## Description: Program to investigate bikeshare data in 3 American cities.

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city would you like to explore Chicago, New York City or Washington?\n').lower()
    
    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
        "City is name is invalid! Please select from the choice above: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nPlease enter the month, between January and June, you would like to view or \'all\' for all 6 months:\n').lower()
    
    while month not in ['all','january','february','march','april','may','june']:
        month = input(
        "Month name is invalid! Please select enter a month between January and June: ").lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nPlease enter the day of the week which you would like to view or \'all\' for the full week:\n').lower()
    
    while day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day = input(
        "Day of the week is invalid! Please select enter a day of the week: ").lower()
        
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: {}".format(
        str(df['month'].mode()[0]))
    )

    # TO DO: display the most common day of week
    print("The most common day of the week: {}".format(
        str(df['day_of_week'].mode()[0]))
    )

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(
        str(df['start_hour'].mode()[0]))
    )

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: {} ".format(
        df['Start Station'].mode()[0])
    )

    # TO DO: display most commonly used end station
    print("The most common end station is: {}".format(
        df['End Station'].mode()[0])
    )

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    print("The most common route, start and end station combination is: {}".format(
        df['routes'].mode()[0])
    )

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['duration'] = df['End Time'] - df['Start Time']
    print("The total travel time is: {}".format(
        str(df['duration'].sum()))
    )

    # TO DO: display mean travel time
    print("The mean travel time is: {}".format(
        str(df['duration'].mean()))
    )

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Here are the counts of various user types:")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city != 'washington':
        print("\nHere are the counts of gender:")
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print("\nThe earliest birth year is: {}".format(
            str(int(df['Birth Year'].min())))
             )
        print("The latest birth year is: {}".format(
            str(int(df['Birth Year'].max())))
             )
        print("The most common birth year is: {}".format(
            str(int(df['Birth Year'].mode()[0])))
             )
    else :
        print('\nSorry! No gender or birthdate data avaialble for Washington.')
        
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)
    
def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """
    print('\nCalculating Display Data...\n')
    start_time = time.time()
    
    start_loc = 0
    end_loc = 5

    display_choice = input("Do you want to see the raw data?: Enter yes or no ").lower()

    if display_choice== 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you wish to continue?: Enter yes or no ").lower()
            if end_display == 'no':
                break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
