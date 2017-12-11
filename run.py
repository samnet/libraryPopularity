from flask import Flask
import liPop

app = liPop.views.app # ... does nt work if I write "import liPop.views.app as app"
print("instance var: ", app.config["MY_VARIABLE"])
print("instance path:", app.instance_path)
if __name__ == "__main__":
    app.run(debug = app.config["DEBUG"])
