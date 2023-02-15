import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'wa': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities=['ch','ny','wa']

    months=['january','february','march','april','may','june','all']

    days= ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input('\nPlease enter the name of the city to filter by form the following list\n [CH , NY, WA]\n').casefold().strip()
        
            if city not in cities:
                print('\n you enterd an invalid city\n')
                continue
        except ValueError:
            print('\nSorry i didn\'t understand the input\n')
        
        else:
            break
        
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month= input('\nPlease enter the month you want to filter by from the list\n  [january, february, march, april, may, june, all]\n').casefold().strip()
            if month not in months:
                print('\nYou enterd an invalid month\n')
                continue
        except ValueError:
            print('\nSorry i did not understand the input\n')
        else:
            break
               
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day=input('\nPlease Enter the day you want to filter by from the list\n[saturday, sunday, monday, tuesday, wednesday, thursday, friday, all]\n').casefold().strip()
            if day not in days :
                print('\n sorry yoy entered wrong value\n')
                continue
        except ValueError:
            print('\nSorry i did not understand the input\n')
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
    # load data file into dataframe
    df=pd.read_csv(CITY_DATA[city])
    #convert start time into datetiem stamp
    df['Start Time']=pd.to_datetime(df['Start Time'])
    #Extract month from the Start Time Column
    df['month']=df['Start Time'].dt.month
    #Extract the weekday name from the start time column
    df['weekday_name']=df['Start Time'].dt.weekday_name.str.lower()
    #Filter by month
    if month != 'all':
        months=['january','february','march','april','may','june','all']
        month=months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['weekday_name'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mode_month=df['month'].mode()[0]
    print(' most common month:',mode_month)
    # TO DO: display the most common day of week
    mode_day=df['weekday_name'].mode()[0]
    print('most common day of week:',mode_day)
    
    # TO DO: display the most common start hour
    mode_hour=df['Start Time'].dt.hour.mode()[0]
    print('most common start hour:', mode_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station= df['Start Station'].value_counts().idxmax()
    print('\n Most commonly start station :\n', start_station)

    # TO DO: display most commonly used end station
    end_station= df['End Station'].value_counts().idxmax()
    print('\n Most commonly end station:\n',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combine='\nFrom\n'+' '+ df['Start Station']+' '+'\nTo\n'+' '+df['End Station']
    mode_combination = start_end_combine.mode()[0]
    print('\nMost frequent combination of start station and end starion trip:\n',mode_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_travel_duration= df['Trip Duration'].sum()
    print('Total travel time in days:',int(sum_travel_duration/(60*60*24)))

    # TO DO: display mean travel time
    mean_travel_duration=df['Trip Duration'].mean()
    print('Averge Travel Duration in minutes:', int(mean_travel_duration/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
          """Displays statistics on bikeshare users."""

          print('\nCalculating User Stats...\n')
          start_time = time.time()

          # TO DO: Display counts of user types
          user_type_count= df['User Type'].value_counts()
          print('\nCount of users types:\n',user_type_count)
          # TO DO: Display counts of gender
          try:
              gender_count = df['Gender'].value_counts()
              print('\nCount of gender types\n',gender_count)
          

          # TO DO: Display earliest, most recent, and most common year of birth
    
          
              earliest_birth=df['Birth Year'].min()
              print('\n Earliest year of birth\n', int(earliest_birth))
          
              
      
          
              common_birth=df['Birth Year'].mode()[0]
              print('\n Most common Year of Birth\n', int(common_birth))
              
          
              recent_birth=df['Birth Year'].max()
              print('\n Most recent year of birht\n', int(recent_birth))
          except KeyError:
              print('\nNo Data Available for Gender and Date of Birth avilable in this city')  
          
          
          print("\nThis took %s seconds." % (time.time() - start_time))
          print('-'*40)
########
def head_data(df):
    """
       Asks user if he wants to see five rows of the raw data
       
       Reurns:
              The first five rows of the data
       If the answer id no the program show nothing
    """
    while True:
        
        try:
            start=0
            end=0
            while end <= 300001:
               
                answer=input('Do you wnat to see five rows of data yes or no ?\n')
                
                if answer == 'yes':
                    end+=5                   
                    pd.set_option('display.max_columns',200)
                    print(df.iloc[start:end])
                    
                    start=end
                else:
                    break
                
        except ValueError:
            print('I do not understand the input')
                    
        else:
            break
        
    
              
              
######################              
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        head_data(df)
        restart = input('\nDo you want to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()