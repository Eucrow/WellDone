'use strict';

import tap from 'gulp-tap';
import uglify from 'gulp-uglify';
import postcss from 'gulp-postcss';
import sourcemaps from 'gulp-sourcemaps';
import lazypipe from 'lazypipe';
import cssnano from 'cssnano';
import browserify from 'browserify';


const mincss = lazypipe()
	.pipe(sourcemaps.init)
	.pipe(postcss, [cssnano()])
	.pipe(sourcemaps.write, './');

const minjs = lazypipe()
	.pipe(sourcemaps.init)
	.pipe(uglify, { preserveComments: 'license' })
	.pipe(sourcemaps.write, './');

const babelify = lazypipe()
	.pipe(tap, file => {
		file.contents = browserify(file.path)
			.transform('babelify', {presets: ["es2015"]})
			.bundle();
	});


export default { mincss, minjs, babelify }
