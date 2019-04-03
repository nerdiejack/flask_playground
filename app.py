from flask import Flask
app = Flask(__name__)

def factors(num):
    return [x for x in range(1, num+1) if num%x == 0]


@app.route('/factors/<int:n>')
def factors_route(n):
    factors_list = factors(int(n))
    # First we put the stuff at the top, adding "n" in there
    html = "<h1> The factors of " + str(n) + " are</h1>" + "\n" + "<ul>"

    # for each factor, we make a <li> item for it
    for f in factors_list:
        html += "<li>" + str(f) + "</li>" + "\n"
    html += "</ul> </body>"  # the close tags at the bottom
    return str(html)


if __name__ == '__main__':
  app.run(host='127.0.0.1')