apt update && \
apt install -y zsh && \
chsh -s $(which zsh) && \
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"