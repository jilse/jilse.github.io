docker run --rm --label=jekyll --volume=%CD%:/srv/jekyll -it -p 4000:4000 jekyll/jekyll ^
jekyll serve ^
	--incremental ^
	--config _config.yml,_config-dev.yml ^
	--watch ^
	--force_polling ^
