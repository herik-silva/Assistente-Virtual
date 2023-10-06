class Event:
    title: str
    description: str
    date: str

    def __init__(self, title: str, description: str, date: str):
        self.title =  title
        self.description = description
        self.date = date

    def toString(self):
        return f"Evento: {self.title}. Descrição: {self.description}. Vai ocorrer em: {self.date}"
    
class EventList:
    _events: list[Event]

    def __init__(self):
        self._events = []

    def show_events(self) -> str:
        if len(self._events) == 0:
            return "Nenhum evento cadastrado"
        
        message = ""

        index = 1
        for event in self._events:
            message += f"{index}° - Evento: {event.title}. Descrição: {event.description}. Data do Evento: {event.date}. "

        return message
    
    def add_event(self, event: Event):
        self._events.append(event)

    def remove_event(self, event: Event):
        self._events.pop(event)