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
    run("npm clean-install")
#    run("npm run build")
    run("python manage.py collectstatic --noinput")
    rsync(ctx, ".", "app/ducktest", exclude=exclude_dirs)
    ctx.run("touch app/ducktest/app/wsgi.py")
