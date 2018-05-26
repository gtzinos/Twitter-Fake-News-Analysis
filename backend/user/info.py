from datetime import datetime, date, time, timedelta


def printUserDetails(loggedUser):
    tweets = loggedUser.statuses_count
    account_created_date = loggedUser.created_at
    delta = datetime.utcnow() - account_created_date
    account_age_days = delta.days
    print("Account age (in days): " + str(account_age_days))

    print("Account age (in years): " + str(account_age_days / 365))

    if account_age_days > 0:
        print("Average tweets per day: " + "%.2f" %
              (float(tweets) / float(account_age_days)))
