"""
Pour installer Pyenv sous windows : 

Etape 1 -> 

git clone https://github.com/pyenv-win/pyenv-win.git $HOME/.pyenv
export PYENV="$HOME/.pyenv"
export PATH="$PYENV/bin:$PYENV/shims:$PATH"
echo 'export PYENV="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV/bin:$PYENV/shims:$PATH"' >> ~/.bashrc
source ~/.bashrc

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