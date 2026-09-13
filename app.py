from flask import Flask, render_template, request, redirect
import json
import os
from datetime import date

app = Flask(__name__)

DATA_FOLDER = "data"


# --------------------------------------------------
# JSON FUNCTIONS
# --------------------------------------------------

def load_data(filename):

    path = os.path.join(DATA_FOLDER, filename)

    if not os.path.exists(path):
        return []

    try:
        with open(path, "r") as file:
            return json.load(file)
    except:
        return []


def save_data(filename, data):

    path = os.path.join(DATA_FOLDER, filename)

    with open(path, "w") as file:
        json.dump(data, file, indent=4)


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

@app.route("/")
def home():

    cows = load_data("cows.json")
    milk = load_data("milk.json")
    health = load_data("health.json")
    feed = load_data("feed.json")
    sales = load_data("sales.json")

    today = str(date.today())

    today_milk = 0
    milk_sold = 0
    today_revenue = 0

    for item in milk:

        if item.get("date") == today:

            today_milk += float(item.get("total_milk", 0))

    for item in sales:

        if item.get("date") == today:

            milk_sold += float(item.get("quantity", 0))
            today_revenue += float(item.get("amount", 0))

    healthy = 0
    checkup = 0
    treatment = 0

    for item in health:

        condition = item.get("condition", "")

        if condition == "Healthy":
            healthy += 1

        elif condition == "Needs Checkup":
            checkup += 1

        elif condition == "Under Treatment":
            treatment += 1

    return render_template(
        "index.html",
        cows=cows,
        today_milk=today_milk,
        milk_sold=milk_sold,
        today_revenue=today_revenue,
        healthy=healthy,
        checkup=checkup,
        treatment=treatment
    )


# ==================================================
# COW MANAGEMENT
# ==================================================

@app.route("/cows")
def cows():

    cows = load_data("cows.json")

    search = request.args.get("search", "")

    if search:

        search = search.lower()

        cows = [
            cow for cow in cows
            if search in cow["id"].lower()
            or search in cow["name"].lower()
            or search in cow["breed"].lower()
        ]

    return render_template(
        "cows.html",
        cows=cows,
        search=search
    )


@app.route("/add_cow", methods=["GET", "POST"])
def add_cow():

    if request.method == "POST":

        cows = load_data("cows.json")

        new_cow = {
            "id": request.form["id"],
            "name": request.form["name"],
            "breed": request.form["breed"],
            "age": request.form["age"],
            "health": request.form["health"]
        }

        cows.append(new_cow)

        save_data("cows.json", cows)

        return redirect("/cows")

    return render_template("add_cow.html")


@app.route("/edit_cow/<cow_id>", methods=["GET", "POST"])
def edit_cow(cow_id):

    cows = load_data("cows.json")

    cow = next(
        (c for c in cows if c["id"] == cow_id),
        None
    )

    if cow is None:
        return "Cow not found"

    if request.method == "POST":

        cow["name"] = request.form["name"]
        cow["breed"] = request.form["breed"]
        cow["age"] = request.form["age"]
        cow["health"] = request.form["health"]

        save_data("cows.json", cows)

        return redirect("/cows")

    return render_template(
        "edit_cow.html",
        cow=cow
    )


@app.route("/delete_cow/<cow_id>")
def delete_cow(cow_id):

    cows = load_data("cows.json")

    cows = [
        cow for cow in cows
        if cow["id"] != cow_id
    ]

    save_data("cows.json", cows)

    return redirect("/cows")


# ==================================================
# MILK MANAGEMENT
# ==================================================

@app.route("/milk")
def milk():

    milk = load_data("milk.json")

    return render_template(
        "milk.html",
        milk=milk
    )


@app.route("/add_milk", methods=["GET", "POST"])
def add_milk():

    if request.method == "POST":

        milk = load_data("milk.json")

        morning = float(request.form["morning"])
        evening = float(request.form["evening"])

        total = morning + evening

        new_milk = {

            "cow_id": request.form["cow_id"],

            "date": request.form["date"],

            "morning": morning,

            "evening": evening,

            "total_milk": total
        }

        milk.append(new_milk)

        save_data("milk.json", milk)

        return redirect("/milk")

    cows = load_data("cows.json")

    return render_template(
        "add_milk.html",
        cows=cows
    )


# ==================================================
# HEALTH MANAGEMENT
# ==================================================

@app.route("/health")
def health():

    health = load_data("health.json")

    return render_template(
        "health.html",
        health=health
    )


@app.route("/add_health", methods=["GET", "POST"])
def add_health():

    if request.method == "POST":

        health = load_data("health.json")

        new_health = {

            "cow_id": request.form["cow_id"],

            "date": request.form["date"],

            "condition": request.form["condition"],

            "temperature": request.form["temperature"],

            "treatment": request.form["treatment"],

            "next_checkup": request.form["next_checkup"]
        }

        health.append(new_health)

        save_data("health.json", health)

        return redirect("/health")

    cows = load_data("cows.json")

    return render_template(
        "add_health.html",
        cows=cows
    )


# ==================================================
# FEED MANAGEMENT
# ==================================================

@app.route("/feed")
def feed():

    feed = load_data("feed.json")

    return render_template(
        "feed.html",
        feed=feed
    )


@app.route("/add_feed", methods=["GET", "POST"])
def add_feed():

    if request.method == "POST":

        feed = load_data("feed.json")

        new_feed = {

            "name": request.form["name"],

            "quantity": request.form["quantity"],

            "price": request.form["price"],

            "date": request.form["date"]
        }

        feed.append(new_feed)

        save_data("feed.json", feed)

        return redirect("/feed")

    return render_template("add_feed.html")


# ==================================================
# SALES MANAGEMENT
# ==================================================

@app.route("/sales")
def sales():

    sales = load_data("sales.json")

    return render_template(
        "sales.html",
        sales=sales
    )


@app.route("/add_sales", methods=["GET", "POST"])
def add_sales():

    if request.method == "POST":

        sales = load_data("sales.json")

        quantity = float(request.form["quantity"])
        price = float(request.form["price"])

        amount = quantity * price

        new_sale = {

            "customer": request.form["customer"],

            "date": request.form["date"],

            "quantity": quantity,

            "price": price,

            "amount": amount
        }

        sales.append(new_sale)

        save_data("sales.json", sales)

        return redirect("/sales")

    return render_template("add_sales.html")


# ==================================================
# RUN APPLICATION
# ==================================================

if __name__ == "__main__":

    app.run(debug=True)