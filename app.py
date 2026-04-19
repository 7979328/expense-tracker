from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"


# ------------------ DATABASE CONNECTION ------------------
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# ------------------ HOME ------------------
@app.route("/")
def home():
    if "user_id" in session:
        return redirect("/dashboard")
    return redirect("/login")


# ------------------ REGISTER ------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


# ------------------ LOGIN ------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect("/dashboard")
        else:
            return "Invalid Credentials"

    return render_template("login.html")


# ------------------ LOGOUT ------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ------------------ DASHBOARD ------------------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()

    expenses = conn.execute(
        "SELECT * FROM expenses WHERE user_id = ?",
        (session["user_id"],)
    ).fetchall()

    # TOTAL EXPENSE
    total = sum([float(e["amount"]) for e in expenses])

    # CATEGORY WISE DATA (FOR CHART)
    categories = conn.execute("""
        SELECT category, SUM(amount) as total
        FROM expenses
        WHERE user_id = ?
        GROUP BY category
    """, (session["user_id"],)).fetchall()

    conn.close()

    labels = [c["category"] for c in categories]
    values = [float(c["total"]) for c in categories]

    return render_template(
        "dashboard.html",
        expenses=expenses,
        total=total,
        labels=labels,
        values=values
    )


# ------------------ ADD EXPENSE ------------------
@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        description = request.form["description"]
        date = request.form.get("date")

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO expenses (user_id, amount, category, description, date)
            VALUES (?, ?, ?, ?, ?)
        """, (session["user_id"], amount, category, description, date))

        conn.commit()
        conn.close()

        return redirect("/dashboard")

    return render_template("add.html")


# ------------------ EDIT EXPENSE ------------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_expense(id):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()

    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        description = request.form["description"]
        date = request.form.get("date")

        conn.execute("""
            UPDATE expenses
            SET amount = ?, category = ?, description = ?, date = ?
            WHERE id = ?
        """, (amount, category, description, date, id))

        conn.commit()
        conn.close()

        return redirect("/dashboard")

    expense = conn.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template("edit.html", expense=expense)


# ------------------ DELETE EXPENSE ------------------
@app.route("/delete/<int:id>")
def delete_expense(id):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    conn.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/dashboard")


# ------------------ RUN APP ------------------
if __name__ == "__main__":
    app.run(debug=True, port=5001)
