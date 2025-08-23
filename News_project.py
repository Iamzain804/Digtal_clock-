import requests
import json

api_key = "27e61ef6fe634bd8baf721adbf9bb761"

while True:
    print("\nOptions: jobs, sports, scholarship-ai, scholarship-mba, exit")
    choice = input("Enter category: ").lower().strip()

    if choice == "exit":
        print("Exiting program. Goodbye!")
        break

    if choice == "sports":
        url = f"https://newsapi.org/v2/top-headlines?country=pk&category=sports&apiKey={api_key}"
    elif choice == "jobs":
        url = f"https://newsapi.org/v2/everything?q=Pakistan jobs&sortBy=publishedAt&apiKey={api_key}"
    elif choice == "scholarship-ai":
        url = f"https://newsapi.org/v2/everything?q=Germany scholarship AI&sortBy=publishedAt&apiKey={api_key}"
    elif choice == "scholarship-mba":
        url = f"https://newsapi.org/v2/everything?q=Germany scholarship MBA&sortBy=publishedAt&apiKey={api_key}"
    else:
        print("Invalid choice! Please enter one of the given options.")
        continue

    response = requests.get(url)
    news = json.loads(response.text)

    if news.get("articles"):
        for article in news["articles"]:
            print(article["title"])
            print(article["description"])
            print("======================")
    else:
        print("No news found.")
