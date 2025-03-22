import unittest
import os
from scripts.docker_handler import DockerHandler
from scripts.asm_runner import AssemblyRunner

class TestAssemblyPrograms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        DockerHandler.start_container()

    @classmethod
    def tearDownClass(cls):
        DockerHandler.stop_container()

    def test_1(self):
        asm_file = "sum.asm"
        input_file = "input4.txt"
        output_file = "output4.txt"

        AssemblyRunner.compile_asm(asm_file)
        output = AssemblyRunner.run_asm(asm_file, input_file)

        output_path = os.path.join(AssemblyRunner.TEST_CASES_FOLDER, "out", output_file)
        with open(output_path, "r") as f:
            expected_output = [line.strip() for line in f.readlines()]

        self.assertEqual(output[5:], expected_output, f"Unexpected output for {asm_file}")


if __name__ == "__main__":
    unittest.main()
