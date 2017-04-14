'use strict';

import { dirs, config, __PROD__ } from './gulp.config';
import tasks from './gulp.task';

import gulp from 'gulp';
import ifelse from 'gulp-if';
import rename from 'gulp-rename';
import postcss from 'gulp-postcss';
import sass from 'gulp-sass';
import autoprefixer from 'autoprefixer';
import runSequence from 'run-sequence';
import browserSync from 'browser-sync';
import buffer from 'vinyl-buffer';


// Definicion de tareas
gulp
	.task('default', () => runSequence(['build-statics', 'serve'], 'watch'))

	.task('build-statics', ['build-css', 'build-js'])

	.task('build-css', () => {
		gulp.src(config.src_path.sass)
			.pipe(sass().on('error', sass.logError))
            .pipe(postcss([autoprefixer()]))
            .pipe(ifelse(__PROD__, tasks.mincss()))
            .pipe(rename({suffix: '.min'}))
            .pipe(gulp.dest(config.dist_path.css))
            .pipe(browserSync.stream())
	})

	.task('build-js', () => {
		gulp.src(config.src_path.js)
            .pipe(tasks.babelify())
            .pipe(buffer())
            .pipe(ifelse(__PROD__, tasks.minjs()))
            .pipe(rename({suffix: '.min'}))
            .pipe(gulp.dest(config.dist_path.js))
            .pipe(browserSync.stream())
	})

	.task('serve', () => {
		browserSync.create();
        browserSync.init({
			proxy: "http://127.0.0.1:8000/"
		});
	})

	.task('watch', () => {
		gulp.watch(`${dirs.src}/**/*.{css,scss}`, ['build-css']);
		gulp.watch(`${dirs.src}/**/*.js`, ['build-js']);
		gulp.watch('./**/*.html').on('change', browserSync.reload);
	});
