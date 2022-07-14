from crontab import CronTab

# local_cronjob = CronTab(user='hyacinth')
local_cronjob = CronTab(user=True)


'''
    minute (0-59)
    hour (0-24)
    day of month (1-31)
    month (1-12)
    day of week (0-6) (Sunday=0 or 7)
'''
def cronjob(command, cron_time, comment):
    job = local_cronjob.new(
        command=command, 
        comment=comment
    )
    
    minute, hour, day, month = cron_time
    if (minute is not None):
        job.minute.every(minute)
    if (hour is not None):
        job.hour.every(hour)
    if (day is not None):
        job.day.every(day)
    if (month is not None):
        job.month.every(month)

    local_cronjob.write()

    print('cronjob added')

# cronjob('python3 /home/hyacinth/Desktop/iclab_yolov5/cronjob/test.py', [1, None, None, None], 'testdate')

def remove_cron(comment):
    for job in local_cronjob:
        if (job.comment == str(comment)):
            local_cronjob.remove(job)
            local_cronjob.write()

remove_cron('testdate')
