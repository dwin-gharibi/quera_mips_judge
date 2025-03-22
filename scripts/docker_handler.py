import subprocess

class DockerHandler:
    @staticmethod
    def start_container():
        subprocess.run(["docker-compose", "up", "-d"], check=True)

    @staticmethod
    def stop_container():
        subprocess.run(["docker-compose", "down"], check=True)

    @staticmethod
    def exec_command(command, input_data=None):
        process = subprocess.Popen(
            command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        output, error = process.communicate(input=input_data)
        print(error)
        return [line.strip() for line in output.split("\n") if line], error.strip()