.PHONY: css html

css:
	lessc style.less light_theme.css --global-var='dark=false'
	lessc style.less dark_theme.css --global-var='dark=true'

html : 
	python3 gen.py