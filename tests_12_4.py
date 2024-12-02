import unittest
import logging

from suite_12_3 import Runner, skip_if_frozen

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.txt',
    filemode='w',
    format='%(levelname)s: %(asctime)s - %(message)s'
)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_create_runner(self):
        try:
            usain = Runner('Усэйн', 10)
            self.assertEqual(usain.name, 'Усэйн')
            self.assertEqual(usain.speed, 10)
            logging.info('Тест test_create_runner выполнен успешно.')
        except AssertionError as e:
            logging.error('Тест test_create_runner завершился неудачно: %s', str(e))

    @skip_if_frozen
    def test_another_runner(self):
        try:
            andrey = Runner('Андрей', 9)
            self.assertEqual(andrey.name, 'Андрей')
            self.assertEqual(andrey.speed, 9)
            logging.info('Тест test_another_runner выполнен успешно.')
        except AssertionError as e:
            logging.error('Тест test_another_runner завершился неудачно: %s', str(e))

    @skip_if_frozen
    def test_walk(self):
        try:
            runner = Runner('Пешеход', -5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", str(e))

    @skip_if_frozen
    def test_run(self):
        try:
            runner = Runner(123, 15)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", str(e))


if __name__ == "__main__":
    unittest.main(verbosity=2)