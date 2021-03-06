def set_lang(lang):
    if lang == 'rus':
        locs = ['База террористов', 'Банк', 'Больница', 'Воинская часть', 'Войско крестоносцев', 'Казино', 'Киностудия', 'Корпоративная вечеринка', 'Овощебаза',
                'Океанский лайнер', 'Орбитальная станция', 'Отель', 'Партизанский отряд', 'Пассажирский поезд', 'Пиратский корабль', 'Пляж', 'Подводная лодка',
                'Полицейский участок', 'Полярная станция', 'Посольство', 'Ресторан', 'Самолёт', 'Спа-салон', 'Станция техобслуживания', 'Супермаркет', 'Театр',
                'Университет', 'Церковь', 'Цирк-шапито', 'Школа', 'Зоопарк', 'Выставка настольных игр', 'Карнавал', 'Луна-парк', 'Хоккейная арена', 'Ночной клуб',
                'Стройплощадка', 'Метро', 'Парламент', 'Шоколадная фабрика', 'Кладбище', 'Стадион', 'Музей', 'Дом престарелых', 'Джаз-бенд', 'Виноградник',
                'Экскурсионный автобус', 'Рок-концерт', 'Шахта', 'Порт', 'Автогонки', 'Свадьба', 'Заправочная станция', 'Библиотека', 'Тюрьма', 'Выставка кошек']
        rules = '''Игра проходит в режиме разговора.
• :spy: Один из игроков тайно становится шпионом и его задача — узнать, где же он находится.
• :man: Другие игроки знают локацию, но не знают, кто же шпион — это им предстоит вычислить, задавая друг другу вопросы.
Танцуя таким образом вокруг да около, игроки нащупывают почву, стараются понять, кто из игроков шпион и начинают подозревать игроков.
Здесь шпиону потребуется импровизировать, вдруг кто-то задаст вопрос ему? Или он сам решит повыспрашивать, чтобы отвести от себя подозрения? Шпиону необходимо во время всех разговоров понять, где он находится и сделать об этом заявление до того, как его раскусят!''' 
        settings = ['Список команд', 'Вы шпион!', 'Локация:', 'Вы хотите предложить новую локацию? y\\n', 'Какое название у новой локации?', 'Локация отправлена на одобрение',
                    'Игра началась!', 'Игроки: ']
        
    elif lang == 'eng':
        locs = ['Airplane', 'Bank', 'Beach', 'Broadway Theater', 'Casino', 'Cathedral', 'Circus Tent', 'Corporate Party', 'Crusader Army', 'Day Spa', 'Embassy',
                'Hospital', 'Hotel', 'Military Base', 'Movie Studio', 'Ocean Liner', 'Passenger Train', 'Pirate Ship', 'Polar Station', 'Police Station',
                'Restaurant', 'School', 'Service Station', 'Space Station', 'Submarine', 'Supermarket', 'University']
        rules = '''Spyfall is played over several rounds, and at the start of each round all players receive cards showing the same location — a casino, a traveling circus, a pirate ship, or even a space station — except that one player receives a card that says "Spy" instead of the location. Players then start asking each other questions — "Why are you dressed so strangely?" or "When was the last time we got a payday?" or anything else you can come up with — trying to guess who among them is the spy. The spy doesn't know where he is, so he has to listen carefully. When it's his time to answer, he'd better create a good story!

At any time during a round, one player may accuse another of being a spy. If all other players agree with the accusation, the round ends and the accused player has to reveal his identity. If the spy is uncovered, all other players score points. However, the spy can himself end a round by announcing that he understands what the secret location is.

After a few rounds of guessing, suspicion and bluffing, the game ends and whoever has scored the most points is victorious!'''
        settings = ['List of commands', 'You are a spy!', 'Location is', 'Do you want to suggest a new location? y\\n', 'What is name of new location?', 'Your location will be approved',
                    'Game is started!', 'Players: ']
    return locs, rules, settings
