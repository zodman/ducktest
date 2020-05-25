from fabric import task
from patchwork.transfers import rsync
from invoke import run

exclude_dirs =[".git","node_modules", '.cache',".github"]

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
    rsync(ctx, ".", "apps/ducktest", exclude=exclude_dirs)
    with ctx.cd("apps/ducktest"):
        with ctx.prefix("source ~/.virtualenvs/ducktest/bin/activate"):
            ctx.run("pip install -r requirements.txt")
        ctx.run("touch app/wsgi.py")
