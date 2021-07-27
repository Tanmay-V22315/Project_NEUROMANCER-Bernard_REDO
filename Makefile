.DEFAULT_GOAL := help
# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
 
help:           ## Show this help (Sorry for camel-cased arguments, I just like it that way).
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
 
installArch:           ## Install dependencies and stuff for Arch-based distros (Arch, Manjaro, Garuda etc.)
	bash "./src/Voice/installation/TTSinstallationforArch_based.sh"

installDeb:           ## Install dependencies and stuff for Debian-based distros (Debian, Ubuntu, Pop!OS etc.)
	bash "./src/Voice/installation/TTSinstallationforDebian_based.sh"






