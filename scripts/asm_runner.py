import os
from scripts.docker_handler import DockerHandler

class AssemblyRunner:
    SOLUTION_FOLDER = os.path.abspath("solution")
    TEST_CASES_FOLDER = os.path.abspath("test_cases")
    DOCKER_EXEC = ["docker-compose", "exec", "-T", "asm-container"]

    @staticmethod
    def compile_asm(asm_file):
        # There is no compile needed for mips
        pass

    @staticmethod
    def run_asm(asm_file, input_file):
        input_path = f"/test_cases/in/{input_file}"
        with open(os.path.join(AssemblyRunner.TEST_CASES_FOLDER, "in", input_file), "r") as f:
            expected_input = "\n".join([line.strip() for line in f.readlines()])

        command = AssemblyRunner.DOCKER_EXEC + ["bash", "-c", f"echo \"{expected_input}\" | spim -f {asm_file}"]
        output, _ = DockerHandler.exec_command(command)
        return output
