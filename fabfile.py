from fabric import task
from patchwork.transfers import rsync
from invoke import run

exclude_dirs = [".git", "node_modules", ".cache", ".github", "db.sqlite3"]


@task
def reinit(ctx):
    run("rm db.sqlite3")
    run("python manage.py migrate")
    run("python populate.py")


@task
def test(c):
    run(" coverage run manage.py test --failfast")
    run("coverage report -m ")


@task
def deploy(ctx):
    run("npm install", echo=True)
    run("npm run build", echo=True)
    run("python manage.py collectstatic --noinput", echo=True)
    run("find . -name '__pycache__' |xargs rm -rf ", echo=True)
    rsync(ctx, ".", "apps/ducktest", exclude=exclude_dirs)
    with ctx.cd("apps/ducktest"):
        with ctx.prefix("source ~/.virtualenvs/ducktest/bin/activate"):
            ctx.run("pip install -r requirements.txt")
            ctx.run("python manage.py migrate")
        ctx.run("touch app/wsgi.py")

@task
def log(ctx):
    run("pip-compile requirements.in -o requirements.txt")
    run("jrnl --export md > Log.md")
    run("DJANGO_SETTINGS_MODULE=app.extra_settings python manage.py graph_models --pygraphviz -o graph_models.png ducks -g")

@task
def t(ctx):
    run("touch media/src/main.js")
