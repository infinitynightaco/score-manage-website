from flask import Flask, render_template, request

app = Flask(__name__)

# 科目與權重
subjects = ["國文", "英文", "數學A", "物理",
            "化學", "歷史", "地理", "公民"]

weights = [4, 4, 4, 2, 2, 2, 2, 3]


@app.route("/", methods=["GET", "POST"])
def index():

    results = None
    error = None

    if request.method == "POST":

        scores = []

        try:
            for i in range(len(subjects)):
                score = float(request.form[f"score_{i}"])

                if not 0 <= score <= 100:
                    raise ValueError

                scores.append(score)

            # 加權計算
            total = sum(
                score * weight
                for score, weight in zip(scores, weights)
            )

            average = total / sum(weights)

            results = {
                "scores": scores,
                "total": total,
                "average": average,
                "highest": max(scores),
                "lowest": min(scores)
            }

        except (ValueError, KeyError):
            error = "請輸入 0～100 之間的有效成績！"

    return render_template(
        "index.html",
        subjects=subjects,
        weights=weights,
        results=results,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
