book_pages = int(input())
pages_for_hour = int(input())
due_days = int(input())

hours_needed = book_pages / pages_for_hour
hours_per_day = hours_needed / due_days

print(int(hours_per_day))
