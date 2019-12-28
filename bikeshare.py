import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities=['chicago','new york city ','washington']
months=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December','All']
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=str(input('Select a city from Chicago, New York City and Washington. \n')).lower()
        if city not in cities:
            print('please enter a valid input.')
        else:
            break
            
            
       
     # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=str(input('Do you want to filter by month? If yes, then type out the month. If not, type in all\n')).title()
        if month not in months:
            print('please enter a valid input')
        else:
            break
            
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=str(input('Do you want to filter by day? If yes, then type out the day. If not, type in all\n')).title()
        if day not in days:
            print('please enter a valid input')
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
    
    
    df = pd.read_csv(CITY_DATA[city])
   
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
     # filter by month if applicable
    if month != 'All':
          month = months.index(month) + 1
        # filter by month to create the new dataframe
          df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
          df = df[df['day_of_week'] == day]
   

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.weekday_name

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('The most common month is: {}'.format(months[popular_month-1]))


    # TO DO: display the most common day of week
    print('The most common day of week is: {}'.format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: {}'.format(df['hour'].mode()[0]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: {}'.format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print('The most commonly used end station is: {}'.format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combenation= df['Start Station'] + ' to ' + df['End Station']
    print('The most frequent combination is: {}'.format(most_frequent_combenation.mode()[0]))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_m, total_s = divmod(df['Trip Duration'].sum(), 60)
    total_h, total_m = divmod(total_m, 60)
    print ('The total travel time is: ',total_h,' hours, ', total_m,' minutes, and ', total_s,' seconds.')
    


    # TO DO: display mean travel time
    mean_m, mean_s = divmod(df['Trip Duration'].mean(), 60)
    mean_h, mean_m = divmod(mean_m, 60)
    print ('The mean travel time is: ',mean_h,' hours, ', mean_m,' minutes, and ', mean_s,' seconds.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types are \n{}'.format(df['User Type'].value_counts()))


    # TO DO: Display counts of gender
    if('Gender' not in df):
        print('gender data is not avalible for Washington')
    else:
         print('The genders are \n{}'.format(df['Gender'].value_counts()))
        

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' not in df):
        print('birth data is not avalible for Washington')
    else:
        print('The Earliest year of birth is: {}'.format(df['Birth Year'].min()))
        print('The most recent year of birth is: {}'.format(df['Birth Year'].max()))
        print('The most common year of birth is: {}'.format(df['Birth Year'].mode()[0]))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def view_data(df):
    start=0
    choice=input('\nDo you want to view the data? Enter yes or no.\n')
    while choice=='yes':
        try:
            n=int(input('Enter the number of rows to view\n'))
            n=start+n
            print(df[start:n])
            choice=input('More rows? Enter yes or no.\n')
            start=n

        except ValueError:
            print('Enter appropriate integer value')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
