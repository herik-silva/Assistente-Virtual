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