import linear_search_recursion as tested_script


# Testing all instructions:

class TestAllInstructions:
    def test_answer1(self):
        assert -1 == tested_script.rec_search([7, 10, 6, 8, 0, 12], 3, 2, 0)

    def test_answer2(self):
        assert 2 == tested_script.rec_search([7, 10, 6, 8, 0, 12], 0, 5, 6)

    def test_answer3(self):
        assert 5 == tested_script.rec_search([7, 10, 6, 8, 0, 12], 0, 5, 12)
