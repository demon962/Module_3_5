import unittest


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


class Tournament:
    def __init__(self, runners):
        self.runners = runners

    def start(self):
        results = []
        for runner in self.runners:
            distance = 100
            time = distance / runner.speed
            results.append((runner.name, time))

        results.sort(key=lambda x: x[1])

        return results


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up class...")

    def setUp(self):
        print("Setting up test case...")
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)
        self.tournament = Tournament([self.usain, self.andrey, self.nick])

    def tearDown(self):
        print("Tearing down test case...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class...")

    def test_usain_vs_nick(self):
        tournament = Tournament([self.usain, self.nick])
        results = tournament.start()
        expected_results = [('Усэйн', 10), ('Ник', 33.333333333333336)]
        self.assertEqual(results, expected_results)
        print({i + 1: result[0] for i, result in enumerate(expected_results)})

    def test_andrey_vs_nick(self):
        tournament = Tournament([self.andrey, self.nick])
        results = tournament.start()
        expected_results = [('Андрей', 11.11111111111111), ('Ник', 33.333333333333336)]
        self.assertEqual(results, expected_results)
        print({i + 1: result[0] for i, result in enumerate(expected_results)})

    def test_all_runners(self):
        tournament = Tournament([self.usain, self.andrey, self.nick])
        results = tournament.start()
        expected_results = [('Усэйн', 10), ('Андрей', 11.11111111111111), ('Ник', 33.333333333333336)]
        self.assertEqual(results, expected_results)
        print({i + 1: result[0] for i, result in enumerate(expected_results)})


if __name__ == '__main__':
    unittest.main(verbosity=2)
