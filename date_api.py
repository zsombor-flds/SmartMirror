def date():
    import datetime
    data = {}
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    date = datetime.datetime.now()
    weekday = date.weekday()

    data["month"] = months[date.month-1]
    data["day"] = str(date.day)
    data["weekday"] = days[weekday]
    data["year"] = str(date.year)

    return data


if __name__ == "__main__":
    date = date()
    print date["month"]
