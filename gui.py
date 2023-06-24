from flask import Flask, render_template, request
from functools import cache

app = Flask(__name__)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(i, j) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            res = dp(i + 1, j)
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            return res

        return dp(0, 0)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        S = request.form.get("s", "")
        T = request.form.get("t", "")
        if S and T:
            try:
                result = Solution().numDistinct(S, T)
            except Exception as e:
                result = f"Error: {str(e)}"
        else:
            result = "Please enter values for both S and T."
        return render_template("index.html", result=result, S=S, T=T)
    else:
        return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
