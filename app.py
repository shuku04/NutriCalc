# NutriCalc - Nutrition Calculator by Shubham (Web Version)

from flask import Flask, render_template, request

app = Flask(__name__)

food_categories = {
    "Fruits": {
        "banana": {"calories": 0.89, "protein": 0.011, "carbs": 0.23, "fat": 0.003},
        "apple": {"calories": 0.52, "protein": 0.003, "carbs": 0.14, "fat": 0.002},
        "orange": {"calories": 0.47, "protein": 0.009, "carbs": 0.12, "fat": 0.001},
        "mango": {"calories": 0.60, "protein": 0.008, "carbs": 0.15, "fat": 0.004},
        "grapes": {"calories": 0.69, "protein": 0.006, "carbs": 0.18, "fat": 0.001}
    },
    "Vegetables": {
        "spinach": {"calories": 0.23, "protein": 0.029, "carbs": 0.036, "fat": 0.004},
        "carrot": {"calories": 0.41, "protein": 0.009, "carbs": 0.10, "fat": 0.002},
        "potato": {"calories": 0.87, "protein": 0.020, "carbs": 0.20, "fat": 0.001},
        "tomato": {"calories": 0.18, "protein": 0.009, "carbs": 0.039, "fat": 0.002},
        "onion": {"calories": 0.40, "protein": 0.011, "carbs": 0.09, "fat": 0.002}
    },
    "Grains & Breads": {
        "white rice": {"calories": 1.30, "protein": 0.027, "carbs": 0.28, "fat": 0.003},
        "chapati": {"calories": 1.04, "protein": 0.030, "carbs": 0.15, "fat": 0.030},
        "white bread": {"calories": 2.65, "protein": 0.090, "carbs": 0.49, "fat": 0.032},
        "brown rice": {"calories": 1.11, "protein": 0.026, "carbs": 0.23, "fat": 0.009},
        "oats": {"calories": 3.89, "protein": 0.17, "carbs": 0.66, "fat": 0.07}
    },
    "Dairy": {
        "milk": {"calories": 0.61, "protein": 0.032, "carbs": 0.050, "fat": 0.033},
        "paneer": {"calories": 2.65, "protein": 0.180, "carbs": 0.012, "fat": 0.200},
        "butter": {"calories": 7.17, "protein": 0.009, "carbs": 0.001, "fat": 0.810},
        "curd": {"calories": 0.98, "protein": 0.036, "carbs": 0.035, "fat": 0.042},
        "cheese": {"calories": 4.02, "protein": 0.250, "carbs": 0.013, "fat": 0.330}
    },
    "Proteins": {
        "egg": {"calories": 1.55, "protein": 0.130, "carbs": 0.011, "fat": 0.110},
        "chicken breast": {"calories": 1.65, "protein": 0.310, "carbs": 0.000, "fat": 0.036},
        "tofu": {"calories": 0.76, "protein": 0.080, "carbs": 0.019, "fat": 0.048},
        "rajma": {"calories": 1.27, "protein": 0.090, "carbs": 0.22, "fat": 0.005},
        "chickpeas": {"calories": 1.64, "protein": 0.090, "carbs": 0.27, "fat": 0.027}
    },
    "Nuts & Seeds": {
        "almonds": {"calories": 5.79, "protein": 0.210, "carbs": 0.22, "fat": 0.50},
        "cashews": {"calories": 5.53, "protein": 0.180, "carbs": 0.30, "fat": 0.44},
        "peanuts": {"calories": 5.67, "protein": 0.260, "carbs": 0.16, "fat": 0.49},
        "walnuts": {"calories": 6.54, "protein": 0.150, "carbs": 0.14, "fat": 0.65}
    },
    "Dips & Extras": {
        "mayonnaise": {"calories": 7.00, "protein": 0.010, "carbs": 0.01, "fat": 0.75},
        "ketchup": {"calories": 1.10, "protein": 0.010, "carbs": 0.25, "fat": 0.002},
        "hummus": {"calories": 2.60, "protein": 0.060, "carbs": 0.14, "fat": 0.16},
        "peanut butter": {"calories": 5.88, "protein": 0.250, "carbs": 0.20, "fat": 0.50}
    },
    "Beverages": {
        "cola": {"calories": 0.42, "protein": 0.000, "carbs": 0.11, "fat": 0.000},
        "orange juice": {"calories": 0.45, "protein": 0.007, "carbs": 0.10, "fat": 0.001},
        "coffee": {"calories": 0.50, "protein": 0.020, "carbs": 0.07, "fat": 0.015},
        "tea": {"calories": 0.40, "protein": 0.010, "carbs": 0.06, "fat": 0.010}
    }
}


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        category = request.form.get('category')
        food = request.form.get('food')
        grams = request.form.get('grams')

        if category and food and grams:
            try:
                grams = float(grams)
                item_data = food_categories[category][food]
                result = {
                    'food': food,
                    'grams': grams,
                    'calories': round(item_data['calories'] * grams, 2),
                    'protein': round(item_data['protein'] * grams, 2),
                    'carbs': round(item_data['carbs'] * grams, 2),
                    'fat': round(item_data['fat'] * grams, 2)
                }
            except Exception as e:
                result = {'error': str(e)}

    return render_template('index.html', food_categories=food_categories, result=result)


if __name__ == '__main__':
    app.run(debug=True)
