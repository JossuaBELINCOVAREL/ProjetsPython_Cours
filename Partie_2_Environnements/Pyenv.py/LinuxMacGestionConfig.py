"""
Pour installer Pyenv sous Linux/Mac : 

Etape 1 -> 

Installer Pyenv
    -> curl https://pyenv.run | bash
Ajoute les lignes suivantes à ton fichier ~/.bashrc ou ~/.zshrc
    -> export PATH="$HOME/.pyenv/bin:$PATH"
       eval "$(pyenv init --path)"
       eval "$(pyenv virtualenv-init -)"
Recharge le terminal
    -> source ~/.bashrc (ou source ~/.zshrc si tu utilises Zsh)

Etape 2 ->  

pyenv install 3.11.6 (-> ici installe la version souhaitée)
    pyenv global 3.11.6 (-> Pour définir cette version globalement)
    pyenv local 3.11.6 (-> Ou uniquement pour un projet spécifique)

Etape 3 ->  

Installe le plugin pyenv-virtualenv (si ce n'est pas déjà fait)
    -> pyenv install virtualenv
Crée/active/désactive un environnement virtuel
    -> pyenv virtualenv 3.11.6 mon_env
    -> pyenv activate mon_env
    -> pyenv deactivate


"""