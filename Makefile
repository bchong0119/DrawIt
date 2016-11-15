SCRIPTS= $(shell ls draw_*.py)

test:
	@python -m unittest -v drawit.tests

ppms:	${SCRIPTS:.py=.ppm}

pngs:	${SCRIPTS:.py=.png}

clean:
	@echo Removing PNG, PPM, and PYC files...
	@rm -f *.png *.ppm *.pyc

%.ppm:	%.py
	@echo Generating $@...
	@python $< > $@

%.png:	%.ppm
	@echo Converting $< to $@...
	@convert $< $@
