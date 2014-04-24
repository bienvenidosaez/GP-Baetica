// include plug-ins
var gulp        = require('gulp');
var concat      = require('gulp-concat');
var stripDebug  = require('gulp-strip-debug');
var uglify      = require('gulp-uglify');
var jshint      = require('gulp-jshint');
var stylus      = require('gulp-stylus');
var minifyCSS   = require('gulp-minify-css');

// JS hint task
gulp.task('jshint', function() {
  gulp.src([
            './js/mymain.js'
    ])
    .pipe(jshint())
    .pipe(jshint.reporter('default'));
});

// JS concat, strip debugging and minify
gulp.task('js', function() {
  gulp.src([
          './bower_components/jquery/dist/jquery.js',
          './bower_components/bootstrap/js/alert.js',
          './bower_components/bootstrap/js/tab.js',
          './js/mymain.js'
        ])
    .pipe(concat('/js/production.js'))
    .pipe(stripDebug())
    .pipe(uglify())
    .pipe(gulp.dest('./'));
});

// Get one .styl file and render
gulp.task('stylus', function () {
    gulp.src('./stylus/estilos.styl')
        .pipe(stylus({
            paths: ["/home/stylus-plugins/"],
            set:['compress']
        }))
        .pipe(gulp.dest('./css'));
});


var optionsMinifyCSS = {
  'keepSpecialComments':0
};

gulp.task('css', function() {
  gulp.src(['./css/*.css'])
    .pipe(concat('styles.css'))
    .pipe(minifyCSS(optionsMinifyCSS))
    .pipe(gulp.dest('./produccion/css/'));
});


gulp.task('default', ['stylus'], function() {
// gulp.task('default', ['js', 'stylus'], function() {

  // watch for JS changes
  gulp.watch('./js/*.js', function() {
    gulp.run('jshint','js');
  });

  // watch for stylus changes
  gulp.watch('./stylus/*.styl', function() {
    gulp.run('stylus');
  });

});
