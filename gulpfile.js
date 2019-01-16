const { task, src, dest, watch, series } = require("gulp");
const sass = require("gulp-sass");
const autoPrefixer = require("gulp-autoprefixer");
const htmlmin = require("gulp-htmlmin");
const prettify = require("gulp-jsbeautifier");
const prettier = require("gulp-prettier");

/// Compile Sass
task("sass", function() {
	return src("scss/main.scss")
		.pipe(sass({ outputStyle: "expanded" }))
		.pipe(autoPrefixer({ browsers: ["last 20 versions"] }))
		.pipe(dest("themes/web1/source/css"));
});

/// Prettify HTML
task("prettify", function() {
	return src(["./public**/*.html"])
		.pipe(htmlmin({
			collapseWhitespace: true,
			customAttrCollapse: /content/
		}))
		.pipe(prettify())
		.pipe(dest("./public"));
});
