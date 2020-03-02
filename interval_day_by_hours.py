#encoding=utf-8
import time
import datetime

'''
start_date=2020:01:12
work_days=2
'''
#获取起始时间与现在时间间隔
def get_days_interval(start_date):
    #start_date = '2017:06:01'
    end_date=time.strftime("%Y:%m:%d")
    start_sec = time.mktime(time.strptime(start_date, '%Y:%m:%d'))
    end_sec = time.mktime(time.strptime(end_date, '%Y:%m:%d'))
    work_days = int((end_sec - start_sec) / (24 * 60 * 60))
    return work_days

#获取起始时间
'''
days=3
end_time_str=2020:01:12
'''
def get_start_date(days):
    days=-days
    now_time_str=time.strftime("%Y:%m:%d")
    now_time_date=datetime.datetime.strptime(now_time_str,"%Y:%m:%d")
    #向前天数
    end_time_date=now_time_date+datetime.timedelta(days=days)
    end_time_str=datetime.datetime.strftime(end_time_date,"%Y:%m:%d")
    return end_time_str

'''
day_interval=3
milis=unix毫秒时间戳(以小时为单位)
'''
def get_evey_hour_milis(day_interval):
    milis=[]
    start_date_str = get_start_date(day_interval)
    #print(start_date_str)
    interval_days=get_days_interval(start_date_str)
    for i in range(interval_days):
        interval_days-=1
        start_date = get_start_date(interval_days)
        start_date=datetime.datetime.strptime(start_date,"%Y:%m:%d")
        for x in range(24):
            timestring = datetime.datetime.strftime(start_date,"%Y:%m:%d") + " %2d:00:00" % x
            timeArray = time.strptime(timestring, "%Y:%m:%d %H:%M:%S")
            timeStamp = int(time.mktime(timeArray))
            millisecond = int((timeStamp * 1000))
            milis.append(millisecond)
        timestring_24= datetime.datetime.strftime(start_date,"%Y:%m:%d") + " 23:59:59"
        timeArray_24 = time.strptime(timestring_24, "%Y:%m:%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray_24))
        millisecond_24 = int((timeStamp * 1000))
        milis.append(millisecond_24)
    milis.sort(reverse=False)
    return milis

#毫秒时间戳转换为日期
def timeStamp(timeNum):
    timeStamp = float(timeNum / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

ss=get_evey_hour_milis(3)
for line in ss:
    time_t=timeStamp(line)
    print (line,time_t)
