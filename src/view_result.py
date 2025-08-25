import webbrowser

def view_in_browser(results_dir:str, file:str):
    vizfile = file+"_viz.html"
    url = f"File:///{results_dir}/{vizfile}"
    webbrowser.open(url)

if __name__=="__main__":
    dir = input("Directory: ")
    file = input("Base filename (without `_viz.html`): ")
    view_in_browser(dir, file)