from flask import Blueprint, render_template, request, jsonify, redirect

main = Blueprint("main", __name__)

@main.route("/")
def home():
  return render_template("index.html")

@main.route("/about")
def about():
  context = {
    "name" : "Ioana",
    "description" : "Leverage my expertise to develop, and maintain web sites, ensuring they meet high-quality standards and industry best practices. \n Constantly strive to enhance your skills and stay up-to-date with the latest industry trends and technologies to deliver cutting-edge solutions.",
    "contact": "test@gmail.com"
  }
  return  render_template("about.html", context=context)

@main.route("/portfolio")
def portfolio():
  project_list = [
    {"name" : "Taskmate", "description" : " first project", "link":"taskmate"},
     {"name" : "Codebook", "description" : " second project", "link": "codebook"},
  
     
  ]
  return  render_template("portfolio.html", projects = project_list)

@main.route("/portfolio/<project>")
def project(project):
  project_list = ["taskmate", "codebook"]
  if project in project_list:
    return  render_template(f"portfolio/{project}.html")
  else:
    return  redirect("/404")
  
@main.route("/s")
def search():
  keyword = request.args.get("k")
  return f"{keyword}"

@main.route("/portfolio/json")
def portfolio_json():
  
  projects = {
    "taskmate" : {
      "language": "Python", 
      "framework" : "Django",
      "status":"completed"
    },
    "codebook" : {
      "language": "Javascript", 
      "framework" : "React",
      "status": "in course"
    }
  }
  return jsonify(projects)

@main.route("/404")
def not_found_404():
  return render_template("404.html"), 404

@main.app_errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404