from fabric import task
from patchwork.transfers import rsync
from invoke import run

@task
def deploy(ctx):
    run("npm run build")
    run("python manage.py collectstatic --noinput")
    rsync(ctx, ".", "app/ducktest", exclude=[".git","node_modules", '.cache'])
