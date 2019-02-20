import unittest

from hw4Abezzam_565 import get_repo_info


class TestGetRepo(unittest.TestCase):
    def test_normal_response(self):
        expected = ['User: Abezzam10',
                    'Repo: AI-metrics Number of commits: 30',
                    'Repo: das Number of commits: 2',
                    'Repo: ML_agorithms-in-a-dataset-Python- Number of commits: 2',
                    'Repo: ssw690ossmgmt Number of commits: 2',
                    'Repo: TestFiles Number of commits: 2']
        self.assertEqual(get_repo_info(), expected)

    def test_bad_user_name(self):
        self.assertEqual(get_repo_info('aaaabbbbcccc'), 'unable to fetch repos from user')
        self.assertEqual(get_repo_info(''), 'unable to fetch repos from user')


if __name__ == '__main__':
    unittest.main()
