from datetime import timedelta, date, timezone, datetime
from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter(name='get_due_date_string')
def get_due_date_string(value):

    now = datetime.now(timezone.utc)
    try:
        difference = now - value
    except:
        return value

    if difference <= timedelta(minutes=1):
        return '방금'

    time_str = '%(time)s 전' % {'time': ''.join(timesince(value).split(' ')[0].split())}

    return time_str.lstrip()\
        .replace('months', '달').replace('month', '달')\
        .replace('weeks', '주').replace('week', '주')\
        .replace('days','일').replace('days', '일')\
        .replace('hours', '시간').replace('hour', '시간')\
        .replace('minutes', '분').replace('minute', '분').replace(",", "")
