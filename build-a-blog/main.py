import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Post(db.Model):
    title = db.StringProperty(required = True)
    body = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)


class MainPage(Handler):
    def render_post_form(self, posts=""):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC LIMIT 5;")

        self.render("new_post_form.html", posts = posts)

    def get(self):
        self.render_post_form("new_post_form.html")



class NewPost(Handler):
    def render_entry(self, title="", body="", error=""):
        self.render("post.html", title = title, body = body, error = error)

    def get(self):
        self.render("post.html")

    def post(self):
        title = self.request.get("title")
        body = self.request.get("body")

        if title and body:
            p = Post(title = title, body = body)
            p.put()

            self.redirect("/")
        else:
            error = "Both fields are both required."
            self.render_entry(title, body, error)

class ViewPost(Handler):
    def get(self, id):
        id = int(id)
        post = Post.get_by_id(id)
        self.render("permalink.html", id = id, post = post)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newpost', NewPost),
    webapp2.Route('/post/<id:\d+>', ViewPost)
], debug=True)
