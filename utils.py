import subprocess


def restart_worker(name):
    subprocess.call("systemctl restart " + name, shell=True)


def restart_scheduler(name):
    subprocess.call("systemctl restart " + name, shell=True)
