import COVID19Py

covid19 = COVID19Py.COVID19(data_source="jhu")
latest = covid19.getLatest()

from pynotifier import Notification

Notification(
        title="Today COVID 19 News updates.",
        description=str(latest),
        duration=30,
        ).send()