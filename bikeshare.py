import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTH_LIST = ['january',
              'february',
              'march',
              'april',
              'may',
              'june',
              'all']

DAYS_LIST = ['monday',
             'tuesday',
             'wednesday',
             'thursday',
             'friday',
             'saturday',
             'sunday',
             'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    try:
        city = input('Which city would you like to analyze? chicago, new york city or washington?')
        while city not in CITY_DATA:
            print('There seems to be a typo, please enter the city again')
            city = input('Which city would you like to analyze? chicago, new york city or washington?')

        print('Analyse data for city: ', city)


        month = input('Which month would you like to analyse data for from january to june or all?')
        while month not in MONTH_LIST:
            print('There seems to be a typo, plese enter the month again?')
            month = input('Which month would you like to analyse data for from january to june or all?')

        print('Analyse data for month: ', month)



        day = input('Which day would you like to analyse data for?')
        while day not in DAYS_LIST:
            print('There seems to be a typo, plese enter the day again?')
            day = input('Which day would you like to analyse data for?')

        print('Analyse data for day: ', day)
        return city, month, day
    except Exception as e:
        print('An error occured with your inputs: {}'.format(e))
    print('-' * 40)
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
    try:
        # load data file into a dataframe
        df = pd.read_csv(CITY_DATA[city])

        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        # filter by month if applicable
        if month != 'all':
            # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = MONTH_LIST.index(month) + 1

            # filter by month to create the new dataframe
            df = df[df['month'] == month]

        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]
            return df
    except Exception as e:
        print('Could not load the data, an error occurred {}'.format(e))


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        popular_month_num = df['Start Time'].dt.month.mode()[0]
        popular_month = MONTH_LIST[popular_month_num - 1].title()
        print('The most popular month is:', popular_month)
    except Exception as e:
        print('Could not calculate the most common month due to the following error: {}'.format(e))


    try:
        popular_day_of_week = df['day_of_week'].mode()[0]
        print('The most popular weekday is:', popular_day_of_week)
    except Exception as e:
        print('Could not calculate the most common day of week due to the following error: {}'.format(e))


    try:
        popular_start_hour = df['hour'].mode()[0]
        print('The most popular starting hour is:', popular_start_hour)
    except Exception as e:
        print('Could not calculate the most common start hour due to the following error: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    try:
        popular_start_station = df['Start Station'].mode()[0]
        popular_start_station_amount = df['Start Station'].value_counts()[0]
        print(
        'The most popular start station is: ', popular_start_station, ' and was used ', popular_start_station_amount,
        ' times.')
    except Exception as e:
        print('Could not calculate the most commonly used start station due to the following error: {}'.format(e))


    try:
        popular_end_station = df['End Station'].mode()[0]
        popular_end_station_amount = df['End Station'].value_counts()[0]
        print('The most popular end station in is: ', popular_end_station, ' and was used ', popular_end_station_amount,
              ' times.')
    except Exception as e:
        print('Could not calculate the most commonly used end station due to the following error: {}'.format(e))


    try:
        popular_trip = df.loc[:, 'Start Station':'End Station'].mode()[0:]
        popular_trip_amt = df.groupby(["Start Station", "End Station"]).size().max()
        print('the most popular trip is: ', popular_trip, ' and was driven ', popular_trip_amt, ' times')
    except Exception as e:
        print(
            'Could not calculate the most frequent combination of start station and end station due to the following error: {}'.format(
                e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    try:
        travel_time = df['Trip Duration'].dropna()
        total_travel_time = travel_time.sum()
        print('the total travel time was: ', total_travel_time)
    except Exception as e:
        print('Could not calculate the total travel time of users due to the following error: {}'.format(e))


    try:
        total_mean = travel_time.mean()
        print('the mean travel time is: ', total_mean)
    except Exception as e:
        print('Could not calculate the mean travel time of users due to the following error: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    try:
        print('The count of user types are: ', df['User Type'].value_counts())
    except Execption as e:
        print('Could not calculate the user types due to the following error: {}'.format(e))


    try:
        print('The gender count is: ', df['Gender'].value_counts())
    except Exception as e:
        print('Could not calculate the gender count due to the following error: {}'.format(e))

    
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('The oldest customer was born in: ', int(earliest_year), '\n' 'The youngest customer was born in: ',
              int(most_recent_year), '\n' 'The most common year of birth is :', int(most_common_year))
    except Exception as e:
        print('Could not calculate the earliest, recent or the common birth year due to the following error: {}'.format(
            e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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
