import unittest

import ex_17_3_1_testing_python_repos as python_repos

class PythonReposTestCase(unittest.TestCase):
    """Tests for python_repos.py."""

    def setUp(self):
        """Initial call for all the functions to be tested."""
        self.r = python_repos.get_api_response()
        self.repo_dicts = python_repos.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels = python_repos.get_data(
                self.repo_dicts)

    def test_get_api_response(self):
        """Test that we get a status code 200"""
        self.assertEqual(self.r.status_code, 200)

    def test_get_repo_dicts(self):
        """Test that we're getting the required data."""
        # We should get dicts for 30 repositories.
        self.assertEqual(len(self.repo_dicts), 30)

        # Repositories should have required keys.
        required_keys = ["name", "html_url", "stargazers_count", "owner",
                        "description"]
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()