var gulp = require("gulp");
var sass = require("gulp-sass");
var autoprefixer = require("gulp-autoprefixer");

// Compile Sass files to CSS
gulp.task("scss", function() {
	gulp
		.src("src/scss/main.scss")
		.pipe(
			sass({
				outputStyle: "expanded"
			})
		)
		.pipe(
			autoprefixer({
				browsers: ["last 20 versions"]
			})
		)
		.pipe(gulp.dest("static/css"));
});

// Watch the asset folder for changes
gulp.task("watch", ["scss"], function() {
	gulp.watch("src/scss/**/*", ["scss"]);
});

// Set `watch` as the default task
gulp.task("default", ["watch"]);
