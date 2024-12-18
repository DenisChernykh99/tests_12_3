import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        Runner1 = Runner('Денис')
        for _ in range(10):
            Runner1.walk()
        self.assertEqual(Runner1.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        Runner2 = Runner('Антон')
        for _ in range(10):
            Runner2.run()
        self.assertEqual(Runner2.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        Runner3 = Runner('Дима')
        Runner4 = Runner('Вика')
        for _ in range(10):
            Runner3.run()
            Runner4.walk()
        self.assertNotEqual(Runner3.distance, Runner4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.Runner1 = Runner('Усейн', speed=10)
        self.Runner2 = Runner('Андрей', speed=9)
        self.Runner3 = Runner('Ник', speed=3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_start(self):
        tournament = Tournament(90, self.Runner1, self.Runner3)
        result = tournament.start()
        TournamentTest.all_results['Забег 1:'] = result
        list_runner = [place for place in result.values()]
        self.assertTrue(list_runner[-1], self.Runner3.name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_start1(self):
        tournament = Tournament(90, self.Runner2, self.Runner3)
        result = tournament.start()
        TournamentTest.all_results['Забег 2:'] = result
        list_runner = [place for place in result.values()]
        self.assertTrue(list_runner[-1], self.Runner3.name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_start2(self):
        tournament = Tournament(90, self.Runner1, self.Runner2, self.Runner3)
        result = tournament.start()
        TournamentTest.all_results['Забег 3:'] = result
        list_runner = [place for place in result.values()]
        self.assertTrue(list_runner[-1], self.Runner3.name)

    @classmethod
    def tearDownClass(cls):
        for race in TournamentTest.all_results.items():
            winners = []
            winners.append(race[0])
            for winner in race[1].items():
                winners.append(f'{winner[0]} {winner[1]},')
            print(*winners)



