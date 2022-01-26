from booking.booking import Booking

# Initialise class with 'with' to execute teardown actions as soon as program goes out of indentation.
# Teardown actions are specified in class as magic __exit__ method.
try:
    with Booking(teardown=False) as bot:  # set to true to enable teardown under __exit__ in class Booking
        bot.land_first_page()
        bot.change_currency(currency='EUR')
        bot.select_place_to_go(input("Where do you want to go? :"))
        bot.select_dates(check_in_date=input('What is the check in date(YYYY-MM-DD)?: '),
                         check_out_date=input('What is the check out date(YYYY-MM-DD)?: '))

        bot.select_adults(int(input('How many people? :')))
        bot.click_search()
        bot.handle_cookie_banner()
        bot.apply_filtrations()
        bot.refresh()  # Workaround to give bot some time to sort results
        bot.report_results()
        bot.quit()


except Exception as e:  # Raise exception if program is run from cmd
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:\path-to-your-folder\ \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise  # Raise original exception
