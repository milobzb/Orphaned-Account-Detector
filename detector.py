from datetime import date, datetime
import csv

total = 0
flagged = 0
ok = 0
THRESHOLD = 90

with open('report.txt', 'w') as output:
    output.write("ORPHANED ACCOUNT DETECTOR REPORT\n")
    output.write("Generated: " + str(date.today()) + "\n")
    output.write("\nFLAGGED ACCOUNTS:\n")

    with open('accounts.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            login_date = datetime.strptime(row['last_login_date'], '%Y-%m-%d').date()
            days_inactive = (date.today() - login_date).days

            if days_inactive >= THRESHOLD:
                status = "Flagged"
                flagged += 1
                output.write(row['username'] + " | " + str(days_inactive) + " days inactive | Flagged\n")
            else:
                status = "OK"
                ok += 1

            total += 1

    output.write("\nSUMMARY:\n")
    output.write("Total accounts scanned: " + str(total) + "\n")
    output.write("Flagged: " + str(flagged) + "\n")
    output.write("OK: " + str(ok) + "\n")