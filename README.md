# confugration
celery is simple flexible, and reliable distributed system to process vast amount of message, while provided oprations with the tool required maintain such as system

it mins  task it will take time for exicute than that time we can use celery. 

1) asynchronous task
2) long runing api call
3) data scaning
4) real time notification

`how to use args and kwargs`

`args`

    **tasks.py**
    @shared_task
    def add(x,y):
        sleep(10)
        return x+y

    **def my_view(request):
        result = add.apply_async(args=[10,20])
        retun render(req**uest, html, context={})


`kwargs`

    **tasks.py**
    @shared_task
    def add(x,y, user=None):
        sleep(10)
        return x+y

    **def my_view(request):
        result = add.apply_async(args=[10,20],kwargs={"user":"roy"})
        retun render(req**uest, html, context={})

`delay()`

this function is used to enqueue task for asynchronous execution

    @shared_task
    def add(x,y):
        sleep(10)
        return x+y

    **def my_view(request):
        result = add.delay(args=[10,20])
        retun render(req**uest, html, context={})


check radis status on your local system
**sudo service redis status**

create celery.py file in root directory

    import os
    from celery import Celery
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
    app = Celery('proj')
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.autodiscover_tasks()
    @app.task(bind=True, ignore_result=True)
    def debug_task(self):
        print(f'Request: {self.request!r}')


**init file in project folder** 

    from .celery import app as celery_app
    
    __all__ = ('celery_app',)


**setting.py file**

    CELERY_TIMEZONE = "Asia/Kolkata"
    # radis access
    CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"




### *celery **worker is exicute assigned task and return result it mins like work similor add in que***

''' create normal api''

    @api_view(['GET'])
    def snippet_detail(request, pk=None):
        print(add.delay(10,20))
        return Response("Done")

'''and celery.py file'''

    @app.task
    def add(x, y):
        sleep(10)
        return x+y

    celery -A projectname worker -l info

'''celery worker show your pending task when exicute then it will retun result'''

