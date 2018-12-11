from collections import Counter
from datetime import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from typing import List, Tuple
from api import messages_get_history
from api import get_friends
from api_models import Message
import config


dates = List[datetime.date]
frequencies = List[int]

plotly.tools.set_credentials_file(
    username=config.PLOTLY_CONFIG['username'],
    api_key=config.PLOTLY_CONFIG['api_key']
)


def fromtimestamp(ts: int) -> datetime.date:
    return datetime.fromtimestamp(ts).date()


def count_dates_from_messages(messages: List[Message]) -> Tuple[dates, frequencies]:
    """ Получить список дат и их частот
    :param messages: список сообщений
    """
    date = []
    cnt = Counter()

    for message in messages:
        message.date = datetime.utcfromtimestamp(message.date).strftime("%Y-%m-%d")
        date.append(message.date)

    for val in date:
        cnt[val] += 1

    return list(cnt.keys()), list(cnt.values())


def plotly_messages_freq(dates: List[dates], freq: List[frequencies]) -> None:
    """ Построение графика с помощью Plot.ly
    :param dates:
    :param date: список дат
    :param freq: число сообщений в соответствующую дату
    """
    data = [go.Scatter(x=dates, y=freq)]
    py.plot(data)


if __name__ == "__main__":
    friend_id = get_friends(config.VK_CONFIG['user_id'], '')[14]
    dates, freq = count_dates_from_messages(messages_get_history(friend_id, count=2000))
    plotly_messages_freq(dates, freq)