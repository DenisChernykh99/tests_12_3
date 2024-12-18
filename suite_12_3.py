import unittest
import tests_12_3


runSuite = unittest.TestSuite()
runSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runSuite)