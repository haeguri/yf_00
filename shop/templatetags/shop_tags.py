from datetime import timedelta, date, timezone, datetime
from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter(name='get_due_date_string')
def get_due_date_string(value):
    # delta = value - date.today()
    #
    # print(delta)

    # if delta.days == 0:
    #     return "Today!"
    #
    # else:
    #     delta.days < 1
    #     return "%s %s ago!" % (abs(delta.days),
    #         ("day" if abs(delta.days) == 1 else "days"))



    now = datetime.now(timezone.utc)
    try:
        difference = now - value
    except:
        return value

    if difference <= timedelta(minutes=1):
        return '방금'

    time_str = '%(time)s 전' % {'time': ''.join(timesince(value).split(' ')[0].split())}

    return time_str.lstrip().replace('days','일').replace('hours', '시간').replace('week', '주').replace(",", "")
