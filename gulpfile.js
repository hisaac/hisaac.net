const { src, dest, watch, series } = require("gulp");
const sass = require("gulp-sass");
const autoPrefixer = require("gulp-autoprefixer");
const htmlmin = require("gulp-htmlmin");
const prettify = require("gulp-jsbeautifier");
const prettier = require("gulp-prettier");

/// Transpile Sass files to CSS
function scss() {
	return src("scss/main.scss")
		.pipe(sass({ outputStyle: "expanded" }))
		.pipe(autoPrefixer({ browsers: ["last 20 versions"] }))
		.pipe(dest("themes/web1/source/css"));
}

/// Prettify HTML
function clean() {
	return src(["./public**/*.html"])
		.pipe(htmlmin({
			collapseWhitespace: true,
			customAttrCollapse: /content/
		}))
		.pipe(prettify())
		.pipe(dest("./public"));
}

watch("scss/**/*", scss);

exports.scss = scss;
exports.clean = clean;
exports.default = watch;
