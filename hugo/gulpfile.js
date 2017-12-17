const gulp = require("gulp");
const sass = require("gulp-sass");
const autoprefixer = require("gulp-autoprefixer");
const htmlmin = require("gulp-htmlmin");
const prettify = require("gulp-jsbeautifier");

/// Compile Sass files to CSS
gulp.task("scss", function() {
	gulp.src("src/scss/main.scss")
		.pipe(sass({ outputStyle: "expanded" }))
		.pipe(autoprefixer({ browsers: ["last 20 versions"] }))
		.pipe(gulp.dest("static/css"));
});

/// Beautify HTML
gulp.task("beautify", function() {
	gulp.src(["./public/**/*.html"])
		.pipe(htmlmin({
			collapseWhitespace: true,
			customAttrCollapse: /content/
		}))
		.pipe(prettify())
		.pipe(gulp.dest("./public"));
});

/// Watch the `src` folder for changes
gulp.task("watch", ["scss"], function() {
	gulp.watch("src/scss/**/*", ["scss"]);
});

// Set `watch` as the default task
gulp.task("default", ["watch"]);
