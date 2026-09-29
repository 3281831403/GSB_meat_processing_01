import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_store(self):
        state = core.new_game()
        self.assertTrue(core.store(state, 1, 10))
        self.assertFalse(core.store(state, 1, 10))

    def test_02_cold_capacity(self):
        state = core.new_game()
        state["cold_load"] = 2
        result = core.receive(state, 1)
        self.assertFalse(result)

    def test_03_fee_exact(self):
        state = core.new_game()
        self.assertEqual(core.fee(state, 1, 3), 2)

    def test_04_cancel_refunds_meat(self):
        state = core.new_game()
        core.store(state, 1, 5)
        core.cancel(state, 1)
        self.assertEqual(state["meat"], 100)

    def test_05_no_output_on_fault(self):
        state = core.new_game()
        state["cold_fault"] = True
        result = core.output(state, 5)
        self.assertFalse(result)

    def test_06_spoil_once(self):
        state = core.new_game()
        core.spoil(state)
        self.assertEqual(state["loss"], 10)

    def test_07_no_inspect_without_quarantine(self):
        state = core.new_game()
        state["quarantine"] = False
        result = core.inspect(state, 1)
        self.assertFalse(result)

    def test_08_load_preserves_batch(self):
        state = core.new_game()
        state["batch_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["batch_id"], 4)


if __name__ == "__main__":
    unittest.main()
