import unittest
import HtmlTestRunner

from proiectaboutyou import Login


class TestSuites(unittest.TestCase):

    def test_suite(self):

        test_to_run = unittest.TestSuite()

        test_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
        ])
        #outfile = open("C:\\Users\\bianc\\OneDrive\\Desktop\\report.html", "w")
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='My Report Name',
            report_title='My First Report Title',
            #stream= outfile
        )

        runner.run(test_to_run)