from conan import ConanFile
import os
import shutil

class HelloDllConan(ConanFile):
    name = "hellodll"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"

    def upload_to_github(self):
        repo_url = "https://github.com/Razintras/Conan.git"
        source_dir = r"C:\Users\cparis\Documents\SVN_bac_a_sable\HelloProjectTrunk\Hello\Src\HelloDll"
        clone_dir = os.path.join(self.build_folder, "repo_clone")

        # Cloner le dépôt GitHub
        self.run(f"git clone {repo_url} {clone_dir}")

        # Copier les fichiers du dossier source vers le dossier cloné
        self.copy_files(source_dir, clone_dir)

        # Committer et pousser les modifications
        self.run("git add .", cwd=clone_dir)
        self.run('git commit -m "Upload hellodll to GitHub"', cwd=clone_dir)
        self.run("git push", cwd=clone_dir)

    def copy_files(self, src, dst):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                if not os.path.exists(d):
                    os.makedirs(d)
                self.copy_files(s, d)
            else:
                shutil.copy2(s, d)

    def deploy(self):
        self.upload_to_github()
