'use strict';

const __PROD__ = false; //indica si minificar o no los js y css

const dirs = {
    src: 'welldone/static/src',
    dist: 'welldone/static/dist'
};

const config = {
    src_path : {
        'sass': `${dirs.src}/scss/*.scss`,
        'js': `${dirs.src}/js/*.js`,
        'img': `${dirs.src}/img`
    },

    dist_path : {
        'css': `${dirs.dist}/css`,
        'js': `${dirs.dist}/js`,
        'img': `${dirs.dist}/img`
    }
}

export { dirs, config, __PROD__ }
