# kenmen
金門小島下酒菜

預設情況下，只能以 root用戶 或 Docker中的用戶 運行docker命令，因此這邊提供以下命令，可以不用輸入 sudo 即可運行命令，運行完重新連線後才可生效。

sudo usermod -aG docker ${USER}
