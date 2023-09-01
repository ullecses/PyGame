class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """иниуиализирует статистику"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """статистика изменения в игре"""
        self.guns_left = 2
        self.score = 0