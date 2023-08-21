import subprocess
import os

def main():
    # Construct the absolute path to the activation script of the virtual environment
    activate_script = os.path.abspath(os.path.join("myGitanaEnv", "Scripts", "activate"))

    # Use Git Bash to activate the environment and run the script
    bash_command = "source {} && bash script.sh".format(activate_script.replace('\\', '/'))
    subprocess.run([r"C:\Program Files\Git\bin\bash.exe", "-c", bash_command], cwd="Gitana")

if __name__ == '__main__':
    main()
