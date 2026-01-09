import csv
import os
from django.shortcuts import render
from django.conf import settings


def quote_list(request):
    csv_path = os.path.join(
        settings.BASE_DIR,
        "..",
        "data",
        "quotes.csv"
    )

    quotes = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            quotes.append(row)

    return render(request, "quotes/list.html", {"quotes": quotes})
